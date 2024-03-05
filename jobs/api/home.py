from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from jobs.models import PostJob
from jobs.api.serializers import PostJobSerializer


class JobHomeAPIView(APIView):
    queryset = PostJob.objects.all()
    serializer_class = PostJobSerializer

    def get(self, request):
        latest3Jobs = self.queryset.order_by("-createdAt")[:3]
        latest3JobsSerializer = self.serializer_class(
            latest3Jobs, many=True, context={"request": request}
        )

        best3Internships = self.queryset.filter(
            jobType=PostJob.JOB_TYPE.INTERNSHIP
        ).order_by("-createdAt")[:3]
        best3InternshipsSerializer = self.serializer_class(
            best3Internships, many=True, context={"request": request}
        )

        return Response(
            {
                "latest3Jobs": latest3JobsSerializer.data,
                "best3Internships": best3InternshipsSerializer.data,
            },
            status=status.HTTP_200_OK,
        )
