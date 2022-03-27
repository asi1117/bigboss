import  sys

from  PyQt5 import  QtWidgets
app=QtWidgets.QApplication(sys.argv)
widget =QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle("hello ,adas")
widget.show()
sys.exit(app.exec_())