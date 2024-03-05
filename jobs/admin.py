from django.contrib import admin
from django.contrib.auth.models import User as CustomUser
from jobs.models import PostJob

# Register your models here.


@admin.register(PostJob)
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = "Job Portal"
admin.site.site_title = "Job Portal"


# @admin.register(CustomUser)
# class CustomerAdmin(admin.ModelAdmin):
#     pass
