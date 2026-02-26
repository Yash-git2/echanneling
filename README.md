# CareConnect – E-Channeling System  

CareConnect is a full-stack Django web application developed for online doctor appointment booking. The system enables patients to browse doctors, check availability, schedule appointments, and manage bookings securely. Doctors and administrators are provided with dedicated dashboards to manage schedules and appointments efficiently.

## Overview  

This project was built to streamline the traditional doctor appointment process by providing a centralized and user-friendly digital platform. It demonstrates full-stack development using Django, role-based authentication, and structured database management.

## Key Features  

### Patient Module
- User registration and secure login  
- Browse available doctors  
- View doctor profiles and schedules  
- Book appointments  
- Manage or cancel bookings  

### Doctor Module
- Manage availability schedules  
- View upcoming appointments  
- Update appointment status  

### Administrator Module
- Add, edit, or remove doctors  
- Manage patient records  
- Monitor and oversee all appointments  
- Full administrative access via Django Admin Panel  


## Tech Stack  

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap 5  
- **Database:** SQLite  
- **Version Control:** Git & GitHub  
- **IDE:** Visual Studio Code  


## Installation Guide  

### 1. Clone the Repository  

```bash
git clone https://github.com/Yash-git2/echanneling.git
cd echanneling
```

### 2. Create a Virtual Environment  

```bash
python -m venv venv
```

Activate the environment:  

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies  

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations  

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional for Admin Access)  

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server  

```bash
python manage.py runserver
```

Access the application at:  
http://127.0.0.1:8000/

---

