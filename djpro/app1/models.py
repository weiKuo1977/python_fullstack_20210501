from django.db import models


# Create your models here.

class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    btitle = models.CharField(max_length=255)
    # 日期类型 出版日期
    bpub_data = models.DateField()

    def __str__(self):
        return self.btitle


class Heroinfo(models.Model):
    """英雄类"""
    hname = models.CharField(max_length=25)
    hsex = models.BooleanField(default=False)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    # type_News=models.ManyToManyField("BookInfo")

    def __str__(self):
        return self.hname


class Areas(models.Model):
    atitle = models.CharField(max_length=255)
    aparent = models.ForeignKey("self", null=True, blank=True)
