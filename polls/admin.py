from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
        ('Has answers', {'fields': ['has_choices']})
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'has_choices', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


#class ChoiceAdmin(admin.ModelAdmin):
    #fields = ['question', 'choice_text', 'votes']


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice, ChoiceAdmin)
