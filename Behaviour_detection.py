from robobopy.Robobo import Robobo
# from robobopy.utils.Acceleration import Acceleration
# from robobopy.utils.Blob import Blob
# from robobopy.utils.Color import Color
# from robobopy.utils.BlobColor import BlobColor
# from robobopy.utils.ConnectionState import ConnectionState
# from robobopy.utils.DetectedObject import DetectedObject
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
from robobopy.utils.Wheels import Wheels

#Robobo performs a scan of the area, detects and save the location of the current objects. 

robobo = Robobo('localhost')
robobo.connect()

robobo.moveTiltTo(90,20,False)
robobo.startObjectRecognition()
# robobo.movePanTo(-160,20, True)
# robobo.movePanTo(160,20, True)
# robobo.movePanTo(0,20, False)
print(robobo.readDetectedObject())






