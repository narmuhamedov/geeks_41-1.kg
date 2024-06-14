from django.contrib import admin
from news_blog.models import Employees, Poster, ReviewEmployees, Tag, Product
from django.utils.safestring import mark_safe




class EmpPreview(admin.ModelAdmin):
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

admin.site.register(Employees, EmpPreview)
admin.site.register(Poster)
admin.site.register(ReviewEmployees)
admin.site.register(Tag)
admin.site.register(Product)
