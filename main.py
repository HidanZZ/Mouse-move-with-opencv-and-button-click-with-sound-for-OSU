import voice
import objectDetection
from threading import Thread
from directkey import releasekey, presskey, A

detect = objectDetection.ObjectDetection()


def voiceclick():
    v = voice.VoiceDetector()
    while True:
        if v.detect() >= 1:
            presskey(A)
        else:
            releasekey(A)

p2 = Thread(target=voiceclick)
p2.start()
p1 = Thread(target=detect.detect)
p1.start()
p1.join()
p2.join()
