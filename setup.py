from setuptools import setup

setup(
    name='qgbd',
    version='0.1',
    description='quick git branch deleter',
    author='Spencer Hawkins',
    url='https://github.com/shawkinsl/qgbd',
    scripts=['qgbd.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Git Usage'
    ],
    license='MIT',
    install_requires=[
        'inquirer>=2.6.3'
    ],
    entry_points={
        'console_scripts': [
            'qgbd=qgbd:main'
        ]
    }
)