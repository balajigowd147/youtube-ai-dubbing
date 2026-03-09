import subprocess

def extract_audio(video_path, audio_path):

    command = [
    "ffmpeg",
    "-y",
    "-i", video_path,
    "-vn",
    "-ac", "1",
    "-ar", "16000",
    "-acodec", "pcm_s16le",
    audio_path
    ]

    subprocess.run(command, check=True)