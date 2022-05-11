from msilib.schema import Class
from tkinter import Label
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtGui, QtCore
import sys
from ast import Break
import wave
import matplotlib
import sys
from msilib.schema import Class
from tkinter import Label
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5 import uic, QtGui, QtCore
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
#import simpleaudio as sa
import time
from PyQt5.QtWidgets import QFileDialog
#import pyaudio
import numpy as np
import atexit
from sympy import false
import pyqtgraph
import matplotlib.pyplot as plot

def exit_handler():
        os.remove(r'CurrentNote.wav')
        os.remove(r'TempSpec.png')
atexit.register(exit_handler)
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        ############################################### LOAD UI ####################################################
        self.timer=QtCore.QTimer()
        self.int=0
        self.scaling_factor= 4410
        self.scaling_factor_i= 0
        self.counter = 0
        self.zoom = 1
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
        uic.loadUi(r"TASK3TEST4.ui", self)
        self.horizontalSlider = QtWidgets.QSlider(self.tab)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_8.addWidget(self.horizontalSlider, 1, 0, 1, 2)
        
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setMinimum(1)
        self.GuitarE_pushbutton.clicked.connect(lambda: self.SetIndex(0))
        self.GuitarE_pushbutton.clicked.connect(self.PlayGuitarNote)
        self.GuitarA_pushbutton.clicked.connect(lambda: self.SetIndex(1))
        self.GuitarA_pushbutton.clicked.connect(self.PlayGuitarNote)
        self.GuitarD_pushButton.clicked.connect(lambda: self.SetIndex(2))
        self.GuitarD_pushButton.clicked.connect(self.PlayGuitarNote)
        self.GuitarG_pushButton.clicked.connect(lambda: self.SetIndex(4))
        self.GuitarG_pushButton.clicked.connect(self.PlayGuitarNote)
        self.GuitarB_pushbutton.clicked.connect(lambda: self.SetIndex(3))
        self.GuitarB_pushbutton.clicked.connect(self.PlayGuitarNote)
        #########################   PIANO CONNECTIONS   #######################
        self.C2_pushbutton.clicked.connect(lambda: self.SetIndex(0))
        self.C2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.CHash2_pushbutton.clicked.connect(lambda: self.SetIndex(1))
        self.CHash2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.D2_pushbutton.clicked.connect(lambda: self.SetIndex(2))
        self.D2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.DHash2_pushbutton.clicked.connect(lambda: self.SetIndex(3))
        self.DHash2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.E2_pushbutton.clicked.connect(lambda: self.SetIndex(4))
        self.E2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.F2_pushbutton.clicked.connect(lambda: self.SetIndex(5))
        self.F2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.FHash2_pushButton.clicked.connect(lambda: self.SetIndex(6))
        self.FHash2_pushButton.clicked.connect(self.PlayPianoNote)
        self.G2_pushbutton.clicked.connect(lambda: self.SetIndex(7))
        self.G2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.GHash2_pushButton.clicked.connect(lambda: self.SetIndex(8))
        self.GHash2_pushButton.clicked.connect(self.PlayPianoNote)
        self.A2_pushbutton.clicked.connect(lambda: self.SetIndex(9))
        self.A2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.AHash2_pushButton.clicked.connect(lambda: self.SetIndex(10))
        self.AHash2_pushButton.clicked.connect(self.PlayPianoNote)
        self.B2_pushbutton.clicked.connect(lambda: self.SetIndex(11))
        self.B2_pushbutton.clicked.connect(self.PlayPianoNote)
        self.C3_pushbutton.clicked.connect(lambda: self.SetIndex(12))
        self.C3_pushbutton.clicked.connect(self.PlayPianoNote)
        self.CHash3_pushButton.clicked.connect(lambda: self.SetIndex(13))
        self.CHash3_pushButton.clicked.connect(self.PlayPianoNote)
        self.D3_pushbutton.clicked.connect(lambda: self.SetIndex(14))
        self.D3_pushbutton.clicked.connect(self.PlayPianoNote)
        self.DHash3_pushButton.clicked.connect(lambda: self.SetIndex(15))
        self.DHash3_pushButton.clicked.connect(self.PlayPianoNote)
        self.E3_pushbutton.clicked.connect(lambda: self.SetIndex(16))
        self.E3_pushbutton.clicked.connect(self.PlayPianoNote)
        ########################## Synth Connections ############################
        self.pushButton.clicked.connect(self.Synthesizer)
        ########################## Bongo Connections ############################
        self.Drums_pushbutton1.clicked.connect(lambda: self.BongoPlayer(0))
        self.Drums_pushButton2.clicked.connect(lambda: self.BongoPlayer(1))
        ########################## EQ Connections ############################
        self.Browse_pushbutton.clicked.connect(self.BrowseFiles)
        self.Play_pushButton.clicked.connect(self.Play)
        self.Pause_pushButton.clicked.connect(self.Pause)
        self.Stop_pushButton.clicked.connect(self.Stop)
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
        self.label = QtWidgets.QLabel(self.Frequency_groupBox)
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setStyleSheet("image: url(:/newPrefix/orange-piano-icon.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Frequency_groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setStyleSheet("image: url(:/newPrefix/guitar-icon-png-7.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Places-folder-orange-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Browse_pushbutton.setIcon(icon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/play-icon-11-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_pushButton.setIcon(icon1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setStyleSheet("image: url(:/newPrefix/speaker-icon-15.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/R (6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Stop_pushButton.setIcon(icon2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/pause-icon-11-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Pause_pushButton.setIcon(icon3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("R (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Music, icon4, "")
        
      
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("R (10).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.widget, icon5, "")
        self.label_7.setStyleSheet("image: url(:/newPrefix/screen-3.webp);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/screen-3.webp"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("R (8).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_2, icon6, "")
        self.label_3.setStyleSheet("image: url(:/newPrefix/front-Horizontal-1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("R (9).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_3, icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("002_051_sound_wave_sine_synth_music-128.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("002_054_sound_wave_square_synth_music-512.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_2.setIcon(icon9)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("R (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.instruments, icon10, "")
        self.tabWidget_2.addTab(self.tab, icon8, "")
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
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()            