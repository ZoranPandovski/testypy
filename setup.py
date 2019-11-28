import os
import sys
import setuptools
import subprocess


# @TODO: Figure out a way to check for this
is_installed_from_pypi = False


def remove_requirements(requirements, name, replace=None):
    new_requirements = []
    for requirement in requirements:
        if requirement.split(' ')[0] != name:
            new_requirements.append(requirement)
        elif replace is not None:
            new_requirements.append(replace)
    return new_requirements

sys_platform = sys.platform

with open('requirements.txt') as req_file:
    requirements = [req.strip() for req in req_file.read().splitlines()]

# Linux specific requirements
if sys_platform == 'linux' or sys_platform.startswith('linux'):
    pass
    #requirements = remove_requirements(requirements,'torch',replace='torch >= 1.1.0')


# OSX specific requirements
elif sys_platform == 'darwin':
    pass
    #requirements = remove_requirements(requirements,'torch',replace='torch >= 1.1.0.post2')

# Windows specific requirements
elif sys_platform in ['win32','cygwin','windows']:
    if is_installed_from_pypi:
        requirements = remove_requirements(requirements,'torch')
        requirements = remove_requirements(requirements,'torchvision')

   

    requirements.append('cwrap')

# For stuff like freebsd
else:
    print('\n\n====================\n\nError, platform {sys_platform} not recognized, proceeding to install anyway, but testypy might not work properly !\n\n====================\n\n')

if is_installed_from_pypi and (sys_platform in ['win32','cygwin','windows']):
    try:
        subprocess.call(['pip','install','torch===1.3.1 torchvision===0.4.2 -f https://download.pytorch.org/whl/torch_stable.html'])
        print('Successfully installed pytorch !')
    except:
        print('Failed to install pytroch, please install pytroch and torchvision manually be following the simple instructions over at: https://pytorch.org/get-started/locally/')

  


setuptools.setup(name='testypy',
      version='0.9.5',
      description='The testpypy awesome module',
      url='https://github.com/ZoranPandovski/testypy',
      author='Zoran Pan',
      author_email='zoran.pandovski@gmail.com',
      license='MIT',
      packages=['testypy'],
      package_data={'project': ['requirements.txt']},
      install_requires=requirements,
      zip_safe=False)