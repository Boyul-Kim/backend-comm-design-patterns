from django.shortcuts import render
from django.http import HttpResponse
import asyncio

# Create your views here.
def index(request):
    return HttpResponse("Push testing")

async def pushWebsocket(request):
    print('testing websocket')
    return HttpResponse("websocket test")
