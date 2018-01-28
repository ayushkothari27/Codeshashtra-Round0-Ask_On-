from django.contrib import admin
from .models import UserProfile, Question, Answer, AnswerComment, QuestionComment
from .models import Domain


admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerComment)
admin.site.register(QuestionComment)
admin.site.register(Domain)
