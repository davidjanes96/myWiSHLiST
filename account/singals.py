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

def deleteAccount(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createAccount, sender=User)
post_delete.connect(deleteAccount, sender=Account)