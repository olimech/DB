from datetime import date

from django.shortcuts import render
from .models import Course, Student, Enrollment, Student2, Course2, Account, Person


def index(request):
    # students = Student.objects.filter(course__name='Algebra')
    # courses = Student.objects.get(id=2).course.all()
    #
    # python, _ = Course.objects.get_or_create(name='Algebra')
    # student, _ = python.student_set.get_or_create(name='Bob')
    #
    # student = Student.objects.create(name='Tom')
    # python.student_set.add(student)
    #
    # st = Student.objects.get(id=3)
    # alg = Course.objects.get(name='Algebra')
    #
    # alg.student_set.add(st)
    # res = Student.objects.get(id=3).course.all()
    # res.student_set.remove(st)
    # res = alg.student_set.all()

    # django = Course2.objects.create(name='Django')
    # tom = Student2.objects.create(name='Tom')
    #
    # res = Enrollment(student=tom, course=django, date=date.today(), mark=5)
    # res.save()

    # st = Student2.objects.get(id=1)
    # crs = Course2.objects.get(id=2) ###############3
    # res = st.course.all()
    # res = crs.student2_set.all()############3#

    # res, _ = Account.objects.get_or_create(login='Sam1234', password='1234556', user=sam)

    # res = Account.objects.get(user__id=2)
    # res.user.name = 'Sany'
    # res.user.save()

    tom = Person.objects.create(name='Tom')
    # acu = Account(login='sdfsdf', password='5345345')
    # tom.account = acu
    # tom.account.save()

    tom = Person.objects.get(account__login='ertert')

    return render(request, 'app/index.html', context={'students': res})




