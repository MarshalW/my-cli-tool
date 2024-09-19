from setuptools import setup, find_packages

setup(
    name="my-cli-tool",            # 你的工具名称，发布到PyPI时的名称
    version="0.1.0",               # 版本号
    packages=find_packages(),      # 自动发现并包含所有包
    install_requires=[],           # 项目的依赖，可以填入例如 ['click', 'requests'] 等
    entry_points={
        'console_scripts': [
            'mycli=my_cli_tool.cli:main',  # 创建 'mycli' 命令行命令, 指向 `cli.py` 的 `main` 函数
        ],
    },
    author="Marshal Wu",
    author_email="marshal.wu@gmail.com",
    description="A simple CLI tool",
    long_description=open('README.md').read(),  # 详细描述，通常来自README
    long_description_content_type="text/markdown",
    url="https://github.com/marshalw/my-cli-tool",  # 你的项目网址
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',  # 指定支持的 Python 版本
)
