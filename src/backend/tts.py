__author__ = "Idan Talker"
__version__ = "1.0.1"
__maintainer__ = "Idan Talker"
__email__ = ["talkeridan@gmail.com"]
__status__ = "Prototype"

# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks Joe!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")




