import platform

if platform.system() == 'Windows':
    filename = 'c:\\Users\\asimpson\\Downloads\\transactions.txt'
elif platform.system() == 'Linux':
    filename = '/mnt/c/Users/asimpson/Downloads/transactions.txt'
else:
    exit('I don\'t know who i am', platform.system())

print('Opened file', filename)

with open(filename) as f:
    read_data = f.read()
f.closed
