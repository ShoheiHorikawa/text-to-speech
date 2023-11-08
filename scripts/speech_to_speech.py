import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import time

# マイクからの音声をテキストに変換
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    start_time = time.time()  # 開始時間を記録
    audio = r.listen(source)
    end_time = time.time()  # 終了時間を記録

# 音声入力が5秒以上なかった場合
if end_time - start_time < 5:
    text = "マイクに向かって何か喋りかけてください。"
else:
    try:
        text = r.recognize_google(audio, language='ja-JP')
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        text = "うまく聞き取れませんでした。もう一度マイクに向かって喋りかけてください。"
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# テキストを音声に変換
tts = gTTS(text=text, lang='ja')
tts.save('output.mp3')

# 音声を再生
mixer.init()
mixer.music.load('output.mp3')
mixer.music.play()
while mixer.music.get_busy():
    pass
