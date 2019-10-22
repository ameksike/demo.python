from django.db import models


# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=1)
    born = models.DateField()

    def fullName(self):
        return "{0} {1}".format(self.firstName, self.lastName)

    def __str__(self):
        return self.fullName()


class Work(models.Model):
    place = models.CharField(max_length=35)
    status = models.BooleanField()

    def __str__(self):
        return "{0} ({1})".format(self.place, self.status)


class Contracts(models.Model):
    person = models.ForeignKey(Person, null=False, blank=False, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} -> {1} ({2})".format(self.person, self.work.place, self.date)