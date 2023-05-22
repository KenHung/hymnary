from pydub import AudioSegment

# Load the processed audio file using pydub
audio = AudioSegment.from_wav("cut_audio_file.wav")

# Export the audio file as an MP3 file
audio.export("cut_audio_file.mp3", format="mp3")
