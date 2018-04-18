django2.0开始只支持python3， 所以升级前确保之前是用django1.11和python3.6开发的，代码可以在相应分支获取

    1. 所有model的外键需要加上on_delete的行为 改为 on_delete=models.CASCADE

    此处说明一下如果改为 models.SET_NULL需要将外键设置为可以为NULL，不然启动的时候会报错
    并说明一下CASCADE、SET_NULL等参数的意思


    2. 修改所有from django.core.urlresolvers import NoReverseMatch, reverse
    3. from django.core.urlresolvers import reverse 全部改为 from django.urls import reverse


    3. 下载最新的xadmin-从私人仓库获取，不要下载官方的2版本，里面还有些bug没有解决，不排除后期会解决
        xadmin修复了图片需要重传的bug
        index out of range的bug
    
    4. url中关于include的地方全部改为 url(r'^course/', include(('courses.urls','courses'), namespace="course"))的模式
    5. 说明一下 urls.py中url(r'^captcha/', include('captcha.urls')), 一定不能加namespace也不能用上面的模式，保持原来模式就行了
    6. 将settings中的MIDDLEWARE_CLASSES 改为 MIDDLEWARE并删除'django.contrib.auth.middleware.SessionAuthenticationMiddleware' 这一行
    7. 重新安装xadmin的依赖包，使得支持django2.0

        django-crispy-forms
        django-formtools
        django-import-export
        django-simple-captcha
    
    8. 课程中关于request.user.is_authenticated()中的地方要改为request.user.is_authenticated
    

