import sys
import os
import wave
import pyaudio
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt, QTimer

class AudioRecorderApp(QDialog):
    def __init__(self):
        super().__init__()


        self.is_recording = False

        self.init_ui()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer_interval = 1000  # Interval in milliseconds
        self.total_time = 0

    def init_ui(self):
        self.setWindowTitle("Enregistreur Vocal")

        layout = QVBoxLayout()

        self.start_button = QPushButton("Démarrer l'enregistrement")
        self.start_button.clicked.connect(self.start_recording)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Arrêter l'enregistrement")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_recording)
        layout.addWidget(self.stop_button)

        self.timer_label = QLabel("Temps écoulé: 00:00")
        layout.addWidget(self.timer_label)

        self.setLayout(layout)

    def start_recording(self):
        if not self.is_recording:
            self.audio = pyaudio.PyAudio()
            self.frames = []
            self.is_recording = True
            self.frames = []
            self.total_time = 0
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.timer.start(self.timer_interval)
            self.audio_stream = self.audio.open(format=pyaudio.paInt16,
                                                channels=1,
                                                rate=44100,
                                                input=True,
                                                frames_per_buffer=1024,
                                                stream_callback=self.callback)

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.audio_stream.stop_stream()
            self.audio_stream.close()
            self.audio.terminate()

            self.save_audio()

    def callback(self, in_data, frame_count, time_info, status):
        if self.is_recording:
            self.frames.append(in_data)
            self.total_time += frame_count / 44100
            return in_data, pyaudio.paContinue
        else:
            return in_data, pyaudio.paComplete

    def update_timer(self):
        minutes = int(self.total_time // 60)
        seconds = int(self.total_time % 60)
        self.timer_label.setText(f"Temps écoulé: {minutes:02d}:{seconds:02d}")

    def save_audio(self):
        output_file = "enregistrement.wav"
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        print(f"Enregistrement sauvegardé sous : {output_file}")

def main():
    app = QApplication(sys.argv)
    window = AudioRecorderApp()
    window.exec_()

if __name__ == "__main__":
    main()
