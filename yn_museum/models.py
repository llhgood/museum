from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe


# Create your models here.

class Order(models.Model):
    State_chose = {
        ("s", "预约成功"),
        ("r", "已入馆"),
    }
    Type_chose = {
        ("c", "参观预约"),
        ("h", "活动预约"),
        ("z", "展览预约"),
    }
    Encoded = models.CharField(verbose_name="编码", max_length=32)
    Type = models.CharField(verbose_name="所属分类", max_length=16)
    EnterTime = models.DateTimeField(verbose_name="入场时间")
    Name = models.CharField(verbose_name="姓名", max_length=16)
    Idnumber2 = models.CharField(verbose_name="身份证号码", max_length=32 ,blank=True,null=True)
    State = models.CharField(verbose_name="预约状态", max_length=16)
    @admin.display(description="身份证号")
    def idnumber2(self):
        idnum2 = self.Idnumber2[0:6] + "********" + self.Idnumber2[14:]
        return f"{idnum2}"
    class Meta:
        verbose_name = "预约管理"
        verbose_name_plural = "预约管理"


class Visitor(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=16)
    Idnumber = models.CharField(verbose_name="身份证号码", max_length=32)

    # 对Idnumber字段的显示进行字符串操作，身份证号脱敏
    @admin.display(description="身份证号")
    def idnumber(self):
        idnum = self.Idnumber[0:6] + "********" + self.Idnumber[14:]
        return f"{idnum}"

    class Meta:
        verbose_name = "访客管理 "
        verbose_name_plural = "访客管理"

class Order_Type(models.Model):
    Type = models.CharField(verbose_name="预约类型", max_length=16)
    class Meta:
        verbose_name = "预约类型"
        verbose_name_plural = "预约类型"


class Group(models.Model):
    Name=models.CharField(verbose_name="姓名", max_length=32)
    Date=models.CharField(verbose_name="参观日期", max_length=16)
    number=models.CharField(verbose_name="人数",max_length=16)
    state=models.CharField(verbose_name="预约状态",max_length=16)
    notes=models.CharField(verbose_name="备注",max_length=32,blank=True,null=True)

    class Meta:
        verbose_name = "团体预约管理"
        verbose_name_plural = "团体预约管理"




