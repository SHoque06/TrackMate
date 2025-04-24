from PySide6.QtWidgets import QWidget, QTableWidgetItem
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
        reps = self.lineEdit_reps.text()
        sets = self.lineEdit_sets.text()
        exercise_name = self.lineEdit_exercise.text()
        # duration = self.lineEdit_duration
        weight = self.lineEdit_weight.text()


        # Save the workout data to the database
        if self.db.logExercise(exercise_name, sets, reps, weight):
            self.add_row(exercise_name, sets, reps, weight)
            # Clear the input fields after saving
            self.lineEdit_reps.clear()
            self.lineEdit_sets.clear()
            self.lineEdit_exercise.clear()
            self.lineEdit_weight.clear()

        # Optionally, you can add a message to indicate success


    def add_row(self, exercise_name, sets, reps, weight):
        row_position = self.tableWidget_exercises.rowCount()
        self.tableWidget_exercises.insertRow(row_position)
        self.tableWidget_exercises.setItem(row_position, 0, QTableWidgetItem(exercise_name))
        self.tableWidget_exercises.setItem(row_position, 1, QTableWidgetItem(sets))
        self.tableWidget_exercises.setItem(row_position, 2, QTableWidgetItem(reps))
        self.tableWidget_exercises.setItem(row_position, 3, QTableWidgetItem(weight))