import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes
from sqlalchemy import text

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()

todos = {}

def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    _init_swagger(app)
    #_init_trigger(app)
    #_init_function(app)

    #_init_programs(app)
    # _init_procedures(app)
    #add_program_log(app, visitor_id=2, exercise_id=1, log_date="2024-10-25", unit="reps")

    # _do_cursor_task(app)

    # _init_program_exercise(app, 1, 2, 10)  # disabled: caused FK error when seed rows are missing
    return app

def _do_cursor_task(app:Flask):
    with open("cursor.sql", "r") as file:
        sql_script = file.read()
    with app.app_context() as connection:
        db.session.execute(text(sql_script))
        print("SQL script executed successfully.")


#C-пакет-зроблено
def _init_programs(app: Flask):
    with app.app_context():
        db.session.execute(
            """
DROP PROCEDURE IF EXISTS insert_programs;
CREATE PROCEDURE insert_programs()
BEGIN
    DECLARE i INT DEFAULT 3;

    WHILE i < 13 DO
        INSERT IGNORE INTO programs (id, name, description)
        VALUES (i, CONCAT('Program ', i), CONCAT('This is the description for Program ', i));
        SET i = i + 1;
    END WHILE;
END;
            """
        )
        db.session.execute("CALL insert_programs();")
        db.session.commit()

#A-парамт
# def _init_program_exercise(app: Flask, program_id: int, exercise_id: int, target_value: int) -> None:
#     with app.app_context():
#         db.session.execute(
#             """
#             INSERT INTO program_exercises (program_id, exercise_id, target_value)
#             VALUES (:program_id, :exercise_id, :target_value)
#             """,
#             {
#                 'program_id': program_id,
#                 'exercise_id': exercise_id,
#                 'target_value': target_value
#             }
#         )
#         db.session.commit()

#B-M:M-зроблено
def _init_procedures(app: Flask) -> None:
    with app.app_context():
        db.session.execute('''
            DROP PROCEDURE IF EXISTS AddProgramLog;_
            CREATE PROCEDURE AddProgramLog(
                IN p_visitor_id INT,
                IN p_exercise_id INT,
                IN p_log_date DATE,
                IN p_unit VARCHAR(50)
            )
            BEGIN
                INSERT INTO programs_logs (visitor_id, exercise_id, log_date, unit)
                VALUES (p_visitor_id, p_exercise_id, p_log_date, p_unit);
            END;
        ''')
        db.session.commit()

def add_program_log(app: Flask, visitor_id: int, exercise_id: int, log_date: str, unit: str) -> None:
    with app.app_context():
        db.session.execute(
            "CALL AddProgramLog(:visitor_id, :exercise_id, :log_date, :unit)",
            {
                'visitor_id': visitor_id,
                'exercise_id': exercise_id,
                'log_date': log_date,
                'unit': unit
            }
        )
        db.session.commit()

#D - МAX - готово
def _init_function(app: Flask) -> None:
    with app.app_context():
        db.session.execute('''
        DROP FUNCTION IF EXISTS MaxTargetValue;
        CREATE FUNCTION MaxTargetValue() 
        RETURNS INTEGER
        DETERMINISTIC
        BEGIN
            DECLARE max_value INTEGER;
            SELECT MAX(target_value) INTO max_value 
            FROM program_exercises;
            RETURN max_value;
        END;
        ''')
        db.session.commit()
        result = db.session.execute('SELECT MaxTargetValue()').scalar()
        print(f"The maximum target value is {result}")

#1
def _init_trigger(app: Flask) -> None:
    with app.app_context():
        db.session.execute('''
        DROP TRIGGER IF EXISTS trigger_gender;
        CREATE TRIGGER trigger_gender
        BEFORE INSERT ON trainers
        FOR EACH ROW
        BEGIN
            IF NEW.Id < 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Primary key cannot be negative';
            END IF;
            IF NOT EXISTS (SELECT 1 FROM gender WHERE gender.Id = NEW.gender) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'No such gender exist';
            END IF;
        END;
        ''')
        db.session.execute('''
                DROP TRIGGER IF EXISTS trigger_gender_upd;
                CREATE TRIGGER trigger_gender_upd
                BEFORE UPDATE ON trainers
                FOR EACH ROW
                BEGIN
                    IF NEW.Id < 0 THEN
                        SIGNAL SQLSTATE '45000'
                        SET MESSAGE_TEXT = 'Primary key cannot be negative';
                    END IF;
                    IF NOT EXISTS (SELECT 1 FROM gender WHERE gender.Id = NEW.gender) THEN
                        SIGNAL SQLSTATE '45000'
                        SET MESSAGE_TEXT = 'No such gender exist';
                    END IF;
                END;
                ''')
        #меньше 6 буков
        db.session.execute('''
        DROP TRIGGER IF EXISTS program_limiter;
        CREATE TRIGGER program_limiter
        BEFORE UPDATE ON programs 
        FOR EACH ROW
        BEGIN
            IF CHAR_LENGTH(NEW.description) < 6 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Thanos skazav that award description chinne more that 6 characters';
            END IF;
        END;
        ''')
        #не модифікувати
        db.session.execute('''
        DROP TRIGGER IF EXISTS gender_mod;
        CREATE TRIGGER gender_mod
        BEFORE UPDATE ON gender 
        FOR EACH ROW
        BEGIN                              
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Lushe dva genderu isnue :) ';
        END;
        ''')
        #дубль О
        db.session.execute('''
        DROP TRIGGER IF EXISTS zero_trigger;
        CREATE TRIGGER zero_trigger
        BEFORE UPDATE ON visitors 
        FOR EACH ROW
        BEGIN
            IF RIGHT(NEW.phone, 2) = '00' THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Phone number cannot end with two zeros';
            END IF;
        END;
        ''')
        db.session.commit()


def _init_swagger(app: Flask) -> None:
    restx_api = Api(app, title='Fitness Center API',
                    description='API for managing fitness center operations',
                    version='1.0',
                    doc='/swagger')

    # Models
    #exercise_model = restx_api.model('Exercise', {
    #    'id': fields.Integer(readonly=True, description='Exercise identifier'),
    #    'name': fields.String(required=True, description='Exercise name'),
    #    'description': fields.String(description='Exercise description'),
    #    'unit': fields.String(description='Exercise measurement unit (e.g., reps, kg, minutes)')
    #})

    program_model = restx_api.model('Program', {
        'id': fields.Integer(readonly=True, description='Program identifier'),
        'name': fields.String(required=True, description='Program name'),
        'description': fields.String(required=True, description='Program description')
    })

    gender_model = restx_api.model('Gender', {
        'id': fields.Integer(readonly=True, description='Gender identifier'),
        'name': fields.String(required=True, description='Gender name')
    })

    trainer_model = restx_api.model('Trainer', {
        'id': fields.Integer(readonly=True, description='Trainer identifier'),
        'name': fields.String(required=True, description='Trainer name'),
        'gender': fields.Integer(required=True, description='Gender ID'),
        'phone': fields.String(required=True, description='Phone number')
    })

    visitor_model = restx_api.model('Visitor', {
        'id': fields.Integer(readonly=True, description='Visitor identifier'),
        'name': fields.String(required=True, description='Visitor name'),
        'gender': fields.Integer(required=True, description='Gender ID'),
        'phone': fields.String(required=True, description='Phone number')
    })

    program_exercise_model = restx_api.model('ProgramExercise', {
        'program_id': fields.Integer(required=True, description='Program ID'),
        'exercise_id': fields.Integer(required=True, description='Exercise ID'),
        'target_value': fields.Integer(required=True, description='Target value for the exercise')
    })

    # Namespaces
    #exercise_ns = restx_api.namespace('exercises', description='Exercise operations')
    program_ns = restx_api.namespace('programs', description='Program operations')
    gender_ns = restx_api.namespace('genders', description='Gender operations')
    trainer_ns = restx_api.namespace('trainers', description='Trainer operations')
    visitor_ns = restx_api.namespace('visitors', description='Visitor operations')
    program_exercise_ns = restx_api.namespace('program-exercises', description='Program Exercise operations')

    # Exercise endpoints
    # @exercise_ns.route('/')
    # class ExerciseList(Resource):
    #     @exercise_ns.doc('list_exercises')
    #     @exercise_ns.marshal_list_with(exercise_model)
    #     def get(self):
    #         """List all exercises"""
    #         from my_project.auth.domain import Exercise
    #         return Exercise.query.all()
    #
    #     @exercise_ns.doc('create_exercise')
    #     @exercise_ns.expect(exercise_model, validate=True)
    #     @exercise_ns.marshal_with(exercise_model, code=201)
    #     def post(self):
    #         """Create a new exercise"""
    #         from flask import request
    #         from my_project.auth.domain import Exercise
    #         payload = request.get_json(force=True)
    #         exercise = Exercise(
    #             name=payload['name'],
    #             description=payload.get('description'),
    #             unit=payload.get('unit')
    #         )
    #         db.session.add(exercise)
    #         db.session.commit()
    #         return exercise, 201
    #
    # @exercise_ns.route('/<int:id>')
    # class Exercise(Resource):
    #     @exercise_ns.doc('get_exercise')
    #     @exercise_ns.marshal_with(exercise_model)
    #     def get(self, id):
    #         """Get an exercise by ID"""
    #         return {}
    #
    #     @exercise_ns.doc('update_exercise')
    #     @exercise_ns.expect(exercise_model)
    #     @exercise_ns.marshal_with(exercise_model)
    #     def put(self, id):
    #         """Update an exercise"""
    #         return {}
    #
    #     @exercise_ns.doc('delete_exercise')
    #     @exercise_ns.response(204, 'Exercise deleted')
    #     def delete(self, id):
    #         """Delete an exercise"""
    #         return '', 204

    # Program endpoints
    @program_ns.route('/')
    class ProgramList(Resource):
        @program_ns.doc('list_programs')
        @program_ns.marshal_list_with(program_model)
        def get(self):
            """List all programs"""
            from my_project.auth.domain import Program
            return Program.query.all()

        @program_ns.doc('create_program')
        @program_ns.expect(program_model, validate=True)
        @program_ns.marshal_with(program_model, code=201)
        def post(self):
            """Create a new program"""
            from flask import request
            from my_project.auth.domain import Program
            payload = request.get_json(force=True)
            program = Program(
                name=payload['name'],
                description=payload['description']
            )
            db.session.add(program)
            db.session.commit()
            return program, 201

    @program_ns.route('/<int:id>')
    class Program(Resource):
        @program_ns.doc('get_program')
        @program_ns.marshal_with(program_model)
        def get(self, id):
            """Get a program by ID"""
            return {}

        @program_ns.doc('update_program')
        @program_ns.expect(program_model)
        @program_ns.marshal_with(program_model)
        def put(self, id):
            """Update a program"""
            return {}

        @program_ns.doc('delete_program')
        @program_ns.response(204, 'Program deleted')
        def delete(self, id):
            """Delete a program"""
            return '', 204

    # Gender endpoints
    @gender_ns.route('/')
    class GenderList(Resource):
        @gender_ns.doc('list_genders')
        @gender_ns.marshal_list_with(gender_model)
        def get(self):
            """List all genders"""
            from my_project.auth.domain import Gender
            return Gender.query.all()

        @gender_ns.doc('create_gender')
        @gender_ns.expect(gender_model, validate=True)
        @gender_ns.marshal_with(gender_model, code=201)
        def post(self):
            """Create a new gender"""
            from flask import request
            from my_project.auth.domain import Gender
            payload = request.get_json(force=True)
            gender = Gender(name=payload['name'])
            db.session.add(gender)
            db.session.commit()
            return gender, 201

    @gender_ns.route('/<int:id>')
    class Gender(Resource):
        @gender_ns.doc('get_gender')
        @gender_ns.marshal_with(gender_model)
        def get(self, id):
            """Get a gender by ID"""
            return {}

        @gender_ns.doc('update_gender')
        @gender_ns.expect(gender_model)
        @gender_ns.marshal_with(gender_model)
        def put(self, id):
            """Update a gender"""
            return {}

        @gender_ns.doc('delete_gender')
        @gender_ns.response(204, 'Gender deleted')
        def delete(self, id):
            """Delete a gender"""
            return '', 204

    # Trainer endpoints
    @trainer_ns.route('/')
    class TrainerList(Resource):
        @trainer_ns.doc('list_trainers')
        @trainer_ns.marshal_list_with(trainer_model)
        def get(self):
            """List all trainers"""
            from my_project.auth.domain import Trainer
            return Trainer.query.all()

        @trainer_ns.doc('create_trainer')
        @trainer_ns.expect(trainer_model, validate=True)
        @trainer_ns.marshal_with(trainer_model, code=201)
        def post(self):
            """Create a new trainer"""
            from flask import request
            from my_project.auth.domain import Trainer
            payload = request.get_json(force=True)
            trainer = Trainer(
                name=payload['name'],
                gender=payload['gender'],
                phone=payload['phone']
            )
            db.session.add(trainer)
            db.session.commit()
            return trainer, 201

    @trainer_ns.route('/<int:id>')
    class Trainer(Resource):
        @trainer_ns.doc('get_trainer')
        @trainer_ns.marshal_with(trainer_model)
        def get(self, id):
            """Get a trainer by ID"""
            return {}

        @trainer_ns.doc('update_trainer')
        @trainer_ns.expect(trainer_model)
        @trainer_ns.marshal_with(trainer_model)
        def put(self, id):
            """Update a trainer"""
            return {}

        @trainer_ns.doc('delete_trainer')
        @trainer_ns.response(204, 'Trainer deleted')
        def delete(self, id):
            """Delete a trainer"""
            return '', 204

    # Visitor endpoints
    @visitor_ns.route('/')
    class VisitorList(Resource):
        @visitor_ns.doc('list_visitors')
        @visitor_ns.marshal_list_with(visitor_model)
        def get(self):
            """List all visitors"""
            from my_project.auth.domain import Visitor
            return Visitor.query.all()

        @visitor_ns.doc('create_visitor')
        @visitor_ns.expect(visitor_model, validate=True)
        @visitor_ns.marshal_with(visitor_model, code=201)
        def post(self):
            """Create a new visitor"""
            from flask import request
            from my_project.auth.domain import Visitor
            payload = request.get_json(force=True)
            visitor = Visitor(
                name=payload['name'],
                gender=payload['gender'],
                phone=payload['phone']
            )
            db.session.add(visitor)
            db.session.commit()
            return visitor, 201

    @visitor_ns.route('/<int:id>')
    class Visitor(Resource):
        @visitor_ns.doc('get_visitor')
        @visitor_ns.marshal_with(visitor_model)
        def get(self, id):
            """Get a visitor by ID"""
            return {}

        @visitor_ns.doc('update_visitor')
        @visitor_ns.expect(visitor_model)
        @visitor_ns.marshal_with(visitor_model)
        def put(self, id):
            """Update a visitor"""
            return {}

        @visitor_ns.doc('delete_visitor')
        @visitor_ns.response(204, 'Visitor deleted')
        def delete(self, id):
            """Delete a visitor"""
            return '', 204

    # # Program Exercise endpoints
    # @program_exercise_ns.route('/')
    # class ProgramExerciseList(Resource):
    #     @program_exercise_ns.doc('list_program_exercises')
    #     @program_exercise_ns.marshal_list_with(program_exercise_model)
    #     def get(self):
    #         """List all program exercises"""
    #         from my_project.auth.domain import ProgramExercise
    #         return ProgramExercise.query.all()
    #
    #     @program_exercise_ns.doc('create_program_exercise')
    #     @program_exercise_ns.expect(program_exercise_model, validate=True)
    #     @program_exercise_ns.marshal_with(program_exercise_model, code=201)
    #     def post(self):
    #         """Create a new program exercise"""
    #         from flask import request
    #         from my_project.auth.domain import ProgramExercise
    #         payload = request.get_json(force=True)
    #         pe = ProgramExercise(
    #             program_id=payload['program_id'],
    #             exercise_id=payload['exercise_id'],
    #             target_value=payload['target_value']
    #         )
    #         db.session.add(pe)
    #         db.session.commit()
    #         return pe, 201
    #
    # @program_exercise_ns.route('/<int:program_id>/<int:exercise_id>')
    # class ProgramExercise(Resource):
    #     @program_exercise_ns.doc('get_program_exercise')
    #     @program_exercise_ns.marshal_with(program_exercise_model)
    #     def get(self, program_id, exercise_id):
    #         """Get a program exercise by Program ID and Exercise ID"""
    #         from my_project.auth.domain import ProgramExercise
    #         from flask_restx import abort
    #         pe = ProgramExercise.query.filter_by(program_id=program_id, exercise_id=exercise_id).first()
    #         if not pe:
    #             abort(404, "ProgramExercise not found")
    #         return pe
    #
    #     @program_exercise_ns.doc('update_program_exercise')
    #     @program_exercise_ns.expect(program_exercise_model, validate=True)
    #     @program_exercise_ns.marshal_with(program_exercise_model)
    #     def put(self, program_id, exercise_id):
    #         """Update a program exercise"""
    #         from flask import request
    #         from my_project.auth.domain import ProgramExercise
    #         from flask_restx import abort
    #         pe = ProgramExercise.query.filter_by(program_id=program_id, exercise_id=exercise_id).first()
    #         if not pe:
    #             abort(404, "ProgramExercise not found")
    #         payload = request.get_json(force=True)
    #         # Only target_value is updatable in this minimal variant
    #         if 'target_value' in payload:
    #             pe.target_value = payload['target_value']
    #         db.session.commit()
    #         return pe
    #
    #     @program_exercise_ns.doc('delete_program_exercise')
    #     @program_exercise_ns.response(204, 'Program exercise deleted')
    #     def delete(self, program_id, exercise_id):
    #         """Delete a program exercise"""
    #         from my_project.auth.domain import ProgramExercise
    #         from flask_restx import abort
    #         pe = ProgramExercise.query.filter_by(program_id=program_id, exercise_id=exercise_id).first()
    #         if not pe:
    #             abort(404, "ProgramExercise not found")
    #         db.session.delete(pe)
    #         db.session.commit()
    #         return '', 204
def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    # Set root username and password in app_config
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
