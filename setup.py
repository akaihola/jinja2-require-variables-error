from setuptools import setup

setup(
    name='jinja2-require-variables-error',
    version='0.0.1',
    description=('A custom Jinja tag `require`: '
                 'raise an exception if any of the mentioned variables '
                 'is missing'),
    author='Antti Kaihola',
    author_email='antti+github@kaihola.fi',
    url='https://github.com/akaihola/jinja2-require-variables-error',
    license='MIT',
    packages=['jinja2_ext_require_variables_error'],
    install_requires=['Jinja2>=2.4'],
    classifiers=[])
