from unrar import rarfile
from brute import brute

# Iterate over *only* numbers (0 - 9).
for s in brute(start_length=4, length=4, letters=False, numbers=True, symbols=False):
    print(s)

#r = rarfile.RarFile('./second.rar')
#r.printdir()
#r.extractall(pwd='koko')


