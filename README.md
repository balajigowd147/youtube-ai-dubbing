# YouTube AI Dubbing 

This project automatically translates and dubs videos into English using AI.

# Features

* Extract audio from video
* Convert speech to text
* Translate text
* Generate speech using Text-to-Speech
* Replace original audio with generated audio

## Project Structure

```
youtube-ai-dubbing
│
├── ai_dubber
│   ├── app
│   │   ├── audio_extractor.py
│   │   ├── pipeline.py
│   │   ├── speech_to_text.py
│   │   ├── text_to_speech.py
│   │   └── translator.py
│   │
│   └── main.py
│
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```
git clone https://github.com/balajigowd147/youtube-ai-dubbing.git
cd youtube-ai-dubbing
```

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the pipeline:

```
python ai_dubber/main.py
```

## Pipeline Workflow

1. Extract audio from video
2. Convert speech to text
3. Translate the text
4. Generate speech from translated text
5. Combine generated audio with video

## Future Improvements

* Automatic language detection
* Voice cloning
* Web interface

---

Made with Python and AI.
