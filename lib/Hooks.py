def Error(Message: str):
    print("[Error]", Message)

def HookElement(Array, Element, NewElement):
    if isinstance(Array, list):
        for i in range(len(Array)):
            if Array[i] == Element:
                Array[i] = NewElement
    else:
        Error("The first parameter must be a list.")

def HookFunction(Function, NewFunction):
    IsFunction = None
    if Function != None:
        return IsFunction
    else:
        Error("Invalid function/new function.")
