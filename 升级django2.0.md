django2.0开始只支持python3， 所以升级前确保之前是用django1.11和python3.6开发的，代码可以在相应分支获取
    
    1. 安装依赖包
        新装
            pip install requests
        重装
            django-crispy-forms
            django-formtools
            django-import-export
            django-simple-captcha
            django-pure-pagination
    2. 拷贝django2分支下的xadmin和djangoueditor源码
       
    3. 所有model的外键需要加上on_delete的行为 改为 on_delete=models.CASCADE

    4. from django.core.urlresolvers import reverse 全部改为 from django.urls import reverse
    
    5. url中关于include的地方全部改为 url(r'^course/', include(('courses.urls','courses'), namespace="course"))的模式
    
    6. 说明一下 urls.py中url(r'^captcha/', include('captcha.urls')), 一定不能加namespace也不能用上面的模式，保持原来模式就行了
    
    7. 将settings中的MIDDLEWARE_CLASSES 改为 MIDDLEWARE并删除'django.contrib.auth.middleware.SessionAuthenticationMiddleware' 这一行
   
    8. 课程中关于request.user.is_authenticated()中的地方要改为request.user.is_authenticated
    

