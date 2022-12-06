# pyTABS
## Description
A Python wrapper for CSi ETABS .NET API - a simple yet robust Python interface to the ETABS .NET API. Not affiliated with Computer and Structures Inc.


## Installation
*pyTABS* can be installed through the Python package manager:
```
$ pip install pytabs
```


## Requirements
 - Python 3.8+
 - pythonnet


## Usage
Documentation is currently work in progress.

_For examples, please refer to the [examples](./examples/)._


## Licence
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.


## Contibutors
Contributors welcome.

IntelliSense of the ETABSv1 namespace (ETABSv1.dll) can be achieved via the included stub file. This stub file has been generated using [IronPython Stubs](https://github.com/gtalarico/ironpython-stubs) by [gtalarico](https://github.com/gtalarico).

To make use of this stub file in VS Code add the following to your settings.json:
```json
    "python.autoComplete.extraPaths": ["<path_to_stub.min>"],
    "python.analysis.extraPaths": ["<path_to_stub.min>"]
```