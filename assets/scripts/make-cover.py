"""Generate the book cover image: a Leontief input-output network.

Run from the project root:
    uv run python assets/scripts/make-cover.py

Writes to assets/images/cover.png. The cover is a stylized directed graph of
eight sectors with weighted inter-sector flows, rendered on a deep navy
background with the book's title and subtitle overlaid.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).resolve().parents[2] / "assets" / "images" / "cover.png"

SECTORS = [
    "Agriculture",
    "Energy",
    "Materials",
    "Manufacturing",
    "Construction",
    "Services",
    "Transport",
    "Knowledge",
]

# A synthetic but plausible technical-coefficient matrix A (rows = inputs,
# cols = sectors using them). Values in [0, 0.4].
rng = np.random.default_rng(7)
A = rng.uniform(0.02, 0.35, size=(8, 8))
np.fill_diagonal(A, 0.0)
# Sparsify: keep only the top ~3 inputs per sector for visual clarity.
for j in range(A.shape[1]):
    col = A[:, j].copy()
    keep = np.argsort(col)[-3:]
    mask = np.ones_like(col, dtype=bool)
    mask[keep] = False
    A[mask, j] = 0.0

BG = "#0b1b2b"
FG = "#e8eef7"
ACCENT = "#f5b400"
EDGE_LO = "#3a6ea5"
EDGE_HI = "#7fc7ff"


def lerp_color(t: float, lo: str, hi: str) -> str:
    lo_rgb = np.array([int(lo[1:3], 16), int(lo[3:5], 16), int(lo[5:7], 16)])
    hi_rgb = np.array([int(hi[1:3], 16), int(hi[3:5], 16), int(hi[5:7], 16)])
    rgb = (1 - t) * lo_rgb + t * hi_rgb
    return "#{:02x}{:02x}{:02x}".format(*rgb.astype(int))


def main() -> None:
    fig = plt.figure(figsize=(8, 10), dpi=200)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-2.1, 1.4)
    ax.set_axis_off()

    # Lay nodes out on a circle.
    n = len(SECTORS)
    angles = np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, n, endpoint=False)
    radius = 0.95
    pos = {i: (radius * math.cos(a), radius * math.sin(a)) for i, a in enumerate(angles)}

    # Edges, weighted by A[i, j].
    G = nx.DiGraph()
    for i in range(n):
        for j in range(n):
            if A[i, j] > 0:
                G.add_edge(i, j, weight=float(A[i, j]))

    weights = np.array([G[u][v]["weight"] for u, v in G.edges()])
    w_min, w_max = weights.min(), weights.max()

    for u, v in G.edges():
        w = G[u][v]["weight"]
        t = (w - w_min) / (w_max - w_min + 1e-9)
        color = lerp_color(t, EDGE_LO, EDGE_HI)
        lw = 0.4 + 2.6 * t
        alpha = 0.35 + 0.55 * t
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        # Curve the edges so reciprocal flows don't overlap.
        rad = 0.18 if (u + v) % 2 == 0 else -0.18
        arrow = FancyArrowPatch(
            (x0, y0), (x1, y1),
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>",
            mutation_scale=8 + 8 * t,
            color=color,
            alpha=alpha,
            linewidth=lw,
            shrinkA=14, shrinkB=14,
            zorder=2,
        )
        ax.add_patch(arrow)

    # Nodes.
    for i, (x, y) in pos.items():
        ax.scatter([x], [y], s=900, c=BG, edgecolors=ACCENT, linewidths=2.0, zorder=3)
        ax.scatter([x], [y], s=300, c=ACCENT, alpha=0.9, zorder=4)
        # Label outside the ring.
        a = angles[i]
        lx = 1.18 * math.cos(a)
        ly = 1.18 * math.sin(a)
        ha = "left" if math.cos(a) > 0.05 else ("right" if math.cos(a) < -0.05 else "center")
        va = "bottom" if math.sin(a) > 0.05 else ("top" if math.sin(a) < -0.05 else "center")
        ax.text(lx, ly, SECTORS[i], color=FG, fontsize=10, ha=ha, va=va,
                fontweight="medium", zorder=5)

    # Title block (well below the bottom-most "Construction" label).
    ax.text(0, -1.55, "The Morishima Track", color=FG, fontsize=26,
            ha="center", va="center", fontweight="bold", family="serif")
    ax.text(0, -1.80, "A Computational-Economics Curriculum",
            color=FG, fontsize=12, ha="center", va="center",
            alpha=0.85, family="serif", style="italic")
    ax.text(0, -1.97, "from Multivariable Calculus to Climate-Constrained Planning",
            color=FG, fontsize=10, ha="center", va="center",
            alpha=0.7, family="serif", style="italic")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=200)
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
