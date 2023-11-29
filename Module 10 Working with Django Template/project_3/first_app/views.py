from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author': 'Rahim', 'age': 20, 'lst': [1,2,3], 'courses': [
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