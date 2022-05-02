import json, bcrypt, jwt
from os import access

from django.http            import JsonResponse
from django.views           import View
from users.models           import User
from django.core.exceptions import ValidationError
from users.validation       import Validation
from django.conf            import Settings
from pj88.settings          import SECRET, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data         = json.loads(request.body)
            email        = data['email']
            password     = data['password']
            name         = data['name']
            phone_number = data['phone_number']
            birth_date   = data['birth_date']
            address1     = data['address1']
            address2     = data['address2']

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'ALREADY_EXISTS'},status=401)

            Validation.email_validate(email)
            Validation.password_validate(password)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                email        = email,
                password     = hashed_password,
                name         = name,
                phone_number = phone_number,
                birth_date   = birth_date,
                address1     = address1,
                address2     = address2
            )
            return JsonResponse({'message':'SUCCESS'},status=201)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)
        except ValidationError as error:
            return JsonResponse({'message':error.message})

class SignInView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_PASSWORD'},status=401)

            access_token = jwt.encode({'id':user.id, 'user_name' : user.name}, SECRET, algorithm=ALGORITHM)

            return JsonResponse({'message':access_token},status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)
        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_EMAIL'},status=401)

# Create your views here.
