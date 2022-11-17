from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import AuthUser
from .serializers import dataSerializer

#Create your views here.

@api_view(['GET']) # 데코레이션 : GET 메서드 사용
def getTestDatas(request): 
    datas = AuthUser.objects.all() # user 테이블에 있는 모든 데이터를 읽어들임
    serializer = dataSerializer(datas, many=True) # 데이터 직렬화 (json -> DB data or DB data -> json 여기서는 DB에 있는 데이터를 json 형태로 바꿔줌)
    return Response(serializer.data)