from django.contrib import admin
from .models import Student, Course, Enrollment, Student2, Course2, Person, Account

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Student2)
admin.site.register(Course2)
admin.site.register(Enrollment)
admin.site.register(Account)
admin.site.register(Person)