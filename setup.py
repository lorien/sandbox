from setuptools import setup

setup(
    name="sandbox",
    version="0.0.2",
    packages=["sandbox"],
    include_package_data=True,
    extras_require={
        "pyquery": [
            "six",
        ]
    },
)
