from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import ProductType, PC
from .serializers import ProductType_serializer


@api_view(['GET', 'POST'])
def box_list(request):
    pass

@api_view(['GET', 'POST'])
def producttype_list(request):

    if request.method == 'GET':
        types = ProductType.objects.all() # select * from producttypes
        serializer = ProductType_serializer(types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductType_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQmakeUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def producttype_detail(request, pk):

    try:
        product_type = ProductType.objects.get(pk=pk)
    except ProductType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductType_serializer(product_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductType_serializer(product_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product_type.active = False
        product_type.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['delete'])
def test_tasks(request, task):
    if task == 1:
        result = PC.objects.filter(price__range=(300,  600))
        for item in result:
            print(item.model_id, item.speed, item.hd, item.price)

    elif task == 2:
        pass


    return Response(status=status.HTTP_200_OK)