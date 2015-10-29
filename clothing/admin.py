from django.contrib import admin
from .models import ApparelInfo, Category, Department, Store, CarouselImage


class CarouselImageAdmin(admin.ModelAdmin):
    model = CarouselImage
    extra = 3




# class ApparelImageInline(admin.TabularInline):
#     model = ApparelImage
#     extra = 3



class ApparelInfoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ['title', 'brand']
	list_filter = ['category', 'department', 'likes_counter']
	# inlines = [ ApparelImageInline, ]
	search_fields = ('title',)
	fieldsets = [
		(None, {'fields': ['category', 'department', 'title', 'brand', 'price', 'description', 'likes_counter', 'slug']}),
		('Sizes', {'fields': ['xsmall', 'small', 'medium', 'large', 'xlarge']}),
		('images', {'fields': ['image', 'image2', 'image3', 'image4', 'image5']})
	]

	class Meta:
		model = ApparelInfo





    





class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

	class Meta:
		model = Category


class DepartmentAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

	class Meta:
		model = Department


class StoreAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = Store

admin.site.register(ApparelInfo, ApparelInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(CarouselImage, CarouselImageAdmin)
# admin.site.register(UserProfile)