from ai_dubber.app.pipeline import process_video

if __name__ == "__main__":
    print("Main file started")

    url = input("Enter the video link here")

    result = process_video(url)

    print("Process completed!")
    print("Output saved at:", result)