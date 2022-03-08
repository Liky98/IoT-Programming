# -*- coding: utf-8 -*
import RPi.GPIO as GPIO
import time
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GOOGLE_CLOUD_SPEECH_CREDENTIALS =r"""{
  "type": "service_account",
  "project_id": "iot-p-project-33506",
  "private_key_id": "59d9d6de03491f7df6c15914c652743723d7d80c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvkTstdTU3vgV6\nDi8/uZpkIYXIdiZ5PMMkIBhxgBn59WHZooiZhE90GUVKFleK2faTOg4WI9a/W9+u\naCmeTXlS8+Btm3UiIIKqcgB5ZkKLzUn3rCZwLHbSzwplpd4g8Fg/Bw8eyDO9cNOG\nAI24cYUWJOyZUDHhlvC7KDK6DP+w0kCwK1o60MeDaqd5zZ2G7CFxOnXtDN4wpv9M\nRzGsl0JuvTCK/hYu2eyf7n1qbX9GXbN7P5QjWfk5J7XjhTgvfOwMFUsexZg7bYTm\nNdn0LYumffaAviPHS7QvBImdW1Gv/KetVFLgBTjEW6a6INu/wjidWHs2YObb+EHU\n+LJKcguHAgMBAAECggEAG8hsx/XLVSXh8f26pmf1sbDIXf+sePUPoHDfzV5LPg4B\nzRH2cezJMgMpvt6oPdXeOlAumHxVaHTegdgD9gQmleT3+ABo2dyxMM3Xm15+W2dC\nNEpuzsOKjjOrXoiQDUBbhqXUU7e00F7Bamw+ARkdyXJQaraRHjTnpYZn+J9D+zQX\nOLnAl2Mq5Ux/gC8SicuiHCL97blmBpSiSloBoBi3z5TcU3AKjJZWBGuv1omVSlYI\nk+5zi6h0z2PvvzRA1bZB2EHQtQ26O/w8weZtIohJub4StZx6Lyadnsjl2d+nKD1b\nyDed3plGDFOPujwwTpCsRl7tcTihwQ6QGifRn92JkQKBgQDj15cJAiNuYObxzfYB\nsCsdqwC90NonjGAG7vNB16hldpXFR7xOTD3ZwBcMD3+4Wm8qDhefZUkvmuPOagry\nnI2cm6SQPAgCruGw6oJgEFZCMc/4sAoUv93+LHuXM0gk76Qg22suv/PmjhfkDbYi\nB+aM3gypfd5hTHxbXxOw9ZiSLwKBgQDFQ8iXMpxbw7emcu5TOJ9lrXb1iA9fL6DG\nR9hklefhO3nXhTRBEbXBTI7jti0MA8TMRakd42mp88DA6g/0tZbUDghkBnKpFNDs\n74CmhSRR6/Vw7O//PYRA2UZbn8Z67c0otaMvFGnF/aYTi0Sf1J2eZFrB/kP/STmR\n3+pLBYj+KQKBgQCsrEMm7Jv1lzLvpuv+M4k5ntOdB5+NwXE1T/rDt7FD1C+Fp+wq\nWtW1JUNSPJzLFp6Q/MUiZBynG3fyg6NwYv1f5wU82oInpmodLl1IeJkm6aF4E9JQ\nD2kqrIOt/4t5krSMwj3k3Ez4OlAY4dtaxyoPMGngOihDDThh9xhxUHAkuQKBgEt1\nA0z62h6r/hsYiZuh5C8zrHZ9Zkvl3x0ZrGfFg95/LrtHQ9bEHH9ldp8aN58J7gSp\nfOhm7itJh2kD37ieoaRZ/dGtObz9rnGDp/WKpnsDxG4+5AsBkA5yTlyMAJNTVZAF\n8vb2WwOWZCnDsytkXCqTfrgIOCB19SScv3WVF3MJAoGAWj7egCmJJHSnw7XG3ufB\nc+nTA2g6spS8NhkRdzvH+320CHhkmo2pjCl8vXQ1UAV0aMv6H7ES/8mUXOf5kL1l\neE6FrRC84s2bcKqhriW+tTLlDME2oBFKMnMu35Rdapxk83xTL/OcTu0fo6cUYN7z\nYJJ6IL3rtOUkgP714p1Oajk=\n-----END PRIVATE KEY-----\n",
  "client_email": "gc-iot-p@iot-p-project-33506.iam.gserviceaccount.com",
  "client_id": "102117428216454425110",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gc-iot-p%40iot-p-project-33506.iam.gserviceaccount.com"
}"""
try:
    print("A moment of silence, please...")
    with mic as source:
        r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
        gcSTT = r.recognize_google_cloud(audio, language = 'ko',credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
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
