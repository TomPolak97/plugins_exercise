from dummy_api_plugin import DummyApiPlugin

"""
This class is responsible for creating new plugins.
Every new plugin should be created in this class.
"""


def create_plugin(plugin_type, app_key):
    if plugin_type == 'dummy_api':
        return DummyApiPlugin(app_key)
