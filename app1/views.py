from rest_framework.views import APIView
from app1.models import Student
from django.contrib.auth.models import User
from app1.serializers import StudentSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated







class Create_student(APIView):
    def post(self,request):
        data = request.data
        try:
            Student_obj = Student.objects.filter(email=data.get('email'))
            print(Student_obj)
            if len(Student_obj) > 0:
                return Response({
                'status':203,
                'message': 'your account has been already exist!!'
            })

            serializer = StudentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                'status': 200,
                'message': 'Student account has been successfully created!!'
            })
            else:
                return Response(serializer.errors)
        except Student.DoesNotExist:
            return Response({
            'status': 202,
            'message': 'Something went wrong!!',
            'errors': serializer.errors
        })

class StudentDetail(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get (self,request): # this method is used to get all the data 
        obj=Student.objects.all()
        serializer=StudentSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request): # to insert the data 
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)



class RegisterUser(APIView):
    def post(self, request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors,'message':'something went wrong'})

        serializer.save()
       
        user=User.objects.get(username= serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user = user)
        return Response({'status':200, 'payload':serializer.data ,'token': str(token_obj), 'message':'your data is saved'})
        
# class Login(APIView):
#     def post(self, request):
#         data = request.data
        
#         print(Student)
#         if Student is not None:
#             Student = Student.objects.get(id=Student.id)
#             serializer = StudentfrofileSerializer(Student)

#             return Response({
#                 'status': 200,
#                 'message': 'Your account has been successfully logged in!!',
#                 'payload': serializer.data
#             })
#         return Response({
#             'status': 202,
#             'message': 'Login details are wrong. Please try again!!'
#         })
        

class StudentList(APIView):
    def post(self,request):
        data = request.data
        try:
            Student_obj = Student.objects.filter(email=data.get('email'))
            if Student_obj is not None:   
                serializer = StudentSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({
                        'status': 200,
                        'message': 'Student details has been successfully created!!'    
                        })
                else:
                    return Response(serializer.errors)
        except Student.DoesNotExist:
           
            return Response({
                'status': 200,
                'message': 'Student details already exists'
            })
    
        return Response({
            'status': 202,
            'message': 'Student details are wrong, please try again!!'
        })


"""""""""
class Create_student(APIView):
    def post(self,request):
        data = request.data
        Student_obj = Student.objects.filter(email=data.get('email'))
        if Student_obj is not None:
            return Response({
                'status':203,
                'message': 'your account has been already exist!!'
             })

        serializer = Create_StudentfrofileSerializer(data=data)
        if serializer.is_valid():
            serializer.save
            return Response({
            'status': 200,
            'message': 'Student account has been successfully created!!'
        })

        return Response({
            'status': 202,
            'message': 'Something went wrong!!',
            'errors': serializer.errors
        })
"""""""""
class Update(APIView):
    def put(self, request, pk):
        try:    
            user_obj = Student.objects.get(id=pk)
            print('user: ', user_obj)
        except Student.DoesNotExist:
            user_obj = None
        
        if user_obj is not None:

            user_obj.name = request.data.get('name')
            user_obj.phone_no = request.data.get('phone_no')
            user_obj.email = request.data.get('email')
            user_obj.save()
            return Response({'status': 200,
            'message': 'Your profile has been updated'})
        else:
            return Response({'status': 204,
            'message': 'Profile does not exists'})



class Delete(APIView):
    def get(self, request, pk):
        try:
            user_obj = Student.objects.get(id=pk)
            user_obj.delete()
            return Response({
                'status': 200, 'message': 'Data has been successfully deleted!!'
                })
        except Student.DoesNotExist:
            return Response({
                'status': 404, 'message': f"Something went wrong! Like!!"
                })
        








