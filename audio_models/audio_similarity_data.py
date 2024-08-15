import numpy as np
from pydub import AudioSegment
import audio_processing

class AudioNoiseGenerator:
    def add_gaussian_noise(self, audio_file):
        audio = AudioSegment.from_file(audio_file)

        audio_raw_data = np.array(audio.get_array_of_samples())

        audio_channels = audio.channels
        frame_rate = audio.frame_rate

        left_channel = audio_raw_data

        gaussian_noise = np.random.normal(5,15, left_channel.shape)

        noisy_data = audio_raw_data + gaussian_noise
        
        noisy_audio = AudioSegment(
            noisy_data.astype(np.int64).tobytes(),
            frame_rate = frame_rate,
            sample_width = audio.sample_width,
            channels = audio_channels
        )
        
        audio_proc = audio_processing.Audio_Processing(audio_file)
        noise_filename = audio_proc.audio_filename()[0] + '.wav'
        noisy_audio.export(noise_filename, format='wav')
        
        return audio_file

noisyObj = AudioNoiseGenerator()
noisyObj.add_gaussian_noise("./audio_set/blues_1.wav")