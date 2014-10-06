# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DailyWinner(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('User', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_winner'


class Datamart(models.Model):
    user = models.ForeignKey('User', primary_key=True)
    longest_stand = models.IntegerField(blank=True, null=True)
    longest_sit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datamart'


class DeskheightHistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('User', blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deskheight_history'


class MotionHistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('User', blank=True, null=True)
    inmotion_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motion_history'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20, blank=True)
    stand_height = models.IntegerField(blank=True, null=True)
    sit_height = models.IntegerField(blank=True, null=True)
    presensce_status = models.IntegerField(blank=True, null=True)
    sit_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
