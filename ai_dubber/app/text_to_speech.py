from gtts import gTTS
from pydub import AudioSegment
import os


def text_to_speech(text, output_path):

    chunk_size = 400
    words = text.split()

    chunks = [
        " ".join(words[i:i+chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

    temp_files = []

    for i, chunk in enumerate(chunks):

        tts = gTTS(text=chunk, lang="en")

        temp_file = f"temp_{i}.mp3"
        tts.save(temp_file)

        temp_files.append(temp_file)

    combined = AudioSegment.empty()

    for file in temp_files:
        audio = AudioSegment.from_mp3(file)
        combined += audio

    combined.export(output_path, format="mp3")

    for file in temp_files:
        os.remove(file)