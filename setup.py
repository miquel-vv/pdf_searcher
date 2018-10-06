import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf_text_searcher",
    version="0.0.6",
    author="Miquel Vande Velde",
    author_email="miquel.vandevelde@gmail.com",
    description="CLI Tool to search words in multiple PDFs within a directory.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miquel-vv/pdf_searcher",
    entry_points = {
        'console_scripts': ['pdf-text-searcher=pdf_text_searcher.search_directory:main']
        },
    install_requires = ['PyPDF2'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)