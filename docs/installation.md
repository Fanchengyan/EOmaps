(installation)=
# 🐛 Installation

```{contents} Contents:
:local:
:depth: 1
```

The following sections provide information how to install **EOmaps**.

- A quick tutorial on how to **get started from scratch** is available here: {ref}`quickstart_guide`
- More details on how to **configure your favorite IDE** to get the most out of **EOmaps** can be found in the {ref}`faq` section {ref}`configuring_the_editor`.
- If you want to know how to setup **EOmaps** for development, have a look at the {ref}`contribute`


## Installation with ``conda`` or ``mamba``

EOmaps is available on [conda-forge](https://anaconda.org/conda-forge/eomaps) and can be installed via:

```
conda install -c conda-forge eomaps
```

This will install all required and optional dependencies.


:::{dropdown} Greatly speed up the installation!
:color: info
:icon: info
:open:
:margin: 3

Since the dependencies of EOmaps can be demanding to solve for ``conda``, it is **highly recommended**
that you use [mamba](https://github.com/mamba-org/mamba) to install EOmaps in a conda-environment!

[mamba](https://github.com/mamba-org/mamba) is a reimplementation of the conda package manager in C++, capable of solving environments a lot faster.

The recommended way to get started is to use [miniforge](https://github.com/conda-forge/miniforge), a minimalistic installer
that provides both ``conda`` and ``mamba``, pre-configured to use the ``conda-forge`` channel by default.
For other options, checkout the [mamba-docs](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)

Once ``mamba`` is installed, you just need to replace the term ``conda`` with ``mamba`` and you're good to go!

```
mamba install -c conda-forge eomaps
```

:::


## Installation with ``pip``


EOmaps is also available on [pypi](https://pypi.org/project/eomaps/).

To install EOmaps with a **minimal set of dependencies**, use:

```
pip install eomaps
```

### Optional dependencies


Some features ({ref}`webmap_layers`, {ref}`companion_widget`, etc.) require additional dependencies.
To use them you have to install the required dependency-groups:

To get **all features of EOmaps**, you can use one of:

- ``pip install eomaps[all]`` Install **ALL** requuired and optional dependencies
- ``pip install eomaps[all_nogui]`` Same as ``all`` but without installing the ``Qt`` GUI framework


In addition, you can use the following dependency-groups to activate only selected features:

- ``pip install eomaps[wms]`` Add dependencies required to use {ref}`WebMap services <webmap_layers>`
- ``pip install eomaps[gui]`` Add dependencies for ``Qt`` GUI framework (and the {ref}`CompanionWidget <companion_widget>`)
- ``pip install eomaps[io]`` Add support for ``pandas``, ``xarray``, ``geopandas`` and ``rioxarray``
- ``pip install eomaps[shade]`` Add capabilities to visualize extremely large datasets (via ``datashader``)
- ``pip install eomaps[classify]`` Add support for ``mapclassify`` to classify datasets

It is also possible to combine dependency-groups, e.g.: ``pip install eomaps[wms, gui]``.

A full list of all associated packages can be found in {ref}`setup_a_dev_env` or in the ``pyproject.toml`` file.
