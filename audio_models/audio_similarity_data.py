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

        gaussian_noise = np.random.normal(3,10, left_channel.shape)

        noisy_data = audio_raw_data + gaussian_noise

        noisy_audio = AudioSegment(
            noisy_data.tobytes(),
            frame_rate,
            sample_width = audio.sample_width,
            channels = audio_channels
        )
        
        noise_filename = audio_processing.Audio_Processing.audio_filename(audio_file) + '.wav'
        noisy_audio.export(noise_filename, format='wav')
        
        return audio_file

noisyObj = AudioNoiseGenerator()
noisyObj.add_gaussian_noise("./audio_set/blues_1.wav")