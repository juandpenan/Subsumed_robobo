from robobopy.Robobo import Robobo
from enum import Enum
from Common_information import Server
from Behaviour_objectDetection import Obj_Detection
from Behaviour_approach import ObjectApproach 


on_off = True

robobo = Robobo(Server)  
robobo.connect()

class Behaviours(Enum):
    Detection = 1
    Approach_object = 2
    Push_to_goal = 3
    Escape = 4 
    Clap = 5

CurrentBehaviour = Behaviours.Detection

while on_off:
    if CurrentBehaviour.name == "Detection":
       temp_dict= Obj_Detection()
       transition = temp_dict.get("transition")
       last_object = temp_dict.get("last_object")
       if transition == 2:
           CurrentBehaviour = Behaviours.Approach_object
                    

    elif CurrentBehaviour.name == "Approach_object":
        temp_dict =  ObjectApproach(last_object)
        on_off = temp_dict.get("on_off")









    

