import setuptools




def setup_writer(project_name,version,author):
   return f"""with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
    name="{project_name}",
    version="{version}",
    author="{author}",
    author_email="TODO:author@example.com",
    description="TODO:A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TODO: Enter URL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',    
    )"""