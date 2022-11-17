from django.db import models
from accounts.models import Account



class Follow(models.Model):
    following = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="following")
    followers = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="followers")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.following} - {self.followers}"