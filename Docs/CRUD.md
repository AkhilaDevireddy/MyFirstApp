######################### Create #########################
### Method 1:
- In [2]: biryani = BiryaniDB(biryani_name="Chettinad Chicken Biryani", origin_place="Chettinad", favourite_percentage=70, does_akhila_like="True")
- In [3]: biryani.save()
- In [4]: biryani.get_does_akhila_like_display()
- Out[4]: True

### Method 2 (creates & saves in a single step):
- biryani = BiryaniDB.objects.create(biryani_name="SP Infocity Regular Biryani", origin_place="SP Infocity Chennai", favourite_percentage=20, does_akhila_like=False)

### Method 3 (using dict):
- biryani_dict = {"biryani_name": "SASTRA Punjabi Dhaba Chicken Biryani", "origin_place": "SASTRA Punjabi Dhaba", "favourite_percentage": 50, "does_akhila_like": True}
- biryani = BiryaniDB.objects.create(**biryani_dict)

<!-- biryani_dict = {"biryani_name": "abcd", "origin_place": "temp", "favourite_percentage": 0, "does_akhila_like": False}
biryani_dict = {"biryani_name": "XYZ", "origin_place": "Temp1", "favourite_percentage": 0, "does_akhila_like": False} -->





######################### Read #########################
### Method 1 (using get):
# creates exception when the queried data doesn't exist in db
# creates exception when the query returns more than 1 object
- biryani = BiryaniDB.objects.get(biryani_name="SP Infocity Regular Biryani")
- biryani = BiryaniDB.objects.get(does_akhila_like=False)

### Method 2 (using filter):
# Doesn't create any exception when the queried data doesn't exist in db, instead returns an empty QuerySet.
# Doesn't create any exception when the query returns more than 1 object, instead returns QuerySet with all the matched objects.
- biryani = BiryaniDB.objects.filter(biryani_name="SP Infocity Regular Biryani")
- biryani = BiryaniDB.objects.filter(does_akhila_like=False)






######################### Update #########################
### Method 1 (using get):
- BiryaniDB.objects.get(biryani_name="SP Infocity Regular Biryani").update(biryani_name="SP Infocity Regular Chicken Biryani")

### Method 2 (using filter):
- BiryaniDB.objects.filter(biryani_name="SP Infocity Regular Biryani").update(biryani_name="SP Infocity Regular Chicken Biryani")





######################### Delete #########################
- biryani = BiryaniDB.objects.filter(favourite_percentage__lt=10)
- biryani.delete()
