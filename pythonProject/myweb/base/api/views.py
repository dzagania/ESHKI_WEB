from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Eshkhi
from .serialicers import ClotheSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET / api",
        "GET /api/clothes",
        "GET /api/clothe/:id"

    ]
    return Response()


@api_view(['GET'])
def get_clothes(request):
    clothes = Eshkhi.objects.all()
    serializer = ClotheSerializer(clothes, many=True)
    return Response(serializer.data)


@api_view(['GTE'])
def get_clothe(request, id):
    clothe = Eshkhi.objects.get(id=id)
    serializer = ClotheSerializer(clothe, many=False)
    return Response(serializer.data)
