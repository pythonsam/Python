
import json

# Convert dict to (json)string
main_data = {"a":1, "b":2, 'c':3}
str_data = json.dumps(main_data)

# Convert (json)string back to dictionary
main_data = json.loads(str_data)



# Working with files
fobj = open("data.json")
data = json.load(fobj)
fobj.close()

print(data["message"])
print(data["stages"])

# Modifying the data of the returned dictionary from "load"
data["stages"]["added_key"]=[1,2,3]
del data["stages"]["Provision"]

fobj = open("modified_data.json", "w")
json.dump(data, fobj, indent=4)
fobj.close()
