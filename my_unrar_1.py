from unrar import rarfile

r = rarfile.RarFile('./first.rar')
r.printdir()
r.extractall()


