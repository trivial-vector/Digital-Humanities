from pyproj import Proj, transform


def to_latlon(x, y):
    proj_in = 'epsg:2278'
    proj_out = 'epsg:4326'
    in_proj = Proj(init=proj_in, preserve_units=True)
    out_proj = Proj(init=proj_out)
    return transform(in_proj, out_proj, x, y)
