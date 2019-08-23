import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import *
from .models import *

# Create your views here.

@swagger_auto_schema(method='post', request_body=ClientInfoPostSerializer)
@api_view(['POST'])
def get_client_info(request):
    user_id = request.data.get('user_id', None)
    tariff_id = request.data.get('tariff_id', None)
    try:
        client_info = ClientInfo.objects.get(client__ext_id=user_id,
                                             tariff__ext_id=tariff_id)
    except ClientInfo.DoesNotExist:
        USERS_URL = 'https://api.test.brn.pw/clients/'
        TARIFFS_URL = 'https://api.test.brn.pw/tariffs/'

        ext_user = requests.get(USERS_URL + str(user_id)).json()
        new_user = ExtUser.objects.get_or_create(
            ext_id=ext_user['id'],
            name=ext_user['name'],
            username=ext_user['username'],
            email=ext_user['email'],
        )
        ext_tariff = requests.get(TARIFFS_URL + str(tariff_id)).json()
        new_tariff = ExtTariff.objects.get_or_create(
            ext_id=ext_tariff['id'],
            name=ext_tariff['name'],
            size=ext_tariff['size'],
            websites=int(ext_tariff['websites']),
            databases=int(ext_tariff['databases']),
        )

        client_info = ClientInfo.objects.get_or_create(
            client=new_user[0],
            tariff=new_tariff[0],
        )[0]
    serializer = ClientInfoReadSerializer(client_info, many=False)
    return Response(serializer.data, status=200)