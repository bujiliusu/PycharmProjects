import os
print os.getcwd()
print os.listdir('c:\\')
#os.remove(r'c:\text\qiye1.txt')
print  os.path.isfile(r'c:\text')
print os.path.isabs(r'c:\text')
print os.path.exists(r'c:\text')
print os.path.split(r'c:\text\qiye.txt')
print os.getenv('path')
print os.linesep
print os.stat(r'c:\text/qiye.txt')
print os.path.getsize(r'c:\text/qiye.txt')