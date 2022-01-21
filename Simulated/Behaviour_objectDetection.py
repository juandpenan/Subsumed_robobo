
from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from Common_information import Server, wait_time, detection_speed,Screen_center,tilt_angle_object

robobo = Robobo(Server)
robobo.connect()


def Obj_Detection():
    dict={}   
    robobo.startObjectRecognition()
    robobo.sayText("Time to Recycle!!",True)
    robobo.moveTiltTo(tilt_angle_object,100,True)
    dict["last_object"] = robobo.readDetectedObject().label
    dict["x_distance"]  = robobo.readDetectedObject().x
    tap = robobo.readTapSensor().x
    while tap == 0 and not (Screen_center - 5 <=dict["x_distance"]<= Screen_center + 5):      
        robobo.moveWheels(detection_speed, -detection_speed)
        dict["last_object"] = robobo.readDetectedObject().label
        dict["x_distance"]  = robobo.readDetectedObject().x
        robobo.wait(wait_time)
        print(dict["last_object"])
        tap = robobo.readTapSensor().x
    robobo.stopMotors()
    robobo.setEmotionTo(Emotions.HAPPY)
    robobo.sayText("One "+robobo.readDetectedObject().label+" Found",False)
    if tap != 0:
        dict["transition"]=5
    else:
        dict["transition"]=2       
    return dict
    

















    
    
























