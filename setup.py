#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# normal setuptool inputs
setuptools.setup(
    name='pollination-leed-daylight-option-two',                                     # will be used for package name unless it is overwritten using __queenbee__ info.
    author='pollination',                                                 # the owner account for this package - required if pushed to Pollination
    author_email='info@pollination.solutions',
    packages=setuptools.find_namespace_packages(                            # required - that's how pollination find the package
        include=['pollination.*'], exclude=['tests', '.github']
    ),
    install_requires=requirements,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    url='https://github.com/pollination/leed-daylight-option-two',                   # will be translated to home
    project_urls={
        'icon': 'https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_components/honeybee/png/leeddaylight.png',
        'docker': 'https://hub.docker.com/r/ladybugtools/honeybee-radiance'
    },
    description='Evaluate LEED daylight credits using the point-in-time illuminance '
    'method (Option 2).',                  # will be used as package description
    long_description=long_description,                                      # will be translated to ReadMe content on Pollination
    long_description_content_type="text/markdown",
    maintainer='chris, pollination',                                   # Package maintainers. For multiple maintainers use comma
    maintainer_email='chris@ladybug.tools, info@pollination.solutions',
    keywords='honeybee, radiance, leed, daylight, illuminance',  # will be used as keywords
    license='PolyForm Shield License 1.0.0, https://polyformproject.org/wp-content/uploads/2020/06/PolyForm-Shield-1.0.0.txt',  # the license link should be separated by a comma
    zip_safe=False
)
