from subprocess import Popen, PIPE
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import subprocess

#IQ is 8 bit unsigned
#all frequency stuff should be double checked and not exact

def rearr(arr): #Used because fft frequencies go from 0->max_freq->-max_freq->-min_freq
	return np.roll(arr,arr.shape[0]/2)

center_freq = 460E6 #Hz #144.0E6
sample_rate=2700000 #Hz
bin_size=65536 #samples

max_freq = sample_rate/2.0
min_freq = sample_rate/float(bin_size)
freqs=center_freq+np.arange(-max_freq,max_freq,min_freq)

dat1 = np.zeros((300,bin_size/50))

process = Popen("rtl_sdr -f %i -g 8 -" % (center_freq),stdout=PIPE,bufsize=-1,shell=True)
for j in range(300):
	print j
	bytestring=process.stdout.read(2*bin_size)
	print time.time()
	arr=np.array([(float(int(e.encode('hex'),16))-127.5) for e in bytestring],dtype=np.complex_).reshape(bin_size,2)
	arr=arr[:,0]+1.0j*arr[:,1]
	dat=np.log(np.sum(rearr(np.abs(np.fft.fft(arr)))[:(bin_size/50)*50].reshape(arr.shape[0]/50,50),1))
	#plt.plot(freqs[::50][:-1],dat)
	#plt.pause(0.001)
	#plt.clf()
	
 	dat1[j]=dat


plt.imshow(dat1)
plt.show()
