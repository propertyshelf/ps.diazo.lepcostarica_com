# -*- coding: utf-8 -*-
"""Test Layer for ps.diazo.lepcostarica_com."""

# zope imports
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
    applyProfile,
)
from plone.testing import (
    Layer,
    z2,
)


class PsDiazoLepcostaricaComLayer(PloneSandboxLayer):
    """Custom Test Layer for ps.diazo.lepcostarica_com."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import ps.diazo.lepcostarica_com
        self.loadZCML(package=ps.diazo.lepcostarica_com)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ps.diazo.lepcostarica_com:default')


PS_DIAZO_LEPCOSTARICA_COM_FIXTURE = PsDiazoLepcostaricaComLayer()


PS_DIAZO_LEPCOSTARICA_COM_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PS_DIAZO_LEPCOSTARICA_COM_FIXTURE,),
    name='PsDiazoLepcostaricaComLayer:IntegrationTesting'
)


PS_DIAZO_LEPCOSTARICA_COM_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PS_DIAZO_LEPCOSTARICA_COM_FIXTURE,),
    name='PsDiazoLepcostaricaComLayer:FunctionalTesting'
)


PS_DIAZO_LEPCOSTARICA_COM_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PS_DIAZO_LEPCOSTARICA_COM_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PsDiazoLepcostaricaComLayer:AcceptanceTesting'
)


ROBOT_TESTING = Layer(name='ps.diazo.lepcostarica_com:Robot')
