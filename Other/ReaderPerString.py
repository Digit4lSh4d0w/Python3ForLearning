import os, time, sys

listOfFiles = os.listdir()
listOfBanners = []
timeForWait = 0.1

if 'banner.txt' in listOfFiles:
	listOfBanners.append('banner.txt')
for i in range(101):
	if 'banner(%s).txt'%(i) in listOfFiles:
		listOfBanners.append('banner(%s).txt'%(i))

for z in range(len(listOfBanners)):
	print('%s %s'%(z+1, listOfBanners[z]))

if not listOfBanners:
	sys.exit()

choise = int(input('Какой баннер выводить ?  -->  '))

file = open(str(listOfBanners[choise - 1]), 'r')
strings = file.readlines()
file.close()
while True:
	for s in strings:
		print(s, end='')
		time.sleep(timeForWait)
	print()
	time.sleep(timeForWait)
	print()
	time.sleep(timeForWait)
	print()
	time.sleep(timeForWait)
