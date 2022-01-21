
from robobopy.Robobo import Robobo
from Common_information import Server, Screen_centerQr,detection_speed,wait_time

# Caliberar el .X porque no se cuanto es la cantidad de pixeles, este va hasta 100 por lo que use 50 e igual la velocidad
robobo = Robobo(Server)
robobo.connect()

def Qr_detection(last_object):  

    dict={}   
    dict["last_object"]=last_object
    if last_object == "bottle" or last_object == "fork"\
        or last_object == "knife" or last_object == "spoon":
        target = "ceda"
        print("Escogi ceda ")
    elif last_object == "banana" or last_object == "apple" or last_object == "orange":
        target = "peatones"
        print("Escogi peatones ")
    elif last_object == "book" or last_object == "cup":
        target = "derecha"
        print("Escogi derecha ")
    else:
        target =""
        print("no escogi nada  ")

    dict["last_qr"] = robobo.readQR().id
    dict["pos_x"] = robobo.readQR().x
    dict["target"] = target
    
    tap = robobo.readTapSensor().x
    robobo.moveTiltTo(86,100,True)
    # Probar sin el screen center
    while dict["last_qr"] != target and tap == 0 :      
        robobo.moveWheelsByTime(detection_speed, -detection_speed,0.5,True)
        dict["last_qr"] = robobo.readQR().id
        dict["pos_x"] = robobo.readQR().x
        print(dict)
        tap = robobo.readTapSensor().x
        robobo.wait(wait_time)

    robobo.stopMotors()
    
    if tap != 0:
        dict["transition"] = 5
    else:
        dict["transition"]= 4
    
    return dict














    
    
























