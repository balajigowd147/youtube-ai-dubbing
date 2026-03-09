from .audio_extractor import extract_audio
from .speech_to_text import audio_to_text
#from .translator import translate_text
from .text_to_speech import text_to_speech

def process_video(video_path):

    audio_path = "ai_dubber/data/audio/extracted.wav"
    output_audio = "ai_dubber/data/outputs/english_audio.wav"

    # Step 1: Extract audio
    extract_audio(video_path, audio_path)

    text = audio_to_text(audio_path)
    print("\n--- TRANSCRIPTION SAMPLE ---")
    print(text[:])
    print("-----------------------------")
    # print("Hindi text length:", len(hindi_text))

    
    # Step 4: Convert English text to speech
    text_to_speech(text, output_audio)

    return output_audio