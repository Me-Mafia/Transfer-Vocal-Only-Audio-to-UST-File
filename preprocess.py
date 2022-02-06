#Transfer.py

# Part 0

import librosa as lb
from librosa import feature
import speech_recognition as spr
import numpy as np

def load_vocal_in(vocal_in):
    voice_in, sr_voice_in = lb.load(vocal_in, sr = None)
    voice_mfcc = feature.mfcc(voice_in, sr_voice_in)
    return voice_in, sr_voice_in, voice_mfcc

def vocal_cut(vocal_in):
    array_voice = np.zeros((vocal_in.shape[0] // 160 + 1, 160))
    for i in range(array_voice.shape[0]):
        for j in range(160):
            if (i * 160 + j) < vocal_in.shape[0]:
                array_voice[i, j] = vocal_in[i * 160 + j]
            else:
                array_voice[i, j] = 0
    return array_voice

# 1 - 1 MIDI

def find_pitch(vocal_cut_in):
    pnum = vocal_cut_in.shape[0]; sr_default = 16000
    pitch_out = np.zeros(pnum)
    for i in range(pnum):
        pitch = lb.pyin(vocal_cut_in[i], 65, 2093, sr = sr_default)
        if pitch[1]:
            pitch_out[i] = pitch[0]
    return pitch_out
