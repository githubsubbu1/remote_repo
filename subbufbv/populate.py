import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','subbufbv.settings')
import django
django.setup()
from firstapp.models import Employee
from random import*
from faker import Faker
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(10000,25000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
populate(25)
