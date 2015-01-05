from django.contrib import admin
from polls.models import Question, Choice

# This block makes it possible to create up to three Choices
# simultaenously when you create a Question
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class ChoiceAdmin(admin.ModelAdmin):
	fields = ['choice_text']
	list_display = ('choice_text', 'votes')
	list_filter = ['votes']
	search_fields = ['choice_text', 'votes'] # search by text or by integer from the same field

class QuestionAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question_text']
	fieldsets = [
		(None,				 {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date'] 
	search_fields = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)