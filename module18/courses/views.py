from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.views.generic import ListView, CreateView, DetailView
from .forms import AddCourseForm, AddCommentForm
from .models import Courses, Comment


class HomePageView(ListView):
    model = Courses
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx=super(HomePageView, self).get_context_data(**kwargs)
        ctx['title'] = 'Courses'
        return ctx


class AddCourseView(CreateView):
    model = Courses
    template_name = 'courses/add-course.html'
    form_class = AddCourseForm

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx=super(AddCourseView, self).get_context_data(**kwargs)
        ctx['title'] = 'Add course'
        return ctx


class DetailCourseView(LoginRequiredMixin, DetailView):
    model = Courses
    template_name = 'courses/detail-course.html'
    context_object_name = 'course'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(DetailCourseView, self).get_context_data(**kwargs)
        ctx['title'] = 'Course'
        ctx['form'] = AddCommentForm()
        current_course = self.get_object()
        ctx['comments'] = Comment.objects.filter(course=current_course)
        return ctx

    def post(self, request, *args, **kwargs):
        course = Courses.objects.get(pk=self.kwargs['pk'])
        post = request.POST.copy()
        post['user'] = request.user
        post['course'] = course
        request.POST = post

        form = AddCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('course_detail', kwargs={'pk': course.id}))
