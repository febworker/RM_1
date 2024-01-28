from setuptools import setup, find_namespace_packages

setup(name='remind_me',
    version='1.0.0',
    description='contact_assistant, sort_direcrory_function',
    author='Svitlana Shulha, Roman Gryshko, Oksana Horishna',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['contact=remind_me.main:run']}
    ) 
