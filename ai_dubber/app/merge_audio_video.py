import subprocess


def merge_audio_video(video_path, audio_path, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        output_path
    ]

    subprocess.run(command, check=True)

    print("Video with new audio saved at:", output_path)