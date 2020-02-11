from datetime import date, timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'dates':
                [
                    date.today(),
                    date.today() + timedelta(days=1),
                    date.today() + timedelta(days=2)
                ]
        }
        return Response(data)
