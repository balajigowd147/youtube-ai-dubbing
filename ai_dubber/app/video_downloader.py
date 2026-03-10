import yt_dlp
import os

def download_youtube_video(url, output_folder="ai_dubber/data/uploads"):

    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)

    print("Video downloaded at:", video_path)

    return video_path