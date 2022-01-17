
from robobopy.Robobo import Robobo
from Behaviour_objectDetection import Obj_Detection
from Behaviour_approach import ObjectApproach 
from Behaviour_qrDetection import Qr_detection
from Behaviour_push_to_goal import PushToGoal
from transitions import TransitionManager
from Behaviours import Behaviours
from Common_information import Server



on_off = True

robobo = Robobo(Server)  
robobo.connect()



CurrentBehaviour = Behaviours.ObjDetection

while on_off:
    if CurrentBehaviour.name == "ObjDetection":
       temp_dict= Obj_Detection()
       transition = temp_dict.get("transition")
       last_object = temp_dict.get("last_object")                

    elif CurrentBehaviour.name == "Approach_object":
        temp_dict =  ObjectApproach(last_object)
        transition = temp_dict.get("transition")
        
        
    elif CurrentBehaviour.name == "QrDetection":
        temp_dict = Qr_detection(last_object)
        last_qr = temp_dict.get("last_qr")      

    elif CurrentBehaviour.name == "Push_to_goal":
        temp_dict = PushToGoal(last_qr)
    elif CurrentBehaviour.name == "Terminator":
        on_off = False
    else:
        CurrentBehaviour =TransitionManager(transition)




       









    

