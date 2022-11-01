from django.db import models

# Create your models here.
#메모리 반도체 시장 점유율
class MSemi(models.Model):
    country = models.CharField(max_length=30)
    share = models.IntegerField()

#시스템 반도체 시장 점유율
class SSemi(models.Model):
    country = models.CharField(max_length=30)
    share = models.IntegerField()

#팹리스 시장 점유율
class Fabless(models.Model):
    country = models.CharField(max_length=30)
    share = models.IntegerField()

#한국의 글로벌 시장 점유율
class KorSemiShare(models.Model):
    year = models.CharField(max_length=30)
    semi = models.FloatField()
    Msemi = models.FloatField()
    Ssemi = models.FloatField()

#반도체 시장 규모
class SemiShare(models.Model):
    year = models.CharField(max_length=30)
    semi = models.IntegerField()
    Msemi = models.IntegerField()
    Ssemi = models.IntegerField()

#반도체 수출 비중
class SemiExport(models.Model):
    year = models.CharField(max_length=30)
    semi = models.IntegerField()
    oil = models.IntegerField()
    car = models.IntegerField()

#반도체 연구비
class Research(models.Model):
    year = models.CharField(max_length=30)
    researchFunds = models.IntegerField()



#한국 반도체 수출
class KorSemiExport(models.Model):
    year = models.CharField(max_length=30)
    all = models.IntegerField()
    export = models.IntegerField()
    share = models.FloatField()

#세계 반도체 수입 규모
class WorldSemiImport(models.Model):
    year = models.CharField(max_length=30)
    export = models.IntegerField()

#중국 반도체 수입 규모
class ChinaSemiImport(models.Model):
    year = models.CharField(max_length=30)
    export = models.IntegerField()

#중국 반도체 수입과 수출
class ChiSemiExport(models.Model):
    year = models.CharField(max_length=30)
    export = models.IntegerField()
    Simport = models.IntegerField()

#세계 대중국 수입 및 수출
class WorldSemiImExport(models.Model):
    year = models.CharField(max_length=30)
    export = models.IntegerField()
    Simport = models.IntegerField()
    both = models.FloatField()