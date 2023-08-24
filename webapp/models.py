from django.db import models


class users(models.Model):

    gender = (
        ('male' , 'male' ),
        ('female', 'female')
    )

    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=20)
    gender=models.CharField(max_length=20 , default='female' , choices=gender)
    image=models.FileField(upload_to='user_image')

    def __str__(self) -> str:
        return self.fname

class book(models.Model):
    image=models.ImageField(upload_to='book_image')
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    review=models.IntegerField()
    page=models.IntegerField()
    description=models.TextField()
    about=models.TextField()
    stock=models.IntegerField()
    price=models.IntegerField()

    def __str__(self) -> str:
        return self.name
    
class histroy(models.Model):
    user_id=models.IntegerField()
    book_id=models.IntegerField()
    price=models.IntegerField()
    quntity=models.IntegerField()
    rent_date=models.DateField()
    return_data=models.DateField(null=True,blank=True)
    isRenew=models.BooleanField()
    pyment=models.BigIntegerField()
    pyment_Mode=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.pyment_Mode