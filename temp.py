import os
f = open('cval_data.txt', 'a')

for (path, dirnames, filenames) in os.walk('/home/jaden/tensorflow/imageclass/photos/people/crossval/'):
    for name in filenames:
        f.write(os.path.join(path, name) + ' 0\n')




for (path, dirnames, filenames) in os.walk('/home/jaden/tensorflow/imageclass/photos/machines/crossval/'):
    for name in filenames:
        f.write(os.path.join(path, name) + ' 1\n')

f = open('train_data.txt', 'a')

for (path, dirnames, filenames) in os.walk('/home/jaden/tensorflow/imageclass/photos/people/train/'):
    for name in filenames:
        f.write(os.path.join(path, name) + ' 0\n')




for (path, dirnames, filenames) in os.walk('/home/jaden/tensorflow/imageclass/photos/machines/train/'):
    for name in filenames:
        f.write(os.path.join(path, name) + ' 1\n')
