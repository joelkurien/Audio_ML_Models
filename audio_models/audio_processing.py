from pydub import AudioSegment
import os

class Audio_Processing:
    file_count = 0

    def __init__(self, audio):
        self.audio = audio
    
    def audio_filename(self, audio_file=None):
        if audio_file == None:
            audio_file = self.audio
        fname, fextn= os.path.splitext(audio_file)
        fnamelist = fname.split('.')
        return f".{fnamelist[1]}_{Audio_Processing.file_count}", fextn
    
    def audio_processing(self):
        Audio_Processing.file_count += 1
        new_filename, fextn = self.audio_filename()
        audio_file = AudioSegment.from_file(self.audio)
        file_content = self.audio
        print(fextn)
        if fextn != '.wav':
            file_content = new_filename + '.wav'
            audio_file.export(file_content, format='wav')
        return file_content
        