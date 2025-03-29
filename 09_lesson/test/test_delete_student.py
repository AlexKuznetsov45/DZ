import pytest
from sqlalchemy import func
from models import Student, User
from db import get_session


@pytest.fixture(scope="module")
def session():
    session = get_session()
    yield session
    session.close()


def test_delete_student(session):
    # Получаем максимальное значение user_id из базы данных
    max_user_id = session.query(func.max(User.user_id)).scalar()

    # Если max_user_id равен None (база данных пуста),
    #  устанавливаем начальное значение 1
    next_user_id = max_user_id + 1 if max_user_id else 1

    # Создаем пользователя и добавляем его в базу данных
    user = User(
        user_id=next_user_id,
        user_email="test@example.com",
        subject_id=1
    )
    session.add(user)
    session.commit()

    # Создаем студента и добавляем его в базу данных
    student = Student(
        user_id=user.user_id,
        level="beginner",
        education_form="online",
        subject_id=1
    )
    session.add(student)
    session.commit()

    # Удаляем студента
    deleted_student = session.query(Student).filter_by(
        user_id=user.user_id
    ).first()
    session.delete(deleted_student)
    session.commit()

    # Проверяем, что студент был удален
    nonexistent_student = session.query(Student).filter_by(
        user_id=user.user_id
    ).first()
    assert nonexistent_student is None

    # Удаляем пользователя после завершения теста
    session.delete(user)
    session.commit()
