import pytest
from tasks.models import Task
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_task():
    user = User.objects.create_user(
        username="testuser", password="testpassword")
    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        completed=False,
        user=user
    )

    assert Task.objects.count() == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False


@pytest.mark.django_db
def test_read_task():
    user = User.objects.create_user(
        username="testuser", password="testpassword")
    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        completed=False,
        user=user
    )

    retrieved_task = Task.objects.get(id=task.id)
    assert retrieved_task == task
    assert retrieved_task.title == "Test Task"


@pytest.mark.django_db
def test_update_task():
    user = User.objects.create_user(
        username="testuser", password="testpassword")
    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        completed=False,
        user=user
    )

    task.title = "Updated Task"
    task.completed = True
    task.save()

    updated_task = Task.objects.get(id=task.id)
    assert updated_task.title == "Updated Task"
    assert updated_task.completed is True


@pytest.mark.django_db
def test_delete_task():
    user = User.objects.create_user(
        username="testuser", password="testpassword")
    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        completed=False,
        user=user
    )

    task_id = task.id
    task.delete()

    with pytest.raises(Task.DoesNotExist):
        Task.objects.get(id=task_id)
