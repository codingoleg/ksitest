from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mother = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children_mother',
        on_delete=models.SET_NULL
    )
    father = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children_father',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
