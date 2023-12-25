from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=3, choices=[('MR', 'Mr.'), ('MRS', 'Mrs'), ('MS', 'Ms.')])
    # Если мы не хотил заполнять поле рождения
    birth_day = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.name

