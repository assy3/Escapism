from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import *

class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.all()  # データベースからオブジェクトを取得して
        context['workers'] = workers  # 入れ物に入れる

        return render(self.request, self.template_name, context) # URL, html, data  htmlとdataを混ぜてURLに表示
