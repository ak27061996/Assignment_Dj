
from django.db import models
import datetime


class UserManager(models.Manager):
    """
    manager for Recruiter model.
    """

    def create_user(self, username, password='xyz', email=''):
        """
        Creates and saves a User with the given username, e-mail and password.
        """

        user = self.model(username=username)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        if bool(email):
            user.email = email
        user.save(using=self._db)
        return user


class User(models.Model):
    name = models.CharField(_('name'), max_length=30, blank=True)
    username = models.CharField(
        max_length=30, unique=True,
        help_text=_(
            "Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters"),
        verbose_name="User name")
    password = models.CharField(
        _('password'), max_length=128,
        help_text=_(
            "Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change "
            "password form</a>."))
    objects = UserManager()


class AnswerM(models.model):
    ans = models.CharField(max_length=500, blank=False)
    date = models.DateTimeField(_('created date'), default=datetime.datetime.now)

class QuestionM(models.Model):
    question = models.CharField(max_length=500, blank=False)
    ans = models.ForeignKey(AnswerM, verbose_name="Answer", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Asked BY", on_delete=models.CASCADE)