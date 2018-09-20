from subprocess import Popen, PIPE
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import subprocess

#IQ is 8 bit unsigned

#all freq stuff is made up and haxx

center_freq = 460.0E6#144.0E6
rate=2700000
bin_size=65536
time=0.1

max_freq = rate/2.0
min_freq = max_freq/65536

def rearr(arr):
	return np.roll(arr,arr.shape[0]/2)

dat = np.zeros((300,bin_size/100))

process = Popen("rtl_sdr -f %i -g 2 -" % (center_freq),stdout=PIPE,bufsize=-1,shell=True)
for j in range(300):
	bytestring=process.stdout.read(2*bin_size)
	print [(float(int(e.encode('hex'),16))-127.5) for e in bytestring]
# 	arr=np.zeros(bin_size,dtype=np.complex_)
# 	for i in range(bin_size):
# 		arr[i]=1.0*int(bytestring[2*i].encode('hex'),16)+1.0j*int(bytestring[2*i+1].encode('hex'),16)-127.5*(1.0+1.0j)
# 	freqs=center_freq+min_freq*np.arange(-bin_size/2,bin_size/2)
# 	#plt.plot(freqs[::100][:-1],np.log(np.mean(rearr(np.abs(np.fft.fft(arr)))[:(bin_size/100)*100].reshape((bin_size/100,100)),1)))
# 	#plt.pause(0.01)
# 	#plt.clf()
# 	dat[j]=np.log(np.mean(rearr(np.abs(np.fft.fft(arr)))[:(bin_size/100)*100].reshape((bin_size/100,100)),1))


# plt.imshow(dat)
# plt.show()
