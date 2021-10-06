import io
import os

from IPython import display
from playsound import playsound
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub
import src.audioManagement as am
import sounddevice as sd
import scipy.io.wavfile as wav

fs = 44100
duration = 5  # seconds

yamnet_model_handle = 'https://tfhub.dev/google/yamnet/1'
yamnet_model = hub.load(yamnet_model_handle)


def start():
    myrecording = sd.rec(duration * fs, channels=2, dtype='int16')
    print("Recording audio")
    sd.wait()
    print("done recording")
    file = io.BytesIO()
    wav.write(file, fs, myrecording)
    class_map_path = yamnet_model.class_map_path().numpy().decode('utf-8')
    class_names = list(pd.read_csv(class_map_path)['display_name'])

    # testing_wav_file_name = os.path.dirname(os.path.abspath(__file__)) + "/../test_data/audio.wav"
    # print(testing_wav_file_name)
    file_contents = file.getvalue()
    testing_wav_data = am.load_wav_16k_mono(file_contents)
    file.close()


    # Play the audio file.
    display.Audio(testing_wav_data, rate=16000)

    scores, embeddings, spectrogram = yamnet_model(testing_wav_data)
    class_scores = tf.reduce_mean(scores, axis=0)
    top_class = tf.argmax(class_scores)
    inferred_class = class_names[top_class]

    print(f'The main sound is: {inferred_class}')
    print(f'The embeddings shape: {embeddings.shape}')
