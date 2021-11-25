import webbrowser
import os
from PIL import Image
from PIL import ImageGrab
import sys

#webbrowser.open("http://youtube.com", new=1)

#Image.open("Stan.png")

screenshot = ImageGrab.grab()
print(len(screenshot.tobytes()))
a = sys.getsizeof(screenshot)
print(a)
#screenshot.save("screenshots/1.png")
image = open(screenshot, 'rb')

#screenshot.tobytes()
bytes = image.read()
print(len(bytes))
#screenshot.show()



