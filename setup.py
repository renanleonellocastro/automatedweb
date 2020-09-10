import setuptools

#README as long_descriptions
with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name='automatedweb',
    version='1.0.1',
    url='https://github.com/renanleonellocastro/automatedweb.git',
    license='MIT License',
    author='Renan Leonello Castro',
    author_email='renanleonellocastro@gmail.com',
    keywords='automatedweb web automated post get requests rest restfull',
    description='A tool to make it easy to communicate with web systems writting and reading data from them',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    py_modules=["automatedweb"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.22.0",
        "pyquery>=1.4.0",
        "json5>=0.8.5",
        "urllib3>=1.25.10",
    ],
)
