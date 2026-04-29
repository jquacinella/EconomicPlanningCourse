"""Template Dash application.

Copy this directory to start a new app:
    cp -r apps/_template apps/<your-new-app>

Then edit this file to implement the app, update requirements.txt with any
additional dependencies, edit Dockerfile / render.yaml as needed, and rewrite
README.md to describe what the app does.

Run locally with:
    pip install -r requirements.txt
    python app.py

Then open http://localhost:8050.
"""

from __future__ import annotations

import os

from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)
app.title = "Template app"

app.layout = html.Div(
    [
        html.H1("Template app"),
        html.P(
            "Replace this placeholder with your app's UI. "
            "See apps/demo-budget-explorer/ for a worked example."
        ),
        dcc.Input(id="echo-input", type="text", value="hello", debounce=True),
        html.Div(id="echo-output"),
    ]
)


@app.callback(Output("echo-output", "children"), Input("echo-input", "value"))
def echo(value: str) -> str:
    return f"You typed: {value}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=True)
