import math

SENTINEL = object()


def NULL_not_found(object: any = SENTINEL) -> int:
    if object is SENTINEL:
        return 1
    varType = type(object)
    if object is None:
        print(f"Nothing : None {varType}")
    elif varType == float and math.isnan(object) == True:
        print(f"Cheese : nan {varType}")
    elif varType == int and object == 0:
        print(f"Zero : 0 {varType}")
    elif varType == str and object == "":
        print(f"Empty : {varType}")
    elif varType == bool and object == False:
        print(f"Fake : False {varType}")
    else:
        print("Type not found")
        return 1
    return 0


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found()
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
