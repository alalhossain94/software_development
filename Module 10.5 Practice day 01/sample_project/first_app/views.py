from django.shortcuts import render
import datetime
def home(request):
    d={'author': 'Rahim', 'age': 20, 'lst': ['python', 'is', 'best'], 'birthday': datetime.datetime.now(),    'courses': [
           {
               'id': 1,
               'name': 'Python',
               'fee': 5000
           },
           {
               'id': 2,
               'name': 'django',
               'fee': 7000
           },
           {
               'id': 3,
               'name': 'Database',
               'fee': 4000
           },
       ]}
    return render(request, 'home.html', d)