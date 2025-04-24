from PySide6.QtWidgets import QWidget
from networkx.classes import selfloop_edges

from ui_workoutLogPage import Ui_WorkoutLogPage

class logworkoutDisplay(Ui_WorkoutLogPage, QWidget):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.db = database


        self.pushButton_add.clicked.connect(self.save_workout)

    def save_workout(self):
        # Get the values from the input fields
        reps = self.lineEdit_reps
        sets = self.lineEdit_sets
        exercise_name = self.lineEdit_exercise
        # duration = self.lineEdit_duration
        weight = self.lineEdit_weight


        # Save the workout data to the database
        self.db.logExercise(exercise_name, sets, reps, weight)
        # Clear the input fields after saving
        self.lineEdit_reps.clear()
        self.lineEdit_sets.clear()
        self.lineEdit_exercise.clear()
        self.lineEdit_weight.clear()
        # Optionally, you can add a message to indicate success
