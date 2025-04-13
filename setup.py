from setuptools import setup, find_packages

setup(
    name='linwatcher',
    version='0.1.0',
    description='A simple CLI tool to display Linux system information',
    author='Frank',
    author_email='frank@example.com',
    url='https://github.com/spiewak7/linwatcher',
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
    entry_points={
        'console_scripts': [
            'linwatcher=linwatcher.cli:display_system_info'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
)
