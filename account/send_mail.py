from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здраствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылки: \n{full_link}',
        'sanzhar.turumov@gmail.com',
        [user],
        fail_silently=False
    )
