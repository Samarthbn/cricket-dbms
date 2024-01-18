# from django.db import models


from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField, DateTimeField, EmailField, IntegerField
from django.db.models.fields.related import ForeignKey
# Create your models here.

# umpire
# match
# player
# team
# captain



class player(models.Model):
    player_id = models.CharField(primary_key=True, max_length=30)
    player_name = models.CharField(max_length=200)
    batting_average = models.FloatField()
    no_of_totalruns = models.IntegerField()
    no_of_wickets = models.IntegerField()
    type_of_bowler = models.CharField(max_length=30)
    economy = models.FloatField()


class umpire(models.Model):
    umpire_id = models.CharField(primary_key=True, max_length=30)
    umpire_name = models.CharField(max_length=30)
    no_of_matches = models.IntegerField()
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.umpire_name

    

class matches(models.Model):
    match_id = models.CharField(primary_key=True, max_length=30)
    match_date = models.DateField()
    team_1_name = models.CharField(max_length=30)
    team_2_name = models.CharField(max_length=30)
    winner = models.CharField(max_length=30)
    loser = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    umpired_by = models.ManyToManyField(umpire)
    umpire_name = models.CharField(max_length=200)

    def __str__(self):
        return self.team_1_name

    def __str__(self):
        return self.team_2_name


class team(models.Model):
    team_id = models.CharField(primary_key=True, max_length=20)
    team_rank = models.IntegerField()
    team_name = models.CharField(max_length=20)
    no_of_wins = models.IntegerField()
    
    no_of_loses = models.IntegerField()
    no_of_bowlers = models.IntegerField()
    no_of_batsmen = models.IntegerField()
    player_name = models.CharField(max_length=20)
    match_date = models.DateField()
    has = models.ManyToManyField(player)
    plays = models.ManyToManyField(matches)


class captain(models.Model):
    captain_id = models.CharField(primary_key=True, max_length=30)
    captain_name = models.CharField(max_length=20)
    team_name = models.CharField(max_length=20)
    leads = models.ManyToManyField(team)


class sign(models.Model):
    fullname = models.TextField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class usign(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

