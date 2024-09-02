words_starting_with_a = ["animal:","appel","ant"]
print(words_starting_with_a)

addres = [24,"pizza road","london","England"]

#creating dictionary
dict_addres = {
    "house_no":24,
    "area":"Pizza road",
    "city":"London",
    "country":"England"
}
print(dict_addres)

#Printing the values of individual keys
print(dict_addres["area"])
print(dict_addres["house_no"])
print(dict_addres["city"])

#printing all the keys of the dictionary
print(dict_addres.keys())

#printing all the values of the dictionary
print(dict_addres.values())

#how to add a new item to a dictionary
dict_addres["postcode"] = "Lo2347"
print(dict_addres)
dict_addres["mobile"] = "071276372781"
print(dict_addres) 

#deleting an item from the list
del dict_addres["postcode"]
print(dict_addres)