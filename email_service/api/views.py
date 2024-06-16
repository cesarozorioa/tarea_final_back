from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class EmailAPIView(APIView):

    def post(self, request):
        try:
            to_email = 'cesarozorioa@gmail.com'
            subject = 'Mensaje de Prueba'
            message = 'Asignado una nueva tarea'
            from_email = 'cesarozorioa'
            send_mail(subject,message,None,[to_email],fail_silently=False)
            return Response({'message': 'Email enviado'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': 'Email no enviado','error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
