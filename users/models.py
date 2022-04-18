from django.db import models
from django.contrib.auth.models import User

Gender_Option = (
    ('Male','Male'),
    ('Female','Female'),
    ('Other', 'Other'),
)

class AdminProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
	age = models.IntegerField(verbose_name='Age')
	cnic = models.IntegerField(verbose_name='CNIC #')
	contact_number = models.IntegerField(verbose_name='Contact #')
	address = models.CharField(max_length=500, verbose_name='Address')
	gender = models.CharField(max_length=6, choices = Gender_Option, verbose_name='Gender')

	def __str__(self):
		return f'User: {self.user.first_name} Profile: {self.pk}'

	class Meta:
		verbose_name = 'Admin Profile'
		verbose_name_plural = 'Admin Profiles'

class FarmerProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	age = models.IntegerField(verbose_name='Age')
	cnic = models.IntegerField(verbose_name='CNIC #')
	contact_number = models.IntegerField(verbose_name='Contact #')
	address = models.CharField(max_length=500, verbose_name='Address')
	gender = models.CharField(max_length=6, choices = Gender_Option, verbose_name='Gender')

	def __str__(self):
		return f'User: {self.user.first_name} Profile: {self.pk}'

	class Meta:
		verbose_name = 'Farmer Profile'
		verbose_name_plural = 'Farmer Profiles'

class CompanyProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='compnay_profile')
	ntn = models.IntegerField(verbose_name='NTN #')
	address = models.CharField(max_length=500, verbose_name='Address')
	office_contact_number = models.IntegerField(verbose_name='Contact #')

	def __str__(self):
		return f'User: {self.user.first_name} Profile: {self.pk}'

	class Meta:
		verbose_name = 'Company Profile'
		verbose_name_plural = 'Company Profiles'


class CompanyOwner(models.Model):
	compnay = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='compnay_owner')
	first_name = models.CharField(max_length=150, verbose_name='First Name')
	last_name = models.CharField(max_length=150, verbose_name='Last Name')
	cnic = models.IntegerField(verbose_name='CNIC #')
	contact_number = models.IntegerField(verbose_name='Contact #')
	address = models.CharField(max_length=500, verbose_name='Address')
	gender = models.CharField(max_length=6, choices=Gender_Option, verbose_name='Gender')

	def __str__(self):
		return f'User: {self.user.first_name} Company Profile: {self.company.pk} Owner Profile: {self.pk}'

	class Meta:
		verbose_name = 'Company Owner'
		verbose_name_plural = 'Company Owners'

class CompanyManager(models.Model):
	compnay = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='compnay_manager')
	first_name = models.CharField(max_length=150, verbose_name='First Name')
	last_name = models.CharField(max_length=150, verbose_name='Last Name')
	cnic = models.IntegerField(verbose_name='CNIC #')
	contact_number = models.IntegerField(verbose_name='Contact #')
	address = models.CharField(max_length=500, verbose_name='Address')
	gender = models.CharField(max_length=6, choices=Gender_Option, verbose_name='Gender')

	def __str__(self):
		return f'User: {self.user.first_name} Company Profile: {self.company.pk} Manager Profile: {self.pk}'

	class Meta:
		verbose_name = 'Company Manager'
		verbose_name_plural = 'Company Managers'
