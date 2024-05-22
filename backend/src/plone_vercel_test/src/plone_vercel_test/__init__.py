"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "plone_vercel_test"

_ = MessageFactory("plone_vercel_test")

logger = logging.getLogger("plone_vercel_test")
