from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=64)
    image = models.FilePathField(path="/img")
    def __str__(self):
        return "%s" % (self.title)

class Duration(models.Model):
    duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s min" % (self.duration)

class Extra(models.Model):
    PEELING = 'PLN'
    ENTFERNUNG = 'ENT'
    NAGELLACK = 'NGL'
    SHELLAC = 'SHL'
    SHELLAC_FRENCH = 'SLF'
    AB_ZUPFEN = 'AZP'
    AB_FARBEN = 'AFR'
    WI_FARBEN = 'WFR'
    OL_ENTHAARUNG = 'OLE'
    AC_ENTHAARUNG = 'ACE'
    ENTHAARUNG_KN = 'KNE'
    ENTHAARUNG_BE = 'BEE'
    ENTHAARUNG_RU = 'RUE'
    MANI = 'M'
    PEDI = 'P'
    KMTK = 'K'

    EXTRA = (
        (PEELING, 'Peeling'),
        (ENTFERNUNG, 'Entfernung fremder Gele oder Shellac'),
        (NAGELLACK, 'Nagellack'),
        (SHELLAC, 'Shellac'),
        (SHELLAC_FRENCH, 'Shellac French'),
        (AB_ZUPFEN, 'Augenbraunen zupfen'),
        (AB_FARBEN, 'Augenbraunen färben'),
        (WI_FARBEN, 'Wimpern färben'),
        (OL_ENTHAARUNG, 'Oberlippen Enthaarung'),
        (AC_ENTHAARUNG, 'Achsel Enthaarung'),
        (ENTHAARUNG_KN, 'Enthaarung der Beine bis zum Knie'),
        (ENTHAARUNG_BE, 'Enthaarung der ganzen Beine'),
        (ENTHAARUNG_RU, 'Enthaarung des Rückens oder Brust'),
    )

    REL = (
        (MANI, 'M'),
        (PEDI, 'P'),
        (KMTK, 'K'),
    )

    extra = models.CharField(max_length=64, choices=EXTRA)
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    relation = models.CharField(max_length=1, choices=REL)

    def __str__(self):
        return "%s kostet €%s und dauert %s min" % (self.get_extra_display(), self.price, self.duration.duration)


class Mani(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s %s kostet €%s und dauert %s min" % (self.title, self.description, self.price, self.duration.duration)

class Pedi(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    duration = models.ForeignKey(Duration, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s %s kostet €%s und dauert %s min" % (self.title, self.description, self.price, self.duration.duration)


