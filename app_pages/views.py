from django.shortcuts import render


def index(request):
    oylar =[
    {'id ' : 1, 'oy': 'yanvar' , 'kunligi': 'yanavar 31 kun bor' },
    {'id ' : 2, 'oy': 'fevral', 'kunligi': 'fevral 28 kun bor' },
    {'id ' : 3, 'oy': 'mart' , 'kunligi': 'mart 31 kun bor'},
    {'id ' : 4, 'oy': 'aprel','kunligi': 'aprel 30 kun bor' },
    {'id ' : 5, 'oy': 'may' , 'kunligi': 'may 31 kun bor'},
    {'id ' : 6, 'oy': 'iyun', 'kunligi': 'iyun 30 kun bor' },
    {'id ' : 7, 'oy': 'iyul' , 'kunligi': 'iyul 31 kun bor'},
    {'id ' : 8, 'oy': 'avgust' ,'kunligi': 'avgust 31 kun bor'},
    {'id ' : 9, 'oy': 'sentabr', 'kunligi': 'sentabr 30 kun bor'},
    {'id ' : 10, 'oy': 'oktabt' , 'kunligi': 'oktabr 31 kun bor'},
    {'id ' : 11, 'oy': 'noyabr', 'kunligi': 'noyabr 30 kun bor' },
    {'id ' : 12, 'oy': 'dekabr', 'kunligi': 'dekabr 31 kun bor' }

    ]

    return render(request, 'index5.html', context={'oylar': oylar})


def kunlari(request, pk):
    global oylar
    return render(request, 'kunlar.html', context={'man': oylar[pk-1]})