class Home:
    bedrooms = 5
    bathrooms = 4


my_home = Home()
result = getattr(my_home, "bedrooms", "no bedrooms")
print(result)

try:
    if getattr(my_home, "living_rooms", None) == None:
        my_home.living_rooms = 2
        print(my_home.living_rooms)
except AttributeError:
    print("something")
    


