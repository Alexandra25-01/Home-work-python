from db import StudentTable
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

connection_string = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
db = StudentTable(connection_string)


def test_add_student():
    user_id = db.get_max_id() + 1 or 1
    db.create(
        user_id, level="Beginner", education_form="Full-time", subject_id=101
        )

    students = db.get_students()
    added = [s for s in students if s["user_id"] == user_id]

    # Проверка
    assert len(added) == 1
    assert added[0]["level"] == "Beginner"

    # Чистим БД
    db.delete(user_id)


def test_update_student():
    user_id = db.get_max_id() + 1 or 1
    db.create(
        user_id, level="Beginner", education_form="Full-time", subject_id=101
        )

    db.update_level(user_id, "Advanced")
    students = db.get_students()
    updated = [s for s in students if s["user_id"] == user_id]

    assert updated[0]["level"] == "Advanced"

    db.delete(user_id)


def test_delete_student():
    user_id = db.get_max_id() + 1 or 1
    db.create(
        user_id, level="Beginner", education_form="Full-time", subject_id=101
        )

    db.delete(user_id)
    students = db.get_students()
    deleted = [s for s in students if s["user_id"] == user_id]

    assert len(deleted) == 0
