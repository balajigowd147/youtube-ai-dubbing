from .audio_extractor import extract_audio
from .speech_to_text import audio_to_text
#from .translator import translate_text
from .text_to_speech import text_to_speech
from .merge_audio_video import merge_audio_video
from .video_downloader import download_youtube_video
def process_video(url):

    audio_path = "ai_dubber/data/audio/extracted.wav"
    output_audio = "ai_dubber/data/outputs/english_audio.wav"
    output_video = "ai_dubber/data/outputs/final_video.mp4"
    # Step 1: Extract audio
    video_path = download_youtube_video(url)

    extract_audio(video_path, audio_path)

    text = audio_to_text(audio_path)
    print("\n--- TRANSCRIPTION SAMPLE ---")
    print(text[:])
    print("-----------------------------")
    # print("Hindi text length:", len(hindi_text))

    
    # Step 4: Convert English text to speech
    text_to_speech(text, output_audio)
    
    merge_audio_video(
    video_path=video_path,
    audio_path=output_audio,
    output_path=output_video
    )

    return output_video