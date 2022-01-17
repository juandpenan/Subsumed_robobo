
from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from Common_information import Server, wait_time, detection_speed,Screen_center,tilt_angle

robobo = Robobo(Server)
robobo.connect()



def Obj_Detection():
    dict={}   
    robobo.startObjectRecognition()
    robobo.sayText("Time to Recycle!!",True)
    robobo.moveTiltTo(tilt_angle,100,True)
    dict["last_object"] = robobo.readDetectedObject().label
    dict["x_distance"]  = robobo.readDetectedObject().x
    #(Screen_center - 5 <=dict["x_distance"]<= Screen_center + 5)
    #and (not (Screen_center - 5 <=dict["x_distance"]) and (not (dict["x_distance"]<= Screen_center + 5))))
    while ((dict["last_object"] != "bottle" and dict["last_object"] != "banana" and dict["last_object"] != "cup" )\
         and robobo.readClapCounter()==0) :      
        robobo.moveWheels(detection_speed, -detection_speed)
        dict["last_object"] = robobo.readDetectedObject().label
        dict["x_distance"]  = robobo.readDetectedObject().x
        robobo.wait(wait_time)
        print(dict["last_object"])
    robobo.stopMotors()
    #dict["last_object"] = robobo.readDetectedObject().label
    robobo.setEmotionTo(Emotions.HAPPY)
    robobo.sayText("An "+robobo.readDetectedObject().label+" Found",False)
    if robobo.readClapCounter()>0:
        dict["transition"]=5
    else:
        dict["transition"]=2       
    return dict
    
# To test it
#Obj_Detection()
















    
    
























