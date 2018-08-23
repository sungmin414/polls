from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Question, Choice

# admin 필드 순서 변경
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']


# 각 필드 분리해서 보기
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Question Statement', {'fields': ['question_text']}),
#         ('Date Information', {'fields': ['pub_date']}),
#     ]


# 필드 접어서보기(date information 에만 설정했음
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                ('Question Statement', {'fields': ['question_text']}),
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
            ]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
