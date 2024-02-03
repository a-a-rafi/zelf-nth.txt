from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ddjango
from .serializers import ddjangoSerializer
from rest_framework.decorators import api_view
import requests




@api_view(['GET', 'POST'])
def ddjango_list(request):
    # get all the ddjangos
    # serialize them
    # return json
    if request.method == 'GET':
        ddjangos = ddjango.objects.all()
        serializer = ddjangoSerializer(ddjangos, many=True)
        return JsonResponse(data={'ddjangos': serializer.data}, safe=False)
    if request.method == 'POST':
        # serializer = ddjangoSerializer(data=request.data)
        serializer = ddjangoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_created)


@api_view(['GET', 'PUT', 'DELETE'])
def ddjango_detail(request, id):

    try:
        ddjangos = ddjango.objects.get(pk=id)
    except ddjangos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ddjangoSerializer(ddjango)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ddjango.serializer(ddjango, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ddjangos.delete

