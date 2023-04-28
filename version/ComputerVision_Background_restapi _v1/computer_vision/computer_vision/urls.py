"""computer_vision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# up file
from django.conf.urls.static import static
from django.conf import settings


from home import views as home
from image import views as img

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.get_home),
    path('removeBG', img.get_removeBG),
    path('removeBG_act', img.remove_background),
    path('close_all', img.close_all_image),
    # thay đổi nền ảnh
    path('changeBG', img.get_changeBG),
    path('changeBG_act', img.change_background),
    # làm mờ nền hình ảnh
    path('blurBG', img.get_blurBG),
    path('blurBG_act', img.blur_background),
    # làm xám nền ảnh
    path('grayBG', img.get_grayBG),
    path('grayBG_act', img.gray_background),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
