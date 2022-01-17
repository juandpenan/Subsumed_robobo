
from robobopy.Robobo import Robobo
from Common_information import Server, Screen_center,detection_speed,wait_time

# Caliberar el .X porque no se cuanto es la cantidad de pixeles, este va hasta 100 por lo que use 50 e igual la velocidad
robobo = Robobo(Server)
robobo.connect()

def Qr_detection(last_object):  

    dict={}   
    target =""
    if last_object == "bottle" or last_object == "fork"\
        or last_object == "knife" or last_object == "spoon":

        target = "ceda"
    elif last_object == "banana" or last_object == "apple" or last_object == "orange":
        target = "peatones"
    elif last_object == "book" or last_object == "cup":
        target = "peatones"

    dict["last_qr"] = robobo.readQR().id
    dict["pos_x"] = robobo.readQR().x
    robobo.moveTiltTo(75,100,True)
    while ((dict["last_qr"] != target) and (not (Screen_center - 5 <= dict["pos_x"] <= Screen_center + 5)) and (robobo.readClapCounter() <= 0)) :      
        robobo.moveWheels(detection_speed, -detection_speed)
        robobo.wait(wait_time)
        dict["last_qr"] = robobo.readQR().id
        dict["pos_x"] = robobo.readQR().x
        print(dict)

    robobo.stopMotors()
    if robobo.readClapCounter() > 0:
        dict["transition"] = 5
    else:
        dict["transition"]= 1
    
    return dict














    
    








#robobo.readPanLastTime()















