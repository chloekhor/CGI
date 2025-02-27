from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate
from django.middleware.csrf import get_token
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
def register(request):
    data = request.data
    if 'name' not in data or 'email' not in data or 'password' not in data:
        return Response({'error': 'Missing required fields'}, status=400)

    # 检查 email 是否已经注册
    if User.objects.filter(email=data['email']).exists():
        return Response({'error': 'Email already exists'}, status=400)

    # 哈希密码
    hashed_password = make_password(data['password'])

    # 创建用户
    user = User.objects.create(name=data['name'], email=data['email'], password_hash=hashed_password)
    return Response({'message': 'User registered successfully'}, status=201)


@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=400)

    # 查找用户
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Invalid email or password'}, status=400)

    # 检查密码
    if not check_password(password, user.password_hash):
        return Response({'error': 'Invalid email or password'}, status=400)

    # 生成 JWT Token
    refresh = RefreshToken.for_user(user)

    return Response({
        'message': 'Login successful',
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,
        }
    }, status=200)