"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime is an original proprietary software system.
"""

from setuptools import setup, find_packages

setup(
    name="thalos-prime",
    version="1.0.0",
    description="Thalos Prime - Deterministic System Framework",
    author="Tony Ray Macier III",
    license="Proprietary",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "thalos=main:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3.12",
    ],
)
