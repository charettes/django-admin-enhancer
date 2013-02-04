from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author)
    collection = models.ForeignKey(Collection, null=True, blank=True)
    themes = models.ManyToManyField('Theme')


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book)
    main_theme = models.ForeignKey(Theme)

    def __unicode__(self):
        return self.name
