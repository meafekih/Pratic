from django.db import models




class Tag(models.Model):
    name = models.CharField(max_length=20)
    blogs= models.ManyToManyRel('name', 'Blog')
    
    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    CATEGORIES = [
        ("Politic", "Politic"),
        ("Food", "Food"),
        ("Life style", "Life style"),
    ]
    name = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return f"{self.name}"

class Blog(models.Model):
    name = models.CharField(max_length=50)
    age  = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

   
    def __str__(self):
        return f"{self.name} : {self.tags.name}"


