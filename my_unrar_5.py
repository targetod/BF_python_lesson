from unrar import rarfile
from captcha.image import ImageCaptcha
from PIL import Image
import os

def unRar(rarFilename, password):
    isWrongPass = False
    rar = rarfile.RarFile(rarFilename)   
    #print(password)
    try:
        rar.extractall(pwd=password)
        print("File extracted.")
    except RuntimeError as e:
        print("Wrong password %s. " % password)
        print("Are you robot?")
        isWrongPass = True
    return isWrongPass



def genCaptcha(captcha_text):
    WIDTH=100
    HEIGHT=60
    image_captcha = ImageCaptcha(width=WIDTH, height=HEIGHT, font_sizes=[30])
    image = image_captcha.generate(captcha_text)
    return image
	
	
if __name__ == '__main__':
    filename = './fourth.rar' 
    print("Start captcha program")
	# Should be gen randomly
    captcha_text = "baby8)"
    
	#1wa
    while True:
        passw = input("Enter your password: ")
        status = unRar(filename, passw)
        if status:
            img = genCaptcha(captcha_text)
			# Display the image
            c_img = Image.open(img)
            c_img.show()
            pwd_captcha = ''
            while pwd_captcha != captcha_text:
                pwd_captcha = input("Enter your captcha: ")
            print("Ok. You are not a robot.")
            c_img.close()
        else:
            break
		    
















    