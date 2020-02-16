from datetime import date, timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class GetTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if hasattr(user, 'vendor'):
            type = 'vendor'
            name = user.vendor.name
        elif hasattr(user, 'buyer'):
            type = 'buyer'
            name = user.buyer.name
        else:
            type = 'admin'
            name = user.username
        data = {
            'name': name,
            'type': type,
            'username': user.username
        }
        return Response(data)
