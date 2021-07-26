from django.shortcuts import render
from django.views.generic import (FormView, DetailView, ListView, TemplateView
                                    , CreateView, UpdateView, DeleteView)
from .models import Standard, Subject, Lesson, Comment, Reply
from .forms import LessonForm, CommentForm, ReplyForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy

class StandardView(ListView):
    model=Standard
    context_object_name='standards'
    template_name='standards.html'

class SubjectView(DetailView):
    model=Standard
    context_object_name='standards'
    template_name='subjects_details.html'

class LessonView(DetailView):
    model=Subject
    context_object_name='subjects'
    template_name='lesson_details.html'

class LessonContentsView(DetailView, FormView):
    model=Lesson
    context_object_name='lessons'
    template_name='lesson_contents.html'

    fields=('__all__',)
    form_class=CommentForm
    second_form_class=ReplyForm

    def get_context_data(self, **kwargs):
        context=super(LessonContentsView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class()
        if 'form2' not in context:
            context['form2']=self.second_form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object= self.get_object()
        if 'form' in request.POST:
            form_class=self.form_class
            form_name='form'
        else:
            form_class=self.second_form_class
            form_name='form2'
        
        form=self.get_form(form_class)
        
        if form_name=='form' and form.is_valid():
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            return self.form2_valid(form)
        
    def form_valid(self, form):
        self.object= self.get_object()
        fm=form.save(commit=False)
        fm.author=self.request.user
        fm.lesson_name=self.object.comments.name
        fm.lesson_id=self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form2_valid(self, form):
        self.object= self.get_object()
        fm=form.save(commit=False)
        fm.author=self.request.user
        fm.comment_id=self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        self.object= self.get_object()
        return reverse_lazy('lesson_contents', kwargs={
            'standard':self.object.standard.slug,
            'chapter': self.object.subject.slug,
            'slug':self.object.slug
        })


class LessonCreateView(CreateView):
    form_class=LessonForm
    model=Subject
    context_object_name='subject'
    template_name='lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard=self.object.standard
        return reverse_lazy('lesson_details', kwargs={'standard':standard.slug,
                                                        'slug':self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object=self.get_object()
        fm=form.save(commit=False)  
        fm.created_by=self.request.user
        fm.standard=self.object.standard
        fm.subject=self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LessonUpdateView(UpdateView):
    fields=('lesson_name', 'chapter_num', 'video', 'ppt', 'notes') 
    model=Lesson
    template_name='update_lesson.html'
    context_object_name='lessons'



class LessonDeleteView(DeleteView):
    model=Lesson
    template_name='delete_lesson.html'
    context_object_name='lessons'

    def get_success_url(self):
        return reverse_lazy('lesson_details', kwargs={'slug': self.object.subject.slug, 'standard':self.object.standard.slug})