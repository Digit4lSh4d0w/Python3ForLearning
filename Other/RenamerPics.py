import os
import time
import shutil
import hashlib

def hashFile(dirPics,fileOldName,ext):
    contentFile=open(dirPics+fileOldName,'rb')
    newName=hashlib.sha256(contentFile.read()).hexdigest()
    contentFile.close()
    return newName+' (Edited by DevRS)'+'.'+ext

PICS_EXTENSION=['jpg', 'psd', 'tiff', 'bmp', 'jpeg', 'jp2', 'j2k', 'jpf', 'jpm', 'jpg2', 'j2c', 'jpc', 'jxr', 'hdp', 'wdp', 'gif', 'eps', 'png', 'pict', 'pcx', 'cdr', 'ai', 'raw', 'svg', 'webp']
time=time.ctime().split()
del time[0]
del time[2]

userName=os.getlogin()
inDirPics='/home/'+userName+'/Pictures/'
outDirPics='/home/'+userName+'/Desktop/newNamedPics('+time[1]+' '+time[0]+' '+time[2]+')/'
inFiles=os.listdir(inDirPics)

try:
    os.mkdir(outDirPics)
except FileExistsError:
    print('Директория вывода уже существует')

for line in inFiles:
    fileExt=line.split('.')[-1]
    for ext in PICS_EXTENSION:
        if fileExt==ext:
            hashName=hashFile(inDirPics,line,fileExt)
            shutil.copy(inDirPics+line,outDirPics)
            os.rename(outDirPics+line,outDirPics+hashName)
            print(line+' : \n'+hashName)
