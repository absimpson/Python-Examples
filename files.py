# Here's the hard way, where I figure out what system we're on
import platform

if platform.system() == 'Windows':
    filename = 'c:\\Users\\asimpson\\Downloads\\transactions.txt'
elif platform.system() == 'Linux':
    filename = '/mnt/c/Users/asimpson/Downloads/transactions.txt'
else:
    exit('I don\'t know who i am: ' +  platform.system())

print('Opened file', filename)

with open(filename) as f:
    read_data = f.read()
f.closed

# Now try the easier way, with pathlib
from pathlib import Path
print("Home sweet", str(Path.home()))
filename = Path(str(Path.home())+"/Downloads/transactions.txt")
print("Full path:", filename)
print("parent\tstem\tsuffix")
print(str(filename.parent) + "\t" + str(filename.stem) + "\t" + str(filename.suffix))
print("Dir path:", filename.parent)
print("Full name:", filename.name)
print("Stem:", filename.stem)
print("Extension:", filename.suffix)

print(filename.read_text())
