from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import MessageForm
from models import * 
from django.views.generic import list_detail 
# Create your views here.
ITEMS_PER_PAGE=10  # 变量 ITEMS_PER_PAGE 中保存对留言对象列表分页后每页能容纳的留言对象数。

def message(request):
	if request.method == 'POST':
		form = MessageForm.request
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			homepage = form.cleaned_data['homepage']
			content = form.cleaned_data['content']
			publish_time = form.cleaned_data['publish_time']
			m = Message( name = name,
						email = email,
						homepage = homepage,
						content =content,
						publish_time = publish_time)
			m.save()
			return HttpResponseRedirect('/message/')
	else:
		form = MessageForm()
	messages = Message.objects.all()

	return render_to_response('message.html',{'form': form,'messages': messages})




  # 定义 msg_list_page 函数。 
def msg_list_page(request):

# 调用 object_list 函数，在浏览器中显示主页。 
	return list_detail.object_list(request, queryset = Message.objects.order_by('-id'),
# 将变量 ITEMS_PER_PAGE 的值赋给paginate_by 参数，实现对 queryset参数中的留言对象列表的分页处理 
	paginate_by = ITEMS_PER_PAGE, # 指定该函数生成主页时，所使用的 # 模板文件名称。 
	template_name = 'msg_list_page.html', 
	# 指定在模板文件中用于表示分页后留言 # 对象列表的模板变量名称，实际的名称 # 是‘msg_list'。 
	template_object_name = 'msg_list' )

