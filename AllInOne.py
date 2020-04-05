import os, shutil

EXTENSION = 'txt'
FilesForReading = []
listFiles = os.listdir()

for file in listFiles:
	if file.split('.')[-1] == EXTENSION:
		FilesForReading.append(file)

if FilesForReading:
	allPass = open('AllPasswords.txt', 'w', encoding='utf-8')
	for file in FilesForReading:
		print('#%s File: %s'%(FilesForReading.index(file), file))
		listOfPasswords = open('%s'%(file), 'r', encoding='utf-8')
		try:
			allPass.write(listOfPasswords.read() + '\n')
		except UnicodeDecodeError:
			print('WRONG SYMBOL')
		listOfPasswords.close()
	allPass.close()
else:
	print('No Files Left')