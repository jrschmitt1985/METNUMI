import sys
from PySide2.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.show()

sys.exit(app.exec_())