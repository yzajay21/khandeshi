from django.db import models

# Create your models here.
class RegisterProfile(models.Model):
	#user 		= models.OneToOneField(User,null=True,blank=True,related_name='profeesional_profile')
	VA_CHOICES = (
        ('Job', 'job'),
        ('Buisness', 'buisness'),
     
    )
	first_name = models.CharField(max_length=64, db_index=True)
	middle_name = models.CharField(max_length=64, db_index=True)
	last_name = models.CharField(max_length=64, db_index=True)
	mobile_no = models.CharField(max_length=64, db_index=True)
	description = models.TextField(max_length=200)    
	date_of_birth = models.DateField(blank=True, null=True)
	pan = models.CharField(max_length=200,blank=True,null=True)
	aadhar = models.CharField(max_length=200,blank=True,null=True)
	state = models.CharField(max_length=200)
	city= models.CharField(max_length=200)
	address = models.CharField(max_length=500)
	permanent_address = models.CharField(max_length=500)
	
	name_of_relative = models.CharField(max_length=200)
	mobile_no_of_relative = models.CharField(max_length=13)
	emergency_contact    =  models.CharField(max_length=13)
	blood_group   = models.CharField(max_length=20)

	Profession = models.CharField(max_length=20, choices=VA_CHOICES)
	#practice = models.ForeignKey(Practice, on_delete=models.CASCADE, blank=True, null=True)
	def __str__(self):
		return 'Profile Of {} {} '.format(self.first_name,self.last_name)