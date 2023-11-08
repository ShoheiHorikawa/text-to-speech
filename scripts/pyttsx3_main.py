# -*- coding: UTF-8 -*-
import pyttsx3
import time

tstamp = int(time.time())

with open("input_text.txt", "r", encoding="utf-8") as f:
    input = f.read()

def text_to_speech(text):
    engine = pyttsx3.init()
    # engine.say(text)
    engine.save_to_file(text, filename=f"output/output_pyttsx3_{tstamp}.mp3")
    engine.runAndWait()


if __name__=="__main__":
    text_to_speech(input)