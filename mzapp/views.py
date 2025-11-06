from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

def portfolio_page(request):
    # YOUR NEW, COMPLETE PROJECTS LIST
    projects = [
        {
            'title': 'All-in-One Media Toolkit',
            'description': 'A powerful desktop GUI tool in Python using Tkinter that combines YouTube downloading, media conversion, PDF tools, and QR code generation.',
            'image': 'mzapp/images/all_in_one.png',
            'github_link': 'https://github.com/Zeelmakwana/allinone-media-toolkit'
        },
        {
            'title': 'Exam Chatbot',
            'description': 'A specialized chatbot for DDCET exam inquiries, built with Python, Flask, and machine learning models.',
            'image': 'mzapp/images/exam_bot.png',
            'github_link': 'https://github.com/Zeelmakwana/exam_chatbot.pdf'
        },
        {
            'title': 'Laptop Price Predictor',
            'description': 'A machine learning project using Streamlit that predicts laptop prices based on a trained model and dataset.',
            'image': 'mzapp/images/laptop_price.png',
            'github_link': 'https://github.com/Zeelmakwana/laptop-price-predictor'
        },
        {
            'title': 'AI Music Player',
            'description': 'An intelligent media player built with Python, featuring a linked list data structure and AI-powered functionalities.',
            'image': 'mzapp/images/music_player.png',
            'github_link': 'https://github.com/Zeelmakwana/music_player_in_python-'
        },
        {
            'title': 'Domain Finder',
            'description': 'A Flask ML web app that recommends a tech domain (e.g., Web Dev, AI) based on user-selected programming languages.',
            'image': 'mzapp/images/domain_finder.png',
            'github_link': 'https://github.com/Zeelmakwana/domain-finder'
        },
        {
            'title': 'AI Image Classifier',
            'description': 'An AI-powered application that uses various APIs for visual predictions and image classification.',
            'image': 'mzapp/images/img_clasi.png',
            'github_link': 'https://github.com/Zeelmakwana/imgclasi'
        },
        {
            'title': 'Student Attendance System',
            'description': 'A full-stack web application for managing student attendance, built with PHP, MySQL, HTML, and CSS.',
            'image': 'mzapp/images/attandance_sys.png',
            'github_link': 'https://github.com/Zeelmakwana/Student-Attandence-System-Using-php'
        }
    ]

    # YOUR EXPERIENCE DATA
    # YOUR EXPERIENCE DATA
    experience = [
        {
            'role': 'Android Development Intern',
            'company': 'Prelax Infotech',
            'period': 'July 2023 - August 2023',
            'location': 'Surat, Gujarat, India',
            'description': 'Honed mobile app development skills by contributing to various stages of app creation, from concept to deployment.',
            'certificate': 'mzapp/images/prelax internship completion certificate.pdf'  # <-- ADD THIS LINE
        },
        {
            'role': 'Web Development Intern (PHP)',
            'company': 'For Each Next',
            'period': 'September 2022 - October 2022',
            'location': 'Surat, Gujarat, India',
            'description': 'Contributed to innovative projects and expanded skills in PHP-based web development and back-end logic.',
            'certificate': 'mzapp/images/Zeel-internship-certi.pdf'  # <-- AND ADD THIS LINE
        }
    ]

    # YOUR SKILLS DATA
    skills = [
        {'name': 'Python', 'icon': 'python/python-original.svg'},
        {'name': 'TensorFlow', 'icon': 'tensorflow/tensorflow-original.svg'},
        {'name': 'PyTorch', 'icon': 'pytorch/pytorch-original.svg'},
        {'name': 'Scikit-learn', 'icon': 'scikitlearn/scikitlearn-original.svg'},
        {'name': 'Django', 'icon': 'django/django-plain.svg'},
        {'name': 'Streamlit', 'icon': 'streamlit/streamlit-original.svg'},
        {'name': 'Jupyter', 'icon': 'jupyter/jupyter-original.svg'},
    ]
    
    # NEW CERTIFICATIONS DATA
   # NEW CERTIFICATIONS DATA
    certifications = [
        {
            'name': 'Tata - Data Visualisation Job Simulation',
            'link': 'https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_sMMd8xSNp3chWX2gF_1755967038855_completion_certificate.pdf'
        },
        {
            'name': 'Data science and business analytics 3.0',
            'link': 'mzapp/images/udemy_datascience_cert.pdf' # Corrected local path
        },
        {
            'name': 'Fundamentals of data science',
            'link': 'https://aiplanet.com/course/certificates/verify/a9a1349e-bbd7-4f0e-9843-dd1bac9508ff'
        },
        {
            'name': 'Machine Learning Bootcamp',
            'link': 'https://aiplanet.com/course/certificates/verify/e23a82cc-d039-4149-bde6-4a14d7da786d'
        },
        {
            'name': 'Introduction to Generative AI Studio',
            'link': 'mzapp/images/google_cloud_cert.pdf' # Corrected local path
        }
    ]
    
    # Pass all data to the template
    context = {
        'projects': projects,
        'experience': experience,
        'skills': skills,
        'certifications': certifications,
    }
    
    return render(request, 'mzapp/index.html', context)

@csrf_exempt
def send_contact_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')
            
            subject = f'Portfolio Contact from {name}'
            email_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ['zeelmakwana55@gmail.com'],
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'message': 'Email sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})
