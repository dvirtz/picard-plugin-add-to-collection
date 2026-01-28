from picard.plugin3.api import PluginApi

from .options import register_options
from .post_save_processor import register_processor


def enable(api: PluginApi):
    register_options(api)
    register_processor(api)
