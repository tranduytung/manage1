from random import randint
from faker import Faker
from manage1.model.meta import Session
import sqlalchemy as sa
import manage1.model as model
from paste.script.command import Command

DB_URL = "sqlite:///development.db"
engine = sa.create_engine(DB_URL)
model.init_model(engine)
faker = Faker()

class Seed(Command):
    summary = "--NO SUMMARY--"
    usage = "--NO USAGE--"
    group_name = "manage1"
    parser = Command.standard_parser(verbose=False)

    def command(self):
        print("----Delete Database----")
        Session.query(model.Course).delete()
        Session.query(model.Student).delete()
        print("----Delete Done----")

        print("----Seed Database----")
        for i in range(100):
            student = model.Student(name=faker.name(), email=faker.email(), password='a123456')
            Session.add(student)
        for i in range(100):
            name = faker.sentence(nb_words=4)
            code = 'IT' + str(randint(1000, 10000))
            course = model.Course(code=code, name=name, number=randint(10, 100))
            Session.add(course)
        Session.commit()
        print("----Seed Done----")