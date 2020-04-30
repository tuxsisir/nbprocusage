import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbprocusage",
    version="0.1.1",
    author="Sisir Ghimire Chettri",
    author_email="samratsisir294@gmail.com",
    description="Dead simple extension of jupyter notebook to overview process usage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuxsisir/nbprocusage",
    packages=setuptools.find_packages(),
    install_requires=["notebook>=5.6.0", "psutil>=5.7.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        (
            "share/jupyter/nbextensions/nbprocusage",
            ["nbprocusage/static/main.js"]
        ),
        # like `jupyter nbextension enable --sys-prefix`
        (
            "etc/jupyter/nbconfig/notebook.d",
            ["nbprocusage/etc/nbextension.json"]
        ),
        # like `jupyter serverextension enable --sys-prefix`
        (
            "etc/jupyter/jupyter_notebook_config.d",
            ["nbprocusage/etc/serverextension.json"]
        )
    ],
    include_package_data=True,
    zip_safe=False
)
