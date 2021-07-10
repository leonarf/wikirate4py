import re
from setuptools import setup, find_packages

VERSION_FILE = "wikirate4py/__init__.py"
with open(VERSION_FILE) as version_file:
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                      version_file.read(), re.MULTILINE)

if match:
    version = match.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")

tests_require = [
    "mock",
    "nose",
    "vcrpy",
    "html2text",
    "python-dotenv"
]
setup(name='wikirate4py',
      version=version,
      description='WikiRate for Python!',
      url='github.com/wikirate/wikirate4py',
      author='Vasiliki Gkatziaki',
      author_email='vasso@wikirate.org',
      license='GPL-3.0',
      packages=find_packages(exclude=["tests", "examples"]),
      install_requires=[
          "requests",
          "html2text"
      ],
      project_urls={
          "Documentation": "https://wikirate4py.readthedocs.io",
          "Issue Tracker": "https://github.com/wikirate4py/wikirate4py/issues",
          "Source Code": "https://github.com/wikirate4py/wikirate4py",
      },
      extras_require={
          "test": tests_require,
      },
      test_suite="nose.collector",
      keywords="wikirate library",
      python_requires=">=3.6",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Libraries",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3 :: Only",
      ],
      zip_safe=True)
