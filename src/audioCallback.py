import threading
import src.audioManagement as am
import tensorflow as tf
import io
import scipy.io.wavfile as wav
from IPython import display
import numpy as np
import tensorflow_hub as hub
import pandas as pd
import sounddevice as sd

yamnet_model_handle = 'https://tfhub.dev/google/yamnet/1'
yamnet_model = hub.load(yamnet_model_handle)
class_map_path = yamnet_model.class_map_path().numpy().decode('utf-8')
class_names = list(pd.read_csv(class_map_path)['display_name'])
lock = threading.Lock()


class AudioCallbackThread(threading.Thread):
    indata = ''

    def __init__(self, indata):
        threading.Thread.__init__(self)
        self.indata = indata

    def run(self):
        with lock:
            print("begin treatment")
            fs = 44100
            duration = 2  # seconds
            file = io.BytesIO()
            wav.write(file, fs, self.indata)

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
