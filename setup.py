import os
import sys
import setuptools
import subprocess


# @TODO: Figure out a way to check for this
is_installed_from_pypi = False



def remove_requirements(requirements, name, replace=''):
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
    requirements = remove_requirements(requirements,'torch')
    requirements = remove_requirements(requirements,'torchvision')
    try:
        subprocess.call(['pip','install','torch===1.2.0', '-f', 'https://download.pytorch.org/whl/torch_stable.html'])
        subprocess.call(['pip','install','torchvision===0.4'])

        print('Successfully installed pytorch and torchvision!')
    except:
        print('Failed to install pytroch, please install pytroch and torchvision manually be following the simple instructions over at: https://pytorch.org/get-started/locally/')


    #requirements.append('cwrap')

setuptools.setup(name='testypy',
      version='1.1.1',
      description='The testpypy awesome module',
      url='https://github.com/ZoranPandovski/testypy',
      author='Zoran Pan',
      author_email='zoran.pandovski@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      package_data={'project': ['requirements.txt']},
      install_requires=requirements,
      zip_safe=False)