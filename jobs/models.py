from django.db import models


class RecruitInfo(models.Model):
    """
    公司用工信息
    """
    company_name = models.CharField(max_length=64, verbose_name='公司名称')
    company_summary = models.TextField(verbose_name='公司简介')
    company_phone = models.CharField(max_length=15, verbose_name='联系电话')
    company_linkman = models.CharField(max_length=10, verbose_name='联系人')
    company_city = models.CharField(max_length=10, verbose_name='市')
    company_region = models.CharField(max_length=10, verbose_name='区')
    company_address = models.CharField(max_length=10, verbose_name='详情地址')
    recruit_type = models.CharField(max_length=10, verbose_name='工种')
    recruit_num = models.PositiveIntegerField(default=0, verbose_name='人数')
    recruit_length = models.PositiveIntegerField(default=0, verbose_name='要求工龄')
    recruit_other = models.CharField(max_length=64, blank=True, null=True, verbose_name='其他额外信息')

    class Meta:
        verbose_name = '公司用工信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.company_name + ' ' + self.recruit_type


class WorkerInfo(models.Model):
    """
    工人个人信息
    """
    name = models.CharField(max_length=10, verbose_name='姓名')
    phone = models.CharField(max_length=15, verbose_name='手机')
    city = models.CharField(max_length=10, verbose_name='市')
    region = models.CharField(max_length=10, verbose_name='区')
    address = models.CharField(max_length=64, verbose_name='详情地址')
    gender = models.CharField(max_length=2, verbose_name='性别')
    age = models.PositiveIntegerField(default=1, verbose_name='年龄')
    work_length = models.PositiveIntegerField(default=0, verbose_name='工龄')
    work_type = models.CharField(max_length=10, verbose_name='工种')
    work_other = models.CharField(max_length=64, blank=True, null=True, verbose_name='其他额外信息')

    class Meta:
        verbose_name = '工人个人信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + ' ' + self.work_type
