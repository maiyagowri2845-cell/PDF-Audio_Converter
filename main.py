import asyncio
from pathlib import Path
from pdf_extractor import extract_text_from_pdf
from text_processor import make_text_clean, convert_to_chunks
from speech_generator import generate_speech
from audio_merger import merge_audio_files

#Getting the proj dir
BASE_DIR = Path(__file__).resolve().parent


async def main():

    try:
        pdf_path = BASE_DIR / "input" / "sample.pdf"

        # Check whether the PDF exists
        if not pdf_path.exists():
            print("Error: PDF file not found.")
            return

        # Extract text
        extracted_text = extract_text_from_pdf(pdf_path)

        # Clean text
        cleaned_text = make_text_clean(extracted_text)

        # Split text into chunks
        chunks = convert_to_chunks(cleaned_text, max_len=3000)

        if not chunks:
            print("Error: No readable text found in the PDF.")
            return

        # Generate audio files
        output_dir = BASE_DIR / "output"
        output_dir.mkdir(exist_ok=True)

        audio_files = []

        for index, chunk in enumerate(chunks, start=1):

            chunk_path = output_dir / f"chunk_{index}.mp3"

            print(f"Generating audio: {index}/{len(chunks)}")

            await generate_speech(chunk, str(chunk_path))

            audio_files.append(str(chunk_path))

            percentage = (index / len(chunks)) * 100
            print(f"Progress: {percentage:.1f}%")

        #Merge audio files
        final_audio_path = output_dir / "audiobook.mp3"

        merge_audio_files(audio_files, str(final_audio_path))

        print("\nAudiobook generation completed!")
        print("Final audiobook:", final_audio_path)

    except FileNotFoundError as error:
        print(f"File error: {error}")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")

    finally:
        print("\nPDF-to-Audiobook process finished.")



#         await generate_speech(
#             chunk,
#             str(chunk_path)
#         )
#
#         audio_files.append(str(chunk_path))
#
#         # Step 5: Merge all audio files
#     final_audio_path = output_dir / "audiobook.mp3"
#
#     merge_audio_files(
#         audio_files,
#         str(final_audio_path)
#     )
#
#     print("\nAudiobook generation completed!")
#     print("Final audiobook:", final_audio_path)

    # await generate_speech(chunks[0],str(output_path))
    #
    # print("Speech generation completed!")
    # print("Audio saved at:", output_path)

# Display results
# print("PDF processing completed!")
# print("Total characters:", len(clean_text))
# print("Total chunks:", len(chunks))
#
# for index, chunk in enumerate(chunks, start=1):
#     print(f"\n--- Chunk {index} ---")
#     print(chunk)

if __name__ == "__main__":
    asyncio.run(main())