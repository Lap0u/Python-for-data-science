def all_thing_is_obj(object: any = None) -> int:
    if object is None:
        return 42
    varType = type(object)
    if varType == list:
        print(f"List : {varType}")
    elif varType == tuple:
        print(f"Tuple : {varType}")
    elif varType == set:
        print(f"Set : {varType}")
    elif varType == dict:
        print(f"Dict : {varType}")
    elif varType == str:
        print(f"{object} is in the kitchen : {varType}")
    else:
        print("Type not found")
    return 42


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
all_thing_is_obj()
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
