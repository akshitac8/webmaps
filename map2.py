import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def colorproducer(elevation):
	if elevation < 1000:
	    return 'green'
	elif 1000<elevation<2000:
		return 'orange'
	else:
		return 'red'

map = folium.Map(location=[38.58,-99.89],zoom_start=6)
fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
	fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el) ,radius=6, icon=folium.Icon(color=colorproducer(el),color="grey" ),fill_opacity=0.7))
     

map.add_child(fg)
map.save("Map1.html")
