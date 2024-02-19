from django.db import models
from utils.models import BaseModel
from django.core.validators import FileExtensionValidator
from utils.choices import TypeOfPrice, TypeOfValuta
# Create your models here.

from django.contrib.auth import get_user_model


class Region(BaseModel):
    title = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.title
    
class District(BaseModel):
    title = models.CharField(max_length=32)
    region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name='districts')

    def __str__(self) -> str:
        return f'{self.title} {self.region}'
    

class Photo(BaseModel):
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey('Post', on_delete = models.CASCADE, related_name = 'photos')
    is_main = models.BooleanField(default=False)

    class Meta:
        unique_together = ('image', 'post')

    def __str__(self) -> str:
        return f'{self.post} - {self.image}'

    def save(self, *args, **kwargs):
        if self.is_main:
            self.post.main_photo = self.image
            self.post.save()
        super().save(*args, **kwargs)


class Category(BaseModel):
    title = models.CharField(max_length = 256)
    parent = models.ForeignKey('self', on_delete = models.CASCADE, related_name = 'children', blank=True, null=True)
    options = models.ManyToManyField('option.Option', blank=True, related_name='categories')
    image = models.ImageField(upload_to='images/', null=True, blank=True )
    is_subcategory = models.BooleanField(default=False) 

    is_price = models.BooleanField(default=False)   
    is_free = models.BooleanField(default=False)   
    is_exchange = models.BooleanField(default=False)  

    def __str__(self) -> str:
        return self.title

class SubCategory(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories')
    options = models.ManyToManyField("option.Option",related_name='subcategories', blank=True)

    def __str__(self):
        return self.title 




class Post(BaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,related_name='posts', null=True, blank=True)
    description = models.CharField(max_length=9000)
    main_photo = models.ImageField(upload_to='images/', null=True, blank=True)

    price_type = models.CharField(max_length=10, choices=TypeOfPrice.choices,default=TypeOfPrice.PRICE, blank=True, null=True)
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    valuta_type = models.CharField(max_length=10, choices=TypeOfValuta.choices,default=TypeOfValuta.SUM, null=True, blank=True)
    is_active_month = models.BooleanField(default=False, null=True, blank=True)
    
    address = models.ForeignKey(District, on_delete=models.CASCADE,related_name='posts')
    email = models.EmailField(default='')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='posts', blank=True, null=True)
    phone_number = models.CharField(max_length=13)

    options = models.ManyToManyField("option.Option", blank=True,through="option.PostOption")

    liked = models.ManyToManyField(get_user_model(),related_name="like_posts", blank=True)
    saved_searches = models.ManyToManyField(get_user_model(),related_name="saved_posts", blank=True)
    PlanDetail = models.ForeignKey('plan.PlanDetail', on_delete=models.CASCADE, blank=True, null=True, related_name = 'posts')


    watcher = models.PositiveIntegerField(default=0, editable=False)
    automate_active = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Chat(BaseModel):
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='buyyers')
    buyer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,related_name='sellers')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'customer: {self.buyer}, owner: {self.seller}'

class Message(BaseModel):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    file = models.FileField(upload_to='files/', blank=True, null=True,validators=[FileExtensionValidator(['png', 'jpg', 'mp4', 'doc', 'docx'])])

    def __str__(self) -> str:
        return f'SMS(id = {self.sender.id})'
    
    
