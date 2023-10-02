import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='proxyscraperservicewrapper',
    version='1.2.3',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Wrapper for Proxy Scraper Service',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['proxyscraperservicewrapper', 'proxyscraperservicewrapper.services'],
    install_requires=[
        "requests",
    ],
)