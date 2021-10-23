from colorpicker import ColorPicker
import sys
from PyQt5 import QtWidgets, uic
from QLed import QLed
import devices as dev


class Smarthome(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("E:\Python\SmartHome\Smarthome.ui", self)

        # Buttons Devices

        win = QtWidgets.QWidget()
        grid = QtWidgets.QGridLayout()
        self.QW_Statusled_1 = QLed(self.ui.QW_Statusled_1, onColour=QLed.Purple, shape=QLed.Square, value=True)
        self.QW_Statusled_2 = QLed(self.ui.QW_Statusled_2, onColour=QLed.Purple, shape=QLed.Square, value=True)


        self.ui.Btn_FridgeOn.clicked.connect(lambda: self.QW_Statusled_1.setOnColour(QLed.Green))
        self.ui.Btn_FridgeOff.clicked.connect(lambda: self.QW_Statusled_1.setOnColour(QLed.Red))
        self.ui.Btn_GTKXB7On.clicked.connect(lambda: self.QW_Statusled_2.setOnColour(QLed.Green))
        self.ui.Btn_GTKXB7Off.clicked.connect(lambda: self.QW_Statusled_2.setOnColour(QLed.Red))


        self.ui.Btn_FridgeOn.clicked.connect(lambda: dev.SwitchDev("AON"))
        self.ui.Btn_FridgeOff.clicked.connect(lambda: dev.SwitchDev("AOff"))
        self.ui.Btn_GTKXB7On.clicked.connect(lambda: dev.SwitchDev("BON"))
        self.ui.Btn_GTKXB7Off.clicked.connect(lambda: dev.SwitchDev("BOff"))

        #ColorPicker
        self.colorpickerAll = ColorPicker(self.ui.W_ColorpickerAll, rgb=(255, 0, 0))
        self.colorpicker1 = ColorPicker(self.ui.W_Colorpicker1, rgb=(255, 255, 0))
        self.colorpicker2 = ColorPicker(self.ui.W_Colorpicker2, rgb=(0, 0, 255))
        self.colorpicker3 = ColorPicker(self.ui.W_Colorpicker3, rgb=(0, 255, 0))


        self.colorpickerAll.colorChanged.connect(self.onColorChangeAll)
        self.colorpicker1.colorChanged.connect(self.onColorChange1)
        self.colorpicker2.colorChanged.connect(self.onColorChange2)
        self.colorpicker3.colorChanged.connect(self.onColorChange3)

        self.SP_Ledband_1.valueChanged.connect(self.show_pin1)
        self.SP_Ledband_2.valueChanged.connect(self.show_pin2)
        self.SP_Ledband_3.valueChanged.connect(self.show_pin3)

        #self.ui.Btn_selectcolor.clicked.connect(self.get_color)
        #self.ui.Btn_selectcolor_2.clicked.connect(self.get_color_2)

    def show_pin1(self):
        value = self.SP_Ledband_1.value()
        self.ui.L_Ledpin1.setText("Ledpin 1: " + str(value))
        return value

    def show_pin2(self):
        value = self.SP_Ledband_2.value()
        self.ui.L_Ledpin2.setText("Ledpin 2: " + str(value))
        return value

    def show_pin3(self):
        value = self.SP_Ledband_3.value()
        self.ui.L_Ledpin3.setText("Ledpin 3: " + str(value))
        return value

    def get_color(self):
        r,g,b = self.colorpicker.getRGB()
        h,s,v = self.colorpicker.getHSV()
        hsv = self.colorpicker.getHSV(360, 1)  # hue in degrees, saturation & value from 0 to 1
        rgb = self.colorpicker.getRGB(100)     # rgb with white = (100,100,100)
        hex = self.colorpicker.getHex(True)    # output with hashtag in string
        print("The Color is: ",r,g,b, "HSV: ", h,s,v)
        print("HSV: ",hsv)
        print("RGB: ",rgb)
        print("HEX: ", hex)
        #print(self.colorpicker.getRGB())
        #print(self.colorpicker.getColor())

    def get_color_2(self):
        r,g,b = self.colorpicker.getRGB()
        h,s,v = self.colorpicker.getHSV()
        hsv = self.colorpicker.getHSV(360, 1)  # hue in degrees, saturation & value from 0 to 1
        rgb = self.colorpicker.getRGB(100)     # rgb with white = (100,100,100)
        hex = self.colorpicker.getHex(True)    # output with hashtag in string
        print("The Color is: ",r,g,b, "HSV: ", h,s,v)
        print("HSV: ",hsv)
        print("RGB: ",rgb)
        print("HEX: ", hex)
        #print(self.colorpicker.getRGB())
        #print(self.colorpicker.getColor())

    def onColorChangeAll(self):
        hex = self.colorpickerAll.getHex(True)
        r,g,b = self.colorpickerAll.getRGB()
        print(r,g,b)
        self.ui.L_ShowColorAll.setText(hex)
        self.ui.L_ShowColorAll.setStyleSheet(f"background-color : rgb({r},{g},{b})")

    def onColorChange1(self):
        r,g,b = self.colorpicker1.getRGB()
        h,s,v = self.colorpicker1.getHSV()
        hex = self.colorpicker1.getHex(True)
        self.ui.L_ShowColor1.setText(hex)

    def onColorChange2(self):
        r,g,b = self.colorpicker2.getRGB()
        h,s,v = self.colorpicker2.getHSV()
        hex = self.colorpicker2.getHex(True)
        self.ui.L_ShowColor2.setText(hex)

    def onColorChange3(self):
        r,g,b = self.colorpicker3.getRGB()
        h,s,v = self.colorpicker3.getHSV()
        hex = self.colorpicker3.getHex(True)
        self.ui.L_ShowColor3.setText(hex)


    def onOK():
        pass

    def onClose(self):
        print("Bis zum nächsten Mal")
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Smarthome()
    dialog.show()
    sys.exit(app.exec())
