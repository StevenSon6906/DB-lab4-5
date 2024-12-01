# Import services with appropriate naming and paths for each entity
from .orders.GenderService import GenderService
from .orders.TrainerService import TrainerService
from .orders.VisitorService import VisitorService
from .orders.ProgramService import ProgramService
from .orders.ProgramTimetableService import ProgramTimetableService
from .orders.ExerciseService import ExerciseService
from .orders.ProgramExerciseService import ProgramExerciseService
from .orders.VisitorProgramService import VisitorProgramService
from .orders.ProgramCompletionService import ProgramCompletionService
from .orders.TrainerVisitService import TrainerVisitService
from .orders.ProgramLogService import ProgramLogService

# Initialize service instances with HelloWorld naming style
genderService = GenderService()
trainerService = TrainerService()
visitorService = VisitorService()
programService = ProgramService()
programTimetableService = ProgramTimetableService()
exerciseService = ExerciseService()
programExerciseService = ProgramExerciseService()
visitorProgramService = VisitorProgramService()
programCompletionService = ProgramCompletionService()
trainerVisitService = TrainerVisitService()
programLogService = ProgramLogService()
