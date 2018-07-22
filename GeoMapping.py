import folium
import pandas

fgv= folium.FeatureGroup(name="Volcanoes")

data= pandas.read_csv("Volcanoes.txt")

lon= list(data["LON"])
lat= list(data["LAT"])

for ln, lt in zip(lon, lat):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup="Hey, I am a volcano.",icon=folium.Icon('green')))

map= folium.Map(location=[44.87,-120.98], zoom_start=4)

map.add_child(fgv)

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(open("world.json","r",encoding = "utf-8-sig").read(), #The read function of the code have changed
style_function=lambda x:{'fillColor':'green' if x["properties"]["POP2005"]< 10000000
else 'orange' if 10000000 <= x["properties"]["POP2005"] < 20000000 else 'red' }))

map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("GeoMap.html")
