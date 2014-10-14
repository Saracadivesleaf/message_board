from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Message(models.Model):

	"""docstring for Message"""

	name = models.CharField(max_length = 100)
	email = models.EmailField()
	homepage = models.URLField()
	user = models.ForeignKey(User)    # 该字段引用用户信息表 id 字段的值，是用户 
	ip = models.IPAddressField()      # 用于存取留言者计算机的 ip 地址信息。
	content = models.CharField(max_length = 100)
	publish_time = models.DateTimeField(auto_now = True)

	def __str__(self): 
		return' 用户%s 发表的标题为%s 的留言 ' % (self.user.username, self.title)