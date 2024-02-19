from django.db import models

# Create your models here.
from utils.models import BaseModel


class Plan(BaseModel):
    title = models.CharField(max_length=255)
    plan_detail = models.ManyToManyField('PlanDetail')

    def __str__(self) -> str:
        return self.title
    

class PlanPrice(BaseModel):
    plan = models.ForeignKey('Plan', on_delete = models.CASCADE)
    category = models.ForeignKey('store.Category', on_delete = models.CASCADE)
    price = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f'PlanPrice(pk = {self.pk}, plan = {self.plan})'
    

class PlanDetailGroup(BaseModel):
    title = models.CharField(max_length = 256)
    is_multiple = models.BooleanField(default = False)
    text = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class PlanDetail(BaseModel):
    class TextChoice(models.TextChoices):
        WEEK = 'WEEK', '7 kun'
        MONTH = 'MONTH', '30 kun'

    class TypeOfStatus(models.TextChoices):
        VIP = 'VIP', 'Vip'
        TOP = 'TOP', 'Top'
        ABOVE = 'ABOVE', 'Above'

    group = models.ForeignKey(PlanDetailGroup, on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length =256,
                            choices = TypeOfStatus.choices, blank=True, null=True)
                            
    choice_text = models.CharField(max_length = 255, choices = TextChoice.choices,blank=True, null=True )
    amount = models.CharField(max_length = 255)

    def __str__(self) -> str:
        return f'PlanDetail(id = {self.pk}, group = {self.group})'
    

class PlanDetailPrice(BaseModel):
    plan_detail = models.ForeignKey(PlanDetail, on_delete=models.CASCADE)
    category = models.ForeignKey('store.Category', on_delete = models.CASCADE)
    price = models.CharField(max_length = 32)

    def __str__(self) -> str:
        return f'PlanDetailPrice(id = {self.pk})'
    
