# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.decorators import task

@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="mul_two_numbers")
def mul(x, y):
    return x * y
