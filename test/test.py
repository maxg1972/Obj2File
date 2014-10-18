import pprint,os
from Obj2File import Obj2File

data1 = {"key1":"value1","key2":2,"key3":[1,"due",{"tre":3}]}
data2 = [1,"two",{"three":3,"key":[4,"four"]}]


obj_cfg_1 = Obj2File("data1_obj.cfg",Obj2File.OBJ)
obj_cfg_2 = Obj2File("data2_obj.cfg",Obj2File.OBJ)

obj_cfg_1.save(data1)
obj_cfg_2.save(data2)

pprint.pprint(obj_cfg_1.load)
pprint.pprint(obj_cfg_2.load)

json_cfg_1 = Obj2File("data1_json.cfg",Obj2File.JSON)
json_cfg_2 = Obj2File("data2_json.cfg")

json_cfg_1.save(data1)
json_cfg_2.save(data2)

pprint.pprint(json_cfg_1.load)
pprint.pprint(json_cfg_2.load)

# os.remove("data1_obj.cfg")
# os.remove("data2_obj.cfg")
# os.remove("data1_json.cfg")
# os.remove("data2_json.cfg")