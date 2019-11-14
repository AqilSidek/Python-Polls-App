from django.db import models

# Create your models here.
# Since this is a polls app, we need:
# Question class
#   question, publish date
# Choice class
#   choice/answer option, number of votes, link to ensure correctly
#   corresponding question/choice.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    # when we call Question.objects.all() it will return the question text
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # giving the choice class a new parameter where we're passing
    # in a question which has the correct foreign key

    def __str__(self):
        return self.choice_text
