import voice
from directkey import releasekey, presskey, A

v = voice.VoiceDetector()
while True:
    if v.detect() >= 1:
        presskey(A)
    else:
        releasekey(A)
