import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import base64
from django.core.files.base import ContentFile
import cv2
import tempfile
from PIL import Image
import io
import face_recognition
from .models import Person, Groups
from django.contrib import messages
from django.shortcuts import redirect

def camera_view(request):
    groups = Groups.objects.all()
    return render(request, 'camera.html', context={'groups': groups})



@csrf_exempt
def get_video(request):
    if request.method == 'POST':
        try:
            # POST so'rovdan tasvirni olish
            photo_data = request.POST.get('faces')  # Base64 tasvir
            if not photo_data:
                return JsonResponse({'error': 'No face data provided'}, status=400)

            # Base64 ma'lumotni dekodlash
            photo_data = photo_data.split(',')[1]
            photo_data = base64.b64decode(photo_data)

            # Tasvirni ochish va OpenCV formatiga aylantirish
            photo = Image.open(io.BytesIO(photo_data))
            photo = cv2.cvtColor(np.array(photo), cv2.COLOR_RGB2BGR)

            # Yuz joylashuvlarini aniqlash
            face_locations = face_recognition.face_locations(photo)
            face_encodings = face_recognition.face_encodings(photo, face_locations)

            recognized_faces = []

            # Har bir yuzni bazadagi ma'lumotlar bilan solishtirish
            for i, face_encoding in enumerate(face_encodings):
                match_found = False

                # Bazadagi barcha yuzlarni ko'rib chiqish
                for person in Person.objects.all():
                    known_face_encoding = np.frombuffer(person.face_encoding, dtype=np.float64)
                    match = face_recognition.compare_faces([known_face_encoding], face_encoding, tolerance=0.5)

                    if match[0]:
                        # Mos keladigan inson topildi
                        # Yuzning tasvirini olish
                        top, right, bottom, left = face_locations[i]
                        face_image = photo[top:bottom, left:right]
                        _, buffer = cv2.imencode('.jpg', face_image)
                        face_image_base64 = base64.b64encode(buffer).decode('utf-8')
                        face_image_base64 = f'data:image/jpeg;base64,{face_image_base64}'

                        recognized_faces.append({
                            'name': person.name,
                            'group': person.group.name,
                            'face_image': face_image_base64
                        })
                        match_found = True
                        break

                
            return JsonResponse({'data': recognized_faces}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def add_data(request):
    def process_image(image, name, group):
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        face_locations = face_recognition.face_locations(image)
        
        if len(face_locations) > 1:
            messages.error(request, 'Rasmda faqatgina bir kishi bo\'lishi mumkin')
            return redirect(request.META.get('HTTP_REFERER', 'app1:home'))
        
        if face_locations:
            face_encoding = face_recognition.face_encodings(image, face_locations)[0]

            # Check if the face already exists in the database
            for person in Person.objects.all():
                known_face_encoding = np.frombuffer(person.face_encoding, dtype=np.float64)
                match = face_recognition.compare_faces([known_face_encoding], face_encoding, tolerance=0.5)
                if match[0]:
                    messages.error(request, 'Shaxs allaqachon mavjud')
                    return redirect(request.META.get('HTTP_REFERER', 'app1:home'))

            top, right, bottom, left = face_locations[0]
            face_image = image[top:bottom, left:right]
            _, buffer = cv2.imencode('.jpg', face_image)
            face_img_base64 = base64.b64encode(buffer).decode('utf-8')
            person = Person.objects.create(name=name, group=group, face_encoding=face_encoding.tobytes(), face_img=face_img_base64)
            messages.success(request, f'Shaxs {person.name} {person.group} guruhiga qo\'shildi')
            return redirect('app1:home')
        
        messages.error(request, 'Yuz aniqlanmadi')
        return redirect(request.META.get('HTTP_REFERER', 'app1:home'))

    if request.method == 'POST':
        name = request.POST.get('name')
        group_id = request.POST.get('group')
        photo_option = request.POST.get('photoOption')

        try:
            group = Groups.objects.get(id=group_id)
        except Groups.DoesNotExist:
            messages.error(request, 'Guruh topilmadi')
            return redirect(request.META.get('HTTP_REFERER', 'app1:home'))

        if photo_option == 'upload':
            photo = request.FILES.get('photo')
            if name and group and photo:
                image = Image.open(photo)
                return process_image(image, name, group)
            messages.error(request, 'Shaxsni qo\'shish muvaffaqiyatsiz tugadi')
            return redirect('app1:home')

        elif photo_option == 'capture':
            captured_photo = request.POST.get('capturedPhoto')
            if name and group and captured_photo:
                captured_photo = base64.b64decode(captured_photo.split(',')[1])
                image = Image.open(io.BytesIO(captured_photo))
                return process_image(image, name, group)
            messages.error(request, 'Shaxsni qo\'shish muvaffaqiyatsiz tugadi')
            return redirect(request.META.get('HTTP_REFERER', 'app1:home'))

        messages.error(request, 'Noto\'g\'ri foto opsiyasi')
        return redirect(request.META.get('HTTP_REFERER', 'app1:home'))

    elif request.method == 'GET':
        groups = Groups.objects.all()

        return render(request, 'add_data.html', context={'groups': groups})
