
# Miracle: DB

*The trace database component of the 
[SCARV](https://github.com/scarv) Miracle project.*

---

## Overview

This tool is developed as part of the SCARV Miracle project.
It is used to store large numbers of compressed trace datasets
and subsequent analyses.
It allows results to be organised by the device and experiment
pairs which generated them.

This repository is not designed to be used as a standalone tool, but
as a sub-component of the
[miracle-experiments](https://github.com/scarv/miracle-experiments)
repository.

## Getting Started

There is a simple command line tool which can be used to create a
new leakage database, and perform basic maintainance.

```sh
$> ./cli.py --help

usage: cli.py [-h] [--backend {sqlite}] [--verbose] [--log LOG]
              dbpath
              {list,insert-targets,insert-experiment,init,show,remove,plot}
              ...

positional arguments:
  dbpath                File-path of the database

optional arguments:
  -h, --help            show this help message and exit
  --backend {sqlite}    Database Backend To Use
  --verbose, -v         Turn on verbose logging.
  --log LOG             Filepath to log too.

Sub-commands:
  {list,insert-targets,insert-experiment,init,show,remove,plot}
    list                list entries in the database
    insert-targets      Insert a new target into the database
    insert-experiment   Add a new experiment to the database. If the
                        experiment already exists, it is not updated.
    init                Create a new database file
    show                Show information on an object in the database
    remove              Remove an entity (and possible sub-entities) from the
                        database.
    plot                Tools for creating simple plots from trace blobs
```


## Acknowledgements

This work has been supported in part by EPSRC via grant 
[EP/R012288/1](http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/R012288/1), under the [RISE](http://www.ukrise.org) programme.

