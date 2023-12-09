from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import Company, Doc, User

class CompanyAPITest(TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.client = APIClient()
        self.company_data = {"name": "New Company", "created_by_user": None}  # Preencha conforme necessário

    def test_create_company(self):
        # Testa a criação de uma nova empresa
        response = self.client.post(reverse("company-list"), data=self.company_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se a empresa foi criada corretamente no banco de dados
        created_company = Company.objects.get(name="New Company")
        self.assertIsNotNone(created_company)

    def test_list_companies(self):
        # Testa a API para listar empresas
        response = self.client.get(reverse("company-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

