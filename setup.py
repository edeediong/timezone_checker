from setuptools import setup, find_packages

setup(
    name="timechecker",
    version="0.0.5",
    author="Edidiong Etuk",
    author_email="edeediong@gmail.com",
    url="https://bit.ly/edeediong-resume",
    description="An aplication that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["timechecker = src.main:main"]},
)
