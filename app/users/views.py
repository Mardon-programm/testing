from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class ConfirmUserView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.user.username)
            if user.is_verified:
                return Response({'message': 'Student already verified'}, status=200)
            return Response(UserSerializer(user).data, status=200)
        except User.DoesNotExist:
            return Response({'message': 'Student not found'}, status=404)

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.user.username)
            user.is_verified = True  
            user.save()  
            return Response({'message': 'Student information confirmed'}, status=200)
        except User.DoesNotExist:
            return Response({'message': 'Student not found'}, status=404)
