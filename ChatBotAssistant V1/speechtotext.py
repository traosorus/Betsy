import pyaudio
import wave
from pydub import AudioSegment
import openai


# set the name of the output file
output_file = "output.mp3"

# set the chunk size and sample rate
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# create the PyAudio object
audio = pyaudio.PyAudio()

# start recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Recording audio...")

frames = []

# loop through the stream and append each chunk to the frames list
for i in range(0, int(RATE / CHUNK * 5)):
    data = stream.read(CHUNK)
    frames.append(data)

# stop recording
stream.stop_stream()
stream.close()
audio.terminate()

print("Finished recording.")

# save the recorded audio to a WAV file
wave_file = wave.open("output.wav", "wb")
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b"".join(frames))
wave_file.close()

# convert the WAV file to MP3 using pydub
audio_file = AudioSegment.from_wav("output.wav")
audio_file.export(output_file, format="mp3")

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
openai.api_key = "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"
audio_file= open("output.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print(transcript)