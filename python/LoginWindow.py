from PyQt5 import QtWidgets, uic
from python.design.loginScreen import Ui_LoginScreen
from os import getcwd, path
from PyP100 import PyL530


from python.HomeForm import HomeForm


class MainWindow(QtWidgets.QMainWindow, Ui_LoginScreen):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # check if loginInfo.txt exists
        self.setupUi(self)
        fileLoc = getcwd() + "/loginInfo.txt"
        self.btn_Login.clicked.connect(self.login)
        self.homeForm = HomeForm(self)
        if (path.exists(fileLoc) == True):
            with open(fileLoc, "r") as f:
                loginInfo = f.read().split(",")
                self.txt_email.setText(loginInfo[0])
                self.txt_pass.setText(loginInfo[1])
                self.txt_ip.setText(loginInfo[2])
                self.cb_rememberMe.setChecked(True)
                self.login()

        
        

    def login(self):
        email = self.txt_email.text()
        passwd = self.txt_pass.text()
        ip = self.txt_ip.text()
        if (self.cb_rememberMe.isChecked()):
            with open(getcwd() + "/loginInfo.txt", "w") as f:
                f.write(email + "," + passwd + "," + ip)
        try:
            l530 = PyL530.L530(ipAddress=ip, email=email, password=passwd)
            l530.handshake()
            l530.login()
            self.showHomeForm(l530)
        except Exception as e:
            print(e)
            

    def showHomeForm(self, l530):
        self.homeForm.show()
        self.homeForm.setL530(l530)
