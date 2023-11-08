from pathlib import Path
import time
from openai import OpenAI


api_path = "api_key.txt"
with open(api_path, "r", encoding="utf-8") as f:
    api_key = f.read()

client = OpenAI(api_key=api_key)

tstamp = int(time.time())

with open("input_text.txt", "r", encoding="utf-8") as f:
    input = f.read()


def text_to_speech(text):
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=text,
    )
    response.stream_to_file(f"output/output_openai_{tstamp}.mp3")


if __name__ == "__main__":
    text_to_speech(input)