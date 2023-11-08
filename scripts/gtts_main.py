from gtts import gTTS
import time

tstamp = int(time.time())

with open("input_text.txt", "r", encoding="utf-8") as f:
    input = f.read()


def text_to_speech(text):
    language = "ja"
    output = gTTS(text=text, lang=language, slow=False)
    output.save(f"output/output_gtts_{tstamp}.mp3")


if __name__=="__main__":
    text_to_speech(input)
