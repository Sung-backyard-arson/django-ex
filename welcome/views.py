import os
import datetime
import json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView
from .forms import PracticeForm

# Create your views here.
def index(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    """Takes an request as a parameter and gives the count of pageview objects as reponse"""
    return HttpResponse(PageView.objects.count())

def test(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
    
    return_dict = {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count(),
        'form': PracticeForm(),
        'medical_institution': '初期値', 
        'phone_number': '初期値', 
        'office_hours': '初期値', 
    }

    medical_institutions = read_medical_institutions()

    if (request.method == 'POST'):
        year, month, day = list(map(int, request.POST['consultation_day'].split("-")))
        dt = datetime.datetime(year, month, day)

        department_dict = {1: "内科", 2: "内科", 3: "歯科", 4: "整形外科", 5: "耳鼻科", 6: "皮膚科", 7: "整形外科"}
        department = department_dict[int(request.POST['condition'])]

        institution = medical_institutions[department]
        return_dict['medical_institution'] = institution["病院名"]
        return_dict['phone_number'] = institution["TEL"]        
        return_dict['office_hours'] = institution["営業時間"][dt.strftime('%a')]
        return_dict['form'] = PracticeForm(request.POST)

    return render(request, 'test/site/public/index.html', return_dict)

def measurements(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    # global CURRENTMODE

    # app.jsから移植
    # ここわかんない。
    
    # logger.debug('called the measurements endpoint for ' + req.query.id);

    # if (request.method == 'GET'):
    #     if (CURRENTMODE == MODE.TEST):
    #         measurements = {
    #             smokerstatus: 'Former smoker',
    #             dia: 88,
    #             sys: 130,
    #             bmi: 19.74,
    #             bmirange: 'normal',
    #             weight: 54.42,
    #             height: 1.6603
    #         }
        
    #     res.send(measurements);

    return render(request, 'test/site/public/measurements.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def jee(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'test/site/public/jee.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def setting(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'test/site/public/setting.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def about(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'test/site/public/about.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def admin(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'test/site/public/admin.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def labs(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'test/site/public/labs.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def login(request):
    """Takes an request object as a parameter and creates an pageview object then responds by rendering the index view."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    # TODO: ここにログイン処理を追加
    print(request.method)
    if (request.method == 'POST'):
        print("Hello")

    # my_dict = {
    #     'username': '',
    #     'password': '', 
    # }
    # if (request.method == 'POST'):
    #     if 'username' in request.GET:
    #         my_dict['username'] = request.GET['username']
    #     if 'password' in request.GET:
    #         my_dict['password'] = request.GET['password']

    return render(request, 'test/site/public/login.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def read_medical_institutions():
    """""
    json_open = open('./medical_institutions.json', 'r')
    medical_institutions = json.load(json_open)
    """""
    medical_institutions = {
        "耳鼻科":{
            "病院名":"〇〇耳鼻科",
            "TEL": "000-1234-5678", 
            "営業時間": {
                "Mon": "10:00~12:00, 15:00~17:00",
                "Tue": "10:00~12:00, 15:00~17:00",
                "Wed": "10:00~12:00, 15:00~17:00",
                "Thu": "休業",
                "Fri": "10:00~12:00, 15:00~17:00",
                "Sat": "10:00~13:00",
                "Sun": "10:00~12:00, 15:00~17:00"
            }
        },
        "内科":{
            "病院名":"△△内科",
            "TEL": "001-1234-5678", 
            "営業時間": {
                "Mon": "9:00~12:00, 14:00~16:00",
                "Tue": "9:00~12:00, 14:00~16:00",
                "Wed": "9:00~12:00, 14:00~16:00",
                "Thu": "9:00~12:00, 14:00~16:00",
                "Fri": "9:00~12:00",
                "Sat": "9:00~12:00, 14:00~16:00",
                "Sun": "9:00~12:00, 14:00~16:00"
            }
        },
        "歯科":{
            "病院名":"□□デンタルクリニック",
            "TEL": "002-1234-5678", 
            "営業時間": {
                "Mon": "10:00~12:00, 15:00~19:00",
                "Tue": "10:00~12:00, 15:00~19:00",
                "Wed": "10:00~12:00, 15:00~19:00",
                "Thu": "休業",
                "Fri": "10:00~12:00, 15:00~19:00",
                "Sat": "10:00~12:00, 15:00~19:00",
                "Sun": "休業"
            }
        },
        "整形外科":{
            "病院名":"◯△整形外科",
            "TEL": "003-1234-5678", 
            "営業時間": {
                "Mon": "10:00~13:00, 15:00~17:00",
                "Tue": "10:00~13:00, 15:00~17:00",
                "Wed": "10:00~13:00",
                "Thu": "10:00~13:00, 15:00~17:00",
                "Fri": "10:00~13:00, 15:00~17:00",
                "Sat": "10:00~13:00, 15:00~17:00",
                "Sun": "休業"
            }
        },
        "皮膚科":{
            "病院名":"◯□皮膚科",
            "TEL": "004-1234-5678", 
            "営業時間": {
                "Mon": "10:00~12:00, 15:00~16:30",
                "Tue": "10:00~12:00, 15:00~16:30",
                "Wed": "10:00~13:00",
                "Thu": "10:00~12:00, 15:00~16:30",
                "Fri": "10:00~12:00, 15:00~16:30",
                "Sat": "10:00~12:00, 15:00~16:30",
                "Sun": "休業"
            }
        }
    }
    return medical_institutions

# app.jsより移植
MODE = {
    "TEST": 1,
    "Z": 2,
    "OPENSHIFT": 3
}
CURRENTMODE = MODE['TEST']
API_URL = ""

def mode(request):
    global CURRENTMODE
    # app.jsの30-38行目を移植
    if (request.method == 'POST'):
        if 'mode' in request.GET:
            CURRENTMODE = request.GET['mode']
        if 'url' in request.GET:
            CURRENTMODE = request.GET['url']
    
        return HttpResponse({
            "modes": MODE,
            "mode": CURRENTMODE
        })
    # app.jsの40-44行目を移植
    elif (request.method == 'GET'):
        return HttpResponse({
            "modes": MODE,
            "mode": CURRENTMODE
        })
    else:
        return

def info(request):
    global CURRENTMODE

    if (request.method == 'GET'):
        # app.jsの48-66行目を移植

        # logger.debug('called the information endpoint for ' + req.query.id);

        if (CURRENTMODE == MODE['TEST']):
            patientdata = {
                "personal": {
                    "name": "Ralph DAlmeida",
                    "age": 38,
                    "gender": "male",
                    "street": "34 Main Street",
                    "city": "Toronto",
                    "zipcode": "M5H 1T1"
                },
                "medications": ["Metoprolol", "ACE inhibitors", "Vitamin D"],
                "appointments": ["2018-01-15 1:00 - Dentist", "2018-02-14 4:00 - Internal Medicine", "2018-09-30 8:00 - Pediatry"]
            }

            return HttpResponse(patientdata)
        else:
            return
            # この辺はbackendpi.jsの書き直しも必要そうなので、書くのが難しい。
            # そのため、現状はCURRENTMODE=TESTでしか動かせない。