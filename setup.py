from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    required = fh.read().splitlines()

setup(
    name="datacamp-downloader-michael",
        version="4.0.0",
    author="Michael Matta",
    author_email="111490505+Michael-Matta1@users.noreply.github.com",
    description="Download your completed courses and their metadata from Datacamp easily!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Michael-Matta1/datacamp-downloader",
    project_urls={
        "Bug Tracker": "https://github.com/Michael-Matta1/datacamp-downloader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=required,
    setup_requires=["setuptools-git"],
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["datacamp=datacamp_downloader.downloader:app"]},
)
