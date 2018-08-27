# admin 사이트 꾸미기

    from django.contrib import admin
    from django.contrib.admin import ModelAdmin
    from .models import Question, Choice

### admin 필드 순서 변경
     class QuestionAdmin(admin.ModelAdmin):
        fields = ['pub_date', 'question_text']


### 각 필드 분리해서 보기
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Question Statement', {'fields': ['question_text']}),
            ('Date Information', {'fields': ['pub_date']}),
        ]

### 필드 접어서보기(date information 에만 설정했음
    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            ('Question Statement', {'fields': ['question_text']}),
            ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]


### Question 및 Choice 를 한 화면에서 변경하는법
    class ChoiceInline(admin.StackedInline):
        model = Choice
        extra = 4


### TabularInline 테이블형식으로 보여주기(완)
    class ChoiceInline(admin.TabularInline):
        model = Choice
        extra = 2


    class QuestionAdmin(admin.ModelAdmin):
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

# 쉘로 데이터 조작하기

###`CURD`
>C = CREATE - 데이터 생성/입력

>R = READ - 데이터 조회

>U = UPDATE - 데이터 수정

>D = DELETE - 데이터 삭제

    데이터를 생성할때는 마지막에 save()를 해줘야 데이터베이스에 반영 함

### 데이터 조회 
`filter() 메소드 : 주어진 조건에 맞는 객체들을 담고 있는 QuerySet 콜렉션을 반환함`

`exclude() 메소드 : 주어진 조건에 맞지 않는 객체들을 담고 있는 QuerySet 콜렉션을 반환함`



### 템플릿 필터


`{{ name|lower }} `   

(|) 파이프 문자. name 변수값의 모든 문자를 소문자로 바꿔주는 필터

`{{ text|escape|linebreaks }}`

text 변수값 중에서 특수 문자를 이스케이프해주고 그결과를 스트링에 html <p> 태그를 붙여준다.

`{{ bio|truncatewords:30 }}`

bio 변수값 중에서 앞에 30개의 단어만 보여주고 줄 바꿈 문자는 모두 없애준다.

`{{ list|join:" // " }}`

빈칸이 있는 경우는 따옴표로 묶어준다. 만일 list가 ['a','b','c']라면 결과는 "a//b//c"가 된다.

`{{ value|default:"nothing" }}`

value 변수값이 False이거나 없는 경워, "nothing"으로 보여준다.

`{{ value|length }}`

변수값길이, value가 ['a','b','c']이면 결과는 3이 된다.

`{{ value|striptags }}`

value 변수값에서 html 태그를 모두 없애준다. 하지만 100% 보장은 안함

이것 말고 더많은 필터 기능들이 있다 필요한건 장고 도큐먼트 페이지 참고하기

  