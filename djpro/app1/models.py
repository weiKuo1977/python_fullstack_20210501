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


class HeroInfoManager(models.Manager):
    # 1、改变查询的结果集
    def all(self):
        hero = super().all()
        # 查询标记为未删除的数据
        hero1 = hero.filter(isDelete=1)
        return hero1

    def save_data(self, hname, hsex):
        obj = Heroinfo()
        obj.hname = hname
        obj.hsex = hsex
        obj.save()
        return obj


class Heroinfo(models.Model):
    """英雄类"""
    hname = models.CharField(max_length=25)
    hsex = models.BooleanField(default=False)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    # 自定义类的模型管理器
    object = HeroInfoManager()

    def __str__(self):
        return self.hname

    class Meta:
        db_table = "heroinfo"


class Areas(models.Model):
    atitle = models.CharField(max_length=255)
    aparent = models.ForeignKey("self", null=True, blank=True)
