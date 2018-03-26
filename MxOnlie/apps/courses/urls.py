# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    #添加课程评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

]