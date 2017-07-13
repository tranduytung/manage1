"""Setup the manage1 application"""
import logging

from manage1.config.environment import load_environment
from manage1.model.meta import Session, Base

log = logging.getLogger(__name__)


def setup_app(command, conf, vars):
    """Place any commands to setup manage1 here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    log.info("Creating tables")
    Base.metadata.drop_all(checkfirst=True, bind=Session.bind)
    Base.metadata.create_all(bind=Session.bind)
    log.info("Successfully setup")

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)
