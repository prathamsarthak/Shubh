import folium
import pandas

fgv= folium.FeatureGroup(name="Volcanoes")

data= pandas.read_csv("Volcanoes.txt")

def marker_color(elev):
    if elev<1000:
        return 'green'
    elif elev<3000:
        return 'orange'
    else:
        return 'red'

lon= list(data["LON"])
lat= list(data["LAT"])
elev=list(data["ELEV"])

for ln, lt ,el in zip(lon, lat, elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=str(el),icon=folium.Icon(marker_color(el))))

map= folium.Map(location=[44.87,-120.98], zoom_start=4)

map.add_child(fgv)

fgp=folium.FeatureGroup(name="Population")

#The read function of the code have changed
fgp.add_child(folium.GeoJson(open("world.json","r",encoding = "utf-8-sig").read(),style_function=lambda x:{'fillColor':'green' if x["properties"]["POP2005"]< 10000000 else 'orange' if 10000000 <= x["properties"]["POP2005"] < 20000000 else 'red' }))

map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("GeoMap.html")
