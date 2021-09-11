from scipy.io.wavfile import read, write 
from sympy import fwht, ifwht
import numpy as np

#read wav file
sampleRate, data = read("jzone-lunch-breaks.wav")

#fast hadamard
transform = fwht(data)

#tamper with the transform... this is not very efficient 
significant200 = sorted(transform)[:100] + sorted(transform)[-100:]
tamperedTransform = [ x if x in significant200 else 0 for x in transform ]

#inverse fast hadamard
invTransform = ifwht(tamperedTransform)

#write the result
write("result.wav", sampleRate, np.array(invTransform).astype(np.int16))
