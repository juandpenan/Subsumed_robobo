from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from robobopy.utils.IR import IR
from Common_information import Server,Collition_distance,Screen_center,nominal_speed,turning_factor,wait_time


robobo = Robobo(Server)
robobo.connect()



def ObjectApproach(last_object):
    
    dict = {}
    robobo.startObjectRecognition()
    robobo.setEmotionTo(Emotions.NORMAL)
    tap = robobo.readTapSensor().x
    while ((robobo.readIRSensor(IR.FrontC)< Collition_distance) and tap == 0 ):
        print(robobo.readDetectedObject().x)    
        if robobo.readDetectedObject().x > Screen_center and robobo.readDetectedObject().label == last_object :
            robobo.moveWheels(nominal_speed , nominal_speed+turning_factor)        
        elif robobo.readDetectedObject().x < Screen_center and robobo.readDetectedObject().label == last_object :
            robobo.moveWheels(nominal_speed + turning_factor , nominal_speed)       
        else:        
            robobo.moveWheels(nominal_speed,nominal_speed)
        tap = robobo.readTapSensor().x
        robobo.wait(wait_time)
    robobo.stopMotors()
    robobo.setEmotionTo(Emotions.HAPPY)
    robobo.sayText("Gotchaa",False)
    if tap != 0:
        dict["transition"] = 5
    else:
        dict["transition"]= 3
    
    return dict
    

















    
    








#robobo.readPanLastTime()















