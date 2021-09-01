import datetime

from django.utils import timezone

from django.db import models
from django.db import models

from polls import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# 使用 display() 装饰器来改进方法
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        # 是不是近一个月的
        # datetime.timedelta 两个时间之间的时间差
        # return now - self.pub_date <= datetime.timedelta(days=30)
        return now - datetime.timedelta(days=30) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # >>> Question.objects.all()
    # 重写前:
    # <QuerySet [<Question: Question object (1)>]>
    # 重写后:
    # <QuerySet [<Question: yup?>]>
    def __str__(self):
        return self.choice_text

    #查询所有、按照id查找、startwith
# >>> Question.objects.all()
# <QuerySet [<Question: yup?>]>
# >>> Question.objects.filter(id=1)
# <QuerySet [<Question: yup?>]>
# >>> Question.objects.filter(question_text__startswith='y')
# <QuerySet [<Question: yup?>]>

# >>> current_year = timezone.now().year
# >>> Question.objects.get(pub_date__year=current_year)
# <Question: yup?>

