from django.db import models
from django.core.validators import RegexValidator

class user_details(models.Model):
   
    user_id_regex = RegexValidator(
        regex=r'^USR\d{5}$', 
        message='User ID must be in the format USR followed by 5 digits',
        code='invalid_user_id'
    )

    user_id = models.CharField(
        max_length=10, 
        primary_key=True, 
        validators=[user_id_regex]
    )
    user_fname = models.CharField(max_length=15)
    user_mname = models.CharField(max_length=15, null=True)
    user_lname = models.CharField(max_length=15, null=True)
    pan_number = models.CharField(max_length=10, unique=True)
    email_id = models.EmailField(max_length=20, unique=True)
    phone_number = models.IntegerField(unique=True)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __meta__():
        table_name = "user_details"

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
