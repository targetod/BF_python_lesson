from unrar import rarfile

r = rarfile.RarFile('./second.rar')
r.printdir()
r.extractall(pwd='koko')


