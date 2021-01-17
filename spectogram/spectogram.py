from AudioSampler.audio_sampler import AudioSampler, SampleRate
from dft.dft import compute_dft_complex
import numpy as np
import matplotlib.pyplot as plt
import struct
import matplotlib.ticker as ticker


def main():
    fs = SampleRate.SAMPLE_RATE_22050
    N = 1024

    asp = AudioSampler(sample_rate=fs, channels=1, chunk_size=N)
    z = np.zeros([5, int(N/2+1)])
    ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x * fs / (N + 1)))

    while True:
        for x in range(5):
            z[x] = np.abs(np.fft.rfft(struct.unpack("{}h".format(N), asp.record_chunk())))
            plt.cla()
            plt.title('MAX VALUE: {} Hz'.format(z[x][1:].argmax() * fs / N))
            plt.ylabel('Amplitude')

            plt.imshow(z.T, aspect='auto')
            plt.gca().yaxis.set_major_formatter(ticks_y)
            plt.gca().invert_yaxis()
            plt.pause(0.0001)


if __name__ == '__main__':
    main()
