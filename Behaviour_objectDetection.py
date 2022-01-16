
from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from Common_information import Server, wait_time, detection_speed,Screen_center

robobo = Robobo(Server)
robobo.connect()



def Obj_Detection():
    dict={}   
    robobo.startObjectRecognition()
    robobo.sayText("Time to Recycle!!",True)
    while not (Screen_center - 5 <=robobo.readDetectedObject().x<= Screen_center + 5) :      
        robobo.moveWheels(detection_speed, -detection_speed)
        robobo.wait(wait_time)
    robobo.stopMotors()
    dict["last_object"] = robobo.readDetectedObject().label
    robobo.setEmotionTo(Emotions.HAPPY)
    robobo.sayText("An "+robobo.readDetectedObject().label+" Found",False)
    dict["transition"]=2
    return dict
    
# To test it
#Obj_Detection()
















    
    
























