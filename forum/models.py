from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    photo = models.FileField(blank=True)
    reputation = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=250, blank=True)
    domains = models.ManyToManyField("Domain", blank=True)

    def __str__(self):
        return self.user.username


class Question(models.Model):
    asked_by = models.ForeignKey(UserProfile, related_name="questions",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=100)
    need = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    domain = models.ForeignKey("Domain", related_name="domain_questions",
                               null=True, blank=True, on_delete=models.SET_NULL)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answered_by = models.ForeignKey(UserProfile, related_name="answers",
                                    null=True, blank=True, on_delete=models.SET_NULL)
    ques = models.ForeignKey(Question, related_name="question_ans", null=True, blank=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    reports = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.answer


class AnswerComment(models.Model):
    comment_by = models.ForeignKey(UserProfile, related_name="comment_answer",
                                   null=True, blank=True, on_delete=models.SET_NULL)
    ans = models.ForeignKey(Answer, related_name="comments",
                            null=True, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment


class QuestionComment(models.Model):
    comment_by = models.ForeignKey(UserProfile, related_name="comment_question",
                                   null=True, blank=True, on_delete=models.SET_NULL)
    question = models.ForeignKey(Question, related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.comment


class Domain(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(UserProfile, related_name="favorites", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="question_favorites", on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(UserProfile, related_name="votes", on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name="answer_votes", on_delete=models.CASCADE)
