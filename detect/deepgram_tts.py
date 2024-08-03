# from deepgram import (
#     DeepgramClient,
#     SpeakOptions,
# )
# from playsound import playsound
# import os

# DEEPGRAM_API_KEY = "dcbc3f4cdee4766ffe7446c940293256b2e3aef3"
# # Define the maximum chunk size (in characters) for text chunking
# MAX_CHUNK_SIZE = 100

# input_text = "Our story begins in a peaceful woodland kingdom where a lively squirrel named Frolic made his abode high up within a cedar tree's embrace. He was not a usual woodland creature, for he was blessed with an insatiable curiosity and a heart for adventure. Nearby, a glistening river snaked through the landscape, home to a wonder named Splash - a silver-scaled flying fish whose ability to break free from his water-haven intrigued the woodland onlookers. This magical world moved on a rhythm of its own until an unforeseen circumstance brought Frolic and Splash together. One radiant morning, while Frolic was on his regular excursion, and Splash was making his aerial tours, an unpredictable wave playfully tossed and misplaced Splash onto the riverbank. Despite his initial astonishment, Frolic hurriedly and kindly assisted his new friend back to his watery abode. Touched by Frolic's compassion, Splash expressed his gratitude by inviting his friend to share his world. As Splash perched on Frolic's back, he tasted of the forest's bounty, felt the sun’s rays filter through the colors of the trees, experienced the conversations amidst the woods, and while at it, taught the woodland how to blur the lines between earth and water."

# def chunk_text(text, chunk_size):
#     chunks = []
#     words = text.split()
#     current_chunk = ''
#     for word in words:
#         if len(current_chunk) + len(word) <= chunk_size:
#             current_chunk += ' ' + word
#         else:
#             chunks.append(current_chunk.strip())
#             current_chunk = word
#     if current_chunk:
#         chunks.append(current_chunk.strip())
#     return chunks


# def main():
#     try:
#         # Create a Deepgram client using the API key
#         deepgram = DeepgramClient(api_key= DEEPGRAM_API_KEY)

#         # Choose a model to use for synthesis
#         options = SpeakOptions(
#             model="aura-asteria-en",
#         )

#         # Chunk the text into smaller parts
#         text_chunks = chunk_text(input_text, MAX_CHUNK_SIZE)
        
#         # Synthesize audio for each chunk
#         for i, chunk in enumerate(text_chunks):
#             print(f"\nProcessing chunk {i + 1}...{chunk}\n")
#             filename = f"chunk_{i + 1}.mp3"

#             SPEAK_OPTIONS = {"text": chunk}
        
#             response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
#             playsound(filename, block=True)
#             print(response.to_json(indent=4))
#             os.remove(filename)

#     except Exception as e:
#         print(f"Exception: {e}")

# if __name__ == "__main__":
#     main()


from deepgram import (
    DeepgramClient,
    SpeakOptions,
)
from playsound import playsound
import os

def synthesize_and_play_text(input_text, api_key="dcbc3f4cdee4766ffe7446c940293256b2e3aef3", chunk_size=500):
  """
  This function takes input text, Deepgram API key (optional), and chunk size (optional) as arguments.
  - Chunks the text into smaller parts.
  - Synthesizes audio for each chunk using Deepgram API.
  - Plays the synthesized audio using playsound library.
  - Removes temporary audio files after playback.
  """
  try:
    # Create a Deepgram client using the API key
    deepgram = DeepgramClient(api_key=api_key)

    # Choose a model to use for synthesis
    options = SpeakOptions(
      model="aura-asteria-en",
    )

    # Chunk the text into smaller parts
    text_chunks = chunk_text(input_text, chunk_size)

    # Synthesize audio for each chunk
    for i, chunk in enumerate(text_chunks):
      print(f"\nProcessing chunk {i + 1}...{chunk}\n")
      filename = f"chunk_{i + 1}.mp3"

      SPEAK_OPTIONS = {"text": chunk}

      response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
      playsound(filename, block=True)
      print(response.to_json(indent=4))
      os.remove(filename)

  except Exception as e:
    print(f"Exception: {e}")

# def chunk_text(text, chunk_size):
#   """
#   Helper function to split text into chunks of a specified size.
#   """
#   chunks = []
#   words = text.split()
#   current_chunk = ''
#   for word in words:
#     if len(current_chunk) + len(word) <= chunk_size:
#       current_chunk += ' ' + word
#     else:
#       chunks.append(current_chunk.strip())
#       current_chunk = word
#   if current_chunk:
#     chunks.append(current_chunk.strip())
#   return chunks


import re

def chunk_text(text, chunk_size, remove_enclosed_words=True):
    """
    Helper function to split text into chunks of a specified size while optionally removing words enclosed within asterisks.
    """
    if remove_enclosed_words:
        # Remove words enclosed within asterisks
        text = re.sub(r'\*.*?\*', '', text)

    chunks = []
    words = text.split()
    current_chunk = ''
    for word in words:
        if len(current_chunk) + len(word) <= chunk_size:
            current_chunk += ' ' + word
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


# # Example usage
# if __name__ == "__main__":
#   input_text = "Our story begins in a peaceful woodland kingdom where a lively squirrel named Frolic made his abode high up within a cedar tree's embrace. He was not a usual woodland creature, for he was blessed with an insatiable curiosity and a heart for adventure. Nearby, a glistening river snaked through the landscape, home to a wonder named Splash - a silver-scaled flying fish whose ability to break free from his water-haven intrigued the woodland onlookers. This magical world moved on a rhythm of its own until an unforeseen circumstance brought Frolic and Splash together. One radiant morning, while Frolic was on his regular excursion, and Splash was making his aerial tours, an unpredictable wave playfully tossed and misplaced Splash onto the riverbank. Despite his initial astonishment, Frolic hurriedly and kindly assisted his new friend back to his watery abode. Touched by Frolic's compassion, Splash expressed his gratitude by inviting his friend to share his world. As Splash perched on Frolic's back, he tasted of the forest's bounty, felt the sun’s rays filter through the colors of the trees, experienced the conversations amidst the woods, and while at it, taught the woodland how to blur the lines between earth and water."

#   your_text = input_text
#   synthesize_and_play_text(your_text)
