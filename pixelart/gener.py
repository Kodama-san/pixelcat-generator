from tkinter import *
from PIL import Image
import turtle, os, glob, arts
for f in glob.glob("collection//kitty*.png"):
    os.remove(f)

def draw(times):
    for i in range(times):
        arts.makeArt()
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="kitty" + str(i + 1) + ".eps")
        img = Image.open("kitty" + str(i + 1) + ".eps")
        img.save("collection//kitty" + str(i + 1) + ".png")
        img.close()
        arts.cleaning()

turtle.hideturtle()
times = int(input('Сколько котиков вам надо? '))
print('Ща будут котики!!')
draw(times)

for f in glob.glob("kitty*.eps"):
    os.remove(f)

#for f in glob.glob("collection//kitty*.png"): #открывает все сгенерированные арты отдельными окошками, ломает галерею при большом количестве сгенерированных картинок, используйте на свой страх и риск
    #im = Image.open(f)
    #im.show()
