from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Company, Doc, User

class DocAPITest(TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.client = APIClient()
        self.company = Company.objects.create(name="Test Company")
        self.user = User.objects.create(email="test@example.com", password="test123")
        self.doc_data = {"name": "Test Doc", "created_by_user": self.user.id, "company": self.company.id}

    def test_create_doc(self):
        # Testa a criação de um novo documento
        response = self.client.post(reverse("doc-list"), data=self.doc_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se o documento foi criado corretamente no banco de dados
        created_doc = Doc.objects.get(name="Test Doc")
        self.assertEqual(created_doc.created_by_user, self.user)
        self.assertEqual(created_doc.company, self.company)

    def test_sign_document(self):
        # Testa a ação de assinar um documento
        doc = Doc.objects.create(name="To be signed", created_by_user=self.user, company=self.company)
        response = self.client.post(reverse("doc-sign_document", args=[doc.id]), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Doc.objects.get(id=doc.id).signed)

    def test_list_docs(self):
        # Testa a API para listar documentos
        response = self.client.get(reverse("doc-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)