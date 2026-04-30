"""Cobb-Douglas budget-line explorer.

Reference Dash application for the calculation-course project. Implements a
stripped-down version of the Week 2 constrained-utility-maximization project:

    max u(x, y) = x**alpha * y**(1 - alpha)
    s.t. p1 * x + p2 * y = M,   x, y >= 0

Closed-form Cobb-Douglas solution:
    x*       = alpha * M / p1
    y*       = (1 - alpha) * M / p2
    u*       = (x*)**alpha * (y*)**(1 - alpha)
    lambda*  = u* / M           (envelope-theorem shadow price)

Inputs:
    - alpha slider (Cobb-Douglas exponent), 0.05..0.95
    - income M slider, 10..500
    - p1, p2 fixed-input fields

Outputs:
    - Plot: budget line, three indifference curves (one through u*),
      optimum point.
    - Numerical readout: x*, y*, u*, lambda*.

Run locally:
    pip install -r requirements.txt
    python app.py
    # then open http://localhost:8050
"""

from __future__ import annotations

import os

import numpy as np
import plotly.graph_objects as go
from dash import Dash, Input, Output, State, dcc, html

app = Dash(__name__)
app.title = "Cobb-Douglas budget explorer"

DEFAULT_ALPHA = 0.4
DEFAULT_INCOME = 100.0
DEFAULT_P1 = 2.0
DEFAULT_P2 = 3.0


def cobb_douglas_solution(alpha: float, income: float, p1: float, p2: float):
    x_star = alpha * income / p1
    y_star = (1.0 - alpha) * income / p2
    u_star = (x_star ** alpha) * (y_star ** (1.0 - alpha))
    # Envelope theorem: dU*/dM = lambda*. For Cobb-Douglas this is u_star / income.
    lambda_star = u_star / income
    return x_star, y_star, u_star, lambda_star


def build_figure(alpha: float, income: float, p1: float, p2: float) -> go.Figure:
    x_star, y_star, u_star, _ = cobb_douglas_solution(alpha, income, p1, p2)

    x_max = max(income / p1, x_star) * 1.2
    y_max = max(income / p2, y_star) * 1.2
    xs = np.linspace(0.01, x_max, 400)

    # Budget line: y = (M - p1 * x) / p2, clipped at >= 0.
    budget_y = (income - p1 * xs) / p2
    budget_mask = budget_y >= 0
    budget_x = xs[budget_mask]
    budget_y = budget_y[budget_mask]

    # Three indifference curves: at u_star, 0.7 * u_star, 1.3 * u_star.
    levels = [0.7 * u_star, u_star, 1.3 * u_star]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=budget_x,
            y=budget_y,
            mode="lines",
            line=dict(color="black", width=2),
            name=f"Budget: {p1:g}x + {p2:g}y = {income:g}",
        )
    )

    colors = ["#a6cee3", "#1f77b4", "#08306b"]
    for level, color in zip(levels, colors):
        # u = x**alpha * y**(1-alpha)  =>  y = (u / x**alpha) ** (1 / (1 - alpha))
        ic_y = (level / xs ** alpha) ** (1.0 / (1.0 - alpha))
        ic_mask = (ic_y > 0) & (ic_y < y_max * 1.5)
        fig.add_trace(
            go.Scatter(
                x=xs[ic_mask],
                y=ic_y[ic_mask],
                mode="lines",
                line=dict(color=color, width=1.5, dash="dot"),
                name=f"u = {level:.3g}",
            )
        )

    fig.add_trace(
        go.Scatter(
            x=[x_star],
            y=[y_star],
            mode="markers+text",
            marker=dict(color="crimson", size=12, symbol="star"),
            text=[f"  (x*={x_star:.2f}, y*={y_star:.2f})"],
            textposition="top right",
            name="Optimum",
        )
    )

    fig.update_layout(
        xaxis=dict(title="x", range=[0, x_max]),
        yaxis=dict(title="y", range=[0, y_max]),
        title=f"Cobb-Douglas: u(x, y) = x^{alpha:.2f} · y^{1 - alpha:.2f}",
        margin=dict(l=40, r=20, t=50, b=40),
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99),
        height=520,
    )
    return fig


app.layout = html.Div(
    style={"maxWidth": "900px", "margin": "0 auto", "padding": "20px"},
    children=[
        html.H1("Cobb-Douglas budget explorer"),
        html.P(
            "Reference Dash app for the Calculation Course project. "
            "Drag the sliders to vary the Cobb-Douglas exponent α and income M; "
            "edit the price boxes to vary p₁ and p₂. The plot updates with the "
            "budget line, three indifference curves, and the optimum point. "
            "Numerical readout below."
        ),
        html.Div(
            style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "20px"},
            children=[
                html.Div(
                    [
                        html.Label("α (Cobb-Douglas exponent on x)"),
                        dcc.Slider(
                            id="alpha-slider",
                            min=0.05,
                            max=0.95,
                            step=0.05,
                            value=DEFAULT_ALPHA,
                            marks={i / 10: f"{i / 10:.1f}" for i in range(1, 10)},
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("M (income)"),
                        dcc.Slider(
                            id="income-slider",
                            min=10,
                            max=500,
                            step=10,
                            value=DEFAULT_INCOME,
                            marks={v: str(v) for v in (10, 100, 200, 300, 400, 500)},
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("p₁ (price of x)"),
                        dcc.Input(
                            id="p1-input",
                            type="number",
                            min=0.1,
                            step=0.1,
                            value=DEFAULT_P1,
                            style={"width": "100%"},
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("p₂ (price of y)"),
                        dcc.Input(
                            id="p2-input",
                            type="number",
                            min=0.1,
                            step=0.1,
                            value=DEFAULT_P2,
                            style={"width": "100%"},
                        ),
                    ]
                ),
            ],
        ),
        dcc.Graph(id="cobb-douglas-plot"),
        html.Div(
            id="readout",
            style={
                "fontFamily": "monospace",
                "padding": "12px",
                "background": "#f5f5f5",
                "borderRadius": "4px",
            },
        ),
        html.Hr(),
        html.P(
            [
                "Source for this app lives in ",
                html.Code("apps/demo-budget-explorer/"),
                ". For the deployment pattern see the project ",
                html.Code("apps/README.md"),
                ".",
            ]
        ),
    ],
)


@app.callback(
    Output("cobb-douglas-plot", "figure"),
    Output("readout", "children"),
    Input("alpha-slider", "value"),
    Input("income-slider", "value"),
    Input("p1-input", "value"),
    Input("p2-input", "value"),
)
def update(alpha, income, p1, p2):
    if alpha is None or income is None or p1 is None or p2 is None:
        # Fall back to defaults if a control hasn't initialized yet.
        alpha = DEFAULT_ALPHA if alpha is None else alpha
        income = DEFAULT_INCOME if income is None else income
        p1 = DEFAULT_P1 if p1 in (None, 0) else p1
        p2 = DEFAULT_P2 if p2 in (None, 0) else p2

    x_star, y_star, u_star, lambda_star = cobb_douglas_solution(
        float(alpha), float(income), float(p1), float(p2)
    )
    fig = build_figure(float(alpha), float(income), float(p1), float(p2))
    readout = html.Pre(
        f"x*       = {x_star:8.4f}\n"
        f"y*       = {y_star:8.4f}\n"
        f"u*       = {u_star:8.4f}\n"
        f"lambda*  = {lambda_star:8.4f}    (envelope theorem: dU*/dM)"
    )
    return fig, readout


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=True)
