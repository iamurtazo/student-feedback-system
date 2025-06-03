from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Feedback
from django.db.models import Count

def home(request):
    """View for the home page with feedback form"""
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        # Basic validation
        if not all([name, course, rating, comment]):
            messages.error(request, 'Please fill out all required fields.')
            return render(request, 'feedback/home.html')
        
        try:
            # Create new feedback
            feedback = Feedback(
                name=name,
                course=course,
                rating=int(rating),
                comment=comment
            )
            feedback.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    
    return render(request, 'feedback/home.html')

def admin_login(request):
    """View for admin login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or insufficient permissions.')
    
    return render(request, 'feedback/admin_login.html')

def admin_logout(request):
    """Logout view for admin"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@login_required
def admin_dashboard(request):
    """View for admin dashboard with all feedbacks"""
    # Get filter parameters
    course_filter = request.GET.get('course', '')
    status_filter = request.GET.get('status', '')
    
    # Start with all feedbacks
    feedbacks = Feedback.objects.all().order_by('-timestamp')
    
    # Apply filters if provided
    if course_filter:
        feedbacks = feedbacks.filter(course__icontains=course_filter)
    if status_filter:
        feedbacks = feedbacks.filter(status=status_filter)
    
    # Get unique course names for the filter dropdown
    courses = Feedback.objects.values('course').annotate(count=Count('course')).order_by('course')
    
    context = {
        'feedbacks': feedbacks,
        'courses': courses,
        'current_course': course_filter,
        'current_status': status_filter
    }
    
    return render(request, 'feedback/admin_dashboard.html', context)

@login_required
def mark_addressed(request, feedback_id):
    """View to mark feedback as addressed"""
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.status = 'addressed'
    feedback.save()
    messages.success(request, f'Feedback #{feedback_id} marked as addressed.')
    return redirect('admin_dashboard')

@login_required
def delete_feedback(request, feedback_id):
    """View to delete feedback"""
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    messages.success(request, f'Feedback #{feedback_id} has been deleted.')
    return redirect('admin_dashboard')
