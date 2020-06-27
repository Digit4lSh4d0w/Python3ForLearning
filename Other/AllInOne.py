import os, time

EXTENSION = 'txt'
filesInDir = os.listdir()
filesForReading = []
countOfStrings = 0
countOfDublicat = 0
progress = 0
for file in filesInDir:
    if file == "NotClean_FILE_PASSWORDS.txt":
        continue
    elif file.split('.')[-1] == EXTENSION:
        filesForReading.append(file)

def progress(filesForReading, file):
    files = deg = index = progress = 0
    progressBar = ''
    files = len(filesForReading)

    deg = 100/files
    index = filesForReading.index(file) + 1
    progress = deg * index
    progressBar = '[' + '#' * round(progress/2) + '] deg: ' + str(round(progress)) + '%'
    return progressBar

print('##########-FILES-##########')
print(filesForReading)
print('##########-FILES-##########')

newFilePasswords = open('NotClean_FILE_PASSWORDS.txt', 'w')

for file in filesForReading:
    passwords = open(file, 'r')
    try:
        for string in passwords:
            newFilePasswords.write(string)
            countOfStrings += 1
            print('count: %s, file: %s, pass: %s' % (countOfStrings, file, string), end='')
        passwords.close()
        print(progress(filesForReading, file))
        time.sleep(0.1)
    except UnicodeDecodeError:
        continue

newFilePasswords.close()

newFilePasswords = open('NotClean_FILE_PASSWORDS.txt', 'r')

DoneFilePasswords = open('DoneFilePasswords.txt', 'w')
for string in newFilePasswords:
    for secondString in newFilePasswords:
        if string == secondString:
            print(string + ' # ' + secondString, end='')
            countOfDublicat += 1
print('Total dublicats: ' + str(countOfDublicat))

newFilePasswords.close()
