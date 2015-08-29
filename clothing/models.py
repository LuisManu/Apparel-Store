from django.db import models
from django.template.defaultfilters import slugify
# from django.core.validators import RegexValidator


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images')



class Category(models.Model):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = 'Categories'

	def __unicode__(self):
		return self.name



class Department(models.Model):
	name = models.CharField(max_length=6, unique=True)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Department, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name




class ApparelInfo(models.Model):
	category = models.ForeignKey(Category)
	department = models.ForeignKey(Department)
	title = models.CharField(max_length=100)
	brand = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	description = models.TextField()
	date_time = models.DateTimeField(auto_now_add=True)
	xsmall = models.IntegerField(default=0)
	small = models.IntegerField(default=0)
	medium = models.IntegerField(default=0)
	large = models.IntegerField(default=0)
	xlarge = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='product_images', null=True, blank=True)
	image2 = models.ImageField(upload_to='product_images', null=True, blank=True)
	image3 = models.ImageField(upload_to='product_images', null=True, blank=True)
	image4 = models.ImageField(upload_to='product_images', null=True, blank=True)
	image5 = models.ImageField(upload_to='product_images', null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(ApparelInfo, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = 'Apparel Item'



# class ApparelImage(models.Model):
#     property = models.ForeignKey(ApparelInfo, related_name='images')
#     image = models.ImageField()











class Store(models.Model):
	title = models.CharField(max_length=50)
	blurb = models.TextField()
	email = models.EmailField()
	# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=150)
	city = models.CharField(max_length=50)
	hours = models.CharField(max_length=100)
	image = models.ImageField(upload_to='store_images')
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Store, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.city
