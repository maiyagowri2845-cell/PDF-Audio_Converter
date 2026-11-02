# PDF-to-Audiobook Converter

A Python-based application that converts PDF documents into downloadable audiobooks using neural text-to-speech synthesis.

## Features

- Upload PDF documents through a Streamlit web interface.
- Extract text from PDF files using PyMuPDF.
- Clean and preprocess extracted text.
- Split long documents into manageable text chunks.
- Generate speech using Microsoft Edge Text-to-Speech voices through `edge-tts`.
- Select different narration voices and adjust speech speed.
- Track audio generation progress.
- Merge generated audio chunks into a single MP3 file.
- Listen to and download the generated audiobook.

## Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **PDF Processing:** PyMuPDF
- **Text-to-Speech:** Edge TTS
- **Audio Processing:** Pydub
- **Audio Encoding:** FFmpeg

## Project Structure

```text
PDF-to-Audiobook/
│
├── input/
│   └── sample.pdf
│
├── output/
│
├── app.py
├── main.py
├── pdf_extractor.py
├── text_processor.py
├── speech_generator.py
├── audio_merger.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/maiyagowri2845-cell/PDF-Audio_Converter.git
cd PDF-to-Audiobook
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

FFmpeg is required by Pydub for MP3 audio processing.

Download FFmpeg from:

https://ffmpeg.org/download.html

Ensure that the FFmpeg executable is added to your system PATH.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

## Usage

1. Upload a PDF document.
2. Select your preferred narration voice.
3. Adjust the speech speed.
4. Click **Generate Audiobook**.
5. Monitor the generation progress.
6. Listen to the generated audiobook.
7. Download the final MP3 file.

## How It Works

1. **PDF Extraction:** Extracts readable text from the uploaded PDF using PyMuPDF.
2. **Text Preprocessing:** Cleans unnecessary whitespace and formatting.
3. **Text Chunking:** Splits the extracted text into smaller chunks to support speech generation.
4. **Speech Generation:** Converts each text chunk into speech using Edge TTS.
5. **Audio Merging:** Combines the generated MP3 chunks into a single audiobook using Pydub and FFmpeg.
6. **Output:** Provides audio playback and an MP3 download through Streamlit.

## Limitations

- Requires an active internet connection for Edge TTS speech generation.
- Scanned PDFs without an embedded text layer are not currently supported.
- Speech generation time depends on document length and network conditions.

## Future Improvements

- OCR support for scanned PDF documents.
- Additional narration customization.
- Improved text extraction and formatting.
- Support for additional document formats.

## License

This project is intended for educational and personal use. Add an appropriate open-source license before publishing if you want others to reuse or distribute the code.
