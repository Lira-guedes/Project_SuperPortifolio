from projects.models import (
    Profile, Project, CertifyingInstitution, Certificate
)
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'github', 'linkedin', 'bio')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'github_url',
            'keyword',
            'key_skill',
            'profile',
        )

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"
        # fields = ('id', 'name', 'timestamp', 'certifying_institution', 'profiles')


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)
    class Meta:
        model = CertifyingInstitution
        # fields = "__all__"
        fields = ('id', 'name', 'url', 'certificates')
        # fields = ["id", "name", "url", "certificates"]

    def create(self, data):
        certificates = data.pop('certificates')
        institution = CertifyingInstitution.objects.create(**data)
        for certificate in certificates:
            certificate['certifying_institution'] = institution
            CertificateSerializer().create(data=certificate)
            # Certificate.objects.create(certifying_institution=institution, **certificate)
        return institution
