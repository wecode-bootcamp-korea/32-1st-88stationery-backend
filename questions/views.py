import json

from django.views        import View
from django.http         import JsonResponse
from questions.models    import Answer,Question
from core.decorator import log_in_decorator
from json.decoder        import JSONDecodeError

from users.models import User


class QuestionView(View):
    @log_in_decorator
    def post(self,request):
        try:    
            data    = json.loads(request.body)
            title   = data['title'] 
            detail  = data['detail'] 
            user_id = request.user.id
    
            Question.objects.create(
                title   = title,
                detail  = detail,
                user_id = user_id
            )

            return JsonResponse({'message':'생성완료'},status=200)
        except KeyError:
            return JsonResponse({'message':'키에러'},status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'})

    @log_in_decorator
    def get(self,request):
        user = request.user
        questions = Question.objects.filter(user_id=user.id)
        result = []
        for question in questions:
            result.append({
                'id'         : question.id,
                'title'      : question.title,
                'detail'     : question.detail,
                'user'       : user.name,
                'date'       : question.created_at
            })
        
        return JsonResponse({'result':result},status=200)

    @log_in_decorator
    def delete(self,request):
        try:
            user        = request.user
            data        = json.loads(request.body)
            question_id = data['question_id']
            question    = Question.objects.get(id=question_id)

            # if not user.id != question.user_id:
            #     return JsonResponse({'message':'권한없음'},status=400)

            Question.objects.filter(id=question.id).delete()
            return JsonResponse({'mesaage':'삭제완료'},status=200)
        except KeyError:
            return JsonResponse({'message':'키에러'},status=400)
        except Question.DoesNotExist:
            return JsonResponse({'message':'삭제할 질문이 존재하지 않습니다.'},status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'},status=400)

class AnswerView(View):
    @log_in_decorator
    def post(self,request):
        try:
            data        = json.loads(request.body)
            user        = request.user
            writer      = user.name
            detail      = data['detail']
            question_id = data['question_id']
            question    = Question.objects.get(id=question_id)

            Answer.objects.create(
                writer = writer,
                detail = detail,
                question_id = question.id
            )

            return JsonResponse({'message':'댓글등록'},status=200)
        except KeyError:
            return JsonResponse({'message':'키에러'},status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'},status=400)
    
    @log_in_decorator
    def get(self,request):
        user = request.user
        answers = Answer.objects.filter(writer=user.email)
        result = []

        for answer in answers:
            result.append({
                'id'          : answer.id,
                'writer'      : answer.writer,
                'detail'      : answer.detail,
                'question_id' : answer.question_id, 
                'date'        : answer.created_at
            })

        return JsonResponse({'result':result},status=200)

    @log_in_decorator
    def delete(self,request):
        try:
            data      = json.loads(request.body)
            answer_id = data['answer_id']
            answer    = Answer.objects.get(id=answer_id)
            user      = request.user
            
            if not user.email != answer.writer:
                return JsonResponse({'message':'권한없음'},status=400)

            Answer.objects.filter(id=answer.id).delete()

            return JsonResponse({'message':'삭제완료'},status=200)
        except KeyError:
            return JsonResponse({'message':'키에러'},status=400)
        except Answer.DoesNotExist:
            return JsonResponse({'message':'삭제할 답글이 존재하지 않습니다.'},status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'json형태이상함'},status=400)
