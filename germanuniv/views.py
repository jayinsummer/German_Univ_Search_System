from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import School, Language


# 로그인
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('main_page')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


# 로그아웃
def logout_view(request):
    logout(request)
    return redirect('login')


# 메인 페이지
@login_required
def main_page(request):
    searched_schools = None  # For storing search results
    if request.method == 'POST' and 'search' in request.POST:
        # Handle search functionality
        tuition_min = request.POST.get('tuition_min', 0)
        tuition_max = request.POST.get('tuition_max', 99999)
        semester_min = request.POST.get('semester_min', 0)
        semester_max = request.POST.get('semester_max', 99999)
        selected_languages = request.POST.getlist('language')
        selected_levels = request.POST.getlist('level')

        searched_schools = School.objects.filter(
            tuition_fee__gte=tuition_min,
            tuition_fee__lte=tuition_max,
            semester_fee__gte=semester_min,
            semester_fee__lte=semester_max,
            languages__name__in=selected_languages,
            languages__level__in=selected_levels
        ).distinct()

    return render(request, 'main_page.html', {
        'schools': School.objects.all(),  # All schools for add/delete section
        'languages': Language.objects.values_list('name', flat=True).distinct(),
        'language_levels': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'],
        'favorites': request.user.favorite_school.all(),
        'searched_schools': searched_schools,  # Search results
    })


# 학교 추가
@login_required
def add_school(request):
    if request.method == 'POST':
        name = request.POST['name']
        tuition_fee = request.POST['tuition_fee']
        semester_fee = request.POST['semester_fee']
        region = request.POST['region']
        School.objects.create(name=name, tuition_fee=tuition_fee, semester_fee=semester_fee, region=region)
        return redirect('main_page')


# 학교 삭제
@login_required
def delete_school(request, school_id):
    school = School.objects.get(id=school_id)
    school.delete()
    return redirect('main_page')


# 즐겨찾기 추가
@login_required
def add_favorite(request):
    if request.method == 'POST':
        school_name = request.POST['school_name']
        school = School.objects.filter(name=school_name).first()
        if school:
            request.user.favorite_school.add(school)
        return redirect('main_page')


# 즐겨찾기 삭제
@login_required
def remove_favorite(request, school_id):
    school = School.objects.get(id=school_id)
    if school in request.user.favorite_school.all():
        request.user.favorite_school.remove(school)
    return redirect('main_page')
