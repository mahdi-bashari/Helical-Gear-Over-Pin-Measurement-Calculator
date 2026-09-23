from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QApplication,
    QMessageBox
)

from PyQt6.QtCore import Qt

from calculator import GearCalculator


class GearWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Helical Gear Over Pin Measurement Calculator"
        )

        self.setMinimumSize(750, 650)

        self.create_ui()
        self.apply_style()


    def create_ui(self):

        main_layout = QVBoxLayout()


        # =============================
        # INPUT SECTION
        # =============================

        input_group = QGroupBox(
            "Input Parameters"
        )

        input_layout = QGridLayout()


        self.module = self.create_input(
            input_layout,
            "Module (m)",
            0,
            "1.8"
        )


        self.teeth = self.create_input(
            input_layout,
            "Number of Teeth (z)",
            1,
            "8"
        )


        self.alpha = self.create_input(
            input_layout,
            "Pressure Angle α (deg)",
            2,
            "20"
        )


        self.beta_degree = self.create_input(
            input_layout,
            "Helix Angle β Degree",
            3,
            "22"
        )


        self.beta_minute = self.create_input(
            input_layout,
            "Helix Angle β Minute",
            4,
            "12"
        )


        self.beta_second = self.create_input(
            input_layout,
            "Helix Angle β Second",
            5,
            "13"
        )


        self.xfactor = self.create_input(
            input_layout,
            "Profile Shift Factor x",
            6,
            "0.5"
        )


        self.manual_pin = self.create_input(
            input_layout,
            "Manual Pin Diameter",
            7,
            "4"
        )


        input_group.setLayout(
            input_layout
        )



        # =============================
        # BUTTON
        # =============================

        self.calculate_btn = QPushButton(
            "CALCULATE"
        )

        self.calculate_btn.clicked.connect(
            self.calculate
        )



        # =============================
        # RESULT SECTION
        # =============================


        result_group = QGroupBox(
            "Calculation Results"
        )


        result_layout = QGridLayout()


        self.result_ideal_pin = QLabel(
            "-"
        )

        self.result_mop_manual = QLabel(
            "-"
        )

        self.result_mop_ideal = QLabel(
            "-"
        )


        result_layout.addWidget(
            QLabel("Ideal Pin Diameter (mm)"),
            0,
            0
        )

        result_layout.addWidget(
            self.result_ideal_pin,
            0,
            1
        )



        result_layout.addWidget(
            QLabel("MOP Manual Pin (mm)"),
            1,
            0
        )

        result_layout.addWidget(
            self.result_mop_manual,
            1,
            1
        )



        result_layout.addWidget(
            QLabel("MOP Ideal Pin (mm)"),
            2,
            0
        )

        result_layout.addWidget(
            self.result_mop_ideal,
            2,
            1
        )


        result_group.setLayout(
            result_layout
        )


        # =============================
        # ADD ALL
        # =============================


        main_layout.addWidget(
            input_group
        )


        main_layout.addWidget(
            self.calculate_btn
        )


        main_layout.addWidget(
            result_group
        )


        self.setLayout(
            main_layout
        )



    def create_input(
            self,
            layout,
            text,
            row,
            default
    ):

        label = QLabel(text)

        edit = QLineEdit()

        edit.setText(default)

        layout.addWidget(
            label,
            row,
            0
        )

        layout.addWidget(
            edit,
            row,
            1
        )

        return edit



    # =============================
    # CALCULATION
    # =============================

    def calculate(self):

        try:

            calculator = GearCalculator(

                module=float(
                    self.module.text()
                ),

                teeth=int(
                    self.teeth.text()
                ),

                pressure_angle=float(
                    self.alpha.text()
                ),

                beta_degree=int(
                    self.beta_degree.text()
                ),

                beta_minute=int(
                    self.beta_minute.text()
                ),

                beta_second=int(
                    self.beta_second.text()
                ),

                profile_shift=float(
                    self.xfactor.text()
                ),

                manual_pin=float(
                    self.manual_pin.text()
                )

            )


            result = calculator.calculate()


            self.result_ideal_pin.setText(
                str(
                    result["Ideal Pin Diameter"]
                )
            )


            self.result_mop_manual.setText(
                str(
                    result["MOP Manual Pin"]
                )
            )


            self.result_mop_ideal.setText(
                str(
                    result["MOP Ideal Pin"]
                )
            )


        except Exception as e:


            QMessageBox.critical(
                self,
                "Calculation Error",
                str(e)
            )



    # =============================
    # STYLE
    # =============================

    def apply_style(self):

        self.setStyleSheet(

        """

        QWidget
        {
            font-family: Segoe UI;
            font-size: 13px;
        }


        QGroupBox
        {
            font-weight: bold;
            border: 1px solid #9aa;
            border-radius: 8px;
            margin-top: 15px;
            padding: 10px;
        }


        QLineEdit
        {
            padding: 6px;
            border-radius: 5px;
            border: 1px solid gray;
        }


        QPushButton
        {
            background-color:#1f6feb;
            color:white;
            padding:10px;
            font-weight:bold;
            border-radius:8px;
        }


        QPushButton:hover
        {
            background-color:#388bfd;
        }


        QLabel
        {
            padding:5px;
        }

        """
        )