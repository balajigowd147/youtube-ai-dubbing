from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-hi-en"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)


def translate_text(text):

    chunk_size = 400
    words = text.split()

    translated_chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i+chunk_size])

        inputs = tokenizer(
            chunk,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        translated = model.generate(**inputs)

        english = tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )

        translated_chunks.append(english)

    return " ".join(translated_chunks)