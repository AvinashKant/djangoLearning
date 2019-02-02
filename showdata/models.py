from django.db import models

# Create your models here.
class ContactUs(models.Model):  
	subject		= models.CharField(max_length=20)  
	message 	= models.CharField(max_length=100)  
	sender 		= models.EmailField()  
	c_myself 	= models.CharField(max_length=15)  
	class Meta:  
		db_table = "ContactUs" 
