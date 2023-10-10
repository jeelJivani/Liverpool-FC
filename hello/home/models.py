from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comment = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)


    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Blog(models.Model):
    blog_image= models.ImageField(upload_to="Blog")
    blog_name=models.TextField()
    blog_desc=models.CharField(max_length=100)
    blog_view_count=models.IntegerField(default=1)
 
    def __str__(self):
        return f"{self.blog_name}{self.blog_view_count}"
    
class Position(models.Model):
    position=models.CharField(max_length=50)

    def __str__(self) -> str:   
        return self.position
    
    class Meta:
        ordering =['position']

class PlayerID(models.Model):
    player_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.player_id
    
class Player(models.Model):
    position = models.ForeignKey(Position,related_name="pos",on_delete=models.CASCADE)
    player_id = models.OneToOneField(PlayerID,related_name="playeridx", on_delete=models.CASCADE)
    player_name = models.CharField(max_length=100)
    player_email=models.EmailField(unique=True)
    player_age=models.IntegerField(default=18)
    player_country=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.player_name 
    
    class Meta:
        ordering=['player_name']
        verbose_name='player'


class Specs(models.Model):
    specs_name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.specs_name
    

class SpecsRating(models.Model):
    player=models.ForeignKey(Player,related_name="playerrating",on_delete=models.CASCADE)
    specs=models.ForeignKey(Specs,related_name='specsname',on_delete=models.CASCADE)
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=1)


    def __str__(self) -> str:
        return f"{self.player.player_name}{self.specs.specs_name}"  

    class Meta:
        unique_together=['player','specs']


class Student(models.Model):
    name= models.CharField(max_length=100)
    roll = models.IntegerField()
    city= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
#Products
    

class Dog(models.Model):
    name = models.CharField(max_length=100)
    datee = models.JSONField(default=list)
    

# def create_rating_marks():
#     try:
#         player_objs = Player.objects.all()
#         for player in player_objs:
#             specs = Specs.objects.all()
#             for spec in specs:
#                 SpecsRating.objects.create(specs=spec,player=player, rating=random.randint(50, 100))
#     except Exception as e:
#            print(e)




