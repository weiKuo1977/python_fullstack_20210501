from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext


# Create your views here.

def login_text(request):
    # 返回httpresponse对象
    # 加载模板文件
    templates_cl = loader.get_template('app1/index.html')
    # 定义模板上下文
    # context = RequestContext(request, {"name": "张三"})
    context = {}
    # 渲染
    resp_html = templates_cl.render(context)
    return HttpResponse(resp_html)


def login(request):
    return render(request, "app1/index.html", {"name": "wdd", "lists": [1, 2, 34, 5]})


def index(request, bid):
    print(bid)
    # return HttpResponse("你好")
    return HttpResponseRedirect('/app1/login')
