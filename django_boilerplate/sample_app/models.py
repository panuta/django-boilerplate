from django.db import models



# ***** PUT YOUR CODE HERE ***** #



# HOWTO: Model Field Reference
# https://docs.djangoproject.com/en/1.3/ref/models/fields/

"""
class SampleModel(models.Model):
    autofield = models.AutoField()
    bigintegerfield = models.BigIntegerField()
    booleanfield = models.BooleanField()
    charfield = models.CharField(max_length=None)
    commaseparatedintegerfield = models.CommaSeparatedIntegerField(max_length=None)
    datefield = models.DateField()
    datetimefield = models.DateTimeField()
    decimalfield = models.DecimalField(max_digits=None, decimal_places=None)
    emailfield = models.EmailField()
    filefield = models.FileField(upload_to=None)
    filepathfield = models.FilePathField(path=None)
    floatfield = models.FloatField()
    imagefield = models.ImageField(upload_to=None)
    integerfield = models.IntegerField()
    ipaddressfield = models.IPAddressField()
    nullbooleanfield = models.NullBooleanField()
    positiveintegerfield = models.PositiveIntegerField()
    positivesmallintegerfield = models.PositiveSmallIntegerField()
    slugfield = models.SlugField()
    smallintegerfield = models.SmallIntegerField()
    textfield = models.TextField()
    timefield = models.TimeField()
    urlfield = models.URLField()
    xmlfield = models.XMLField(schema_path=None)
 
    foreignkey = models.ForeignKey('ModelName')
    manytomanyfield = models.ManyToManyField('ModelName')
    onetoonefield = models.OneToOneField('ModelName')
"""