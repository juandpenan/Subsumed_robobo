from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from robobopy.utils.IR import IR
from Common_information import Server,Collition_distance,Screen_center,nominal_speed,turning_factor


robobo = Robobo(Server)
robobo.connect()



def ObjectApproach(last_object):
    
    dict = {}
    robobo.startObjectRecognition()
    robobo.setEmotionTo(Emotions.NORMAL)
    while robobo.readIRSensor(IR.FrontC)< Collition_distance:    
        if robobo.readDetectedObject().x > Screen_center and robobo.readDetectedObject().label == last_object:
            robobo.moveWheels(nominal_speed , nominal_speed+turning_factor)        
        elif robobo.readDetectedObject().x < Screen_center and robobo.readDetectedObject().label == last_object:
            robobo.moveWheels(nominal_speed + turning_factor , nominal_speed)       
        else:        
            robobo.moveWheels(nominal_speed,nominal_speed)
        robobo.wait(0.02)
    robobo.stopMotors()
    robobo.setEmotionTo(Emotions.HAPPY)
    robobo.sayText("Gotchaa",False)
    #dict["transition"]= 3
    dict["on_off"]= False
    return dict
    


# Uncomment to test by separate
#ObjectApproach()















    
    








#robobo.readPanLastTime()















