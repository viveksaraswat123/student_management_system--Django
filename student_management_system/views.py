from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student, Attendance
from django.core.paginator import Paginator
from django.db.models import Q



#Student Views
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            id=request.POST['id'],
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
            age=request.POST['age'],
            address=request.POST['address']
        )
        return redirect('students')
    return render(request, 'add_student.html')

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.id = request.POST['id']
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.address = request.POST['address']
        student.save()
        return redirect('students')
    return render(request, 'update_student.html', {'student': student})

def delete_student(request, id):
    Student.objects.get(id=id).delete()
    return redirect('students')

# Authentication
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request, 
            username=request.POST.get('username'), 
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('homepage') 
        messages.error(request, 'Invalid username or password!')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        else:
            User.objects.create_user(
                username=username,
                email=request.POST['email'],
                password=request.POST['password']
            )
            messages.success(request, 'Account created successfully!')
            return redirect('login')  
    return render(request, 'register.html')

# Page Views
def homepage(request):
    return render(request, 'homepage.html')

def courses(request):
    return render(request, 'courses.html')

def reports(request):
    return render(request, 'reports.html')



# Attendance
def mark_attendance(request):
    students = Student.objects.all()
    today = timezone.now().date()

    if request.method == 'POST':
        for student in students:
            status = 'Present' if f'attendance_{student.id}' in request.POST else 'Absent'
            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={'status': status}
            )
        return redirect('mark_attendance')  # refresh page to reflect changes
    
    attendance_records = Attendance.objects.filter(date=today)
    attendance_dict = {a.student.id: a.status for a in attendance_records}

    return render(request, 'mark_attendance.html', {
        'students': students,
        'attendance_dict': attendance_dict
    })


def attendance_records(request):
    today = timezone.now().date()
    records = Attendance.objects.filter(date=today).select_related('student')
    present_students = records.filter(status='Present')
    absent_students = records.filter(status='Absent')
    return render(request, 'attendance_records.html', {
        'today': today,
        'present_students': present_students,
        'absent_students': absent_students
    })



def students_list(request):
    query = request.GET.get('q')
    students = Student.objects.all()
    if query:
        students = students.filter(Q(name__icontains=query) | Q(email__icontains=query))
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    return render(request, 'students.html', {'students': students})


from django.shortcuts import render
from .models import Attendance
from django.db.models import Max

def attendance_records(request):
    date = request.GET.get('date')
    status = request.GET.get('status')
    search = request.GET.get('search', '').strip()

    # Base queryset
    attendances = Attendance.objects.select_related('student')

    # Filter by date if provided
    if date:
        attendances = attendances.filter(date=date)
    else:
        # Fetch only latest attendance record per student
        latest_dates = Attendance.objects.values('student').annotate(latest_date=Max('date'))
        attendances = Attendance.objects.filter(
            date__in=[item['latest_date'] for item in latest_dates]
        )

    # Filter by status
    if status == 'present':
        attendances = attendances.filter(status='Present')
    elif status == 'absent':
        attendances = attendances.filter(status='Absent')

    # Filter by student name
    if search:
        attendances = attendances.filter(student__name__icontains=search)

    # Separate present and absent
    present = attendances.filter(status='Present').distinct()
    absent = attendances.filter(status='Absent').distinct()

    context = {
        'today': date or 'All Dates',
        'present_students': present,
        'absent_students': absent,
    }

    return render(request, 'attendance_records.html', context)






#for face recogntiton

from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2

# Load OpenCV's Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def generate_frames():
    cap = cv2.VideoCapture(0)  # 0 for default webcam

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Draw rectangle around each face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame to the browser as part of an HTTP stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def face_feed(request):
    """Video stream view"""
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def face_attendance(request):
    """Render page with video feed"""
    return render(request, 'face_attendance.html')

from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.shortcuts import redirect
from .models import Student, Attendance

def face_attendance(request):
    students = Student.objects.all()
    return render(request, 'face_attendance.html', {'students': students})



def mark_face_attendance(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        student = Student.objects.get(id=student_id)

        # Create attendance record for today if not already marked
        Attendance.objects.get_or_create(
            student=student,
            date=timezone.now().date(),
            defaults={'status': 'Present'}
        )

    return redirect('face_attendance')
