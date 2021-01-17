import numpy as np
import matplotlib.pyplot as plt


def compute_dft_complex(data_in: np.array) -> np.array:
    N = len(data_in)
    data_out = np.zeros(N, dtype=complex)
    for k in range(N):
        s = complex(0)
        for n in range(N):
            angle = 2 * np.pi * n * k / N
            s += data_in[n] * complex(np.cos(angle), -np.sin(angle))
        data_out[k] = s
    return data_out


def compute_idft_complex(data_in: complex) -> np.array:
    N = len(data_in)
    data_out = np.zeros(N, dtype=complex)
    for n in range(N):
        s = 0
        for k in range(N):
            angle = 2 * np.pi * n * k / N
            s += complex(
                data_in[k].real * np.cos(angle) - data_in[k].imag * np.sin(angle),
                data_in[k].real * np.sin(angle) + data_in[k].imag * np.cos(angle),
            )
        data_out[n] = s
    return data_out


# example usage
def main():
    T = 1  # s
    fs = 180  # Hz
    N = T * fs
    dt = 1 / fs
    dfs = fs / N
    print(fs)
    t = np.linspace(0, T, N)
    pure = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)
    noise = np.random.normal(0, 0.5, N)
    signal = pure + noise

    fig, axs = plt.subplots(3)
    fig.suptitle("Pure and noisy signal")

    axs[0].set(ylabel="Amplitude", xlabel="Time [s]")
    axs[0].plot(t, signal)

    # calculate dft of signal with noise
    fft = compute_dft_complex(signal)

    f = np.linspace(0, fs, N)

    axs[1].set(ylabel="Amplitude", xlabel="Frequency [Hz]")

    f_limit = int(N / 2 + 1)
    axs[1].bar(
        f[:f_limit], np.power(np.abs(fft[:f_limit]) / N, 2)
    )  # 1 / N is a normalization factor

    # calculate ifft and plot to check if signal is the same as before dft
    after_dft = compute_idft_complex(fft)
    axs[2].set(ylabel="Amplitude", xlabel="Time [s]")
    axs[2].plot(t, after_dft / N)

    plt.show()


if __name__ == "__main__":
    main()
