#!/usr/bin/env python
# Name: utils.py
# Time:8/3/16 9:05 AM
# Author:luo1fly

from bbs import models
from s10day12bbs import settings
import os

# modules import above


class ArticleHandler(object):

    def __init__(self, request):
        self.request = request

    def create(self):
        data = self.parse_data()
        article = models.Article(**data)
        if self.request.FILES:
            print(self.request.FILES)
            article.head_img = ArticleHandler.file_upload(self.request.FILES['head_img'])
        article.save()

    def parse_data(self):
        title = self.request.POST['title']
        content = self.request.POST['content']
        summary = self.request.POST['summary']
        category = 1
        data = {
            'title': title,
            'content': content,
            'summary': summary,
            'category_id': category,
            'author_id': self.request.user.userprofile.id,
            'head_img': settings.default_img_path,
        }
        return data

    @staticmethod
    def file_upload(file_obj):
        # print(dir(file_obj))
        file_path = os.path.join(settings.BASE_DIR, settings.relative_img_path)
        abs_file = os.path.join(file_path, file_obj.name)
        with open(abs_file, 'wb') as f:
            for i in file_obj.chunks():
                f.write(i)
        file_url = os.path.join(settings.default_img_path, file_obj.name)
        return file_url

    @staticmethod
    def build_comments_tree(art_obj):
        root = {}
        # bbs_obj = models.Article.objects.get(id=article_id)
        comment_list = art_obj.comment_set.select_related().order_by('id')
        for ct in comment_list:
            if not ct.parent_comment:
                root[ct] = {}
            else:
                # print("go to find %s's father comment" % ct)
                ArticleHandler.recursive_search(root, ct)
        # for k, v in root.items():
        #     print(k,v)
        return root

    @staticmethod
    def recursive_search(opt_dic, comment_ins):
        for parent in opt_dic.keys():
            if parent == comment_ins.parent_comment:
                opt_dic[parent][comment_ins] = {}
            else:
                ArticleHandler.recursive_search(opt_dic[parent], comment_ins)






