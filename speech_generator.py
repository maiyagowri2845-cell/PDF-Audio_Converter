import asyncio

import edge_tts

async def generate_speech(text,output_path, voice = "en-US-AriaNeural",rate="+0%"):
    max_attempts = 3
    for attempt in range(1,max_attempts + 1):
        try:
            communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
            await communicate.save(output_path)
            return
        except Exception as error:
            print(f"Attempt {attempt} failed: {error}")
            if attempt == max_attempts:
                raise
            await asyncio.sleep(2 * attempt)
