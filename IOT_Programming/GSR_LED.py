# -*- coding: utf-8 -*
import RPi.GPIO as GPIO
import time
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
#GOOGLE_CLOUD_SPEECH_CREDENTIALS = r """STT 키 콘텐츠(json 파일 콘텐츠) """

try:
    print("A moment of silence, please...")
    with mic as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
        gcSTT = r.recognize_google(audio, language = 'ko')
        print("Google cloud Speech Recognition thinks you said : " + gcSTT)

        if "불 켜세요" in gcSTT:
            print("LED ON!!")
            GPIO.output(16,True)
        elif "불 끄세요" in gcSTT:
            print("LED OFF!!")
            GPIO.output(16,False)
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
except KeyboardInterrupt:
    GPIO.cleanup()