from django.db import models
from accounts.models import Account



class Follow(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user", null=True)
    following = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="following", null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.following.username}"