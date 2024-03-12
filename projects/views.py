from rest_framework import viewsets, permissions
from projects.models import (
    Profile, Project, CertifyingInstitution, Certificate
)
from projects.serializers import (
    ProfileSerializer, ProjectSerializer,
    CertifyingInstitutionSerializer, CertificateSerializer
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if self.request.method == "GET":
            profile_id = self.kwargs.get("pk")
            profile = Profile.objects.get(id=profile_id)
            return render(request, "profile_detail.html", {"profile": profile})
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
