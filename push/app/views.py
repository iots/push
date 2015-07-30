from django.shortcuts import render_to_response,RequestContext,render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from app.forms import PushForm,PushFormAlias
from app.models import *

# Create your views here.

@csrf_protect
def PushView(request):
    if request.method == 'POST':
        form = PushForm(request.POST)
        if form.is_valid():
            """
            #当参数合法后,通过cleaned_data方法读取表单中数据内容
            tmp_msg = form.cleaned_data['push_message']
            tmp_url = form.cleaned_data['push_url']
            print("[DEBUG] Request.POST.get->msg:%s,url:%s)" % (tmp_msg,tmp_url))
            print(form.cleaned_data)

            #入库测试
            tmp = PushForm({'push_message':'abcd','push_url':'baidu.com'})
            t = tmp.save()
            t.save()

            #读数据库测试
            ret = PushModel.objects.all()
            return HttpResponse(ret)

            #通过基于模型表单映射后,直接从表单入数据库
            SaveHandle = form.save()
            SaveHandle.save()
            """

            #use request.POST.get method
            msg = request.POST.get('push_message','')
            url = request.POST.get('push_url','')
            print("[DEBUG] Request.POST.get->msg:%s,url:%s" % (msg,url))
            #print("[DEBUG] PUSH_MESSAGE : %s" % form['push_message'].value())

            #obj = PushModel.objects.get_or_create(push_message=msg,push_url=url)
            try:
                PushModel.objects.get(push_message=msg,push_url=url)
                print("[DEBUG] 该消息已推送过,无需重复入库.")
            except PushModel.DoesNotExist:
                obj = PushModel(push_message=msg,push_url=url)
                obj.save()
            finally:
                return HttpResponseRedirect("/PushList")
        else:
            print("Forms Arguments Error!!!")
    else:
        form = PushForm(initial={'push_message':'Hi,Everyone','push_url':'http://www.nfschina.com'})
    return render_to_response("push.html",{'form':form},context_instance=RequestContext(request))

def PushList(request):
    #ret = PushModel.objects.filter(push_message__icontains='Hi')
    ret = PushModel.objects.all()
    #print(ret)
    return render_to_response("PushList.html",{'ret':ret})
