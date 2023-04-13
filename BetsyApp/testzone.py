import pyaudio
import wave
import tkinter as tk
from tkinter import ttk
from threading import Thread


class Recorder:
    def __init__(self):
        self.frames = []
        self.recording = False
        self.playing = False
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 2
        self.fs = 44100
        self.filename = "recording.wav"
        self.p = pyaudio.PyAudio()

        # create GUI
        self.root = tk.Tk()
        self.root.title("Voice Recorder")

        self.duration_label = ttk.Label(self.root, text="00:00:00")
        self.duration_label.pack()

        self.record_button = ttk.Button(self.root, text="Record", command=self.toggle_record)
        self.record_button.pack()

        self.play_button = ttk.Button(self.root, text="Play", command=self.toggle_play)
        self.play_button.pack()

        self.save_button = ttk.Button(self.root, text="Save", command=self.save)
        self.save_button.pack()

        self.progressbar = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progressbar.pack()

        self.root.mainloop()

    def toggle_record(self):
        if not self.recording:
            self.recording = True
            self.record_button.config(text="Stop")
            self.play_button.config(state="disabled")
            self.save_button.config(state="disabled")
            self.progressbar.start(1000)
            self.frames = []
            self.stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs,
                                      frames_per_buffer=self.chunk, input=True)
            t = Thread(target=self.record)
            t.start()
        else:
            self.recording = False
            self.record_button.config(text="Record")
            self.play_button.config(state="normal")
            self.save_button.config(state="normal")
            self.progressbar.stop()
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()

    def record(self):
        while self.recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)

            # update duration label
            duration = len(self.frames) / self.fs
            self.duration_label.config(text=self.format_time(duration))

    def toggle_play(self):
        if not self.playing:
            self.playing = True
            self.record_button.config(state="disabled")
            self.save_button.config(state="disabled")
            self.progressbar.start(1000)
            t = Thread(target=self.play)
            t.start()
        else:
            self.playing = False
            self.record_button.config(state="normal")
            self.save_button.config(state="normal")
            self.progressbar.stop()

    def play(self):
        wf = wave.open(self.filename, "rb")
        stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                              channels=wf.getnchannels(),
                              rate=wf.getframerate(),
                              output=True)
        data = wf.readframes(self.chunk)
        while data and self.playing:
            stream.write(data)
            data = wf.readframes(self.chunk)

            # update progressbar
            duration = wf.getnframes() / wf.getframerate()
            self.progressbar["value"] = (duration / wf.getnframes()) * 100
            self.duration_label.config(text=self.format_time(duration))

        stream.stop_stream()
        stream.close()
        wf.close()

    def save(self):
        wf = wave.open(self.filename, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b"".join(self.frames))
        wf.close()

    @staticmethod
    def format_time(duration):
        minutes = int(duration / 60)
        seconds = int(duration % 60)
        hours = int(duration / 3600)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


if __name__ == "__main__":
    app = Recorder()