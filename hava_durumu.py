
"""
github.com/blalyasar
medium.com/@blalyasar
kaggle.com/blalyasar
twitter.com/blalyasar
blalyasar@gmail.com

"""

import sys
import os
import json
import time
import datetime
import requests
from platform import uname
from pprint import pprint
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPainter, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QRegExp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLCDNumber

print(os.getlogin())

username = uname().node
print(uname().node)


API_key = 'yourapikey'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

class DigitalClock(QLCDNumber):

    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')

        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        grid = QGridLayout()

        clock = DigitalClock()

        now = QDate.currentDate()
        dtday = now.toString(Qt.DefaultLocaleLongDate)
        timelabel = QLabel(dtday)
        timelabel.setAlignment(Qt.AlignCenter)
        timelabel.setFont(QFont("Robota", 10, QFont.Bold))

        button3 = QPushButton('Exit', self)
        button3.clicked.connect(QCoreApplication.instance().quit)
        button3.setFont(QFont("Robota", 10, QFont.Bold))

        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)

        grid.addWidget(clock, 3, 0)
        grid.addWidget(timelabel)
        grid.addWidget(button3)

        self.setLayout(grid)
        
        self.setWindowTitle("for you " + username +" HAVA DURUMU by @blalyasar")
        self.resize(400, 400)

    def createFirstExclusiveGroup(self):
        
        groupBox = QGroupBox("for Turkey")

        qcomboil = QComboBox()
        qcomboil.addItems(self.iller())

        qcomboil.currentTextChanged.connect(self.onActivated)

        self.label11 = QLabel("sıcaklık")
        self.label12 = QLabel("hissedilen")
        self.label13 = QLabel("havadurumu")
        self.label14 = QLabel("RUZGAR")
        self.label15 = QLabel("NEM")
        self.label16 = QLabel("Gökyüzü")

        self.label11.setFont(QFont("Robota", 10, QFont.Bold))
        self.label12.setFont(QFont("Robota", 10, QFont.Bold))
        self.label13.setFont(QFont("Robota", 10, QFont.Bold))
        self.label14.setFont(QFont("Robota", 10, QFont.Bold))
        self.label15.setFont(QFont("Robota", 10, QFont.Bold))
        self.label16.setFont(QFont("Robota", 10, QFont.Bold))

        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()

        hbox.addWidget(self.label11)
        hbox.addWidget(self.label12)
        hbox.addWidget(self.label13)

        hbox1.addWidget(self.label14)
        hbox1.addWidget(self.label15)
        hbox1.addWidget(self.label16)
        

        vbox.addWidget(qcomboil)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)

        groupBox.setLayout(vbox)

        return groupBox


        vbox = QVBoxLayout()

        hbox = QHBoxLayout()
        hbox1 = QHBoxLayout()

        hbox.addWidget(self.label21)
        hbox.addWidget(self.label22)
        hbox.addWidget(self.label23)

        hbox1.addWidget(self.label24)
        hbox1.addWidget(self.label25)
        hbox1.addWidget(self.label26)
            
        vbox.addWidget(qlineedit)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)

        groupBox.setLayout(vbox)

        return groupBox


    def iller(self):

        illerlist = ['Adana','Adıyaman','Afyonkarahisar','Aksaray','Amasya','Ankara','Antalya',
                    'Ardahan','Artvin','Aydın','Ağrı','Balıkesir','Bartın','Batman','Bayburt',
                    'Bilecik','Bingöl','Bitlis','Bolu','Burdur','Bursa','Denizli','Diyarbakır',
                    'Düzce','Edirne','Elazığ','Erzincan','Erzurum','Eskişehir','Gaziantep','Giresun',
                    'Gümüşhane','Hakkari','Hatay','Isparta','Iğdır','Kahramanmaraş','Karabük','Karaman',
                    'Kars','Kastamonu','Kayseri','Kilis','Kocaeli','Konya','Kütahya','Kırklareli',
                    'Kırıkkale','Kırşehir','Malatya','Manisa','Mardin','Mersin','Muğla','Muş',
                    'Nevşehir','Niğde','Ordu','Osmaniye','Rize','Sakarya','Samsun','Siirt',
                    'Sinop','Sivas','Tekirdağ','Tokat','Trabzon','Tunceli','Uşak','Van',
                    'Yalova','Yozgat','Zonguldak','Çanakkale','Çankırı','Çorum','İstanbul',
                    'İzmir','Şanlıurfa','Şırnak']

        return illerlist


    def onActivated(self, text):

        city_name = text
        Final_url = base_url + "appid=" + API_key + "&q=" + city_name
        weather_data = requests.get(Final_url).json()

        try:
            print(weather_data['wind']["deg"])
        except KeyError:
            weather_data['wind']["deg"] = ""
            print(weather_data['wind']["deg"])

        self.label11.setText("sıcaklık:  " +   str(weather_data["main"]["temp"]))
        self.label12.setText("hissedilen sıcaklık:  " +  str(weather_data["main"]["feels_like"]))
        self.label13.setText("havadurumu "+ weather_data['weather'][0]["description"])
        self.label14.setText("RUZGAR "+ str(weather_data['wind']["deg"])+"hızı"+str(weather_data['wind']["speed"]))
        self.label15.setText("NEM:% " + str(weather_data["main"]["humidity"]))
        self.label16.setText("havadaki bulut %"+str(weather_data["clouds"]["all"]))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

