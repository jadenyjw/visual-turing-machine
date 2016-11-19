import os
for i in range(0,869):
    os.rename(str(i) + ".jpg","train/" + str(i) + ".jpg")
for i in range(870,1159):
    os.rename(str(i) + ".jpg","crossval/" + str(i) + ".jpg")
for i in range(1160,1449):
    os.rename(str(i) + ".jpg","test/" + str(i) + ".jpg")
