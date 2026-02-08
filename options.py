from picard.collection import Collection, user_collections
from picard.plugin3.api import OptionsPage, PluginApi

from .ui_add_to_collection_options import Ui_AddToCollectionOptions

COLLECTION_ID = "add_to_collection_id"


class AddToCollectionOptionsPage(OptionsPage):
    NAME = "add-to-collection"
    TITLE = "Add to Collection"

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.ui = Ui_AddToCollectionOptions()
        self.ui.setupUi(self, self.api)

    def load(self) -> None:
        self.set_collection_name(self.api.plugin_config[COLLECTION_ID] or "")

    def save(self) -> None:
        self.api.plugin_config[COLLECTION_ID] = self.ui.collection_name.currentData()

    def set_collection_name(self, value: str) -> None:
        self.ui.collection_name.clear()
        if len(user_collections) == 0:
            self.ui.set_error(
                self.api.tr(
                    "no.collections",
                    "No collections found. If you are not logged in, log in and restart Picard",
                )
            )
        else:
            self.ui.set_error("")
        collection: Collection
        for collection in sorted(user_collections.values(), key=lambda c: c.name.lower()):
            self.ui.collection_name.addItem(collection.name, collection.id)
        idx = self.ui.collection_name.findData(value)
        if idx != -1:
            self.ui.collection_name.setCurrentIndex(idx)


def register_options(api: PluginApi) -> None:
    api.register_options_page(AddToCollectionOptionsPage)
    api.plugin_config.register_option(COLLECTION_ID, default="")
