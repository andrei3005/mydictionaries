person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person) #get whole dictionary

#print(person['children'][1]) #printing just "Betty"

#print(person["pets"]["cat"]) #list[index][key value]

for child in person["children"]:
    print(child)

print(' ')
for p in person["pets"]: #'p' is the key, the keys are dog and cat
    print(person["pets"][p])

