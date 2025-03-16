from rest_framework import viewsets
from .models import User
# from .serializers import UserSerializer


import json, uuid
from datetime import timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from users.models import Users

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer


@csrf_exempt
def forgot_password(request):
    """用户提交邮箱，系统生成重置 token 并发送邮件"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            if not email:
                return JsonResponse({"error": "Email is required"}, status=400)
            
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return JsonResponse({"error": "No user with that email"}, status=404)
            
            # 生成一个安全的 token（这里使用 UUID）
            reset_token = str(uuid.uuid4())
            # 设置 token 1 小时后过期
            expiry = timezone.now() + timedelta(hours=1)
            
            # 保存 token 和过期时间到用户模型
            user.reset_token = reset_token
            user.reset_token_expiry = expiry
            user.save()
            
            # 构造重置密码链接（前端页面会处理 token 参数）
            reset_link = f"https://localhost:8080/reset-password?token={reset_token}"
            
            # 发送邮件（注意 sender 需与 settings.py 中配置匹配）
            send_mail(
                'Password Reset Request',
                f'Click the following link to reset your password: {reset_link}\nThis link is valid for 1 hour.',
                'timothytan010517@gmail.com',  # 使用你在 settings.py 中配置的发送邮箱
                [email],
                fail_silently=False,
            )
            
            return JsonResponse({"message": "Password reset email sent"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def reset_password(request):
    """用户提交 token 和新密码，验证 token 并重置密码"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reset_token = data.get('token')
            new_password = data.get('new_password')
            confirm_password = data.get('confirm_password')
            
            if not reset_token:
                return JsonResponse({"error": "Reset token is required"}, status=400)
            if not new_password or not confirm_password:
                return JsonResponse({"error": "New password and confirmation are required"}, status=400)
            if new_password != confirm_password:
                return JsonResponse({"error": "Passwords do not match"}, status=400)
            
            try:
                user = Users.objects.get(reset_token=reset_token)
            except Users.DoesNotExist:
                return JsonResponse({"error": "Invalid or expired token"}, status=400)
            
            # 检查 token 是否过期
            if user.reset_token_expiry is None or user.reset_token_expiry < timezone.now():
                return JsonResponse({"error": "Reset token has expired"}, status=400)
            
            # 更新密码（确保进行哈希处理）
            user.password = make_password(new_password)
            # 清除重置 token 及其过期时间
            user.reset_token = None
            user.reset_token_expiry = None
            user.save()
            
            return JsonResponse({"message": "Password has been reset successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def resend_otp(request):
    """重新发送 OTP 到用户邮箱"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')

            if not email:
                return JsonResponse({"error": "Email is required"}, status=400)

            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                return JsonResponse({"error": "No user found with that email"}, status=404)

            # 生成新的 OTP（6 位随机数字）
            otp_code = str(uuid.uuid4().int)[:6]  # 生成 6 位 OTP
            user.otp_code = otp_code
            user.otp_expiry = timezone.now() + timedelta(minutes=10)  # OTP 10 分钟有效
            user.save()

            # 发送 OTP 邮件
            send_mail(
                'Your New OTP Code',
                f'Your new OTP code is: {otp_code}\nThis code is valid for 10 minutes.',
                'timothytan010517@gmail.com', 
                [email],
                fail_silently=False,
            )

            return JsonResponse({"message": "New OTP has been sent to your email."})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)