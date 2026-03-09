from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

def audio_to_text(audio_path):

    segments, info = model.transcribe(audio_path , language='en')

    text = ""

    print("Detected language:", info.language)

    for segment in segments:
        text += segment.text + " "

    return text