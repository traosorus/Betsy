import pyaudio
import wave
from pydub import AudioSegment
import openai
import platform
import os
import sys
import numpy as np

class Transcriber():
    def __init__(self,durationdisplayer):
     

        # set the name of the output file
        self.output_file = "output.mp3"

        # set the chunk size and sample rate
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100

        # create the PyAudio object
        self.audio = pyaudio.PyAudio()

        # create the widgets
       
        self.label = durationdisplayer
      
   

        self.beep(440, 500)
        self.label.setText("Trés bien un instant s'il vous plait")
        self.start_recording()



    def start_recording(self):

        # start recording
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

        print("Recording audio...")

        self.frames = []

        # start recording


     
        for i in range(0, 10*self.RATE//self.CHUNK):
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)

        # stop recording
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        
       

        print("Finished recording.")
        self.beep(440, 500)

        # save the recorded audio to a WAV file
        wave_file = wave.open("output.wav", "wb")
        wave_file.setnchannels(self.CHANNELS)
        wave_file.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wave_file.setframerate(self.RATE)
        wave_file.writeframes(b"".join(self.frames))
        wave_file.close()

        # convert the WAV file to MP3 using pydub
        audio_file = AudioSegment.from_wav("output.wav")
        audio_file.export(self.output_file, format="mp3")

        # transcribe the audio using OpenAI
        openai.api_key = "API key"
        audio_file = open(self.output_file, "rb")
        self.transcript = openai.Audio.transcribe("whisper-1", audio_file)
        self.label.setText("Trés bien vérifiez si j'ai bien noté votre requête avant de l'envoyer")
        self.transcript = self.transcript.text
    
    def beep(self,frequency, duration):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=44100,
                        output=True)
        samples_per_sec = 44100
        x = np.linspace(0, duration/1000, int(duration * samples_per_sec / 1000), endpoint=False)
        wave = np.sin(2 * np.pi * frequency * x)
        stream.write(wave.astype(np.float32).tobytes())
        stream.stop_stream()
        stream.close()
        p.terminate()

 
        


        
        

 