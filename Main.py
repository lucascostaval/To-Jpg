import os
from PIL import Image

class Main:

    def main(self):
        lst = os.listdir('images')
        for i in range(len(lst)):
            im = Image.open("input/"+lst[i])
            rbg_im = im.convert("RGB")
            newName = lst[i]+".jpg"
            rbg_im.save(newName)
            os.rename(newName, "output/"+newName)

            

def run():
    mainObject = Main()
    mainObject.main()

if __name__ == "__main__":
    run()