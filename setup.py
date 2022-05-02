import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='proxyscraperservicewrapper',
    version='0.0.2',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Wrapper for Proxy Scraper Service',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['proxyscraperservicewrapper'],
    install_requires=[
        "requests",
        "cryptocode",
        "compressortoolbox @ git+https://github.com/AlexQ0807/compressortoolbox.git"
    ],
)