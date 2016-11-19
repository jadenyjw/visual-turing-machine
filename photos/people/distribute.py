import os
for i in range(0,3899):
    os.rename(str(i) + ".jpg","train/" + str(i) + ".jpg")
for i in range(3900,5199):
    os.rename(str(i) + ".jpg","crossval/" + str(i) + ".jpg")
for i in range(5200,6499):
    os.rename(str(i) + ".jpg","test/" + str(i) + ".jpg")
