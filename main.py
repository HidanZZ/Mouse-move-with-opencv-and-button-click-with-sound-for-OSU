import voice
import objectDetection
from multiprocessing import Process
from directkey import releasekey, presskey, A

detect = objectDetection.ObjectDetection()


def voiceclick():
    v = voice.VoiceDetector()
    while True:
        if v.detect() >= 1:
            presskey(A)
        else:
            releasekey(A)


p1 = Process(target=detect.detect())
p2 = Process(target=voiceclick())
p1.start()
p2.start()
p1.join()
p2.join()
