#!/usr/bin/env python
# Name: custom.py
# Time:8/3/16 4:19 PM
# Author:luo1fly

from django import template

register = template.Library()


@register.simple_tag
def build_comment_tree(tree_data):

    html_ele = ""
    for p, v in tree_data.items():
        row = '''<div style="margin-top:15px;border-left:1px dashed green;border-bottom:1px  dashed green">
                <span class="comment-user">%s</span>
                <span class="comment-content">%s</span>
                <span class="comment-date">%s</span>
                </div>''' % (p.user.name, p.comment, p.add_date)
        if v is not None:   # has son
            row += insert_comment_node(v, 20)
        html_ele += row
    return html_ele


@register.filter
def insert_comment_node(data_dic, margin_val):
    html = ''
    for p, v in data_dic.items():
        r = '''<div style="margin-left:%spx;margin-top:15px;border-left:1px dashed green;border-bottom:1px dashed green">
                <span class="comment-user">%s</span>
                <span class="comment-content">%s</span>
                <span class="comment-date">%s</span>
                </div>''' % (margin_val, p.user.name, p.comment, p.add_date)
        if v is not None:
            r += insert_comment_node(v, margin_val+20)
        html += r
    # print(html)
    return html
