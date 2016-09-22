from django.db import models
from django.contrib.auth.models import User
from s10day12bbs import settings

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey('Category')    # 一对多关系，单选
    content = models.TextField()
    summary = models.CharField(max_length=256)
    author = models.ForeignKey('UserProfile')   # 一对多关系，单选
    head_img = models.ImageField(upload_to=settings.default_img_path)   # imgs/upload/
    '''
    upload_to参数用于设定admin后台图片上传路径，如直接给定真实路径statics/*则会与前端展示url地址static/*冲突，
    为避免该麻烦，数据库中不写死二级目录，而是写到三级目录imgs/*，前端展示时拼接static/，
    后台的修改采用软连接方式ln -s statics/imgs imgs
    '''
    create_on = models.DateTimeField(auto_now_add=1)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=32, unique=1)
    admins = models.ManyToManyField('UserProfile')  # 多对多关系，一个版块可以有多个管理员，多选

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    user_groups = models.ManyToManyField('UserGroup')   # 多对多关系，一个用户可以属于多个组，多选
    friends = models.ManyToManyField('self', blank=1, related_name='fid')

    def __str__(self):
        return self.name


class UserGroup(models.Model):
    name = models.CharField(max_length=32, unique=1)

    def __str__(self):
        return self.name


class ThumbUp(models.Model):
    article = models.ForeignKey('Article')  # 一对多关系，单选，一个点赞只能针对一条博客
    user = models.ForeignKey('UserProfile')     # 一对多关系，单选，一个点赞只能有一个执行者
    add_date = models.DateTimeField(auto_now_add=1)

    def __str__(self):
        return self.article.title


class Comment(models.Model):
    article = models.ForeignKey('Article')
    comment = models.TextField(max_length=1024)
    user = models.ForeignKey('UserProfile')
    parent_comment = models.ForeignKey('self', blank=1, null=1, related_name='pid')
    # 关联到自己，单选，一条评论只能有一条父评论，但一条父评论可以有多个子评论，另外在做自关联的时候要加related_name参数
    add_date = models.DateTimeField(auto_now_add=1)

    def __str__(self):
        return self.comment
