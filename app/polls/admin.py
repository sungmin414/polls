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
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#                 ('Question Statement', {'fields': ['question_text']}),
#                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#             ]


# Question 및 Choice 를 한 화면에서 변경하는법
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 4

# TabularInline 테이블형식으로 보여주기
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    #     fields = ['pub_date', 'question_text']    # 필드 순서 변경
    fieldsets = [
                    (None, {'fields': ['question_text']}),
                    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                ]
    inlines = [ChoiceInline]    # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')    # 레코드 리스트 항목 지
    list_filter = ['pub_date']  # 필터 사이드 바 추가
    search_fields = ['question_text']   # 검색 박스 추가



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
