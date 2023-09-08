"""
The flask app to display all sites.
"""
from flask import Flask, render_template
import folium

from data_handler import DataHandler

db_path = '../db/test.db'

app = Flask(__name__)

@app.route("/")
def index():
    """View the front page."""
    m = folium.Map(location=[55.886298698145886, 12.310169834623752])
    handler = DataHandler(db_path)
    all_markers = handler.get_all_markers()
    print(all_markers)
    for point in all_markers:
        marker = folium.Marker(
            location=[point[2], point[3]],
            popup=point[1],
            icon=folium.Icon()
            )
        marker.add_to(m)

    m.get_root().width = "1000"
    m.get_root().height = "1200"
    iframe = m.get_root()._repr_html_()

    return render_template('index.html',
                           num_places=len(all_markers),
                           iframe=iframe)

@app.route("/list_all_markers")
def list_all_markers():
    """Show a tabular view of all places."""
    handler = DataHandler(db_path)
    all_markers = handler.get_all_markers()
    return render_template('list_all_markers.html',
                           num_places=len(all_markers),
                           markers=all_markers)

