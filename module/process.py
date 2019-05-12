from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request
from addon import student_food
from addon import train
from addon import find_book
import time
from module.buttons import *
def JsonReturn(msg,buttons):
    return JsonResponse(
        {
        'message': {
            'text': msg,
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': buttons
        }
    },json_dumps_params = {'ensure_ascii': False})

def JsonLibraryReturn(msg,url,width,height,buttons):
    print('http://nanayagoon.ivyro.net/' + str(url) + '.png')
    return JsonResponse(
        {
            'message': {
                'text': msg,
                'photo':{
                    'url': 'http://nanayagoon.ivyro.net/' + str(url) + '.png',
                    'width': int(width),
                    'height': int(height)
            }},
            'keyboard': {
                'type': 'buttons',
                'buttons': buttons
            }
        },json_dumps_params = {'ensure_ascii': False}
    )

def JsonErrorReturn(msg):
    return JsonResponse(
        {
        'message': {
            'text': msg,
        },
        'keyboard': {
            'type': 'text',
        }
    },json_dumps_params = {'ensure_ascii': False}
    )

def JsonMapReturn(msg,url,width,height):
    return JsonResponse(
        {
            'message': {
                'text': msg,
                'photo':{
                    'url': 'http://nanayagoon.ivyro.net/' + str(url),
                    'width': int(width),
                    'height': int(height)

            }},
            'keyboard': {
                'type': 'buttons',
                'buttons': building
                }
            },json_dumps_params = {'ensure_ascii': False}

        )
