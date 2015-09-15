# -*- coding: utf-8 -*-
"""Propertyshelf LEPcostarica.com."""

# python imports
import logging

# zope imports
from zope.i18nmessageid import MessageFactory

# local imports
from ps.diazo.lepcostarica_com import config

logger = logging.getLogger(config.PROJECT_NAME)
_ = MessageFactory('ps.diazo.lepcostarica_com')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
