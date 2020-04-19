import os, shutil

EXTENSION = 'txt'
arrayForReading = []
listFiles = os.listdir()

for file in listFiles:
	if file.split('.')[-1] == EXTENSION:
		arrayForReading.append(file)

if arrayForReading:
	writeFile = open('allPasswords.txt', 'w')
	for filesForReading in arrayForReading:
		print('\n#%s File: %s'%(arrayForReading.index(filesForReading), arrayForReading[arrayForReading.index(filesForReading)]), end='')
		with open(filesForReading, 'r') as readFile:
			try:
				for line in readFile:
					writeFile.write(line)
			except UnicodeDecodeError:
				print(' WRONG SYMBOL')
	writeFile.close()
else:
	print('No Files Left')
	
#### Очистка паролей от дубликатов

print('Началась очистка списка от мусора')
writeFile = open('allPasswords.txt', 'r')
cleanWriteFile = open('cleanPasswordsFromDublicate', 'w')
for password in writeFile:
	for dublicate in writeFile:
		if writeFile.index(dublicate) == len(writeFile):
			print('Завершено')
			break
		elif dublicate == password:
			continue
		cleanWriteFile.write(dublicate)
writeFile.close()
		
print('''################
Все задания завершены
################
Всего паролей : %s'''%(len(cleanWriteFile)))
cleamWriteFile