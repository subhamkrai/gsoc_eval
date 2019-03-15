import cv2
import numpy as np
import h5py
from scipy.signal import medfilt
from matplotlib import pyplot as plt

f = h5py.File('1541962108935000000_167_838.h5', 'r')

#getting image shape
dset='/AwakeEventData/XMPP-STREAK/StreakImage/streakImageData'
a=f[dset][:]

#getting image height
dset1='/AwakeEventData/XMPP-STREAK/StreakImage/streakImageHeight'
b=f[dset1][:]
#getting image width
dset2='/AwakeEventData/XMPP-STREAK/StreakImage/streakImageWidth'
c=f[dset2][:]

#converts the 1D array into a 2D image
d = np.reshape(a,(*b,*c))

#filters the image
e=medfilt(d)

#displays and save the image
fig1=plt.gcf()
plt.plot(e)
plt.show()
fig1.savefig('image.png')

