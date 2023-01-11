from python.design.tapoHome import Ui_HomeScreen
from PyQt5 import QtWidgets
from PyP100.PyL530 import L530



class HomeForm(QtWidgets.QMainWindow, Ui_HomeScreen):
    def __init__(self, parent=None):
        super(HomeForm, self).__init__(parent)
        self.setupUi(self)
        self.btn_onoff.clicked.connect(self.btnOnOff_click)
        self.btn_saveBrightness.clicked.connect(self.btn_saveBrightness_click)

    def setL530(self, l530: L530):
        self.l530 = l530
        self.updateInfo()


    def updateInfo(self):
        deviceInfo = self.l530.getDeviceInfo()["result"]
        self.lbl_model.setText(deviceInfo["model"])
        self.lbl_type.setText(deviceInfo["type"])
        self.lbl_mac.setText(deviceInfo["mac"])
        self.lbl_overheated.setText(str(deviceInfo["overheated"]))
        
        if (deviceInfo["device_on"]):
            self.status = True
        else:
            self.status = False
        self.lbl_deviceOn.setText(str(self.status))

        self.brightness = deviceInfo["brightness"]
        self.slider_brightness.setValue(self.brightness)
        self.lbl_brightness.setText(str(self.brightness))
        
        self.lbl_hue.setText(str(deviceInfo["hue"]))
        self.lbl_saturation.setText(str(deviceInfo["saturation"]))
        self.lbl_colorTemp.setText(str(deviceInfo["color_temp"]))
        self.lbl_fwver.setText(str(deviceInfo["fw_ver"]))
        
    def btnOnOff_click(self):
        if (self.status):
            self.l530.turnOff()
        else:
            self.l530.turnOn()
        self.updateInfo()


    def btn_saveBrightness_click(self):
        self.brightness = self.slider_brightness.value()
        self.l530.setBrightness(self.brightness)
        self.updateInfo()
