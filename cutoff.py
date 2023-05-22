import soundfile as sf
import numpy as np

# Open the audio file using soundfile
signal, sample_rate = sf.read("machinepianist_output/hymnary001.wav")

# Compute the magnitude of the audio signal
magnitude = np.abs(signal)

# Set the threshold for cutting off the audio
threshold = 0.001

# Find the index of the last sample above the threshold
cutoff_idx = len(signal) - np.argmax(magnitude[::-1] > threshold)

# Cut off the audio at the index
signal = signal[:cutoff_idx]

# Save the processed audio data back to disk in WAV format
sf.write("cut_audio_file.wav", signal, sample_rate)
