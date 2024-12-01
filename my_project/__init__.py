import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
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

#rom
def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    _init_db(app)
    register_routes(app)
    _init_swagger(app)
    _init_trigger(app)
    _init_function(app)

    #_init_programs(app)
    # _init_procedures(app)
    add_program_log(app, visitor_id=2, exercise_id=1, log_date="2024-10-25", unit="reps")

    # _do_cursor_task(app)

    _init_program_exercise(app, 1,2, 10)
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
def _init_program_exercise(app: Flask, program_id: int, exercise_id: int, target_value: int) -> None:
    with app.app_context():
        db.session.execute(
            """
            INSERT INTO program_exercises (program_id, exercise_id, target_value)
            VALUES (:program_id, :exercise_id, :target_value)
            """,
            {
                'program_id': program_id,
                'exercise_id': exercise_id,
                'target_value': target_value
            }
        )
        db.session.commit()

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
    # A-lia Swagger
    restx_api = Api(app, title='Pavelchak test backend',
                    description='A simple backend')  # https://flask-restx.readthedocs.io/

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


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
