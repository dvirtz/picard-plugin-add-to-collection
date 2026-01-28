from typing import Optional

from picard import log
from picard.collection import Collection, user_collections
from picard.file import File
from picard.plugin3.api import PluginApi

from .options import COLLECTION_ID


def post_save_processor(api: PluginApi, file: File) -> None:
    collection_id = api.plugin_config[COLLECTION_ID]
    if not collection_id:
        log.error("cannot find collection ID setting")
        return
    collection: Optional[Collection] = user_collections.get(collection_id)
    if not collection:
        log.error(f"cannot find collection with id {collection_id}")
        return
    release_id = file.metadata["musicbrainz_albumid"]
    if release_id and release_id not in collection.releases:
        log.debug("Adding release %r to %r", release_id, collection.name)
        collection.add_releases(set([release_id]), callback=lambda: None)


def register_processor(api: PluginApi) -> None:
    api.register_file_post_save_processor(post_save_processor)
