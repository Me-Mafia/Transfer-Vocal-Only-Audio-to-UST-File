# Transfer-Vocal-Only-Audio-to-UST-File
## PLAN PART 0: Preprocessing

- load the audio of different sampling rates(the voicebank & the audio), produce the array for the original audio, and separate it by characters.

The basic application of **librosa** is needed. 

## PLAN PART 1: Find the 3 main parts of the statistics

### 1.0 The lyrics and the adjustments for pronunciation 

using **Incision** may be helpful

### 1.1 The MIDI File

**librosa.beat** is needed to detect the tempo as a fast reach. 

### 1.2 The variation of Pitch for each character

## PLAN PART 2: Produce the UST File

Turn to **Utaupy** to change the attribute of the file
