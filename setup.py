from setuptools import setup, find_packages

setup(
    name="karasu_scraper",
    version="1.0",
    description="Karasu is a command-line interface for scraping webtoons from different websites",
    author="KKogaa",
    author_email="johndoe@example.com",
    url="https://github.com/KKogaa/karasu-scraper",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pandas",
    ],
    entry_points={
        "console_scripts": [
            "karasu=cli:main",
        ],
    },
)
