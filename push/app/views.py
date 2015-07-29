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
            #for push1.html
            tmp_msg = form.cleaned_data['push_message']
            tmp_url = form.cleaned_data['push_url']
            print("[DEBUG] Request.POST.get->msg:%s,url:%s)" % (tmp_msg,tmp_url))
            print(form.cleaned_data)
            """

            #use request.POST.get method
            msg = request.POST.get('push_message','')
            url = request.POST.get('push_url','')
            #print("[DEBUG] PUSH_MESSAGE : %s" % form['push_message'].value())
            #print("[DEBUG] Request.POST.get->msg:%s,url:%s" % (msg,url))

            '''
            #for test
            tmpform = PushForm({'push_message':'abcd','push_url':'baidu.com'})
            a=tmpform.save()
            a.save()

            #ret = PushModel.objects.all()
            #return HttpResponse(ret)

            SaveHandle = form.save()
            SaveHandle.save()
            '''

            try:
                PushModel.objects.get(push_message=msg,push_url=url)
                return HttpResponse("该消息已推送过")
            except PushModel.DoesNotExist:
                obj = PushModel(push_message=msg,push_url=url)
                obj.save()

            #obj = PushModel.objects.get_or_create(push_message=msg,push_url=url)
            return HttpResponseRedirect("/PushList")
        else:
            print("Arguments Error!!!")
    else:
        form = PushForm(initial={'push_message':'Hi,Everyone','push_url':'http://www.nfschina.com'})
    return render_to_response("push.html",{'form':form},context_instance=RequestContext(request))

def PushList(request):
    #Ret = PushModel.objects.filter(push_message='abcd')
    Ret = list(PushModel.objects.all())
    print(Ret)
    return render_to_response("PushList.html",{'ret':Ret})
