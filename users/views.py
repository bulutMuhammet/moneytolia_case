from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model


User = get_user_model()

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainPairSerializer

class CreateUserView(CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer



