
from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from Common_information import Server, wait_time, detection_speed,Screen_center,tilt_angle

robobo = Robobo(Server)
robobo.connect()



def Obj_Detection():
    dict={}   
    robobo.startObjectRecognition()
    robobo.sayText("Time to Recycle!!",True)
    robobo.moveTiltTo(90,100,True)
    dict["last_object"] = robobo.readDetectedObject().label
    dict["x_distance"]  = robobo.readDetectedObject().x
    tap = robobo.readTapSensor().x
    
    #dict["last_object"] != "bottle" and dict["last_object"] != "banana" and dict["last_object"] != "cup" \
           # and tap == 0
    
    while  dict["last_object"]!="bottle" and dict["last_object"]!="cup"  and tap == 0  :      
        robobo.moveWheels(detection_speed, -detection_speed)
        
        dict["x_distance"]  = robobo.readDetectedObject().x
        print(dict["last_object"])
        tap = robobo.readTapSensor().x
        dict["last_object"] = robobo.readDetectedObject().label
        if dict["last_object"] == "person":
            dict["last_object"]="ruido"
        robobo.wait(wait_time)
    robobo.stopMotors()
    #dict["last_object"] = robobo.readDetectedObject().label
    robobo.setEmotionTo(Emotions.HAPPY)
    robobo.sayText("One "+str(dict["last_object"])+" Found",False)
    
        
    if tap != 0:
        dict["transition"]=5
    else:
        dict["transition"]=2       
    return dict
    
















    
    
























