from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",
    version="0.1",
    description="A simple math quiz game with functions for generating random problems.",
    author="Aadil Ranesh",
    author_email="aadilranesh@outlook.com",
    packages=find_packages(include=["math_quiz"]),  # Specifies to include only the math_quiz package
    install_requires=[],  # Dependencies from requirements.txt
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
