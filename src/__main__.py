import io
import os

from IPython import display
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import src.audioManagement as am
import sounddevice as sd
import tensorflow_hub as hub
import pandas as pd
import time

from src.audioCallback import AudioCallbackThread

fs = 44100
duration = 2  # seconds


def start():
    #myrecording = sd.rec(duration * fs, channels=2, dtype='int16')
    #print("Recording audio")
    #sd.wait()
    #print("done recording")
    while True:
        myrecording = sd.rec(duration * fs, channels=2, dtype='int16')
        sd.wait()
        t1 = AudioCallbackThread(myrecording)
        t1.start()
        t1.join()
        time.sleep(1)

