import sys
from datetime import datetime

from PyQt6.QtWidgets import QLabel, QWidget, QGridLayout, QLineEdit, QApplication, QPushButton


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        birthdate_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.birthdate_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(birthdate_label, 1, 0)
        grid.addWidget(self.birthdate_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        birthdate = self.birthdate_line_edit.text()
        birthyear = datetime.strptime(birthdate, "%m/%d/%Y").date().year
        age = current_year - birthyear
        self.output_label.setText(f"{self.name_line_edit.text()} is {age} years old.")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
