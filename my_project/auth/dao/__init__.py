
from .orders.GenderDAO import GenderDAO
from .orders.TrainersDAO import TrainersDAO
from .orders.VisitorsDAO import VisitorsDAO
from .orders.ProgramsDAO import ProgramsDAO
from .orders.ProgramsTimetableDAO import ProgramsTimetableDAO
from .orders.ExercisesDAO import ExercisesDAO
from .orders.ProgramExercisesDAO import ProgramExercisesDAO
from .orders.VisitorProgramsDAO import VisitorProgramsDAO
from .orders.ProgramCompletionDAO import ProgramCompletionDAO
from .orders.TrainerVisitsDAO import TrainerVisitsDAO
from .orders.ProgramsLogsDAO import ProgramsLogsDAO


genderDao = GenderDAO()
trainersDao = TrainersDAO()
visitorsDao = VisitorsDAO()
programsDao = ProgramsDAO()
programsTimetableDao = ProgramsTimetableDAO()
exercisesDao = ExercisesDAO()
programExercisesDao = ProgramExercisesDAO()
visitorProgramsDao = VisitorProgramsDAO()
programCompletionDao = ProgramCompletionDAO()
trainerVisitsDao = TrainerVisitsDAO()
programsLogsDao = ProgramsLogsDAO()
