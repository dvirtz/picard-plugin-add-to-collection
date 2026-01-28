from picard.i18n import gettext as _
from picard.plugin3.api import OptionsPage, PluginApi
from PyQt6 import QtCore, QtWidgets


class Ui_AddToCollectionOptions(object):
    def setupUi(self, optionsPage: OptionsPage, api: PluginApi):
        optionsPage.setObjectName("AddToCollectionOptions")
        optionsPage.resize(472, 215)
        self.verticalLayout = QtWidgets.QVBoxLayout(optionsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.collection_label = QtWidgets.QLabel(optionsPage)
        self.collection_label.setObjectName("collection_label")
        self.verticalLayout.addWidget(self.collection_label)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.collection_name = QtWidgets.QComboBox(optionsPage)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collection_name.sizePolicy().hasHeightForWidth())
        self.collection_name.setSizePolicy(sizePolicy)
        self.collection_name.setEditable(False)
        self.collection_name.setObjectName("collection_name")
        self.verticalLayout.addWidget(self.collection_name)
        self.error_message = QtWidgets.QLabel(optionsPage)
        self.error_message.setObjectName("error_message")
        self.error_message.setVisible(False)
        self.verticalLayout.addWidget(self.error_message)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(optionsPage, api)
        QtCore.QMetaObject.connectSlotsByName(optionsPage)

    def set_error(self, message: str | None) -> None:
        """Set the error message. If message is None or empty, hide the error."""
        if message:
            self.error_message.setText(message)
            self.error_message.setVisible(True)
        else:
            self.error_message.setText("")
            self.error_message.setVisible(False)

    def retranslateUi(self, optionsPage: OptionsPage, api: PluginApi):
        optionsPage.setWindowTitle(_("Form"))
        self.collection_label.setText(api.tr("collection.label", "Collection to add releases to:"))
