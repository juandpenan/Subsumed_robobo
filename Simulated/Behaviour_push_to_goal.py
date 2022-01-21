from robobopy.Robobo import Robobo
from robobopy.utils.Emotions import Emotions
from Common_information import Server,delivery_distance,Screen_center_qr,detection_speed,turning_factor,wait_time


robobo = Robobo(Server)
robobo.connect()



def PushToGoal(last_qr):
    
    dict = {}
    robobo.startObjectRecognition()
    robobo.setEmotionTo(Emotions.NORMAL)
    #and robobo.readDetectedObject().label == last_object
    tap = robobo.readTapSensor().x
    distance = robobo.readQR().distance
    
    while (distance < delivery_distance) and (tap == 0)  :
        print(robobo.readQR().distance)    
        if robobo.readQR().x < Screen_center_qr :
            robobo.moveWheels(detection_speed+turning_factor , detection_speed)        
        elif robobo.readQR().x > Screen_center_qr :
            robobo.moveWheels(detection_speed  , detection_speed+ turning_factor)       
        else:        
            robobo.moveWheels(detection_speed,detection_speed)
        tap = robobo.readTapSensor().x
        distance = robobo.readQR().distance
        robobo.wait(wait_time)
    robobo.stopMotors()
    robobo.sayText("One Garbage less! YAAY")
    robobo.moveWheelsByTime(-80,-80,1.5,True)
    robobo.moveWheelsByTime(100,-100,0.875,True)
    if tap != 0:
        dict["transition"] = 5
    else:
        dict["transition"]= 1
    return dict
    


















    
    








#robobo.readPanLastTime()















