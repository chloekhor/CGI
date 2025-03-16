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

import redis  

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

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
            
            
            send_mail(
                'Password Reset Request',
                f'Click the following link to reset your password: {reset_link}\nThis link is valid for 1 hour.',
                'timothytan010517@gmail.com',  # Use personal email for now
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

            
            # ✅ Redis Key 设置
            otp_key = f"otp:{email}"  # 存储 OTP
            otp_attempt_key = f"otp_attempts:{email}"  # 记录 OTP 请求次数
            otp_lock_key = f"otp_lock:{email}"  # 锁定用户的 key


            # ✅ 检查用户是否被锁定（如果 key 存在，表示被锁定）
            if redis_client.exists(otp_lock_key):
                return JsonResponse({"error": "Too many attempts. Try again later."}, status=429)
            

            # ✅ 获取用户 OTP 尝试次数
            attempts = redis_client.get(otp_attempt_key)
            if attempts is None:
                attempts = 0
            else:
                attempts = int(attempts)

            # ✅ 超过 5 次后，锁定 1 小时
            if attempts >= 5:
                redis_client.setex(otp_lock_key, 3600, "LOCKED")  # 1 小时锁定
                return JsonResponse({"error": "Too many attempts. Try again in 1 hour."}, status=429)

            
            # ✅ 存入 Redis，设置 10 分钟过期
            redis_client.setex(otp_key, 600, otp_code)

            # ✅ 递增 OTP 尝试次数（过期时间 1 小时）
            redis_client.incr(otp_attempt_key)
            redis_client.expire(otp_attempt_key, 3600)  # 1 小时后重置尝试次数


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