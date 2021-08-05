from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']

    fieldsets = [
        (None, {
            'fields': [
                'question_text'
                ]}),
        ('Date information', {
            'fields': [
                'pub_date'
                ]}),
    ]
    inlines = [ChoiceInline]

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)