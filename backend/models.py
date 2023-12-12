# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Image(models.Model):
    func = models.CharField(blank=False,null=False,max_length=100,choices=[('A', 'segmentation'), ('B', 'explosion_identify')])
    image = models.FileField(upload_to='uploads/')

    class Meta:
        app_label = 'backend'
    def __str__(self):
        return self.name

class Abnormal(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, time, device_id, min, max) found, that is not supported. The first column is selected.
    time = models.DateTimeField()
    device = models.ForeignKey('Device', models.DO_NOTHING)
    min = models.FloatField()
    max = models.FloatField()
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abnormal'
        unique_together = (('id', 'time', 'device', 'min', 'max'),)

class BackendImage(models.Model):
    id = models.BigAutoField(primary_key=True)
    func = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'backend_image'


class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'building'


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=30, blank=True, null=True)
    building = models.ForeignKey(Building, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'device'


class Log(models.Model):
    time = models.DateTimeField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    device = models.ForeignKey(Device, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'log'
        unique_together = (('id', 'time', 'x', 'y', 'z', 'device'),)


class User(models.Model):
    email = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=45)
    authority = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'
