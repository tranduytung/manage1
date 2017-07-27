from random import randint
from faker import Faker
from manage1.model.meta import Session
import sqlalchemy as sa
import manage1.model as model
from paste.script.command import Command
# from pylons import request

DB_URL = "sqlite:///development.db"
engine = sa.create_engine(DB_URL)
model.init_model(engine)
faker = Faker()
# users = request.environ['authkit.users']

class Seed(Command):
    summary = "--NO SUMMARY--"
    usage = "--NO USAGE--"
    group_name = "manage1"
    parser = Command.standard_parser(verbose=False)

    def command(self):
        print("----Delete Database----")
        Session.query(model.Course).delete()
        # Session.query(model.Users).delete()
        print("----Delete Done----")
        # users.role_create("admin")
        # users.role_create("delete")
        # users.role_create("editor")
        # users.group_create("student")
        #
        # users.user_create("tung@gmail.com", password="a123456")
        # users.user_add_role("tung@gmail.com", role="editor")
        # users.user_set_group("tung@gmail.com", 'student')
        # users.user_create("admin@gmail.com", password="admin123")
        # users.user_add_role("admin@gmail.com", role="delete")
        # users.user_add_role("admin@gmail.com", role="admin")
        Session.commit()
        print("----Seed Database----")

        for i in range(100):
            student = model.Users(email=faker.email(), password='a123456', group_id = 2)
            student.user_info = model.UsersInfo(name=faker.name())
            Session.add(student)
        for i in range(100):
            name = faker.sentence(nb_words=4)
            code = 'IT' + str(randint(1000, 10000))
            course = model.Course(code=code, name=name, number=randint(10, 100))
            Session.add(course)
        Session.commit()
        print("----Seed Done----")
