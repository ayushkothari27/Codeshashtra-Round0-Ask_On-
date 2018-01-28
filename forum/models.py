from django.db import models
from django.contrib.auth import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.FileField(blank=True)
    reputation = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=250)
    domains = models.ManyToManyField("Domain", null=True, blank=True, on_delete=models.SET_NULL)
    words = models.ManyToManyField("Question", null=True, blank=True)


class Question(models.Model):
    asked_by = models.ForeignKey(UserProfile, related_name="questions",
                                 null=True, blank=True, on_delete=models.SET_NULL)
    question = models.CharField(max_length=100)
    need = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    domain = models.ForeignKey("Domain", related_name="domain_questions",
                               null=True, blank=True, on_delete=models.SET_NULL)
    time = models.DateTimeField(default=datetime.now, blank=True)


class Answer(models.Model):
    answered_by = models.ForeignKey(UserProfile, related_name="answers")
    ques = models.ForeignKey(Question, related_name="question", null=True, blank=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)


class AnswerComment(models.Model):
    comment_by = models.ForeignKey(UserProfile, related_name="comment")
    ans = models.ForeignKey(Answer, related_name="comments",
                            null=True, blank=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)


class QuestionComment(models.Model):
    comment_by = models.ForeignKey(UserProfile, related_name="comment",
                                   null=True, blank=True, on_delete=models.SET_NULL)
    question = models.ForeignKey(Question, related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    upvotes = models.IntegerField(default=0)
    reports = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=datetime.now, blank=True)


class Domain(models.Model):
    name = models.CharField(max_length=50)
