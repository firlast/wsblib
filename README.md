# WSBLib

![BADGE](https://img.shields.io/static/v1?label=status&message=stable&color=orange)
![BADGE](https://img.shields.io/static/v1?label=license&message=BSD%203-Clause&color=blue)

Web Server Base Library (WSBLib), a library that serves as a basis for creating other web server frameworks in Python. The goal is to be simple, fast and secure.

To create server frameworks, you need to use this library and the [HTTPPyParser](https://github.com/jaedsonpys/http-pyparser) library to get data from the request, as it is your framework that will manage the entire request cycle, the `WSBLib` library just makes it easier for you.

- [Usage Examples](https://github.com/firlast/wsblib/tree/master/examples)
- [Official Documentation](https://firlast.github.io/wsblib)
- [PyPI Project](https://pypi.org/project/wsblib)

## Installation

You can use the PIP package manager to install `WSBLib`:

```
pip install wsblib
```

Or install manually, cloning the repository and running the command below:

```
git clone git@github.com:firlast/wsblib.git
cd wsblib/
python3 setup.py install
```

## License

```text
BSD 3-Clause
Copyright (c) 2022, Jaedson Silva
All rights reserved.
```

This project use the `BSD 3-Clause` license. Please [see LICENSE file](https://github.com/firlast/wsblib/blob/master/LICENSE) to **more information** about license.