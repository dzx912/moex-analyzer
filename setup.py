import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="moex-analyzer",
    version="0.0.1",
    author="Anton Lenok",
    author_email="dzx912@gmail.com",
    description="A simple engine for analyzing Moscow Exchange securities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dzx912/moex-analyzer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="moex",
    install_requires=["numpy", "pandas", "requests", "matplotlib"],
)
