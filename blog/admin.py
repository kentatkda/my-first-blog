from django.contrib import admin
from .models import Post
# Register your models here.

#モデルをAdminページ（管理画面）上で見えるようにするため
admin.site.register(Post)

#ログインするには、superuser （サイトの全てを管理するユーザー）を作る必要があります
