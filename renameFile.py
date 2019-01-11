import os

try:
    os.rename('test1.py', 'test.py')

except:
    print('rename file fail!')

os.rmdir('./dir')
listDir = os.listdir('../')
for dir in listDir:
    print(dir)
