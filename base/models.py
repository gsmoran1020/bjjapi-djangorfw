from django.db import models


class Technique(models.Model):

    CHOICES = ['easy', 'intermediate', 'advanced', 'choke', 'sweep', 'escape',
    'joint_lock', 'takedown', 'mixed']


    EASY = 'easy'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'
    LEVELS = [
        (EASY, 'easy'),
        (INTERMEDIATE, 'intermediate'),
        (ADVANCED, 'advanced')
    ]

    CHOKE = 'choke'
    SWEEP = 'sweep'
    ESCAPE = 'escape'
    JOINT_LOCK = 'joint_lock'
    TAKEDOWN = 'takedown'
    MIXED = 'mixed'
    TYPES = [
        (CHOKE, 'choke'),
        (SWEEP, 'sweep'),
        (ESCAPE, 'escape'),
        (JOINT_LOCK, 'joint_lock'),
        (TAKEDOWN, 'takedown'),
        (MIXED, 'mixed')
    ]


    id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name="ID")
    name = models.CharField(unique=True, max_length=100, null=False)
    type = models.CharField(
        max_length=10,
        choices=TYPES,
        default=MIXED, 
        null=False
    )
    description = models.TextField(null=False)
    difficulty = models.CharField(
        max_length=12,
        choices=LEVELS,
        default=EASY,
        null=False
    )
    link = models.URLField(max_length=350, null=False)

    def __str__(self):
        return self.name
