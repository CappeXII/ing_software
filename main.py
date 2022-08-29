import sys
from PyQt5.QtWidgets import QApplication

from home.view.VistaLogin import VistaLogin

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vista_home = VistaLogin()
    vista_home.show()
    sys.exit(app.exec_())
