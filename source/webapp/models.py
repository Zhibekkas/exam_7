from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Question")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")

    def __str__(self):
        return f"{self.pk} - {self.question}"

    class Meta:
        db_table = 'poll'
        verbose_name = 'Poll'
        verbose_name_plural = 'Poll db'


class Choice(models.Model):
    choice_text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Description")
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, verbose_name="Poll", related_name='choices')

    def __str__(self):
        return f"{self.choice_text}"

    class Meta:
        db_table = 'choices'
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices db'


class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, verbose_name="Question", related_name='answer')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date of creation")
    answer = models.ForeignKey('webapp.Choice', on_delete=models.CASCADE, verbose_name="Choice", related_name='answers')

    def __str__(self):
        return f"{self.poll} : {self.answer}"

    class Meta:
        db_table = 'answers'
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers db'
