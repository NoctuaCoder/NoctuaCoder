import wave
import math
import struct
import base64
import os

# Audio parameters
sample_rate = 44100
duration = 0.05  # seconds (short click)
frequency = 800.0

# Generate WAV file
filename = "beep.wav"
with wave.open(filename, 'w') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    
    for i in range(int(duration * sample_rate)):
        # Simple sine wave
        value = int(32767.0 * 0.5 * math.sin(2.0 * math.pi * frequency * i / sample_rate))
        data = struct.pack('<h', value)
        wav_file.writeframesraw(data)

# Convert to base64
with open(filename, "rb") as f:
    encoded = base64.b64encode(f.read()).decode('utf-8')
    print(f"data:audio/wav;base64,{encoded}")

# Clean up
os.remove(filename)
