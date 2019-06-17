from django.db import models

# Create your models here.
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver


class BaseModel(models.Model):
    """
    Base class for common fields
    """
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    phone_number =  models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        abstract = True



class UserProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)


    class Meta:
        app_label           = 'caller_app'
        verbose_name        = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return ("user {} with phone_number {}" .format(self.user_id,self.phone_number))



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone_number','created')
    search_fields = ('id','user__first_name','user__id','user__email')
    readonly_fields = ('created', 'modified',)

admin.site.register(UserProfile,UserProfileAdmin)


class UserContact(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name   = models.CharField(max_length=200)
    email   = models.EmailField(null=True,blank=True)

    class Meta:
        app_label           = 'caller_app'
        verbose_name        = "User Contact"
        verbose_name_plural = "User Contacts"

    def __str__(self):
        return ("{} : {} : {}" .format(self.id,self.name,self.phone_number))

class UserContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone_number',)
    search_fields = ('id','name','phone_number')
    readonly_fields = ('created', 'modified',)

admin.site.register(UserContact,UserContactAdmin)



class SpamNumber(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        app_label           = 'caller_app'
        verbose_name        = "User Contact"
        verbose_name_plural = "User Contacts"

    def __str__(self):
        return ("{} : {} : {}" .format(self.id,self.name,self.phone_number))

class SpamNumberAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone_number',)
    search_fields = ('id','user__id','phone_number')
    readonly_fields = ('created', 'modified',)

admin.site.register(SpamNumber,SpamNumberAdmin)
