#Preprocess.py

import librosa as lb
from librosa import feature
import speech_recognition as spr
import numpy as np

def load_vocal_in(vocal_in):
    voice_in, sr_voice_in = lb.load(vocal_in, sr = None)
    voice_mfcc = feature.mfcc(voice_in, sr_voice_in)
    return voice_in, sr_voice_in, voice_mfcc

def vocal_cut(vocal_in):
    array_voice = np.zeros((vocal_in.shape[0] // 1000 + 1, 1000))
    for i in range(array_voice.shape[0]):
        for j in range(1000):
            if (i * 1000 + j) < vocal_in.shape[0]:
                array_voice[i, j] = vocal_in[i * 1000 + j]
            else:
                array_voice[i, j] = 0
    return array_voice


