from django.db import models
# Create your models here.
class AssetDate(models.Model):
    assetNum = models.CharField(max_length=11)
    assetName = models.CharField(max_length=22)
    empId = models.CharField(max_length=8)
    userName = models.CharField(max_length=4)
    ownerDept = models.CharField(max_length=20)
    adminId = models.CharField(max_length=11)
    tagText = models.TextField()
    lastTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
