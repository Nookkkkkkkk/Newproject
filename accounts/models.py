from django.db import models



class Accounts(models.Model):
        
    prefixs = (
        ("นาย","นาย"),
        ("นาง","นาง"),
        ("นางสาว","นางสาว"),
    )
    statuss = (
        ("อาจารย์ผู้ประสานงาน","อาจารย์ผู้ประสานงาน"),
        ("อาจารย์ผู้ออกนิเทศนักศึกษา","อาจารย์ผู้ออกนิเทศนักศึกษา"),
        
    )

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255,choices=prefixs)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=statuss,default='อาจารย์ผู้ออกนิเทศนักศึกษา')


