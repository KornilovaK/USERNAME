from datetime import datetime
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Table, Reserve, Category, Menu


def index(request):
    return render(request, "shop/index.html")


def reservation(request):
    if request.method == 'POST':
        d1 = request.POST['day']
        m1 = request.POST['month']
        y1 = request.POST['year']

        h1 = request.POST['hour']
        try:
            dt = datetime(year=int(y1), month=int(m1), day=int(d1), hour=int(h1))
            tdt = datetime.now()
            if 20 < dt.hour < 9 or dt.strftime('%Y-%m-%d %H:%M') < tdt.strftime('%Y-%m-%d %H:%M'):
                return render(request, "shop/reservation.html", {
                    "message": "Choose another time"})

            fdt = f'{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}'
            tables = Table.objects.filter(datetime=dt.strftime('%Y-%m-%d %H:%M'))

            try:
                a = tables[0]
                return render(request, "shop/reservation.html", {
                    "tables": tables, "dt": fdt, "a": a})
            except:
                return render(request, "shop/reservation.html", {
                    "tnumbers": '12345678', "dt": fdt})
        except:
            return render(request, "shop/reservation.html", {
                "message": "Follow the instructions"})

    else:
        return render(request, "shop/reservation.html")


@csrf_exempt
def make(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        number = data.get("number")
        name = data.get("name")
        email = data.get("email")
        time = data.get("time")

        try:
            n, e = name[0], email[0]

            table = Table(number=number, datetime=time)
            table.save()
            reserve = Reserve(table=table, name=name, email=email)
            reserve.save()
            return JsonResponse({
                "message": f"Reservation was made successfully: {n}, {e}"
            }, status=201)

        except:
            return JsonResponse({
                "error": "Not all fields are filled out correctly"
            }, status=400)


def menu(request):
    categories = Category.objects.all()
    menu_pages = Menu.objects.all()
    return render(request, "shop/menu.html", {
        "categories": categories, "menu": [menu_page.serialize() for menu_page in menu_pages]})