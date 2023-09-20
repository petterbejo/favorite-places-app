"""
The flask app to display all sites.
"""
from flask import Flask, render_template, request
import folium

from data_handler import DataHandler

app = Flask(__name__)

@app.route("/")
def index():
    """View the front page."""
    m = folium.Map(location=[55.886298698145886, 12.310169834623752])
    handler = DataHandler()
    all_markers = handler.get_all_markers()
    print(all_markers)
    for point in all_markers:
        marker = folium.Marker(
            location=[point[-2], point[-1]],
            popup=f'<a href="view_single_marker/{point[0]}" target="_parent"'
                  f'>{point[1]}</a>',
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
    handler = DataHandler()
    all_markers = handler.get_all_markers()
    return render_template('list_all_markers.html',
                           num_places=len(all_markers),
                           markers=all_markers)

@app.route("/view_single_marker/<int:id>")
def view_single_marker(id):
    """Show a particular marker on the map in a new tab."""
    handler = DataHandler()
    favorite_place = handler.get_single_marker(id)
    m = folium.Map(location=[favorite_place[-2], favorite_place[-1]],
                   zoom_start=13)
    marker = folium.Marker(
            location=[favorite_place[-2], favorite_place[-1]],
            popup=favorite_place[1],
            icon=folium.Icon()
            )
    marker.add_to(m)
    m.get_root().width = "1000"
    m.get_root().height = "1200"
    iframe = m.get_root()._repr_html_()

    return render_template('view_single_marker.html',
                           favorite_place=favorite_place,
                           iframe=iframe)

@app.route("/add_new_marker")
def add_new_marker():
    """View page to insert a single new marker into the database."""
    categories = DataHandler().get_all_categories()
    return render_template('add_new_marker.html',
                           categories=categories)

@app.route('/submit_data', methods=(["POST"]))
def submit_data():
    """Inserts the manually added marker into the database."""
    handler = DataHandler()
    try:
        handler.insert_new_single_marker(request.form)
        return render_template('index.html')
    except Exception as e:
        return render_template('insert_error.html')

