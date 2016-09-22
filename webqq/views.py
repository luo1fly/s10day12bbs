from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
import datetime
from webqq import utils
from bbs import models


# Create your views here.

global_msg_dic = {}


def dashboard(request):
    return render(request, 'webqq/dashboard.html', locals())


def send_msg(request):
    # print(request.POST)
    data = request.POST['data']
    data = json.loads(data)
    print(data)
    from_id = data['from_id']
    to_id = data['to_id']
    contact_type = data['contact_type']
    data['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if contact_type == 'single':
        if to_id not in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat()
        global_msg_dic[to_id].put_msg(data)
        print("push msg [%s] to user:%s's que" % (data['msg'],
                                                  models.UserProfile.objects.get(id=to_id),
                                                  ))
    # print(global_msg_dic)
    return HttpResponse('success')


def get_msg(request):
    # print(request.GET)
    # print('global_msg_dic:', global_msg_dic)
    uid = request.GET['user_id']
    # print('uid:', uid)
    if uid:
        res = None
        if uid in global_msg_dic:
            res = global_msg_dic[uid].get_msg()
        return HttpResponse(json.dumps(res))
    return HttpResponse(json.dumps('chucuole'))