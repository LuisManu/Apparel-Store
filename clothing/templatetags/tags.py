from django import template
from clothing.models import Category, Department, ApparelInfo

register = template.Library()


@register.inclusion_tag('cats.html')
def get_category_list():
	departments = Department.objects.all()
	category = Category.objects.all()
	apparel = ApparelInfo.objects.all()
	department_list = []
	my_dict = {}
	dict_list_of_keys = []


	print

	for department in departments:
		my_dict[department] = []

	print my_dict

	print

	for x in my_dict:
		dict_list_of_keys.append(x)

	print len(dict_list_of_keys)
	print
	for x in apparel:
		# if x.department == my_dict.has_key
		print x.category

		print

	print
	department = Department.objects.get(slug='womens')
	foo = ApparelInfo.objects.filter(department=department)

	for x in foo:
		print x.category
	print

	return {'cats': Category.objects.all(), 'departments': Department.objects.all()}


	# products = ApparelInfo.objects.filter(department=department).order_by('-date_time')
	# cats = []
	# for product in products:
	# 	if str(product.category) in cats:
	# 		pass
	# 	else:
	# 		cats.append(str(product.category))