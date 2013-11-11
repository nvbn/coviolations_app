from setuptools import setup, find_packages


version = '0.19'

setup(
    name='coviolations_app',
    version=version,
    description="coviolations.io app",
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ],
    keywords='',
    author='Vladimir Iakovlev',
    author_email='nvbn.rm@gmail.com',
    url='http://coviolations.io',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyyaml',
        'requests',
        'sh',
    ],
    entry_points={
        'console_scripts': [
            'covio=coviolations_app.covio:main',
        ]
    },
)
