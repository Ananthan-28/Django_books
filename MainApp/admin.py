from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AuthorDataModel)
admin.site.register(BookDataModel)
admin.site.register(BookCategoryModel)
admin.site.register(ReviewModal)
