# :warning: Testypy

:beginner: :construction: Simple repository for testing TestPyPi publishings. :construction: :beginner:

## Release new version to TestPyPI
```
python setup.py sdist
twine upload -r pypitest dist/testypy-0.1.2.tar.gz
```

## Install latest version

```
pip install -i https://test.pypi.org/simple/ testypy
```