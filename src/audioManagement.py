import tensorflow as tf
import tensorflow_io as tfio


@tf.function
def load_wav_16k_mono(file_contents):
    """ Load a WAV file, convert it to a float tensor, resample to 16 kHz single-channel audio. """
    wav, sample_rate = tf.audio.decode_wav(
        file_contents,
        desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    return wav


def load_wav_for_map(filename, label, fold):
    return load_wav_16k_mono(tf.io.read_file(filename)), label, fold
