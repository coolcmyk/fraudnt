voice_id = "5x4OabTaxKEADQiUryOC"
# url = "https://api.elevenlabs.io/v1/text-to-speech/5x4OabTaxKEADQiUryOC"
import subprocess
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
vlc_path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
strtest = ""
ELEVENLABS_API_KEY = "c1a10fb7682265f79ac607c319123fc2"
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)
def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id= voice_id, # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # uncomment the line below to play the audio back
    # Generating a unique file name for the output MP3 file
    save_file_path = f"output.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")
    subprocess.Popen([vlc_path, '--intf', 'dummy', f"output.mp3"], shell=True)
    # Return the path of the saved audio file
    return save_file_path