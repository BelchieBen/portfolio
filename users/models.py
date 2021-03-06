from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager


# CustomUserManager class
class CustomUserManager(BaseUserManager):
	def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
		if not email:
			raise ValueError("You must provide an email")
		if not password:
			raise ValueError("You must set a password")

		user = self.model(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
			mobile = mobile,
			**extra_fields
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_active',True)
		extra_fields.setdefault('is_superuser',False)
		return self._create_user(email,password,first_name,last_name,mobile,password, **extra_fields)

	def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_active',True)
		extra_fields.setdefault('is_superuser',True)
		return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

# Custom user class
class User(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(unique=True, max_length=256)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	mobile = models.CharField(max_length=11)

	is_staff = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_images')

	def __str__(self):
		return f'{self.user.email} Profile'

