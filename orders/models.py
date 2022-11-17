from django.db import models
from accounts.models import Account
from postad.models import PostAD



class InterestAd(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    adpost = models.ForeignKey(PostAD, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.adpost.title}"