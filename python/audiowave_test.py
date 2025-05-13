import numpy as np
from pydub import AudioSegment
from pydub.playback import play
# Settings
sample_rate = 44100
bit_duration = 0.05  # 50ms per bit
frequencies = { '0': 18000, '1': 20000 }
def generate_tone(freq, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(freq * 2 * np.pi * t) * 0.5
    return (tone * 32767).astype(np.int16)
# Convert hex to binary
hex_data = "AF"
bin_data = bin(int(hex_data, 16))[2:].zfill(len(hex_data)*4)
# Generate audio signal
audio = np.concatenate([generate_tone(frequencies[bit], bit_duration) for bit in bin_data])
# Save or play
audio_segment = AudioSegment(
    audio.tobytes(),
    frame_rate=sample_rate,
    sample_width=2,
    channels=1
)
audio_segment.export("hex_data_audio.wav", format="wav")