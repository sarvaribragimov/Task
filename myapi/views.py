from django.contrib.auth import authenticate, login
from knox.views import LoginView as KnoxLoginView
from rest_framework import authentication, generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Student, Student_information
from .serializers import LoginSerializer, RegisterSerializer, StudentSerializer

from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User

@api_view(['POST'])
def register_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if not username or not password or not email:
        return Response({'error': 'Please provide username, password, and email'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'success': 'User created successfully'})

@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(KnoxLoginView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })


class LoginVieew(KnoxLoginView):
    permission_classes = ()
    
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            print(user)
            login(request, user)
            return Response({
                'user': user.username,
                'token': AuthToken.objects.create(user)[1]
            })
        else:
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response({
                'user': request.user.username,
                'message': 'You are already logged in.'
            })
        else:
            return Response({'message': 'You are not logged in.'})






#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
    
class StudentListApiview(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   


class StudentViewSet(ModelViewSet):
    queryset = Student_information.objects.all()
    serializer_class = StudentSerializer

class LogoutAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.auth.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)