
from setuptools import setup, find_packages

setup(name="da_plugin",
	version="0.1",
	description="da-plugin package",
	url="https://github.com/fumiya-kubota/da-plugin",
	packages=find_packages(),
    data_files=[('da_plugin/js', ['index.js']),
                ('da_plugin/js/components', ['PluginComponent.js'])]
)
