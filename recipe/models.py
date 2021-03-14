from django.db import models
import datetime


class Recipe(models.Model):
    menu = models.CharField(max_length=50)
    ingredient = models.TextField(help_text='なるべくひらがな使おうな。卵は漢字。')
    procedure = models.TextField()
    genre = models.IntegerField(help_text='1:麺, 2:丼, 3:主, 4:副, 5:汁')
    country = models.IntegerField(help_text='1:和, 2:洋, 3:中, 4:伊, 5:他')
    difficulty = models.IntegerField(help_text='1:楽々, 2:普通, 3:大変')
    image = models.ImageField(upload_to='images',blank=True, null=True)
    link = models.URLField()
    published_date = models.DateField(default=datetime.date.today)

    def publish(self):
        self.save()

    def __str__(self):
        return self.menu