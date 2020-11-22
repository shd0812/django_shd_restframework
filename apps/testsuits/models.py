from django.db import models
from utils.base_model import BaseModel


# Create your models here.

class TestSuits(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField('套件名称', max_length=200, help_text='套件名称')
    projects = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, help_text='所属项目')

    include = models.TextField('包含的接口', null=False, help_text='包含的接口')



    class Meta:
        db_table = 'tb_testsuits'
        verbose_name = '套件信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
