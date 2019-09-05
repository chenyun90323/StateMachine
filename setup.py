#from pip.req import parse_requirements 这样的话如果pip版本较高会报错
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)

setup(
    name='statemachine',     #mod名
    version="0.1.0",
    description='状态机模型',
    packages=find_packages(exclude=[]),
    author='chenyun',
    author_email='chenyun_1020@qq.com',
    # license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/chenyun90323/StateMachine',
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
    ],
)