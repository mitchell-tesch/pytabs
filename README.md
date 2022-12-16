<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mitchell-tesch/pytabs">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">pyTABS</h3>

  <p align="center">
    A python wrapper for CSi ETABS .NET API
    <br />
    <a href="temp"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mitchell-tesch/pytabs/issues">Report Bug</a>
    ·
    <a href="https://github.com/mitchell-tesch/pytabs/issues">Request Feature</a>
  </p>
</div>


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