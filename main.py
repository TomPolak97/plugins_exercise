import pluginFactory


def main():

    # Creating dummy_api plugin using the plugin factory.
    plugin_type = 'dummy_api'
    plugin_optional_args = {...}
    plugin = pluginFactory.create_plugin(plugin_type, **plugin_optional_args)
    plugin.run()


if __name__ == '__main__':
    main()
