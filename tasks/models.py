from django.db import models
from uuid import uuid4

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True, null=True)
    emailVerified = models.DateTimeField(null=True)
    image = models.TextField(null=True)

    class Meta:
        db_table = 'users'
        managed = True

class VerificationToken(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.TextField(null=False)
    expires = models.DateTimeField(null=False)
    token = models.TextField(null=False)

    class Meta:
        db_table = 'verification_tokens'
        managed = True
        unique_together = ('identifier', 'token')
        
    def __str__(self):
        return f"{self.identifier} - {self.token}"

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField(null=False)
    type = models.CharField(max_length=255, null=False)
    provider = models.CharField(max_length=255, null=False)
    providerAccountId = models.CharField(max_length=255, null=False)
    refresh_token = models.TextField(null=True)
    access_token = models.TextField(null=True)
    expires_at = models.BigIntegerField(null=True)
    id_token = models.TextField(null=True)
    scope = models.TextField(null=True)
    session_state = models.TextField(null=True)
    token_type = models.TextField(null=True)

    class Meta:
        db_table = 'accounts'
        managed = True


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField(null=False)
    expires = models.DateTimeField(null=False)
    sessionToken = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'sessions'
        managed = True