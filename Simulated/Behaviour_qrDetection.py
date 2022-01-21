
from ast import Break, Return
from pyparsing import And
from robobopy.Robobo import Robobo
from Common_information import Server, Screen_center_qr,detection_speed,wait_time,tilt_angle_qr,max_pan_angle


robobo = Robobo(Server)
robobo.connect()

def Qr_detection(last_object):  

    dict={} 
    flag = False  
    target =""
    if last_object == "bottle":
        target = "plastico"
    elif last_object == "apple":
        target = "vidrio" # El simulador tiene mal el QR de organico, devuelve la palabra vidrio
    elif last_object == "cup":
        target = "papel"

    dict["last_qr"] = robobo.readQR().id
    dict["pos_x"] = robobo.readQR().x
    dict["target"] = target
    dict["pos_qr"] = robobo.readPanPosition()
    
    tap = robobo.readTapSensor().x
    robobo.moveTiltTo(tilt_angle_qr,100,True)
    robobo.movePanTo(-max_pan_angle,100,True)
    print(dict)
    robobo.stopMotors()
    while dict["last_qr"] != target :  
        print(dict)    
        robobo.movePanTo(max_pan_angle,25,False)
        tap = robobo.readTapSensor().x
        dict["last_qr"] = robobo.readQR().id
        dict["pos_qr"] = robobo.readPanPosition()
        if dict["pos_qr"] >= 156:
            flag = True
            break
        
        robobo.wait(wait_time)

    

    if dict["pos_qr"] < 0:
        dict["direccion"]= "izquierda"
    elif dict["pos_qr"] > 0:
        dict["direccion"]= "derecha"
    else:
        dict["direccion"]= "derecho"

    

    robobo.movePanTo(0,100,True)
    
    dict["pos_x"] = robobo.readQR().x
    
    if dict ["last_qr"] == target:
         dict["last_qr"] = "temp_target" # Condicion solo para que entre al While

    #dict["last_qr"] = robobo.readQR().id 
    #(not flag) and and tap == 0  and  not (Screen_center_qr-10 <= dict["pos_x"] <= Screen_center_qr+10)
    while  dict["last_qr"] != target and tap ==0 and not flag  :
        print(dict["pos_x"])
        
        if dict["direccion"] == "izquierda":
            robobo.moveWheels(detection_speed,1)
        elif dict["direccion"] == "derecha":
            robobo.moveWheels(1,detection_speed)
        else:
            robobo.moveWheels(detection_speed,detection_speed)
        tap = robobo.readTapSensor().x
        dict["pos_x"] = robobo.readQR().x
        dict["last_qr"] = robobo.readQR().id
        robobo.wait(wait_time)

    robobo.stopMotors()
    
    if tap != 0:
        dict["transition"] = 5
    elif dict["last_qr"] != target or flag :
        dict["transition"] = 3
    else:
        dict["transition"]= 4
    
    return dict














    
    























