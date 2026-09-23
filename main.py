from PyQt6.QtWidgets import QApplication
import sys

from ui_main import GearWindow


app = QApplication(sys.argv)

window = GearWindow()

window.show()

sys.exit(
    app.exec()
)