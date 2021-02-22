from django.test import TestCase
from app1.models import BookInfo, Heroinfo
from datetime import date

# Create your tests here.

b = BookInfo()
b.btitle = "天龙八部"
b.bpub_data = date(2021, 2, 21)
b.save()

h = Heroinfo()
h.hname = "乔峰"
h.hsex = True
h.hbook = b
h.save()

h2 = Heroinfo.objects.get(id=2)
# 英雄名称
h2.hname
#  图书名称
h2.hbook.btitle
# 图书编号
h2.hbook_id

b.heroinfo_set.all()
