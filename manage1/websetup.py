"""Setup the manage1 application"""
import logging

from manage1.config.environment import load_environment
from manage1.model.meta import Session, Base
from authkit.users.sqlalchemy_driver import UsersFromDatabase
from manage1.model import meta
from manage1 import model

log = logging.getLogger(__name__)

users = UsersFromDatabase(model)
log.info("Adding the AuthKit model...")

def setup_app(command, conf, vars):
    """Place any commands to setup manage1 here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)
    log.info("Creating tables")
    Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
    Base.metadata.create_all(checkfirst=True, bind=Session.bind)

    meta.metadata.bind = meta.engine
    meta.metadata.drop_all(checkfirst=True)
    meta.metadata.create_all(checkfirst=True)
    # log.info("Adding roles and uses...")
    users.role_create("admin")
    users.role_create("delete")
    users.role_create("editor")
    users.group_create("admin")
    users.group_create("student")
    # users.user_create("foo", password="foo123")
    # users.user_add_role("foo", role="editor")
    # users.user_set_group("foo", 'student')
    users.user_create("admin@gmail.com", password="a123456")
    users.user_add_role("admin@gmail.com", role="delete")
    users.user_add_role("admin@gmail.com", role="admin")
    users.user_set_group("admin@gmail.com", 'admin')
    Session.commit()
    log.info("Successfully setup")

    #Create the tables if they don't already exist
    # meta.metadata.create_all(bind=Session.bind)
