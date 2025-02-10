dictionary={
        "name": "Ishu",
        "age": 23,
        "Location" :"Noida"

}
print(dictionary)
# type casting keys tuple into list
typeCastList=list(dictionary.keys())
print(len(typeCastList))
# Return tuple - key value pair
print(dictionary.items())


print(dictionary.get('name'))
# or
print(dictionary['name'])

# difference is if you're using second method then if u write name2 instead of name then it will give error
# print(dict['name2'])   #error
# print(dict.get('name2'))  # returns none
# After error none of the following code will be executed , hence you should use methods and not the direct way
#Nested Dictionary
nested={
    "name":"Ishu",
    "Address": {
        "state": "Rajasthan",
        "City": "Ajmer",
        "Pincode": 305001
    }
}


# print(nested["Address"]["Pincode"])

# Update method
nested.update({"name": "Ishu Jain"})
# print(nested)