import librosa
import audio_processing
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class AudioCompare:
    def __init__(self, org_audio, test_audio):
        self.org_audio = org_audio
        self.test_audio = test_audio
    
    def compare_audio(self):
        org_audio_proc = audio_processing.Audio_Processing(self.org_audio).audio_processing()
        test_audio_proc = audio_processing.Audio_Processing(self.test_audio).audio_processing()

        org_y, org_sr = librosa.load(org_audio_proc, sr = None)
        org_matrix = librosa.feature.mfcc(y=org_y, sr=org_sr, n_mfcc=13)

        test_y, test_sr = librosa.load(test_audio_proc)
        test_matrix = librosa.feature.mfcc(y=test_y, sr=test_sr, n_mfcc=13)

        similarity = cosine_similarity(org_matrix.T, test_matrix.T)
        mean_similarity = np.mean(similarity)
        return mean_similarity

if __name__ == '__main__':
    audio_comp = AudioCompare('./audio_set/blues_1.wav', './audio_set/blues_1.wav')
    print(audio_comp.compare_audio())