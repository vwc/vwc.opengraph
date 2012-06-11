from plone.app.registry.browser import controlpanel

from vwc.opengraph.interfaces import IOpenGraphSettings
from vwc.opengraph import MessageFactory as _


class OpenGraphSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IOpenGraphSettings
    label = _(u"OpenGraph settings")
    description = _(u"""""")

    def updateFields(self):
        super(OpenGraphSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(OpenGraphSettingsEditForm, self).updateWidgets()


class OpenGraphSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = OpenGraphSettingsEditForm
