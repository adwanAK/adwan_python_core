import sys
from django.conf import settings

# building settings.py
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisasecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


# Django settings need to be configured before other imports happen
# thus the uncommone double-import lines above and below here
from django.urls import path
from django.http import HttpResponse

# building views.py
def index(request):
    return HttpResponse("It is loose!")

# building urls.py
urlpatterns = [
    path('', index)
]

# building manage.py
if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
