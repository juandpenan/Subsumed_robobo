from ast import If
from multiprocessing.connection import wait
from pickle import FALSE
from matplotlib.pyplot import flag
from robobopy.Robobo import Robobo
from robobopy.utils.Acceleration import Acceleration
# from robobopy.utils.Blob import Blob
# from robobopy.utils.Color import Color
# from robobopy.utils.BlobColor import BlobColor
# from robobopy.utils.ConnectionState import ConnectionState
from robobopy.utils.DetectedObject import DetectedObject
# from robobopy.utils.Emotions import Emotions
# from robobopy.utils.Face import Face
from robobopy.utils.IR import IR
# from robobopy.utils.Lanes import LaneBasic
# from robobopy.utils.LED import LED
# from robobopy.utils.Lines import Lines
# from robobopy.utils.Message import Message
# from robobopy.utils.Note import Note
from robobopy.utils.Orientation import Orientation
from robobopy.utils.QRCode import QRCode
from robobopy.utils.Sounds import Sounds
# from robobopy.utils.StatusFrequency import StatusFrequency
# from robobopy.utils.Tag import Tag
# from robobopy.utils.Tap import Tap
# el sensor de posicion parece no sguir la mano derecha juh
from robobopy.utils.Wheels import Wheels

# Caliberar el .X porque no se cuanto es la cantidad de pixeles, este va hasta 100 por lo que use 50 e igual la velocidad
robobo = Robobo("localhost")
robobo.connect()

robobo.startObjectRecognition()

robobo.moveWheelsByTime(50,-50,5,False)
robobo.stopMotors()
print(robobo.readWheelSpeed(Wheels.L))   












    
    








#robobo.readPanLastTime()















