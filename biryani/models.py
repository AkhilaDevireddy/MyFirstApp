############ 2 ways to create data using 'objects' (objects is a Model Manager) ############
### Method 1:
# In [2]: biryani = BiryaniDB(biryani_name="Chettinad Chicken Biryani", origin_place="Chettinad", favourite_percentage=70, does_akhila_like="True")
# In [3]: biryani.save()
# In [4]: biryani.get_does_akhila_like_display()
# Out[4]: True


### Method 2 (creates & saves in a single step):
# biryani = BiryaniDB.objects.create(biryani_name="SP Infocity Regular Biryani", origin_place="SP Infocity Chennai", favourite_percentage=20, does_akhila_like=False)



from distutils.command.upload import upload
from django.db import models


# Create your models here.
class BiryaniDB(models.Model):
    AKHILA_LIKES = [
        (True, 'YES'), 
        (False, 'NO')
    ]
    biryani_name = models.CharField(primary_key=True, max_length=30)
    origin_place = models.CharField(max_length=15)
    favourite_percentage = models.IntegerField()
    biryani_image = models.ImageField(upload_to="biryani_images/", default=None, null=True, blank=True)      # ImageField() requires "Pillow" to be installed. Also, "upload_to" field expects relative path, not absolute path
    does_akhila_like = models.BooleanField(max_length=3, choices=AKHILA_LIKES)

    def __str__(self):
        # This will help in printing db object more clearly. For eg:

        # BiryaniDB.objects.all()
        # Out[2]: <QuerySet [<BiryaniDB: Hilight's Special_Chicken>, <BiryaniDB: Paradise's Chicken Dum>, <BiryaniDB: Chettinad's Chettinad Chicken Biryani>, <BiryaniDB: SP Infocity Chennai's SP Infocity Regular Biryani>]>
        return self.origin_place + "\'s " + self.biryani_name
