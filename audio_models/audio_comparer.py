import librosa
import audio_processing
import numpy as np

class AudioCompare:
    def __init__(self, org_audio, test_audio):
        self.org_audio = org_audio
        self.test_audio = test_audio
    
    def compare_audio(self):
        org_audio_proc = audio_processing.Audio_Processing(self.org_audio).audio_processing()
        test_audio_proc = audio_processing.Audio_Processing(self.test_audio).audio_processing()

        print(org_audio_proc)
        #org_filename = librosa.ex(org_audio_proc)
        org_y, org_sr = librosa.load(org_audio_proc)
        org_matrix = librosa.feature.mfcc(org_y)

        test_filename = librosa.ex(test_audio_proc)
        test_y, test_sr = librosa.load(test_filename)
        test_matrix = librosa.feature.mfcc(test_y)

        return np.linalg.norm(org_matrix, test_matrix)

if __name__ == '__main__':
    audio_comp = AudioCompare('./audio_set/blues_1.wav', './audio_set/blues_1.wav')
    audio_comp.compare_audio()