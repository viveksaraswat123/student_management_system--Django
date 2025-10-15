
# 🎓 Student Management System (Django)

A **Role-Based Student Management System** built using **Django Framework**.  
This system enables **admins, teachers, and students** to perform their respective tasks efficiently — from attendance tracking to performance monitoring.  
Currently, a **Face Detection Attendance System** is under development to enhance automation and accuracy.

---

## 🚀 Features

### 👩‍🏫 Role-Based Login System
- **Admin Login:** Manage users, courses, subjects, and view reports.  
- **Teacher Login:** Mark attendance, update student performance, and view academic reports.  
- **Student Login:** View attendance, marks, and overall progress.

### 🧾 Attendance Management
- Teachers can **mark daily attendance** for each class.  
- Students can **view attendance history**.  
- Attendance records are stored securely in the database.  
- (🔧 *Upcoming Feature: Face Detection-based automatic attendance marking.*)

### 📈 Student Performance Monitoring
- Teachers can **record marks and feedback** for each student.  
- Students can **track performance** through graphical and tabular reports.  
- Admins can **analyze academic trends** and identify improvement areas.

### 🧑‍💻 Admin Dashboard
- Add or remove students, teachers, and classes.  
- Manage subjects, timetables, and system settings.  
- Generate summarized reports of attendance and performance.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Database** | SQLite (default) / MySQL (optional) |
| **Authentication** | Django’s built-in auth system |
| **Face Detection (WIP)** | OpenCV & face-recognition library |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate   # For Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📷 Face Detection Attendance (Upcoming)
A **camera-based attendance system** is being developed using **OpenCV** and **face-recognition**.  
This feature will allow:
- Automatic student identification during attendance.
- Reduction in manual marking errors.
- Integration with existing attendance records.

---

## 📊 Future Enhancements
- Integration of **email/SMS notifications** for parents.  
- **AI-based performance prediction** for students.  
- **Export reports** (PDF/Excel).  
- **Mobile-friendly UI** with responsive design.

---

## 🧑‍💻 Author
**Vivek Saraswat**  
B.Tech (CSE) | 7th Semester  
Passionate about building real-world Django projects and AI/ML 💻  

 
🔗 GitHub: https://github.com/viveksaraswat123
🔗 LinkedIn: https://www.linkedin.com/in/saraswat-vivek/

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use and modify it.
