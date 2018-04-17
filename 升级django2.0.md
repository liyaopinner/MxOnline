django2.0开始只支持python3， 所以升级前确保之前是用django1.11和python3.6开发的，代码可以在相应分支获取

    1. 所有model的外键需要加上on_delete的行为 改为 on_delete=models.CASCADE

        此处说明一下如果改为 models.SET_NULL需要将外键设置为可以为NULL，不然启动的时候会报错
        并说明一下CASCADE表示级联删除

    2. 修改所有from django.core.urlresolvers import NoReverseMatch, reverse
    
    3. from django.core.urlresolvers import reverse 全部改为 from django.urls import reverse
    
    4. 下载最新的xadmin-从私人仓库获取，不要下载官方的2版本，这里我修复了一些问题，下载完成后 pip install requests    
    
    5. 为所有没有添加namespace的include配置的url地方添加namespace
    
    6. 说明一下 urls.py中url(r'^captcha/', include('captcha.urls')), 一定不能加namespace也不能用上面的模式，因为fields源码文件中
    
    7. 将settings中的MIDDLEWARE_CLASSES 改为 MIDDLEWARE并删除'django.contrib.auth.middleware.SessionAuthenticationMiddleware' 这一行
    
    8. django2.0的url配置方式已经修改，不过以前的仍然兼容
