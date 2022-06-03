
<p align="center">
    <a href=https://github.com/raphaelquast/EOmaps>
    <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/logo.png?raw=true" alt="EOmaps logo" width="55%">
    </a>
</p>

[![tests](https://github.com/raphaelquast/EOmaps/actions/workflows/testMaps.yml/badge.svg?branch=master)](https://github.com/raphaelquast/EOmaps/actions/workflows/testMaps.yml)
[![codecov](https://codecov.io/gh/raphaelquast/EOmaps/branch/dev/graph/badge.svg?token=25M85P7MJG)](https://codecov.io/gh/raphaelquast/EOmaps)
&nbsp; &nbsp; &nbsp;
[![pypi](https://img.shields.io/pypi/v/eomaps)](https://pypi.org/project/eomaps/)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/eomaps.svg)](https://anaconda.org/conda-forge/eomaps)
&nbsp; &nbsp; &nbsp;
[![Documentation Status](https://readthedocs.org/projects/eomaps/badge/?version=latest)](https://eomaps.readthedocs.io/en/latest/?badge=latest)
<a href="https://www.buymeacoffee.com/raphaelquast" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/yellow_img.png" alt="Buy Me A Coffee" align="right" style="height: 25px !important;" ></a>

<a href="https://zenodo.org/badge/latestdoi/410829039" target="_blank"><img src="https://zenodo.org/badge/410829039.svg" alt="DOI: 10.5281/zenodo.6459598" align="right" style="height: 20px !important;" ></a>

----

### A library to create interactive maps of geographical datasets.

<ul type="none">
  <li>🌍 EOmaps provides a simple and intuitive interface to visualize and interact with geographical datasets.</li>
  <ul type="none">
    <li>⬥ Data can be provided as 1D or 2D <code>lists</code>, <code>numpy-arrays</code>, <code>pandas.DataFrames</code></li>
    <li>  &nbsp; &nbsp; &nbsp; or directly from GeoTIFFs,  NetCDFs and csv-files.</li>
    <li>  &nbsp; &nbsp; &nbsp; ... usable also for large datasets with millions of datapoints!</li>
    <li>⬥ WebMap layers, annotations, markers can be added with a single line of code</li>
    <li>⬥ EOmaps is built on top of <code>matplotlib</code> and <code>cartopy</code> and integrates well <code>pandas</code> and <code>geopandas</code></li>
  </ul>
  <li>🌎 Quickly turn your maps into powerful interactive data-analysis widgets</li>
  <ul type="none">
    <li>⬥ use callback functions to interact with the data (or an underlying database) </li>
    <li>⬥ compare multiple data-layers, WebMaps etc.</li>
  </ul>
</ul>
<br/>

---

> ❗ update notice: [⚙ Port script from EOmaps v3.x to v4.x](https://eomaps.readthedocs.io/en/latest/FAQ.html#port-script-from-eomaps-v3-x-to-v4-x)

---


## 🔨 Installation

To install EOmaps (and all its dependencies) via the `conda` package-manager, simply use:
```python
conda install -c conda-forge eomaps
```
... to get a huge speedup, use `mamba` to solve the dependencies!
```python
conda install -c conda-forge mamba
mamba install -c conda-forge eomaps
```
For more information, have a look at the [installation instructions](https://eomaps.readthedocs.io/en/latest/general.html#installation) or checkout the quickstart guide [🚀 from 0 to EOmaps](https://eomaps.readthedocs.io/en/latest/FAQ.html#from-0-to-eomaps-a-quickstart-guide)!
<br/>

## 📖 Documentation

Make sure to have a look at the <a href=https://eomaps.readthedocs.io/en/latest><b>🌳 documentation 🌳</b></a> which provides a lot of <a href=https://eomaps.readthedocs.io/en/latest/EOmaps_examples.html><b>examples</b></a> on how to create awesome interactive maps (incl. source code)!

## ✔️ Citation
Did EOmaps help in your research?  
Consider supporting the development and add a citation to your publication!

[![https://doi.org/10.5281/zenodo.6459598](https://zenodo.org/badge/410829039.svg)](https://zenodo.org/badge/latestdoi/410829039)


## 🚀 Contribute

Found a bug or got an idea for an interesting feature?  
Open an [issue](https://github.com/raphaelquast/EOmaps/issues) or start a [discussion](https://github.com/raphaelquast/EOmaps/discussions), and I'll see what I can do!  
(I'm of course also happy about actual pull requests on features and bug-fixes!)

---------------
<table>
  <tr>
    <td valign="center" style="width:50%">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/fig6.gif?raw=true" alt="EOmaps example 6">
      </td>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/minigifs/advanced_wms.gif?raw=true" alt="EOmaps example 2">
      </td>
  </tr>
  <tr>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/fig7.gif?raw=true" alt="EOmaps example 7">
      </td>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/fig2.gif?raw=true" alt="EOmaps example 8">
      </td>
  </tr>
  <tr>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/fig9.gif?raw=true" alt="EOmaps example 9">
    </td>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/fig4.gif?raw=true" alt="EOmaps example 4">
    </td>
  </tr>
  <tr>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/inset_maps.png?raw=true" alt="EOmaps inset-maps">
    </td>
    <td valign="center">
        <img src="https://github.com/raphaelquast/EOmaps/blob/dev/docs/_static/fig8.gif?raw=true" alt="EOmaps example 3">
    </td>
  </tr>
</table>



## 🌳 Basic usage

🛸 **Checkout the [documentation](https://eomaps.readthedocs.io/en/latest/api.html)!** 🛸

- A list of coordinates and values is all you need as input!
  - plots of large (>1M datapoints) irregularly sampled datasets are generated in a few seconds!
- Represent your data
  - as shapes with actual geographic dimensions (ellipses, rectangles, geodetic circles)
  - via Voroni diagrams and Delaunay triangulations to get interpolated contour-plots
  - via dynamic data-shading to speed up plots of extremely large datasets
- Re-project the data to any crs supported by <a href=https://scitools.org.uk/cartopy/docs/latest/reference/crs.html#coordinate-reference-systems-crs>cartopy</a>
- Quickly add features and additional layers to the plot
  - Markers, Annotations, WebMap Layers, NaturalEarth features, Scalebars, Compasses (or North-arrows) etc.
- Interact with the data via callback-functions.

```python
from eomaps import Maps

# initialize Maps object
m = Maps(crs=Maps.CRS.Orthographic())

# add basic map-features from NaturalEarth
m.add_feature.preset.coastline()
m.add_feature.cultural_50m.admin_0_countries(fc="none", ec="g")

# easily visualize both structured and unstructured datasets
m.set_data(data=[1, 2, 3, 4], x=[45, 46, 47, 42], y=[23, 24, 25, 26], crs=4326)
# set the shape you want to use to represent the data-points
m.set_shape.geod_circles(radius=10000) # (e.g. geodetic circles with 10km radius)
# (optionally) classify the data
m.set_classify_specs(scheme=Maps.CLASSIFIERS.Quantiles, k=5)
# plot the data
m.plot_map(cmap="viridis", vmin=2, vmax=4)
# add a colorbar with a colored histogram on top
m.add_colorbar(histbins=200)

# add a scalebar
m.add_scalebar()
# add a compass (or north-arrow)
m.add_compass()

# add imagery from a variety of open-access WebMap services
m.add_wms.OpenStreetMap.add_layer.default()

# use callback functions to interact with the map!
m.cb.pick.attach.annotate()

# use multiple layers to compare and analyze different datasets!
m3 = m.new_layer(layer="layer 2")
m3.add_feature.preset.ocean()

# attach a callback to peek on layer 1 if you click on the map
m.cb.click.attach.peek_layer(layer="layer 2", how=0.4)
# attach callbacks to switch between the layers with the keyboard
m.cb.keypress.attach.switch_layer(layer=0, key="0")
m.cb.keypress.attach.switch_layer(layer="layer 2", key="1")

# get a clickable widget to switch between the available plot-layers
m.util.layer_selector()

# add zoomed-in "inset-maps" to highlight areas on th map
m_inset = m.new_inset_map((10, 45))
m_inset.add_feature.preset.coastline(fc="g")

# ---- plot data directly from GeoTIFF / NetCDF or CSV files
m4 = m.new_layer_from_file.GeoTIFF(...)
m4 = m.new_layer_from_file.NetCDF(...)
m4 = m.new_layer_from_file.CSV(...)

```

----

## 🌼 Thanks to

- [Jakob Quast](https://quastquest.jimdofree.com/) for designing the nice logo!
