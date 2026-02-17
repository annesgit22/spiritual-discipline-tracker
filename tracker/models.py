from django.db import models
from django.contrib.auth.models import User


class SpiritualItem(models.Model):
    ITEM_TYPES = [
        ('PRAYER', 'Prayer'),
        ('VIRTUE', 'Virtue'),
        ('NOVENA', 'Novena'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.item_type})"


class DailyLog(models.Model):
    item = models.ForeignKey(SpiritualItem, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    reflection = models.TextField(blank=True)

    def __str__(self):
        return f"{self.item.name} - {self.date}"

