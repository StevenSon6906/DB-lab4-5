from my_project.auth.controller.orders.GenderController import GenderController
from my_project.auth.controller.orders.TrainersController import TrainersController
from my_project.auth.controller.orders.VisitorsController import VisitorsController
from my_project.auth.controller.orders.ProgramsController import ProgramsController
from my_project.auth.controller.orders.ProgramsTimetableController import ProgramsTimetableController
from my_project.auth.controller.orders.ExercisesController import ExercisesController
from my_project.auth.controller.orders.ProgramExercisesController import ProgramExercisesController
from my_project.auth.controller.orders.VisitorProgramsController import VisitorProgramsController
from my_project.auth.controller.orders.ProgramCompletionController import ProgramCompletionController
from my_project.auth.controller.orders.TrainerVisitsController import TrainerVisitsController
from my_project.auth.controller.orders.ProgramsLogsController import ProgramsLogsController

# Initialize controllers
gender_controller = GenderController()
trainers_controller = TrainersController()
visitors_controller = VisitorsController()
programs_controller = ProgramsController()
programs_timetable_controller = ProgramsTimetableController()
exercises_controller = ExercisesController()
program_exercises_controller = ProgramExercisesController()
visitor_programs_controller = VisitorProgramsController()
program_completion_controller = ProgramCompletionController()
trainer_visits_controller = TrainerVisitsController()
programs_logs_controller = ProgramsLogsController()