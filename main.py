from plugins_exercise import pluginFactory
from plugins_exercise.pluginFactory import create_plugin

def main():

    # Creating dummy_api plugin using the plugin factory.
    plugin_type = 'dummy_api'
    app_key = '6429a239efb0fd3067bbd50f'
    plugin = pluginFactory.create_plugin(plugin_type, app_key)
    plugin.run()


if __name__ == '__main__':
    main()
