from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    has_choices = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

    '''
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    '''

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


#creating app to generate invoice
class Invoice(models.Model):
    inv_date = models.DateTimeField('invoice date')
    inv_amount = models.IntegerField(default=0)
    receipient = models.CharField(max_length=200)
    inv_desc = models.CharField(max_length=200)
    pmt_date = models.DateTimeField('pmt date')
    street_adr = models.CharField(max_length=200)
    adr_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=5)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        inv_nbr = str(self.id) + '_' + str(self.inv_date) + '_' + str(self.inv_desc)
        response_inv_nbr = inv_nbr.replace(' ','_')
        return response_inv_nbr

    def was_issued_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.inv_date <= now

    def due_soon(self):
        now = timezone.now()
        return now + datetime.timedelta(days=7) >= self.pmt_date
