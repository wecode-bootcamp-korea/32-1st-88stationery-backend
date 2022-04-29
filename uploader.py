import os, django ,csv, sys
from unicodedata import decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj88.settings")
django.setup()

from products.models  import Category, Product
from users.models     import User
from questions.models import Question, Answer
from orders.models    import Status, Order, Cart

CSV_PATH_PRODUCTS   = './products.csv'
CSV_PATH_CATEGORIES = './categories.csv'
CSV_PATH_USERS      = './users.csv'
CSV_PATH_QUESTIONS  = './questions.csv'
CSV_PATH_ANSWERS    = './answers.csv'
CSV_PATH_STATUSES   = './statuses.csv'
CSV_PATH_ORDERS     = './orders.csv'
CSV_PATH_CARTS      = './carts.csv'

def category_uploader() : 
    with open(CSV_PATH_CATEGORIES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Category.objects.create(name = row[0])

def product_uploader() :
    with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            category_id = Category.objects.get(name = row[5]).id
            
            Product.objects.create(name             = row[0],
                                   price            = row[1],
                                   thumnail_url     = row[2],
                                   detail           = row[3],
                                   detail_image_url = row[4],
                                   category_id      = category_id,
                                   is_new           = row[6])

def user_uploader() :
    with open(CSV_PATH_USERS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            User.objects.create(email        = row[0],
                                password     = row[1],
                                name         = row[2],
                                phone_number = row[3],
                                birth_date   = row[4],
                                address1     = row[5],
                                address2     = row[6])

def question_uploader() :
    with open(CSV_PATH_QUESTIONS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            user_id = User.objects.get(name = row[0]).id

            Question.objects.create(user_id = user_id,
                                    title   = row[1],
                                    detail  = row[2])

def answer_uploader() :
    with open(CSV_PATH_ANSWERS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            question_id = Question.objects.get(title = row[2]).id

            Answer.objects.create(writer      = row[0],
                                  detail      = row[1],
                                  question_id = question_id)

def status_uploader() :
    with open(CSV_PATH_STATUSES) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            Status.objects.create(status = row[0])

def order_uploader() :
    with open(CSV_PATH_ORDERS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            product    = Product.objects.get(name = row[1])
            price      = product.price * decimal(row[0])
            product_id = product.id
            status_id  = Status.objects.get(status = row[2]).id
            user_id    = User.objects.get(name = row[3]).id
            
            Order.objects.create(quantity   = row[0],
                                 price      = price,
                                 product_id = product_id,
                                 status_id  = status_id,
                                 user_id    = user_id)
                                 
def cart_uploader()  :
    with open(CSV_PATH_ORDERS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            product    = Product.objects.get(name = row[1])
            price      = product.price * decimal(row[0])
            product_id = product.id
            user_id    = User.objects.get(name = row[3]).id
            
            Cart.objects.create(quantity   = row[0],
                                 price      = price,
                                 product_id = product_id,
                                 user_id    = user_id)


print("csv 파일을 선택하세요 : \n 1.catagories 2.products 3.users 4.questions")
print("5.answers 6.statuses 7.orders 8.carts")
select = int(input())

if select == 1:
    category_uploader()
elif select == 2 :
    product_uploader()
elif select == 3 :
    user_uploader()
elif select == 4 :
    question_uploader()
elif select == 5 :
    answer_uploader()
elif select == 6 :
    status_uploader()
elif select == 7 :
    order_uploader()
elif select == 8 :
    cart_uploader()