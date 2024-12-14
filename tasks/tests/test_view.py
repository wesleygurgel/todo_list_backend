import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    return User.objects.create_user(username="testuser", password="testpassword")

@pytest.fixture
def create_tasks(create_user):
    tasks = [
        Task.objects.create(
            title=f"Task {i}",
            description=f"Description {i}",
            completed=(i % 2 == 0),
            user=create_user
        ) for i in range(1, 21)
    ]
    return tasks

@pytest.fixture
def authenticate(api_client, create_user):
    login_url = reverse("jwt-create")
    response = api_client.post(
        login_url, {"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == status.HTTP_200_OK
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client

@pytest.mark.django_db
def test_task_list(authenticate, create_tasks):
    # Fazer a requisição para listar tarefas
    url = reverse("task-list")
    response = authenticate.get(url)

    assert response.status_code == status.HTTP_200_OK
    # Verificar paginação padrão (10 itens por página)
    assert len(response.data["results"]) == 10

@pytest.mark.django_db
def test_task_search(authenticate, create_tasks):
    # Fazer a requisição para buscar tarefas
    url = reverse("task-list") + "?search=Task 1&match_type=exact"
    response = authenticate.get(url)

    assert response.status_code == status.HTTP_200_OK
    # Apenas um item deve ser retornado
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == "Task 1"

@pytest.mark.django_db
def test_task_filter_completed(authenticate, create_tasks):
    # Filtrar por tarefas concluídas
    url = reverse("task-list") + "?completed=true"
    response = authenticate.get(url)

    assert response.status_code == status.HTTP_200_OK
    completed_tasks = [
        task for task in response.data["results"] if task["completed"] is True
    ]
    assert len(completed_tasks) > 0

@pytest.mark.django_db
def test_task_pagination(authenticate, create_tasks):
    # Testar a segunda página da paginação
    url = reverse("task-list") + "?page=2"
    response = authenticate.get(url)

    assert response.status_code == status.HTTP_200_OK
    # Verificar que há 10 itens na segunda página
    assert len(response.data["results"]) == 10
