import sqlite3

from flask import Flask, render_template_string, redirect, url_for
import folium

app = Flask(__name__)

@app.route("/")
def index():
    """View the front page."""
    m = folium.Map(location=[55.886298698145886, 12.310169834623752])
    return m.get_root().render()

@app.route("/iframe")
def iframe():
    """Embed a map as an iframe on a page."""
    m = folium.Map(location=[55.886298698145886, 12.310169834623752])

    # set the iframe width and height
    m.get_root().width = "1000"
    m.get_root().height = "1200"
    iframe = m.get_root()._repr_html_()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head></head>
                <body>
                    <h1>Using an iframe</h1>
                    {{ iframe|safe }}
                </body>
            </html>
        """,
        iframe=iframe,
    )


@app.route("/components")
def components():
    """Extract map components and put those on a page."""
    m = folium.Map(
        width=800,
        height=600,
    )

    m.get_root().render()
    header = m.get_root().header.render()
    body_html = m.get_root().html.render()
    script = m.get_root().script.render()

    return render_template_string(
        """
            <!DOCTYPE html>
            <html>
                <head>
                    {{ header|safe }}
                </head>
                <body>
                    <h1>Using components</h1>
                    {{ body_html|safe }}
                    <script>
                        {{ script|safe }}
                    </script>
                </body>
            </html>
        """,
        header=header,
        body_html=body_html,
        script=script,
    )

@app.route("/tst")
def tst():
    """View the front page."""
    m = folium.Map(location=[55.886298698145886, 12.310169834623752])
    marker = folium.Marker(
        location=[55.73931038034454, 12.24586002073197], # coordinates for the marker (Earth Lab at CU Boulder)
        popup='Earth Lab at CU Boulder', # pop-up label for the marker
        icon=folium.Icon()
    )
    marker.add_to(m)

    return m.get_root().render()

