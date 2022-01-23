#Preprocess.py

import librosa as lb
import speech_recognition as spr

def load_vocal_in(vocal_in):
    voice_in, sr_voice_in = lb.load(vocal_in, sr = None)
    print(max(voice_in))
    return voice_in, sr_voice_in
    



