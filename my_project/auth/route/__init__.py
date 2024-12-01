from flask import Flask

from .error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes for each entity
    :param app: Flask application object
    """
    # Register error handler blueprint
    app.register_blueprint(err_handler_bp)

    # Import and register blueprints for each specific entity based on SQL table names
    from .orders.GenderBlueprint import gender_bp
    from .orders.TrainerBlueprint import trainer_bp
    from .orders.VisitorBlueprint import visitor_bp
    from .orders.ProgramBlueprint import program_bp
    from .orders.ProgramTimetableBlueprint import program_timetable_bp
    from .orders.ExerciseBlueprint import exercise_bp
    from .orders.ProgramExerciseBlueprint import program_exercise_bp
    from .orders.VisitorProgramBlueprint import visitor_program_bp
    from .orders.ProgramCompletionBlueprint import program_completion_bp
    from .orders.TrainerVisitBlueprint import trainer_visit_bp
    from .orders.ProgramLogBlueprint import program_log_bp

    # Register each blueprint with the app
    app.register_blueprint(gender_bp)
    app.register_blueprint(trainer_bp)
    app.register_blueprint(visitor_bp)
    app.register_blueprint(program_bp)
    app.register_blueprint(program_timetable_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(program_exercise_bp)
    app.register_blueprint(visitor_program_bp)
    app.register_blueprint(program_completion_bp)
    app.register_blueprint(trainer_visit_bp)
    app.register_blueprint(program_log_bp)
