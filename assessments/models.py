from django.db import models
from students.models import *
from establishments.models import *
# Create your models here.
class Coop13(models.Model):

    Score_type5 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    Score_type10 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
    )
    Score_type20 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
        ("13","13"),
        ("14","14"),
        ("15","15"),
        ("16","16"),
        ("17","17"),
        ("18","18"),
        ("19","19"),
        ("20","20"),
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    establishments = models.ForeignKey(Establishments, on_delete=models.CASCADE)
    assessorname = models.CharField(max_length=255)
    titlename = models.CharField(max_length=255)
    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse2 = models.CharField(max_length=255,choices=Score_type5)
    verse3 = models.CharField(max_length=255,choices=Score_type5)
    verse4 = models.CharField(max_length=255,choices=Score_type5)
    verse5 = models.CharField(max_length=255,choices=Score_type5)
    verse6 = models.CharField(max_length=255,choices=Score_type20)
    verse7 = models.CharField(max_length=255,choices=Score_type10)
    verse8 = models.CharField(max_length=255,choices=Score_type10)
    verse9 = models.CharField(max_length=255,choices=Score_type5)
    verse10 = models.CharField(max_length=255,choices=Score_type10)
    verse11 = models.CharField(max_length=255,choices=Score_type5)
    verse12 = models.CharField(max_length=255,choices=Score_type5)
    verse13 = models.CharField(max_length=255,choices=Score_type5)
    verse14 = models.CharField(max_length=255,choices=Score_type5)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class Coop11(models.Model):

    Score_type5 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )

    establishments = models.ForeignKey(Establishments, on_delete=models.CASCADE)
    student1 = models.CharField(max_length=255)
    student2 = models.CharField(max_length=255)
    student3 = models.CharField(max_length=255)
    student4 = models.CharField(max_length=255)
    student5 = models.CharField(max_length=255)
    assessorname1 = models.CharField(max_length=255)
    assessorname2 = models.CharField(max_length=255)
    assessorname3 = models.CharField(max_length=255)
    assessorname4 = models.CharField(max_length=255)
    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse3 = models.CharField(max_length=255,choices=Score_type5)
    verse4 = models.CharField(max_length=255,choices=Score_type5)
    verse5 = models.CharField(max_length=255,choices=Score_type5)
    verse6 = models.CharField(max_length=255,choices=Score_type5)
    verse7 = models.CharField(max_length=255,choices=Score_type5)
    verse8 = models.CharField(max_length=255,choices=Score_type5)
    verse9 = models.CharField(max_length=255,choices=Score_type5)
    verse10 = models.CharField(max_length=255,choices=Score_type5)
    verse11 = models.CharField(max_length=255,choices=Score_type5)
    verse12 = models.CharField(max_length=255,choices=Score_type5)
    verse13 = models.CharField(max_length=255,choices=Score_type5)
    verse14 = models.CharField(max_length=255,choices=Score_type5)
    verse15 = models.CharField(max_length=255,choices=Score_type5)
    verse16 = models.CharField(max_length=255,choices=Score_type5)
    verse17 = models.CharField(max_length=255,choices=Score_type5)
    verse18 = models.CharField(max_length=255,choices=Score_type5)
    verse19 = models.CharField(max_length=255,choices=Score_type5)
    verse20 = models.CharField(max_length=255,choices=Score_type5)
    verse21 = models.CharField(max_length=255,choices=Score_type5)
    verse22 = models.CharField(max_length=255,choices=Score_type5)
    verse23 = models.CharField(max_length=255,choices=Score_type5)
    verse24 = models.CharField(max_length=255,choices=Score_type5)
    verse25 = models.CharField(max_length=255,choices=Score_type5)
    verse26 = models.CharField(max_length=255,choices=Score_type5)
    verse27 = models.CharField(max_length=255,choices=Score_type5)
    verse28 = models.CharField(max_length=255,choices=Score_type5)
    verse29 = models.CharField(max_length=255,choices=Score_type5)
    verse30 = models.CharField(max_length=255,choices=Score_type5)
    versefull = models.CharField(max_length=255)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class Coop112(models.Model):
    Score_type5 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )

    student = models.CharField(max_length=255)
    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse3 = models.CharField(max_length=255,choices=Score_type5)
    verse4 = models.CharField(max_length=255,choices=Score_type5)
    verse5 = models.CharField(max_length=255,choices=Score_type5)
    verse6 = models.CharField(max_length=255,choices=Score_type5)
    verse7 = models.CharField(max_length=255,choices=Score_type5)
    verse8 = models.CharField(max_length=255,choices=Score_type5)
    verse9 = models.CharField(max_length=255,choices=Score_type5)
    verse10 = models.CharField(max_length=255,choices=Score_type5)
    verse11 = models.CharField(max_length=255,choices=Score_type5)
    verse12 = models.CharField(max_length=255,choices=Score_type5)
    verse13 = models.CharField(max_length=255,choices=Score_type5)
    verse14 = models.CharField(max_length=255,choices=Score_type5)
    verse15 = models.CharField(max_length=255,choices=Score_type5)
    verse16 = models.CharField(max_length=255,choices=Score_type5)
    versefull = models.CharField(max_length=255)
    comment = models.TextField()
    assessorname = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)

class Coop21(models.Model):
    Score_type5 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )

    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse2 = models.CharField(max_length=255,choices=Score_type5)
    verse3 = models.CharField(max_length=255,choices=Score_type5)
    verse4 = models.CharField(max_length=255,choices=Score_type5)
    verse5 = models.CharField(max_length=255,choices=Score_type5)
    verse6 = models.CharField(max_length=255,choices=Score_type5)
    versefull1 = models.CharField(max_length=255)

    verse21 = models.CharField(max_length=255,choices=Score_type5)
    verse22 = models.CharField(max_length=255,choices=Score_type5)
    verse23 = models.CharField(max_length=255,choices=Score_type5)
    verse24 = models.CharField(max_length=255,choices=Score_type5)
    verse25 = models.CharField(max_length=255,choices=Score_type5)
    verse26 = models.CharField(max_length=255,choices=Score_type5)
    versefull2 = models.CharField(max_length=255)

    verse31 = models.CharField(max_length=255,choices=Score_type5)
    verse32 = models.CharField(max_length=255,choices=Score_type5)
    verse33 = models.CharField(max_length=255,choices=Score_type5)
    verse34 = models.CharField(max_length=255,choices=Score_type5)
    verse35 = models.CharField(max_length=255,choices=Score_type5)
    verse36 = models.CharField(max_length=255,choices=Score_type5)
    verse37 = models.CharField(max_length=255)
    versefull3 = models.CharField(max_length=255)

class Coop20(models.Model):
    Score_type5 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    establishments = models.ForeignKey(Establishments, on_delete=models.CASCADE)
    assessorname1 = models.CharField(max_length=255)
    assessorname2 = models.CharField(max_length=255)
    student1 = models.CharField(max_length=255)
    student2 = models.CharField(max_length=255)
    student3 = models.CharField(max_length=255)
    verse1 = models.CharField(max_length=255,choices=Score_type5)
    verse2 = models.CharField(max_length=255,choices=Score_type5)
    verse3 = models.CharField(max_length=255,choices=Score_type5)
    verse4 = models.CharField(max_length=255,choices=Score_type5)
    verse5 = models.CharField(max_length=255,choices=Score_type5)
    verse6 = models.CharField(max_length=255,choices=Score_type5)
    versefull1 = models.CharField(max_length=255)