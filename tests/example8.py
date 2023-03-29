# EOmaps example 8: Adding scalebars - what about distances?

from eomaps import Maps
import matplotlib.pyplot as plt

plt.get_backend()

m = Maps(figsize=(9, 5))
m.add_feature.preset.ocean(ec="k", scale="110m")

s1 = m.add_scalebar(
    -11,
    -50,
    -45,
    scale=500000,
    scale_props=dict(n=10, width=5, colors=("k", ".25", ".5", ".75", ".95")),
    patch_props=dict(offsets=(1, 1.4, 1, 1), fc=(0.7, 0.8, 0.3, 1)),
    label_props=dict(offset=0.5, scale=1.4, every=5, weight="bold", family="Calibri"),
)

s2 = m.add_scalebar(
    50,
    -20,
    45,
    scale_props=dict(n=6, width=3, colors=("k", "r")),
    patch_props=dict(fc="none", ec="none", offsets=(1, 1, 1, 2)),
    label_props=dict(scale=1, rotation=45, weight="bold", family="Impact", offset=0.5),
)

s3 = m.add_scalebar(
    -73,
    8,
    0,
    scale=500000,
    scale_props=dict(n=6, width=3, colors=("w", "r")),
    patch_props=dict(fc=".25", ec="k", lw=0.5, offsets=(1, 1, 1, 2)),
    label_props=dict(color="w", rotation=45, weight="bold", family="Impact"),
    line_props=dict(color="w"),
)

# it's also possible to update the properties of an existing scalebar
# via the setter-functions!
s4 = m.add_scalebar(preset="bw")
s4.set_scale_props(n=6, width=3)

# NOTE that the black-and-white scalebar is automatically re-scaled and re-positioned
#      on zoom events (the default if you don't provide an explicit scale & position)!

m.add_logo()
