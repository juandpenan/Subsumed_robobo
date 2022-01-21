from ast import While
from robobopy.Robobo import Robobo

from Common_information import Server



on_off = True

robobo = Robobo(Server)  
robobo.connect()

robobo.moveWheelsByTime(-80,-80,1.5,True)
robobo.moveWheelsByTime(100,-100,1.75,True)

#robobo.movePanTo(-160,100,True)
# while True:
#     #robobo.movePanTo(160,10,False)
#     print(robobo.readQR())
#     robobo.wait(0.02)
   


