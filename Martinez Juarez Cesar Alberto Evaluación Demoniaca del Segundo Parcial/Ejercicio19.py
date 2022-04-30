# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:42:45 2022

@author: cesar
"""  
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
import pyaudio

def Audio(name,tiempo):
    name+=".wav"
    duracion=tiempo
    archivo=name
    audio=pyaudio.PyAudio()
    stream=audio.open(format=pyaudio.paInt16,channels=2,rate=44100,input=True,frames_per_buffer=1024) 					
    print("Grabando ...")
    frames=[]
    for i in range(0,int(44100/1024*duracion)):
    	data=stream.read(1024)
    	frames.append(data)
    print("Grabacion a terminado ᓚᘏᗢ")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    waveFile=wave.open(archivo,'wb')
    waveFile.setnchannels(2)
    waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(44100)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def Abrir():
    from tkinter import filedialog
    root = Tk() 
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg .mp3"),   ("All Files", "*.*")))
    print(f"Cargando {audio_file_name}")
    root.destroy() 
    root.mainloop() 
    return(audio_file_name)

def Señal():
    frame_rate = 48000.0
    infile =Abrir()
    num_samples =48000
    wav_file = wave.open(infile, 'r')
    data = wav_file.readframes(num_samples) 
    wav_file.close()
    data = struct.unpack('{n}h'.format(n=num_samples), data)
    data = np.array(data)
    data_fft = np.fft.fft(data)
    print(data_fft[:8])
    frecuencias = np.abs(data_fft)
    # Se hallan las frecuencias para mostrar
    xf = np.linspace(0.0, 1.0/(2.0*(1.0/num_samples)), num_samples/2)
    print("La frecuencia es {} Hz".format(np.argmax(frecuencias)))
    plt.subplot(2,1,1)
    plt.plot(data[:300])
    plt.title("Señal de audio")
    plt.subplot(2,1,2)
    plt.plot(xf, frecuencias[:num_samples//2])
    plt.title("Frecuencias")
    plt.xlim(0,1200)
    plt.show()

    



