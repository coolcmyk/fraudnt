from groqLang import Aiko
from deepgram_tts import synthesize_and_play_text
import asyncio

async def initialize_amadeus():
    amadeus = Aiko('')
    await amadeus.initialize_memory()
    return amadeus

async def main():
    amadeus = await initialize_amadeus()
    while True:
        user_input = input(">")
        amadeus.prompt = user_input
        response = await amadeus.generate()
        synthesize_and_play_text(response)
        print(response)


if __name__ == "__main__":
    asyncio.run(main())