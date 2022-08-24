from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# task_1 models
class CreatedAt(models.Model):
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class Account(models.Model):
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)


class Session(CreatedAt):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="sessions",
        blank=True,
        null=True,
    )


class Action(CreatedAt):
    read = "r"
    create = "c"
    update = "u"
    delete = "d"
    TYPE_CHOICES = [
        (read, "read"),
        (create, "create"),
        (update, "update"),
        (delete, "delete")
    ]
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name="actions",
        blank=True,
        null=True,
    )


# task_2 models
class TimeModel(models.Model):
    date = models.DateField(null=False, blank=False)
    month = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(1),
            MaxValueValidator(12),
        )
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.id} {self.date} {self.month}'


class Accrual(TimeModel):
    pass


class Payment(TimeModel):
    pass
