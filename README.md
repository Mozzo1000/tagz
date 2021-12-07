
<div align="center">
<img style='vertical-align:middle;' src='assets/icon.png' width="70">
<div style='vertical-align:middle; display:inline;'>
<strong style="font-size:60px">Tagz</strong>
</div>
</div>

 <p align="center">A file tagger and organizer</p>

<div align="center">

   ![license apache 2.0](https://img.shields.io/badge/license-Apache%202.0-brightgreen)
</div>

# About
Tagz allows you to tag any and all files on your computer to be able to find them easier later on when you need them.

# Installation
There are currently no instructions or files available for you to install tagz. At the moment you need to build from source.

# Packaging application
Pyinstaller
`pyinstaller gui_client.spec`

# Development
## Dependencies
* Python 3 (tested with 3.9.4)
* PyQt5

## Documentation dependencies
* [mkdocs](https://github.com/mkdocs/mkdocs)
* [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
* [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
## Deploying documentation
* Run `mkdocs gh-deploy`
## Running documentation server locally
* Run `mkdocs serve` from same directory as `mkdocs.yml`

## Folder structure
| Folder        | Description                 |
| ------------- |:---------------------------:|
| assets        | images, icons etc           |
| backend       | database                    |
| docs          | documentation, github pages |
| gui           | code for the GUI            |
| lib           | shared code                 |

# Documentation
Documentation can be found [here](https://mozzo1000.github.io/tagz)

# License
`tagz` is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.