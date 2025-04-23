from PySide6.QtWidgets import QWidget
from ui_profilewidget import Ui_profilewidgetDisplay
import sqlite3

class profilewidgetDisplay(Ui_profilewidgetDisplay, QWidget):

    def __init__(self, database, user_id=1):  # Default to user_id=1, can be changed
        super().__init__()
        self.db = database
        self.setupUi(self)
        self.user_id = user_id
        self.load_user_data()

    def load_user_data(self):
        conn = sqlite3.connect("gymapp.db")
        cursor = conn.cursor()




        #cursor.execute("UPDATE users SET age = 25, gender = 'Male' WHERE user_id = 1;")

        # Fetch user age and gender
        #cursor.execute("SELECT age, gender FROM users WHERE user_id = ?", (self.user_id,))
        #user_result = cursor.fetchone()
        user_result = ("n/a","n/a")

        # Fetch latest bodyweight entry
        
        #cursor.execute("""
        #    SELECT bodyweight FROM bodyweight 
        #    WHERE user_id = ? 
        #    ORDER BY bodyweight_date DESC LIMIT 1
        #""", (self.user_id,))
        #weight_result = cursor.fetchone()
        
        weight_result = "n/a"

        if user_result:
            age, gender = user_result
            self.age.setText(f"Age: {age if age else 'N/A'}")
            self.gender.setText(f"Gender: {gender if gender else 'N/A'}")
        else:
            self.age.setText("Age: N/A")
            self.gender.setText("Gender: N/A")

        if weight_result:
            weight = weight_result[0]
            self.weight.setText(f"Weight: {weight} kg")
        else:
            self.weight.setText("Weight: N/A")

        conn.close()
