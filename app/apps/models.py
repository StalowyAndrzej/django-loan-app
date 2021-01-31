from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Approval(models.Model):
    
	"""
	The Approval object represents information about borrower

    Attributes:
        firstname: The name of borrower
        lastname: The lastname of borrower
        dependants: Information about persons who relies for financial support
        applicantincome: The value about borrower income
        coapplicantincome: The value about coappliant income
        loanmt: The value of requested loan
        loanterm: Number of months of the loan
        credithistory: Information about previous loans
        gender: The gender information
        married: Civil status
        graduate: Information about education
        selfemployed: Information about self-employment
        area: Information about the type of live area
	"""

GENDER_CHOICES = (
	    ('Male', 'Male'),
	    ('Female', 'Female')
	)
MARRIED_CHOICES = (
	    ('Yes', 'Yes'),
	    ('No', 'No')
	)
GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not_Graduate', 'Not_Graduate')
	)
SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)
firstname = models.CharField(max_length=15)
lastname = models.CharField(max_length=15)
dependants = models.IntegerField(default=0)
applicantincome = models.IntegerField(default=0)
coapplicatincome = models.IntegerField(default=0)
loanamt = models.IntegerField(default=0)
loanterm = models.IntegerField(default=0)
credithistory = models.IntegerField(default=0)
gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
married = models.CharField(max_length=15, choices=MARRIED_CHOICES)
graduate = models.CharField(max_length=15, choices=GRADUATED_CHOICES)
selfemployed = models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
area = models.CharField(max_length=15, choices=PROPERTY_CHOICES)


def __str__(self):
	return f'{self.firstname} {self.lastname} Approval'