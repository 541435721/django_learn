# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from alipay_API import Alipay
import re

alipay = Alipay(pid='2088421836722555', key='x5b1vxvggtye0br2o0bgl3lp4lz1d2iq',
                seller_email='xmstrongyk@163.com')

trade_no = '1212112212121121221212131223121'
dic = {}

xml = alipay.single_trade_query(out_trade_no=trade_no)


def index(request):
    # return HttpResponse("hello world")

    url = alipay.create_direct_pay_by_user_url(out_trade_no=trade_no,
                                               subject=u'测试', total_fee='0.1',
                                               return_url='http://127.0.0.1:8000/ali',
                                               notify_url='http://127.0.0.1:8000/ali')
    dic = {"article_list": ["1", "2", "3"], 'url': url}
    return render(request, 'index.html', dic)


# trade_status  is_success

def alipy_notify(request):
    if request.method == 'POST':
        dic = {"article_list": ['post']}
        dic['article_list'].append(request.POST['is_success'])
        dic['article_list'].append(request.POST['trade_status'])
        return render(request, 'index.html', dic)
    elif request.method == 'GET':
        dic = {"article_list": ['get']}
        dic['article_list'].append(request.GET['is_success'])
        dic['article_list'].append(request.GET['trade_status'])
    return render(request, 'index.html', dic)
