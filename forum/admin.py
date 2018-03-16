from django.contrib import admin
from .models import UserProfile, Question, Answer, QuestionComment, AnswerComment, Domain, Favorite, Vote

admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
admin.site.register(Domain)
admin.site.register(Favorite)
admin.site.register(Vote)
