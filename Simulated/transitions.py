from Behaviours import Behaviours
def TransitionManager(transition):
    if transition == 5:
        CurrentBehaviour = Behaviours.Terminator
    elif transition == 1:
        CurrentBehaviour = Behaviours.ObjDetection
    elif transition == 2:
        CurrentBehaviour = Behaviours.Approach_object
    elif transition == 3:
        CurrentBehaviour = Behaviours.QrDetection
    elif transition == 4:
        CurrentBehaviour = Behaviours.Push_to_goal
    print(transition)
    return CurrentBehaviour