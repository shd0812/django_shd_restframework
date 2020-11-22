from django.db import models
from utils.base_model import BaseModel


# Create your models here.

class Reports(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('报告名称', max_length=200,  help_text='报告名称')

    result = models.BooleanField('执行结果', default=1, max_length=10,  help_text='执行结果')
    count = models.IntegerField('用例总数',   help_text='用例总数')
    success = models.IntegerField('成功总数',   help_text='成功总数')
    html = models.TextField('报告源码', null=True, blank=True)
    summary = models.TextField('报告详情', null=True, blank=True, default='')


    class Meta:
        db_table = 'tb_reports'
        verbose_name = '环境信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
