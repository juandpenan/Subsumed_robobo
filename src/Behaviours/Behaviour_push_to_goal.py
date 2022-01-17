from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from robobopy.utils.IR import IR
from Common_information import Server,Collition_distance,Screen_center,nominal_speed,turning_factor


robobo = Robobo(Server)
robobo.connect()



def PushToGoal(last_qr):
    
    dict = {}
    robobo.startObjectRecognition()
    robobo.setEmotionTo(Emotions.NORMAL)
    #and robobo.readDetectedObject().label == last_object
    
    while ((robobo.readQR().distance < Collition_distance) and robobo.readClapCounter() <=0 ):
        print(robobo.readQR().x)    
        if robobo.readQR().x < Screen_center and robobo.readQR().id == last_qr :
            robobo.moveWheels(nominal_speed , nominal_speed+turning_factor)        
        elif robobo.readQR().x > Screen_center and robobo.readQR().id == last_qr :
            robobo.moveWheels(nominal_speed + turning_factor , nominal_speed)       
        else:        
            robobo.moveWheels(nominal_speed,nominal_speed)
        robobo.wait(0.02)
    robobo.stopMotors()
    robobo.sayText("One Garbage less! YAAY")
    robobo.moveWheelsByTime(-nominal_speed,-nominal_speed,3,True)
    if robobo.readClapCounter() > 0:
        dict["transition"] = 5
    else:
        dict["transition"]= 1
    return dict
    


















    
    








#robobo.readPanLastTime()















