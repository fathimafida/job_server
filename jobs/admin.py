from django.contrib import admin

from jobs.models import CustomUser, PostJob

# Register your models here.


@admin.register(PostJob)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomUser)
class CustomerAdmin(admin.ModelAdmin):
    pass
