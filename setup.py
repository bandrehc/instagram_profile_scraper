from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="instagram-profile-scraper",
    version="1.0.0",
    author="Bruno Herrera Criollo",
    author_email="bandreherrerac@gmail.com",
    description="A tool to extract metadata from Instagram profiles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bandrehc/instagram_profile_scraper.git",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "instagram-scraper=instagram_scraper:main",
        ],
    },
)