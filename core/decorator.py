import jwt

from django.http  import JsonResponse
from django.conf  import settings
from pj88.settings import SECRET, ALGORITHM
from users.models import User

def log_in_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization')
            payload      = jwt.decode(access_token, SECRET, algorithms=ALGORITHM)
            request.user = User.objects.get(id=payload['id'])

            return func(self, request, *args, **kwargs)

        except User.DoesNotExist:
            return JsonResponse({'message':'IVALID_USER'},status=401)
        except jwt.InvalidSignatureError:
            return JsonResponse({'message':'INVAILD_SIGNATURE'},status=401)
        except jwt.DecodeError:
            return JsonResponse({'message':'IVALID_PAYLOAD'},status=401)

    return wrapper