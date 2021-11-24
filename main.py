mport matplotlib.pyplot as plt
import matplotlib.image as mp
from pynput.mouse import Listener

img = mp.imread('board.jpg')
imgplot = plt.imshow(img)
plt.show()

def click(x, y, button):
        print(x)
            print(y)
                print(button)


                def on_move(x, y):
                         print ("Mouse moved")
                             
                             def on_click(x, y, button, pressed):
                                     if pressed:
                                                 click(x, y, button)


                                                 with Listener(on_move=on_move, on_click=on_click) as listener:
                                                         listener.join()
