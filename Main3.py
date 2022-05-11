from ast import Break
import wave
import matplotlib
from matplotlib.axis import YAxis
from scipy import signal
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from fileinput import filename
from msilib.schema import RadioButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import pysynth_s as guitar
import pysynth_e as epiano
import pysynth_b as grandpiano
import pysynth as toypiano
import scipy 
import soundfile as sf
import sounddevice as sd
import os
from pyqtgraph import PlotWidget
import logo_rc
#import simpleaudio as sa
import time
from PyQt5.QtWidgets import QFileDialog
#import pyaudio
import numpy as np
import atexit
from sympy import false
import pyqtgraph
import matplotlib.pyplot as plot
from msilib.schema import Class
from tkinter import Label
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtGui, QtCore
import sys
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"TASK3TEST66.ui", self)
        ############################################### LOAD UI ####################################################
        self.int=0
        self.scaling_factor= 4410
        self.scaling_factor_i= 0
        self.counter = 0
        self.zoom = 1
        self.fin = 700
        self.size=0
        self.paused=False
        self.volumearray = np.linspace(-65.25, 0, 100)
        self.paused=False
        self.NoteIndex = 0
        self.strings=['e2','a2','d3','g3','b3','e4']
        self.dropDstrings=['d2','a2','d3','g3','b3','e4']
        self.BluesTuning=['d2','g2','d3','g3','b3','d4']
        self.Tunings=[self.strings, self.dropDstrings, self.BluesTuning]
        self.pianonotenames=['c','c#','d','d#','e','f','f#','g','g#','a','a#','b','c5','c#5','d5','d#5','e5','f5','f#5','g5','g#5','a5','a#5','b5','c6']
        self.notefreqs=[130.81,138.59,146.83,155.56,164.81,174.61,185.00,196.00,207.65,220.00,233.08,246.94]
        self.octavemultiplier=[1, 2, 3]
        self.bongo1=r'Bongo1.wav'
        self.bongo2=r'Bongo2.wav'
        
        self.label.setStyleSheet("image: url(:/newPrefix/orange-piano-icon.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Guitar_horizontalSlider = QtWidgets.QSlider(self.Frequency_groupBox)
        self.Guitar_horizontalSlider.setMaximum(100)
        self.Guitar_horizontalSlider.setSliderPosition(50)
        self.Guitar_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Guitar_horizontalSlider.setObjectName("Guitar_horizontalSlider")
        self.gridLayout.addWidget(self.Guitar_horizontalSlider, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Frequency_groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setStyleSheet("image: url(:/newPrefix/guitar-icon-png-7.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Frequency_groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(30, 30))
        self.label_4.setStyleSheet("image: url(:/newPrefix/R (1).png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.Piano_horizontalSlider = QtWidgets.QSlider(self.Frequency_groupBox)
        self.Piano_horizontalSlider.setMaximum(100)
        self.Piano_horizontalSlider.setSliderPosition(50)
        self.Piano_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Piano_horizontalSlider.setObjectName("Piano_horizontalSlider")
        self.gridLayout.addWidget(self.Piano_horizontalSlider, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.Frequency_groupBox, 2, 1, 1, 1)
        self.MainGraph_groupBox = QtWidgets.QGroupBox(self.Music)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.MainGraph_groupBox.setFont(font)
        self.MainGraph_groupBox.setAcceptDrops(False)
        self.MainGraph_groupBox.setFlat(False)
        self.MainGraph_groupBox.setCheckable(False)
        self.MainGraph_groupBox.setObjectName("MainGraph_groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.MainGraph_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.MainGraph_widget = PlotWidget(self.MainGraph_groupBox)
        self.MainGraph_widget.setObjectName("MainGraph_widget")
        self.gridLayout_6.addWidget(self.MainGraph_widget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.MainGraph_groupBox, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.Music)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Volume_horizontalSlider = QtWidgets.QSlider(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Volume_horizontalSlider.setFont(font)
        self.Volume_horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Volume_horizontalSlider.setAutoFillBackground(False)
        self.Volume_horizontalSlider.setMaximum(100)
        self.Volume_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Volume_horizontalSlider.setInvertedAppearance(False)
        self.Volume_horizontalSlider.setInvertedControls(False)
        self.Volume_horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Volume_horizontalSlider.setObjectName("Volume_horizontalSlider")
        self.gridLayout_5.addWidget(self.Volume_horizontalSlider, 2, 1, 1, 2)
        self.Browse_pushbutton = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Browse_pushbutton.setFont(font)
        self.Browse_pushbutton.setStyleSheet("color: rgb(255, 170, 0);\n"
        "color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Places-folder-orange-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Browse_pushbutton.setIcon(icon)
        self.Browse_pushbutton.setObjectName("Browse_pushbutton")
        self.gridLayout_5.addWidget(self.Browse_pushbutton, 4, 0, 1, 3)
        self.Play_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/play-icon-11-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_pushButton.setIcon(icon1)
        self.Play_pushButton.setCheckable(False)
        self.Play_pushButton.setFlat(False)
        self.Play_pushButton.setObjectName("Play_pushButton")
        self.gridLayout_5.addWidget(self.Play_pushButton, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setStyleSheet("image: url(:/newPrefix/speaker-icon-15.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        self.Stop_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/R (6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop_pushButton.setIcon(icon2)
        self.Stop_pushButton.setObjectName("Stop_pushButton")
        self.gridLayout_5.addWidget(self.Stop_pushButton, 0, 2, 1, 1)
        self.Pause_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.Pause_pushButton.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/pause-icon-11-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pause_pushButton.setIcon(icon3)
        self.Pause_pushButton.setFlat(False)
        self.Pause_pushButton.setObjectName("Pause_pushButton")
        self.gridLayout_5.addWidget(self.Pause_pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("R (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Music, icon4, "")
        self.instruments = QtWidgets.QWidget()
        self.instruments.setObjectName("instruments")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.instruments)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.instruments)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 801, 341))
        self.label_5.setStyleSheet("image: url(:/newPrefix/R (2).png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.Drums_pushbutton1 = QtWidgets.QPushButton(self.widget)
        self.Drums_pushbutton1.setGeometry(QtCore.QRect(230, 90, 161, 61))
        self.Drums_pushbutton1.setText("")
        self.Drums_pushbutton1.setFlat(True)
        self.Drums_pushbutton1.setObjectName("Drums_pushbutton1")
        self.Drums_pushButton2 = QtWidgets.QPushButton(self.widget)
        self.Drums_pushButton2.setGeometry(QtCore.QRect(450, 60, 191, 81))
        self.Drums_pushButton2.setText("")
        self.Drums_pushButton2.setFlat(True)
        self.Drums_pushButton2.setObjectName("Drums_pushButton2")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("R (10).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.widget, icon5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 881, 401))
        self.label_7.setStyleSheet("image: url(:/newPrefix/screen-3.webp);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/screen-3.webp"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.PianoTypeCombo =QtWidgets.QComboBox(self.tab_2)
        self.PianoTypeCombo.setGeometry(QtCore.QRect(460, 60, 201, 22))
        self.PianoTypeCombo.addItem("")
        self.PianoTypeCombo.addItem("")
        self.PianoTypeCombo.addItem("")
        self.PianoSustain= QtWidgets.QCheckBox(self.tab_2)
        self.PianoSustain.setGeometry(QtCore.QRect(460, 90, 201, 22))
        self.PianoSustain.setText("Sustain")
        self.C2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.C2_pushbutton.setGeometry(QtCore.QRect(40, 290, 92, 81))
        self.C2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.C2_pushbutton.setStyleSheet("")
        self.C2_pushbutton.setText("")
        self.C2_pushbutton.setFlat(True)
        self.C2_pushbutton.setObjectName("C2_pushbutton")
        self.D2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.D2_pushbutton.setGeometry(QtCore.QRect(120, 290, 92, 81))
        self.D2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.D2_pushbutton.setStyleSheet("")
        self.D2_pushbutton.setText("")
        self.D2_pushbutton.setFlat(True)
        self.D2_pushbutton.setObjectName("D2_pushbutton")
        self.CHash2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.CHash2_pushbutton.setGeometry(QtCore.QRect(80, 170, 92, 91))
        self.CHash2_pushbutton.setText("")
        self.CHash2_pushbutton.setFlat(True)
        self.CHash2_pushbutton.setObjectName("CHash2_pushbutton")
        self.DHash2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.DHash2_pushbutton.setGeometry(QtCore.QRect(170, 170, 93, 91))
        self.DHash2_pushbutton.setText("")
        self.DHash2_pushbutton.setFlat(True)
        self.DHash2_pushbutton.setObjectName("DHash2_pushbutton")
        self.E2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.E2_pushbutton.setGeometry(QtCore.QRect(210, 290, 92, 81))
        self.E2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.E2_pushbutton.setText("")
        self.E2_pushbutton.setFlat(True)
        self.E2_pushbutton.setObjectName("E2_pushbutton")
        self.F2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.F2_pushbutton.setGeometry(QtCore.QRect(290, 300, 92, 71))
        self.F2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.F2_pushbutton.setText("")
        self.F2_pushbutton.setFlat(True)
        self.F2_pushbutton.setObjectName("F2_pushbutton")
        self.FHash2_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.FHash2_pushButton.setGeometry(QtCore.QRect(330, 180, 93, 81))
        self.FHash2_pushButton.setText("")
        self.FHash2_pushButton.setFlat(True)
        self.FHash2_pushButton.setObjectName("FHash2_pushButton")
        self.G2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.G2_pushbutton.setGeometry(QtCore.QRect(380, 290, 92, 81))
        self.G2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.G2_pushbutton.setText("")
        self.G2_pushbutton.setFlat(True)
        self.G2_pushbutton.setObjectName("G2_pushbutton")
        self.GHash2_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.GHash2_pushButton.setGeometry(QtCore.QRect(420, 180, 93, 81))
        self.GHash2_pushButton.setText("")
        self.GHash2_pushButton.setFlat(True)
        self.GHash2_pushButton.setObjectName("GHash2_pushButton")
        self.A2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.A2_pushbutton.setGeometry(QtCore.QRect(460, 300, 92, 71))
        self.A2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.A2_pushbutton.setText("")
        self.A2_pushbutton.setFlat(True)
        self.A2_pushbutton.setObjectName("A2_pushbutton")
        self.AHash2_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.AHash2_pushButton.setGeometry(QtCore.QRect(510, 180, 93, 81))
        self.AHash2_pushButton.setText("")
        self.AHash2_pushButton.setFlat(True)
        self.AHash2_pushButton.setObjectName("AHash2_pushButton")
        self.B2_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.B2_pushbutton.setGeometry(QtCore.QRect(550, 280, 92, 91))
        self.B2_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.B2_pushbutton.setText("")
        self.B2_pushbutton.setFlat(True)
        self.B2_pushbutton.setObjectName("B2_pushbutton")
        self.C3_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.C3_pushbutton.setGeometry(QtCore.QRect(630, 290, 92, 81))
        self.C3_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.C3_pushbutton.setText("")
        self.C3_pushbutton.setFlat(True)
        self.C3_pushbutton.setObjectName("C3_pushbutton")
        self.CHash3_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.CHash3_pushButton.setGeometry(QtCore.QRect(670, 180, 93, 81))
        self.CHash3_pushButton.setText("")
        self.CHash3_pushButton.setFlat(True)
        self.CHash3_pushButton.setObjectName("CHash3_pushButton")
        self.D3_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.D3_pushbutton.setGeometry(QtCore.QRect(720, 290, 92, 81))
        self.D3_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.D3_pushbutton.setText("")
        self.D3_pushbutton.setFlat(True)
        self.D3_pushbutton.setObjectName("D3_pushbutton")
        self.E3_pushbutton = QtWidgets.QPushButton(self.tab_2)
        self.E3_pushbutton.setGeometry(QtCore.QRect(800, 290, 92, 81))
        self.E3_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.E3_pushbutton.setText("")
        self.E3_pushbutton.setFlat(True)
        self.E3_pushbutton.setObjectName("E3_pushbutton")
        self.DHash3_pushButton = QtWidgets.QPushButton(self.tab_2)
        self.DHash3_pushButton.setGeometry(QtCore.QRect(770, 180, 93, 81))
        self.DHash3_pushButton.setText("")
        self.DHash3_pushButton.setFlat(True)
        self.DHash3_pushButton.setObjectName("DHash3_pushButton")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("R (8).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(20, -30, 861, 461))
        self.label_3.setStyleSheet("image: url(:/newPrefix/front-Horizontal-1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.LetRingCheckBox = QtWidgets.QCheckBox(self.tab_3)
        self.LetRingCheckBox.setGeometry(QtCore.QRect(530,120,81,20))
        self.LetRingCheckBox.setText('Let Ring')
        self.TuningLabel = QtWidgets.QLabel(self.tab_3)
        self.TuningLabel.setText('Tuning:')
        self.TuningLabel.setGeometry(QtCore.QRect(770, 130, 55, 16))
        self.TuningCombo = QtWidgets.QComboBox(self.tab_3)
        self.TuningCombo.setGeometry(QtCore.QRect(730, 190, 121, 22))
        self.TuningCombo.addItem("")
        self.TuningCombo.addItem("")
        self.TuningCombo.addItem("")
        self.GuitarE_pushbutton = QtWidgets.QPushButton(self.tab_3)
        self.GuitarE_pushbutton.setGeometry(QtCore.QRect(220, 170, 92, 16))
        self.GuitarE_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.GuitarE_pushbutton.setText("")
        self.GuitarE_pushbutton.setFlat(True)
        self.GuitarE_pushbutton.setObjectName("GuitarE_pushbutton")
        self.GuitarA_pushbutton = QtWidgets.QPushButton(self.tab_3)
        self.GuitarA_pushbutton.setGeometry(QtCore.QRect(270, 180, 92, 16))
        self.GuitarA_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.GuitarA_pushbutton.setText("")
        self.GuitarA_pushbutton.setFlat(True)
        self.GuitarA_pushbutton.setObjectName("GuitarA_pushbutton")
        self.GuitarD_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.GuitarD_pushButton.setGeometry(QtCore.QRect(290, 190, 92, 16))
        self.GuitarD_pushButton.setMinimumSize(QtCore.QSize(92, 0))
        self.GuitarD_pushButton.setText("")
        self.GuitarD_pushButton.setFlat(True)
        self.GuitarD_pushButton.setObjectName("GuitarD_pushButton")
        self.GuitarB_pushbutton = QtWidgets.QPushButton(self.tab_3)
        self.GuitarB_pushbutton.setGeometry(QtCore.QRect(320, 200, 92, 16))
        self.GuitarB_pushbutton.setMinimumSize(QtCore.QSize(92, 0))
        self.GuitarB_pushbutton.setText("")
        self.GuitarB_pushbutton.setFlat(True)
        self.GuitarB_pushbutton.setObjectName("GuitarB_pushbutton")
        self.GuitarG_pushButton = QtWidgets.QPushButton(self.tab_3)
        self.GuitarG_pushButton.setGeometry(QtCore.QRect(360, 210, 92, 16))
        self.GuitarG_pushButton.setMinimumSize(QtCore.QSize(92, 0))
        self.GuitarG_pushButton.setText("")
        self.GuitarG_pushButton.setFlat(True)
        self.GuitarG_pushButton.setObjectName("GuitarG_pushButton")
        



        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("R (9).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_3, icon7, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Notes_comboBox = QtWidgets.QComboBox(self.tab)
        self.Notes_comboBox.setObjectName("Notes_comboBox")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.Notes_comboBox.addItem("")
        self.gridLayout_8.addWidget(self.Notes_comboBox, 0, 0, 1, 1)
        self.sine = QtWidgets.QRadioButton(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sine.setFont(font)
        self.sine.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("002_051_sound_wave_sine_synth_music-128.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sine.setIcon(icon8)
        self.sine.setIconSize(QtCore.QSize(60, 60))
        self.sine.setObjectName("sine")
        self.sine.setChecked(1)
        self.gridLayout_8.addWidget(self.sine, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 2, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_8.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("002_054_sound_wave_square_synth_music-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_2.setIcon(icon9)
        self.radioButton_2.setIconSize(QtCore.QSize(60, 60))
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_8.addWidget(self.radioButton_2, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton, 4, 0, 1, 2)
        self.horizontalSlider = QtWidgets.QSlider(self.tab)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_8.addWidget(self.horizontalSlider, 1, 0, 1, 2)
        self.tabWidget_2.addTab(self.tab, icon8, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("R (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.instruments, icon10, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        #self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setMinimum(1)
        self.Volume_horizontalSlider.valueChanged.connect(self.ChangeSystemVolume)
        self.signal=np.arange(1,10,1)
        self.new_sig=np.array([5])
        self.frequency_interval=1
        self.frequencies=np.array([5])
        self.signal_rfft_Coeff_abs=np.array([5])
        self.total_ts_sec=0
        self.samplerate=44100
        self.data=()
        self.signal_after_gain_1 = np.array([])
        self.signal_after_gain = np.array([])
        self.signal_output_1 = np.array([])
        self.gain_sliders(self.Drums_horizontalSlider)
        self.Drums_horizontalSlider.sliderReleased.connect(lambda:self.Equalizer(10,200,self.Drums_horizontalSlider.value()))
        self.gain_sliders(self.Piano_horizontalSlider)
        self.Piano_horizontalSlider.sliderReleased.connect(lambda:self.Equalizer(250,1290,self.Piano_horizontalSlider.value()))
        self.gain_sliders(self.Guitar_horizontalSlider)
        self.Guitar_horizontalSlider.sliderReleased.connect(lambda:self.Equalizer(1300,5190,self.Guitar_horizontalSlider.value()))
        #self.Volume_horizontalSlider.sliderReleased.connect(self.SeekbarSetter)
        self.Volume_horizontalSlider.setMaximum(99)
        self.show()
      
        
    def Spectrogram(self):
        self.Spectrogram_widget.clear()
        plot.subplot(212)
        plot.figure(figsize=(6,3))
        plot.style.use('dark_background')
        plot.specgram(self.signal, Fs=self.frame_rate)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        plot.axis('off')
        plot.savefig(r'TempSpec.png')
        # self.Spectrogram_widget.getPlotItem().hideAxis('bottom')
        # self.Spectrogram_widget.getPlotItem().hideAxis('left')
        self.Spectrogram_widget.setXRange(75, 540)
        img = pyqtgraph.QtGui.QGraphicsPixmapItem(pyqtgraph.QtGui.QPixmap(r'TempSpec.png'))
        img.scale(1,-1)
        self.Spectrogram_widget.addItem(img)
    
    def SetIndex(self, Gindex):
        self.NoteIndex = Gindex

    def PlayGuitarNote(self):
        LetRing = self.LetRingCheckBox.isChecked()
        global NoteLength
        if LetRing:
            NoteLength = 1
        else:
            NoteLength = 4
        CurrentTuning = self.Tunings[self.TuningCombo.currentIndex()]
        CurrentNote = ((CurrentTuning[self.NoteIndex],NoteLength),)
        guitar.make_wav(CurrentNote, fn = r"CurrentNote.wav")
        filename = r'CurrentNote.wav'
        data, fs = sf.read(filename, dtype='float32')  
        sd.play(data, fs)
    
    def PlayPianoNote(self):
        SustainOn = self.PianoSustain.isChecked()
        global NoteLength
        if SustainOn:
            NoteLength = 1
        else:
            NoteLength = 4
        PianoType=self.PianoTypeCombo.currentIndex()
        CurrentNote = ((self.pianonotenames[self.NoteIndex],NoteLength),)
        if PianoType == 0:
            epiano.make_wav(CurrentNote, fn = r"CurrentNote.wav")
        elif PianoType == 1:
            grandpiano.make_wav(CurrentNote, fn = r"CurrentNote.wav")
        else:
            toypiano.make_wav(CurrentNote, fn = r"CurrentNote.wav")
        filename = r'CurrentNote.wav'
        data, fs = sf.read(filename, dtype='float32')  
        sd.play(data, fs)

    def Synthesizer(self):
        noteindex = self.Notes_comboBox.currentIndex()
        octaveindex = self.comboBox_2.currentIndex()
        resultantfrq = self.notefreqs[noteindex]*self.octavemultiplier[octaveindex]
        p = pyaudio.PyAudio()
        volume = 1
        fs = 44100       
        duration = self.horizontalSlider.value()   
        global samples
        samples=[]
        if self.sine.isChecked() == True:
            samples = (np.sin(2*np.pi*np.arange(fs*duration)*resultantfrq/fs)).astype(np.float32)
        else:
            samples = (signal.square(2 * np.pi * np.arange(fs*duration)*resultantfrq/fs)).astype(np.float32)
        stream = p.open(format=pyaudio.paFloat32,channels=1,rate=fs,output=True)
        stream.write(volume*samples)
        stream.stop_stream()
        stream.close()
        p.terminate()
    
    def BongoPlayer(self, index):
        global bongodata
        global bongofs
        if index == 0:
            bongodata, bongofs = sf.read(self.bongo1, dtype='float32')  
        else:
            bongodata, bongofs = sf.read(self.bongo2, dtype='float32')
        sd.play(bongodata, bongofs)
    
    def Equalizer(self,low, high, gain):    
        if self.Drums_horizontalSlider.value() == 1 & self.Guitar_horizontalSlider.value() == 1 & self.Piano_horizontalSlider.value() == 1: 
            self.signal=self.backup
        Num= len(self.signal)
        self.signal_rfft_Coeff_abs = np.fft.rfft(self.signal)
        self.frequencies = np.fft.rfftfreq(Num, 1 / self.samplerate)
        self.frequency_interval = len(self.frequencies) / (self.samplerate / 2)
        temp=0
        for f in self.frequencies:
            if low < f < high:
                temp=int(self.frequency_interval * f)
                self.signal_rfft_Coeff_abs[temp] = self.signal_rfft_Coeff_abs[temp] * (gain/1.3)
            else:
                pass
        print(self.new_sig)
        print(np.fft.irfft(self.signal_rfft_Coeff_abs))
        self.new_sig = np.fft.irfft(self.signal_rfft_Coeff_abs)
        self.signal=np.int16(self.new_sig)
        self.Spectrogram()

    def gain_sliders(self , Slider ) :
        Slider.setSingleStep(1)
        Slider.setValue(1)
        Slider.setMinimum(0)
        Slider.setMaximum(10)
        return Slider.value()

    def BrowseFiles(self):
        
        global file_name
        file_name=QFileDialog.getOpenFileName(None, str("Browse Files"), None, str("Audio Files (*.wav)"))
        #global wave_object
        #wave_object = sa.WaveObject.from_wave_file(file_name[0])
        raw = wave.open(file_name[0])
        self.signal = raw.readframes(-1)
        self.signal = np.frombuffer(self.signal, dtype ="int16")
        self.backup = self.signal
        self.frame_rate = raw.getframerate()
        #print(self.frame_rate)
        print(len(self.signal))
        time = np.linspace( 0,len(self.signal) / self.frame_rate,num = len(self.signal))
        global x_axis_final
        global y_axis_final
        x_axis=np.array(time)
        x_axis=x_axis.flatten()
        x_axis_final=np.arange(1,len(x_axis),1)
        y_axis=np.array(self.signal)
        y_axis_final=y_axis.flatten()
        self.paused= False
        self.isplayed=False
        self.Play()
       
    def update_plot(self):  
        self.MainGraph_widget.setYRange(np.min(self.signal),np.max(self.signal))
        self.MainGraph_widget.clear()
        if self.counter == 0 :
            self.MainGraph_widget.setXRange(0, self.scaling_factor)
        elif self.counter >= 4410:
            self.MainGraph_widget.setXRange(self.scaling_factor_i, self.scaling_factor)
            self.scaling_factor = self.scaling_factor + 4410 
            self.scaling_factor_i = self.scaling_factor_i + 4410
        elif self.size > 0:
            self.MainGraph_widget.setXRange((self.int + self.size) , (self.fin +self.size))
        self.plt = self.MainGraph_widget.plot(x_axis_final[0:self.counter], y_axis_final[0:self.counter], pen=(255,140,0))
        self.counter = self.counter + 4410
        if self.counter > np.max(x_axis_final):
            self.timer.stop()
            self.counter= 0
    
    def Initialize(self):
        self.int=0
        self.scaling_factor= 4410
        self.scaling_factor_i= 0
        self.counter = 0
        # self.zoom = 1
        # self.fin = 700
        # self.size=0
        self.paused=False
        self.seeker=0

    def Pause(self):
        self.timer.stop()
        #play_object.pause()
        sd.stop()
        self.paused=True
        self.isplayed=False

    def Play(self):
        global play_object
        if self.isplayed==True:
            return
        else:
            if self.paused==True:
                #play_object.resume()
                sd.play(self.signal[self.seeker:-1], self.frame_rate)
                self.timer.start()
                self.isplayed=True
                self.paused=False
            else:
                self.Initialize()
                self.isplayed=True
                self.MainGraph_widget.clear()
                self.timer.setInterval(100)
                self.timer.timeout.connect(self.update_plot)
                self.timer.timeout.connect(self.seek)
                #self.timer.timeout.connect(self.Seekbar)
                self.timer.start()
                sd.play(self.signal[self.seeker:-1], self.frame_rate)
                #play_object = wave_object.play()
                self.Spectrogram()

    def seek(self):
        self.seeker=int(self.seeker+(self.frame_rate/10))
    
    def Stop(self):
        self.timer.stop()
        self.MainGraph_widget.clear()
        self.Spectrogram_widget.clear()
        #play_object.stop()
        sd.stop()
        self.seeker=0
        self.paused=False
        self.isplayed=False

    # def Seekbar(self):
    #     self.currentlocation = int(self.seeker/len(self.signal))
    #     #print(self.currentlocation)
    #     self.Volume_horizontalSlider.setValue(self.currentlocation)
    
    # def SeekbarSetter(self):
    #     self.location = self.Volume_horizontalSlider.value()
    #     print(self.location)
    #     if self.paused:
    #         self.seeker = int((self.location*len(self.signal))/100)

    def ChangeSystemVolume(self):
        Slider = int(self.Volume_horizontalSlider.value())
        devices2 = AudioUtilities.GetSpeakers()
        interface2 = devices2.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume2 = cast(interface2, POINTER(IAudioEndpointVolume))
        volume2.SetMasterVolumeLevel(self.volumearray[Slider], None)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virtual Instruments and Equalizer"))
        MainWindow.setWindowIcon(QtGui.QIcon('orange-piano-icon.png'))
        self.Spectrogram_groupBox.setTitle(_translate("MainWindow", "Spectrogram"))
        self.Frequency_groupBox.setTitle(_translate("MainWindow", "Frequency Range"))
        self.MainGraph_groupBox.setTitle(_translate("MainWindow", "Music File Graph"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Controls"))
        self.Browse_pushbutton.setText(_translate("MainWindow", "Browse"))
        self.Play_pushButton.setText(_translate("MainWindow", "Play"))
        self.Stop_pushButton.setText(_translate("MainWindow", "Stop"))
        self.Pause_pushButton.setText(_translate("MainWindow", "Pause"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Music), _translate("MainWindow", "Music"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.widget), _translate("MainWindow", "Bongos"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Piano"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Guitar"))
        self.Notes_comboBox.setItemText(0, _translate("MainWindow", "C"))
        self.Notes_comboBox.setItemText(1, _translate("MainWindow", "C#"))
        self.Notes_comboBox.setItemText(2, _translate("MainWindow", "D"))
        self.Notes_comboBox.setItemText(3, _translate("MainWindow", "D#"))
        self.Notes_comboBox.setItemText(4, _translate("MainWindow", "E"))
        self.Notes_comboBox.setItemText(5, _translate("MainWindow", "F"))
        self.Notes_comboBox.setItemText(6, _translate("MainWindow", "F#"))
        self.Notes_comboBox.setItemText(7, _translate("MainWindow", "G"))
        self.Notes_comboBox.setItemText(8, _translate("MainWindow", "G#"))
        self.Notes_comboBox.setItemText(9, _translate("MainWindow", "A"))
        self.Notes_comboBox.setItemText(10, _translate("MainWindow", "A#"))
        self.Notes_comboBox.setItemText(11, _translate("MainWindow", "B"))
        self.PianoTypeCombo.setItemText(0, _translate("MainWindow", "Electric Piano"))
        self.PianoTypeCombo.setItemText(1, _translate("MainWindow", "Grand Piano"))
        self.PianoTypeCombo.setItemText(2, _translate("MainWindow", "Toy Piano"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "3rd Octave"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "4th Octave"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "5th Octave"))
        self.TuningCombo.setItemText(0, _translate("MainWindow", "Standard"))
        self.TuningCombo.setItemText(1, _translate("MainWindow", "Drop D"))
        self.TuningCombo.setItemText(2, _translate("MainWindow", "G Blues"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Synthesizer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.instruments), _translate("MainWindow", "Instruments"))


        
app = QApplication(sys.argv)
UIWindow = UI()
#MainWindow = QtWidgets.QMainWindow()
#MainWindow.show()
app.exec_()        

#if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    
    #sys.exit(app.exec_())