from rest_framework import generics
from .serializers import HistorySerializer, UsersSerializer

from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from users.models import Users, History

import redis
import random
import logging
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken  # ✅ 让 JWT 代码能正常工作


# ✅ 初始化 Redis 连接
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# ✅ 设置日志
logger = logging.getLogger('otp_logger')



class HistoryList(generics.ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        user_id = self.request.session.get("user_id")
        print("user_id:", user_id)  # Debugging

        if user_id:
            return History.objects.filter(user_id=user_id)  # Fetch history records for the user
        return History.objects.none()  # Return empty queryset if no user_id


class UsersList(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        print("get_queryset is being called!") 
        user_id = self.request.session.get("user_id")
        print("user id ", user_id)  # Debugging

        if user_id:
            return Users.objects.filter(id=user_id)
        return Users.objects.none()


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            user = Users.objects.filter(email=email).first()

            if not user:
                return JsonResponse({"error": "Invalid email or password"}, status=401)

            if not check_password(password, user.password):
                return JsonResponse({"error": "Invalid email or password"}, status=401)

            # ✅ 生成 6 位数随机 OTP
            otp = str(random.randint(100000, 999999))

            # ✅ 连接 Redis 并存储 OTP，设置 10 分钟过期
            r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
            r.setex(f"otp:{email}", 600, otp)  # 600 秒 = 10 分钟
            
            # ✅ 发送 OTP 邮件
            send_mail(
                'IECGIM Verification Code',
                f'Hi, your verification code is: {otp}. This code is valid for 10 minutes.',
                'IECGIM@outlook.com',
                [email],
                fail_silently=False,
            )

            # ✅ 记录日志
            logger.info(f"Sent OTP to {email}: {otp}")

            return JsonResponse({
                "message": "OTP sent to your email",
                "user_id": user.id,
                "email": user.email
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_user_session(request):
    """Check if the user is logged in by retrieving session user_id"""
    if request.method == 'GET':
        user_id = request.session.get("user_id", None)
        if user_id:
            return JsonResponse({"user_id": user_id})
        return JsonResponse({"error": "No active session"}, status=401)

    return JsonResponse({"error": "Invalid request method"}, status=405)



@csrf_exempt
def update_profile_view(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        data = json.loads(request.body)

        user_id = data.get('user_id')
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        user = Users.objects.filter(id=user_id).first()

        if not user:
            return JsonResponse({"error": "User not found"}, status=404)

        user.name = name
        user.email = email
        if password:
            user.password = make_password(password)

        user.save()

        return JsonResponse({"message": "Profile updated successfully!"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    


def verify_otp(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            otp = data.get('otp')

            if not email or not otp:
                return JsonResponse({"error": "Missing email or OTP"}, status=400)

            # ✅ 3️⃣ 检查是否被锁定（6小时）
            fail_count_key = f"otp_fail:{email}"
            lockout_key = f"lockout:{email}"

            if r.exists(lockout_key):
                return JsonResponse({"error": "Too many failed attempts. Try again after 6 hours."}, status=403)

            # ✅ 4️⃣ 获取存储的 OTP
            otp_stored = r.get(f"otp:{email}")


            if not otp_stored:
                return JsonResponse({"error": "OTP expired or invalid"}, status=400)

            if otp != otp_stored:
                fail_count = r.incr(fail_count_key)  # 失败计数 +1
                if fail_count == 1:
                    r.expire(fail_count_key, 21600)  # 第一次失败时设置 6 小时过期时间

                logger.warning(f"User failed OTP attempt ({fail_count}/10): {email}")

                if fail_count >= 10:
                    r.setex(lockout_key, 21600, "LOCKED")  # 🚨 超过 10 次，锁定 6 小时
                    return JsonResponse({"error": "Too many failed attempts, please try again in 6 hours"}, status=403)

                return JsonResponse({"error": f"Invalid OTP. Attempts left: {10 - fail_count}"}, status=400)

            # OTP 正确，删除 Redis 记录
            r.delete(f"otp:{email}")
            r.delete(fail_count_key)

            logger.info(f"User verified OTP successfully: {email}")

             # ✅ 7️⃣ 生成 JWT Token
            user = Users.objects.filter(email=email).first()
            if not user:
                return JsonResponse({"error": "User not found"}, status=404)

            refresh = RefreshToken.for_user(user)

            return JsonResponse({
                "message": "OTP verified successfully",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

