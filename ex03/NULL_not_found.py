import math

def NULL_not_found(object: any) -> int:

    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese: nan <class 'float'>")
    elif isinstance(object, bool) and object == False:
        print("Fake: False <class 'bool'>")
    elif object == int(0):
        print("Zero: 0 <class 'int'>")
    elif object == '':
        print("Empty: <class 'str'>")
    else:
        print("Type not found")
        return 1

    return 0
