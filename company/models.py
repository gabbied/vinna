from django.db import models

class Company(models.Model):
	company_name = models.CharField(max_length = 30)
	company_description = models.CharField(max_length = 200)
	company_address = models.CharField(max_length = 50)
	company_number = models.CharField(max_length = 20)
	company_contact_person = models.CharField(max_length = 50)
	def __str__(self):
		return self.company_name

class Employee(models.Model):
	employee_fname = models.CharField(max_length = 20)
	employee_mname = models.CharField(max_length = 20)
	employee_lname = models.CharField(max_length = 20)
	employee_sname = models.CharField(max_length = 5)
	employee_description = models.CharField(max_length = 200)	
	def __str__(self):
		return self.employee_fname