from setuptools import setup

setup(
        name = 'covidcli',
        version = '0.1',
        install_requires = ['Click', 'COVID19Py', 'plotext', 'requests',],
        py_modules = ['covidcli'],
        entry_points = '''
        [console_scripts]
        hello=covidcli:hello
        '''
)
