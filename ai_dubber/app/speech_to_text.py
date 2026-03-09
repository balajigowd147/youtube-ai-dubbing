from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cuda",
    compute_type="float16"
)

def audio_to_text(audio_path):

    segments, info = model.transcribe(audio_path, task="translate" , beam_size=5)

    print("Detected language:", info.language)

    text_parts = []

    for segment in segments:
        text_parts.append(segment.text)

    return " ".join(text_parts)