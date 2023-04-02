from dummy_api_plugin import DummyApiPlugin

"""
This class is responsible for creating new plugins.
Every new plugin should be created in this class.
"""


class PluginFactory:
    @staticmethod
    def create_plugin(plugin_type, **kwargs):
        if plugin_type == 'dummy_api':
            return DummyApiPlugin(kwargs)
