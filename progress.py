from PySide6.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui_progress import Ui_progressDisplay  # This is your generated UI class

class ProgressDisplay(QWidget):
    def __init__(self, database):
        super().__init__()
        self.ui = Ui_progressDisplay()
        self.ui.setupUi(self)

        self.db = database

        # Setup matplotlib graph
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Add the canvas to the progressGraph widget
        layout = QVBoxLayout(self.ui.progressGraph)
        layout.addWidget(self.canvas)

        # Example data
        self.dates = ["2025-01-01", "2025-02-01", "2025-03-01", "2025-04-01"]
        self.one_rm = [100, 110, 115, 120]  # 1RM data (kg)
        self.body_weight = [75, 76, 77, 76.5]  # Body weight data (kg)

        # Connect dropdown to update function
        self.ui.exerciseMenu.currentTextChanged.connect(self.update_graph)

        # Initial graph draw
        self.update_graph()

        # Optional: Increase dropdown size if you want
        self.ui.exerciseMenu.setMinimumSize(200, 40)

    def update_graph(self):
        """Update the graph based on dropdown selection"""
        selected_graph = self.ui.exerciseMenu.currentText()
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        if selected_graph == "exercise 1":
            ax.plot(self.dates, self.one_rm, 'o-', color='blue', label='1RM (kg)')
            ax.set_title("1RM Progress Over Time")
            ax.set_ylabel("Weight (kg)")
        else:
            ax.plot(self.dates, self.body_weight, 'o-', color='green', label='Body Weight (kg)')
            ax.set_title("Body Weight Over Time")
            ax.set_ylabel("Weight (kg)")

        # Shared graph settings
        ax.set_xlabel("Date")
        ax.grid(True)
        ax.legend()

        # Rotate date labels
        for label in ax.get_xticklabels():
            label.set_rotation(45)
            label.set_ha('right')

        self.canvas.draw()
