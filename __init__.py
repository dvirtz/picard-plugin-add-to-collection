from picard.plugins.add_to_collection.manifest import *  # noqa: F403
from picard.plugins.add_to_collection import options, post_save_processor  # noqa: F403

options.register_options()
post_save_processor.register_processor()
