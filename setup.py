from setuptools import setup, find_packages
setup(
    name="linkparser",
    version="1.0",
    description="A Simple Python Package to Extract All Links from a Target Domain or URL.",
    author="Gaurav Raj",
    url="https://github.com/thehackersbrain/linkparser",
    author_email="techw803@gmail.com",
    license='MIT',
    keywords=['linkparser', 'thehackersbrain',
              'hacking', 'web scraping', 'python', 'python3'],
    classifiers=[
        'Development Status :: 1 - Intial Build',
        'Intended Audience :: Hackers',
        'Programming Language :: Python :: 3',
        'Operating System :: Linux :: Arch Linux',
        'Operating System :: Linux :: Kali Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X'
    ],
    packages=find_packages(),
    install_requires=['requests', 'rich', 'pyfiglet', 'bs4'],
    entry_points={
        'console_scripts': ['linkparser = linkparser.linkparser:main']
    },

    zip_safe=False,
)
