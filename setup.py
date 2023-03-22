#!/usr/bin/env python3

#  Copyright 2023 G-Research
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from setuptools import setup

jar_version = '2.5.0-3.3-SNAPSHOT'
scala_version = '2.13.8'
scala_compat_version = '.'.join(scala_version.split('.')[:2])
spark_compat_version = jar_version.split('-')[1]
version = jar_version.split('-')[0] + ('.dev0' if jar_version.endswith('-SNAPSHOT') else '')

setup(
    name="pyspark-extension-" + spark_compat_version,
    version=version,
    description="PySpark Extension",
    long_description="A library that provides useful extensions to Apache Spark.",
    long_description_content_type="text/markdown",
    author="Enrico Minack",
    author_email="github@enrico.minack.dev",
    url="https://github.com/G-Research/spark-extension",
    install_requires=[f"pyspark>={spark_compat_version},<4", "py4j"],
    packages=[
        "gresearch",
        "gresearch.spark",
        "gresearch.spark.diff",
        "gresearch.spark.diff.comparator",
        "pyspark.jars",
    ],
    include_package_data=False,
    package_dir={
        "": "python",
    },
    package_data={
        "pyspark.jars": [f"*_{scala_compat_version}-{jar_version}.jar"],
    },
    license="http://www.apache.org/licenses/LICENSE-2.0.html",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Typing :: Typed",
    ],
)