from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import generics

from jobs.models import PostJob

# from jobs.api.serializers import CustomUserSerializer, PostJobSerializer
from jobs.api.serializers import PostJobSerializer

# from django.contrib.auth.models import User as CustomUser
# from django.contrib.auth.hashers import check_password


class PostJobListAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "place", "companyName"]
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer


class PostJobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer


# class UserRegister(APIView):
#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data["email"]
#             if CustomUser.objects.filter(email=email).exists():
#                 return Response(
#                     {"error": "Email already exists"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserLogin(APIView):
#     def post(self, request):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         if email is None or password is None:
#             return Response(
#                 {"error": "Please provide both email and password"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         user = CustomUser.objects.filter(email=email).first()

#         if user is None or not check_password(password, user.password):
#             return Response(
#                 {"error": "Invalid email/password combination"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         # You can implement JWT token authentication here or any other authentication mechanism

#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)


# class BestJobAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         user: User = request.user

#         queryset = PostJob.objects.all()
#         strList = str([job.to_string() for job in queryset])
#         user_skills = ""
#         if user.resume:
#             try:
#                 user_skills = CommonUtils.pdf_to_text(user.resume)
#             except:
#                 user_skills = user.get_user_tech_skills()
#         else:
#             user_skills = user.get_user_tech_skills()
#         try:
#             ai_resp = GeminiUtils.get_gemini_response(
#                 jsonStructure="""{
#                 "ids":[<id-here>,<id-here>,....],
#                 "reason":<user-friendly-reason-here>
#                 }""",
#                 command="Find Best Jobs from the following and return its id  in the above json format",
#                 content=f"""User skill: {user_skills}
#             Available Jobs: {strList}
#             """,
#             )
#             best_job_ids = ai_resp.get("ids")
#             try:
#                 best_jobs = PostJob.objects.filter(id__in=best_job_ids)
#             except:
#                 return Response(
#                     {"reason": ai_resp.get("reason"), "best_jobs": None},
#                     status=status.HTTP_200_OK,
#                 )
#             best_job_serializer = PostJobSerializer(
#                 best_jobs, many=True, context={"request": request}
#             )
#             return Response(
#                 {
#                     "reason": ai_resp.get("reason"),
#                     "best_jobs": best_job_serializer.data,
#                 },
#                 status=status.HTTP_200_OK,
#             )

#         except Exception as e:
#             return Response(
#                 {
#                     "reason": "Unable to find best job due to high demand of AI Server. Please try again later.",
#                     "best_jobs": None,
#                 },
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )
