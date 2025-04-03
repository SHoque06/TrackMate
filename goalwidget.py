from PySide6.QtWidgets import QWidget
from ui_goalwidget import Ui_goalwidgetDisplay

class goalwidgetDisplay(Ui_goalwidgetDisplay, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = 0
        self.addgoal.clicked.connect(self.add_goal)
        self.removegoal.clicked.connect(self.remove_goal)

    def add_goal(self):
        self.goalList.addItem(f"Goal {self.x}")
        self.x += 1
    
    def remove_goal(self):
        selected_items = self.goalList.selectedItems()  # Get selected items
        for item in selected_items:
            self.goalList.takeItem(self.goalList.row(item))  # Remove the selected item