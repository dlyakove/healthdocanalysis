import wand
from wand.image import Image

# Converting page into JPG
class extractor():
    def extractImage(self, stri2, stri, file_name, i):
        with Image(filename= file_name + "[0]", resolution=500) as img:
            img.save(filename= stri2 + stri + "temp" + str(i) + ".jpg")
            return img

