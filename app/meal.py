from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sqlite3

import time

def Response(a):
    return JsonResponse(a,json_dumps_params = {'ensure_ascii':False})

@csrf_exempt
def upload(request):
    query = request.POST['query']

    conn = sqlite3.connect('/ShuttleWhereDB/meals.db')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("업로드 완료")
    return Response({"a":"b"})




@csrf_exempt
def download(request):
    query = request.POST['query']
    conn = sqlite3.connect('/ShuttleWhereDB/meals.db')
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()

    return Response(
    {"status":"ok",
    "content":row[2],
    "time":row[3]}
    )


@csrf_exempt
def login(request):
    ids = request.POST['id']
    password = request.POST['password']
    if (ids == "wookoo" or ids=="helpus") and password == "1q2w3e":
        return Response({"status":"ok"})

    return Response({"status":"bad"})
