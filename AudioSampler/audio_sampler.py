import pyaudio
from enum import IntEnum


class SampleRate(IntEnum):
    SAMPLE_RATE_22050 = 22050
    SAMPLE_RATE_44100 = 44100
    SAMPLE_RATE_48000 = 48000
    SAMPLE_RATE_88200 = 88200
    SAMPLE_RATE_96000 = 96000
    SAMPLE_RATE_176400 = 176400
    SAMPLE_RATE_192000 = 192000


class AudioSampler:
    def __init__(self, sample_rate: SampleRate, channels: int, chunk_size: int):
        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk_size = chunk_size
        self.sample_format = pyaudio.paInt16

        self.pa = pyaudio.PyAudio()  # Create an interface to PortAudio
        self.stream = self.pa.open(format=self.sample_format,
                                    channels=self.channels,
                              rate=self.sample_rate,
                              frames_per_buffer=self.chunk_size,
                              input=True)

    def record_chunk(self):
        data = self.stream.read(self.chunk_size, exception_on_overflow=False)
        print(len(data))
        return data

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
