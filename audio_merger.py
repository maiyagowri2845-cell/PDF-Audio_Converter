from pydub import AudioSegment

# def test_audio_processing():
#     print("Pydub imported successfully!")
#
#     audio = AudioSegment.silent(duration=1000)
#
#     print("Audio duration:", len(audio), "milliseconds")
#
#
# if __name__ == "__main__":
#     test_audio_processing()

def merge_audio_files(audio_files, output_path):

    combined_audio = AudioSegment.empty()

    for audio_file in audio_files:
        audio_segment = AudioSegment.from_mp3(audio_file)

        combined_audio += audio_segment

    combined_audio.export(output_path, format="mp3")

    print("Audio files merged successfully!")