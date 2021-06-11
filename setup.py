import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="transf",
    version="0.0.1",
    author="tgashwinkumar",
    author_email="tgashwinkumar@gmail.com",
    description="Symbolic solver for Laplace transforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tgashwinkumar/transf",
    project_urls={
        "Bug Tracker": "https://github.com/tgashwinkumar/transf/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
