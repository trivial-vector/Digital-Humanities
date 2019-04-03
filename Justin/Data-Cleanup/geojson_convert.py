import csv
import json
from geojson import Feature, FeatureCollection, Point

features = []
with open('../../Data/1900.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for Latitude, Longitude in reader:
        latitude, longitude = map(float, (Latitude, Longitude))
        features.append(
            Feature(
                geometry=Point((longitude, latitude))

            )
        )

collection = FeatureCollection(features)
with open("Geo.json", "w") as f:
    f.write('%s' % collection)
