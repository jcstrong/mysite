from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice


# admin.site.register(Choice)
# StackedInline显示面积太大
# class ChoiceInline(admin.StackedInline):
# TabularInline关联对象以一种表格式的方式展示，显得更加紧凑
class ChoiceInline(admin.TabularInline):
    model = Choice
    # 默认提供 3 个额外的空插槽（选项字段）。
    extra = 3


# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # 这样修改使得 "Publication date" 字段显示在 "Question" 字段之前：
    # fields = ['pub_date', 'question_text']
    # 将表单分为几个字段集，这样每个字段集都有一个标题作为分割
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # 表明Choice 对象要在 Question 后台页面编辑。
    inlines = [ChoiceInline]

    # 展示系统中所有投票的页面      首页 › Polls › Questions
    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)