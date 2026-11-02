
import asyncio
import tempfile
from pathlib import Path

import streamlit as st

from pdf_extractor import extract_text_from_pdf
from text_processor import make_text_clean, convert_to_chunks
from speech_generator import generate_speech
from audio_merger import merge_audio_files


# Page configuration
st.set_page_config(
    page_title="PDF to Audiobook",
    page_icon="🎧",
    layout="centered"
)


# Application title
st.title("🎧 PDF to Audiobook")
st.write("Convert your PDF documents into audiobooks.")


# Voice options
voice_options = {
    "Aria (US English - Female)": "en-US-AriaNeural",
    "Guy (US English - Male)": "en-US-GuyNeural",
    "Jenny (US English - Female)": "en-US-JennyNeural",
    "Sonia (British English - Female)": "en-GB-SoniaNeural",
    "Ryan (British English - Male)": "en-GB-RyanNeural"
}


# PDF upload
uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"]
)


# Voice selection
selected_voice = st.selectbox(
    "Choose narration voice",
    options=list(voice_options.keys())
)


# Speech speed
speech_speed = st.slider(
    "Speech speed",
    min_value=-50,
    max_value=50,
    value=0,
    step=5,
    format="%d%%"
)


async def generate_audiobook(chunks, output_dir, voice, rate, progress_bar):

    audio_files = []

    for index, chunk in enumerate(chunks, start=1):

        chunk_path = output_dir / f"chunk_{index}.mp3"

        await generate_speech(
            chunk,
            str(chunk_path),
            voice=voice,
            rate=rate
        )

        audio_files.append(str(chunk_path))

        progress = index / len(chunks)
        progress_bar.progress(
            progress,
            text=f"Generating audio: {index}/{len(chunks)} chunks"
        )

    final_audio_path = output_dir / "audiobook.mp3"

    merge_audio_files(
        audio_files,
        str(final_audio_path)
    )

    return final_audio_path


# Generate audiobook
if st.button("Generate Audiobook", type="primary"):

    if uploaded_file is None:
        st.warning("Please upload a PDF first.")

    else:

        progress_bar = st.progress(0, text="Preparing your PDF...")

        try:
            with tempfile.TemporaryDirectory() as temp_folder:

                temp_dir = Path(temp_folder)

                # Save uploaded PDF temporarily
                pdf_path = temp_dir / uploaded_file.name
                pdf_path.write_bytes(uploaded_file.getvalue())

                # Extract text
                extracted_text = extract_text_from_pdf(pdf_path)

                # Clean text
                cleaned_text = make_text_clean(extracted_text)

                # Split into chunks
                chunks = convert_to_chunks(
                    cleaned_text,
                    max_len=3000
                )

                if not chunks:
                    st.error("No readable text found in this PDF.")
                    st.stop()

                st.info(f"PDF processed into {len(chunks)} audio chunks.")

                # Generate and merge audio
                output_dir = temp_dir / "audio"
                output_dir.mkdir()

                selected_voice_id = voice_options[selected_voice]
                rate = f"{speech_speed:+d}%"

                final_audio_path = asyncio.run(
                    generate_audiobook(
                        chunks,
                        output_dir,
                        selected_voice_id,
                        rate,
                        progress_bar
                    )
                )

                # Read final audiobook before temporary files are removed
                audio_bytes = final_audio_path.read_bytes()

            progress_bar.progress(1.0, text="Audiobook generation completed!")

            st.success("Your audiobook is ready!")

            # Audio playback
            st.subheader("Listen to your audiobook")
            st.audio(audio_bytes, format="audio/mp3")

            # Download audiobook
            st.download_button(
                label="Download Audiobook",
                data=audio_bytes,
                file_name="audiobook.mp3",
                mime="audio/mpeg"
            )

        except Exception as error:
            st.error(f"Something went wrong: {error}")
