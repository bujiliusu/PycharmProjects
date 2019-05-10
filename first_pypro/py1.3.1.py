try:
    f = open(r'c:\text\qiye.txt')
    print f.read()
finally:
    if f:
        f.close()

with open(r'c:\text\qiye.txt') as fileReader:
    print fileReader.read()
with open(r'c:\text\qiye.txt') as fileReader1:
    for line in fileReader1.readlines():
        print line.strip()
with open(r'c:\text\qiye.txt','w') as fileReader:
    fileReader.write('qiyeqiyeqiye')