from unrar import rarfile
from brute import brute
import os

def bruteRar(rarFilename, passwords):
    rar = rarfile.RarFile(rarFilename)
    found = False
    count = 1
    for password in passwords:
        try:
            #print(password)
            rar.extractall(pwd=password)
            print("File extracted.")
            print("Password is %s" % password)
            found = True
            break
        except RuntimeError as e:
            #os.system('cls')
            #count = count + 1
            #N = int(count / (10**4) *100)
            #print("This may take some time, please wait...")
            #print("["+ '*'*N + ' '*(100-N) + "]")
            #print("Wrong password %s" % password)
            pass
    if not found:
        print("Password has not been found.")

    



if __name__ == '__main__':
    filename = './third.rar' 
    print("Start brute process")
    pwds = brute(start_length=4, length=4, letters=False, numbers=True, symbols=False, spaces=False)
    print("This may take some time, please wait...")
    bruteRar(filename, pwds)