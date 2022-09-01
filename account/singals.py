from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Account

def createAccount(sender, instance, created, **kwargs):
    if created:
        user = instance
        account = Account.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = f"{user.first_name} {user.last_name}",
        )

def updateUser(sender, instance, created, **kwargs):
    account = instance
    user = account.user
    if created == False:
        try:
            user.first_name = account.name.split(' ').pop(0)
            user.last_name = account.name.split(' ').pop(-1)
        except:
            user.first_name = ''
            user.last_name = ''
        user.username = account.username
        user.email = account.email
        user.save()

def deleteAccount(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createAccount, sender=User)
post_save.connect(updateUser, sender=Account)
post_delete.connect(deleteAccount, sender=Account)