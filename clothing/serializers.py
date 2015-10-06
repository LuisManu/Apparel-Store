from rest_framework import serializers

from models import ApparelInfo, Department, Category

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		field = ('name')
		exclude = ['id', 'slug']

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		field = ('name')
		exclude = ['id', 'slug']


class ApparelSerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	department = DepartmentSerializer()
	class Meta:
		model = ApparelInfo
		fields = ('id', 'title', 'brand', 'price', 'description', 'category', 'department', 'image')