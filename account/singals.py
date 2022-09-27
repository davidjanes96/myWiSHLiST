from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import Account
from django.core.mail import send_mail
from django.conf import settings

def createAccount(sender, instance, created, **kwargs):
    if created:
        user = instance
        account = Account.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = f"{user.first_name} {user.last_name}",
        )

        subject = 'Welcome to MyWiSHLiST!'
        message = 'Thank You for creating an account!\nMyWiSHLiST will help you create wishlists and better organize your buying schedule!\n\nGet out there and start wishing!\n\nMyWiSHLiST Team'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [account.email],
            fail_silently=False,
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
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(createAccount, sender=User)
post_save.connect(updateUser, sender=Account)
post_delete.connect(deleteAccount, sender=Account)