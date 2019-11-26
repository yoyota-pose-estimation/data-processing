from setuptools import setup, find_packages

setup(
    name="pose-estimation-data-processing",
    install_requires=["tensorflow>=2.0.0"],
    entry_points={"console_scripts": ["pair_image=pair_image.cli:main"]},
)
