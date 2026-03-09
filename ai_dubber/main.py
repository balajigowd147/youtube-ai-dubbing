from ai_dubber.app.pipeline import process_video

if __name__ == "__main__":
    print("Main file started")

    video_path = "ai_dubber/data/uploads/video2.mp4"

    result = process_video(video_path)

    print("Process completed!")
    print("Output saved at:", result)