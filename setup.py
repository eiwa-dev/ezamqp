from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='ezamqp',
      version='0.1.0',
      description='Remote Procedure Calls for AMQP using aioamqp',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends',
        'Operating System :: OS Independent'
      ],
      keywords='amqp rpc asyncio',
      url='https://github.com/jcarrano-eiwa/ezamqp',
      author='Juan I Carrano <jc@eiwa.ag>',
      author_email='jc@eiwa.ag',
      license='MIT',
      py_modules=['ezamqp'],
      install_requires=[
          'aioamqp'
      ],
      include_package_data=True,
      zip_safe=True
    )
