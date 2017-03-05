import time
from espeak import espeak

def speak(message="What is my purpose?"):
    espeak.synth(message)
    time.sleep(10)
