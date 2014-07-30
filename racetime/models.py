from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RaceEvent(models.Model):
    event_name = models.CharField(max_length=200)
    event_owner = models.ForeignKey(User)
    def __unicode__(self):
        return self.event_name

class Round(models.Model):
    round_event = models.ForeignKey(RaceEvent)
    round_date = models.DateField('run date')

class Qualification(Round):
    round_number = models.IntegerField()
    def __unicode__(self):
        return "%s Qualification %s"%(self.round_event.event_name, self.round_number)


class Final(Round):
    round_number = models.IntegerField()
    final_level = models.CharField(max_length=1)
    def __unicode__(self):
        return "%s %s Final %s"%(self.round_event.event_name, self.final_level, self.round_number)


class Car(models.Model):
    car_chassis = models.CharField(max_length=200)
    car_body = models.CharField(max_length=200)
    car_racer = models.ForeignKey(User)
    car_transponder = models.ForeignKey("Transponder")
    def __unicode__(self):
        return "%s's %s %s"%(self.car_racer.username, self.car_chassis, self.car_body)

class Transponder(models.Model):
    transponder_id = models.IntegerField()
    def __unicode__(self):
        return "Transponder %s"%(self.transponder_id)

