# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

CONDITIONS = (
    (0, 'Over The Fucking Moon'),
    (1, 'Like Dancing'),
    (2, 'Excellent'),
    (5, 'Excited'),
    (10, 'Happy'),
    (15, 'Positive'),
    (20, 'Optimistic'),
    (25, 'Very Dude Like'),
    (27, 'Hungry'),
    (29, 'Tired'),
    (30, 'Bored'),
    (35, 'Pessimistic'),
    (40, 'Overwhelmed'),
    (45, 'Disappointed'),
    (50, 'Worried'),
    (55, 'Angry'),
    (60, 'Jelous'),
    (65, 'Insecure'),
    (70, 'Fear'),
    (75, 'Grief'),
    (80, 'Despair'),
    (85, 'Apathetic'),
)
# Create your models here.
class Thought(models.Model):
    user = models.ForeignKey(User, related_name = 'thoughts')
    recorded_at = models.DateTimeField(default = timezone.now, editable=False)
    condition = models.IntegerField(choices=CONDITIONS)
    notes = models.TextField(blank=True, default='' )

    def __str__(self):
        return '{}: {}'.format(self.recorded_at.strftime('%Y-%m-%d %H:%M:%S'), self.get_condition_display())
