from setuptools import setup, find_packages

setup(
    name="pair-image",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=["tensorflow>=2.0.0", "kubernetes>=10.0.1"],
    entry_points={"console_scripts": ["pair_image=pair_image.cli:main"]},
)
