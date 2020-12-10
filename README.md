# [MIRACLE](https://github.com/scarv/miracle): back-end intrastructure

<!--- -------------------------------------------------------------------- --->

*Acting as a component part of the wider
[SCARV](https://www.scarv.org)
project,
MIRACLE captures a range of components that relate to the study of 
micro-architectural side-channel leakage, i.e., leakage that stems
from micro-architectural behaviour.  Specifically, there are three
main components, namely
a suite of software kernels, specifically constructed to assess
whether or not a given form of leakage is evident;
a framework for executing such kernels and acquiring associated
data sets, e.g., traces of power consumption;
and
a framework for analysing such data sets, and then presenting 
the results (via a web-based front-end).*

<!--- -------------------------------------------------------------------- --->

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

<!--- -------------------------------------------------------------------- --->

## Acknowledgements

This work has been supported in part
by EPSRC via grant
[EP/R012288/1](https://gow.epsrc.ukri.org/NGBOViewGrant.aspx?GrantRef=EP/R012288/1) (under the [RISE](http://www.ukrise.org) programme).

<!--- -------------------------------------------------------------------- --->
