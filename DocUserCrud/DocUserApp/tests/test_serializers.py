from django.test import TestCase
from ..serializers import CompanySerializer, DocSerializer, UserSerializer
from ..models import Company, Doc, User

class CompanySerializerTest(TestCase):
    def test_company_serializer(self):
        company_data = {"name": "Test Company", "created_by_user": None}  # Preencha conforme necessário
        serializer = CompanySerializer(data=company_data)
        self.assertTrue(serializer.is_valid())
        company_instance = serializer.save()

        # Verifica se o objeto foi criado corretamente no banco de dados
        self.assertIsNotNone(Company.objects.get(id=company_instance.id))
