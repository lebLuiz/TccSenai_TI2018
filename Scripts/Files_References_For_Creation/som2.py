from struct import pack
from math import sin, pi
import wave
import random

RATE=44100

## GENERATE MONO FILE ##
#wv = wave.open('test_mono.wav', 'w')
#wv.setparams((1, 2, RATE, 0, 'NONE', 'not compressed'))
#maxVol=2**15-1.0 #maximum amplitude
#wvData=""
#for i in range(0, RATE*3):
#	wvData+=pack('h', maxVol*sin(i*5000.0/RATE)) #500Hz
#wv.writeframes(wvData)
#wv.close()

## GENERATE STERIO FILE ##
wv = wave.open('test_stereo.wav', 'w')
wv.setparams((2, 2, RATE, 0, 'NONE', 'not compressed'))
maxVol=2**15-1.0 #maximum amplitude
wvData=""
for i in range(0, RATE*3):
	wvData+=pack('h', maxVol*sin(i*12000.0/RATE)) #500Hz left
	wvData+=pack('h', maxVol*sin(i*15000.0/RATE)) #200Hz right
wv.writeframes(wvData)
wv.close()
