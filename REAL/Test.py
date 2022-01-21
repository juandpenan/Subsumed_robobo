from ast import While
from robobopy.Robobo import Robobo

from Common_information import Server



on_off = True

robobo = Robobo(Server)  
robobo.connect()

robobo.moveTiltTo(100,100,True)
robobo.startObjectRecognition()
while True:
    print(robobo.readDetectedObject())
    
   


