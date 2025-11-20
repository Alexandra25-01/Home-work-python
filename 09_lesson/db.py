from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:
    __scripts = {
        "select": text("SELECT * FROM student"),
        "insert": text(
            "INSERT INTO student(user_id, level, education_form, subject_id) "
            "VALUES (:user_id, :level, :education_form, :subject_id)"
        ),
        "update": text(
            "UPDATE student SET level = :level WHERE user_id = :user_id"
        ),
        "delete": text("DELETE FROM student WHERE user_id = :user_id"),
        "get_max_id": text("SELECT MAX(user_id) FROM student"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_students(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def create(self, user_id, level, education_form, subject_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert"], {
            "user_id": user_id,
            "level": level,
            "education_form": education_form,
            "subject_id": subject_id
        })
        conn.commit()
        conn.close()

    def update_level(self, user_id, level):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update"], {
            "user_id": user_id,
            "level": level
        })
        conn.commit()
        conn.close()

    def delete(self, user_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["delete"], {"user_id": user_id})
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id
