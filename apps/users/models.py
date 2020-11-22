from django.db import models

# Create your models here.



class UserInfo(models.Model):

    sex_type = (
        (1, "man"),
        (2, "women")
    )
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=4)
    sex = models.IntegerField(choices=sex_type)


    class Meta:
        db_table="tb_users"


class UsersDesc(models.Model):

    users = models.OneToOneField('UserInfo', on_delete=models.CASCADE)
    favorite = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, unique=True)



    class Meta:
        db_table='tb_users_desc'
