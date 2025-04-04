from PySide6.QtWidgets import QWidget
from ui_goalwidget import Ui_goalwidgetDisplay
class goalwidgetDisplay(Ui_goalwidgetDisplay, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.addgoal.clicked.connect(self.add_goal)
        self.removegoal.clicked.connect(self.remove_goal)
        self.inputGoal.setPlaceholderText("Enter your goal")
        self.inputGoal.setVisible(False)

    def add_goal(self):
        if (self.inputGoal.isVisible()):
        
            text = self.inputGoal.text().strip()
            self.goalList.addItem(text)
            self.inputGoal.setVisible(False)
        
        else:
        
            self.inputGoal.setVisible(True)
        
        
        

    
    def remove_goal(self):
        selected_items = self.goalList.selectedItems()  # Get selected items
        for item in selected_items:
            self.goalList.takeItem(self.goalList.row(item))  # Remove the selected item