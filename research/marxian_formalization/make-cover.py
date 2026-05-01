"""Generate the Marxian Formalization research project cover: a game theory decision tree with payoff matrices.

Run from the project directory:
    uv run python make-cover.py

Writes to assets/images/cover.png. The cover visualizes a strategic game tree
with decision nodes, chance nodes, and payoff matrices, representing the
game-theoretic and probabilistic aspects of Zhang's Marxian formalization.
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = Path(__file__).resolve().parent / "assets" / "images" / "cover.png"

BG = "#0b1b2b"
FG = "#e8eef7"
ACCENT = "#f5b400"
PLAYER_1 = "#ff6b6b"
PLAYER_2 = "#4ecdc4"
CHANCE = "#95e1d3"

def main() -> None:
    # 2.5:1 aspect ratio (3000x1200 at dpi=200)
    fig = plt.figure(figsize=(15, 6), dpi=200)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor(BG)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1.4, 1.4)
    ax.set_axis_off()

    # Game tree structure - positioned on the right
    TREE_X = 1.5
    
    # Root node (Player 1 decision)
    ax.scatter([TREE_X], [0], s=800, c=BG, edgecolors=PLAYER_1, linewidths=2.5, zorder=3)
    ax.scatter([TREE_X], [0], s=300, c=PLAYER_1, alpha=0.9, zorder=4)
    
    # Player 1's two choices
    branch_y = 0.6
    branch_x = 2.3
    
    # Upper branch (Cooperate)
    ax.plot([TREE_X, branch_x], [0, branch_y], c=PLAYER_1, lw=2, alpha=0.7, zorder=1)
    ax.scatter([branch_x], [branch_y], s=600, c=BG, edgecolors=PLAYER_2, linewidths=2, zorder=3)
    ax.scatter([branch_x], [branch_y], s=250, c=PLAYER_2, alpha=0.9, zorder=4)
    ax.text(TREE_X + 0.15, branch_y/2 + 0.1, "Cooperate", color=FG, fontsize=11, 
            alpha=0.8, rotation=25, zorder=5)
    
    # Lower branch (Defect)
    ax.plot([TREE_X, branch_x], [0, -branch_y], c=PLAYER_1, lw=2, alpha=0.7, zorder=1)
    ax.scatter([branch_x], [-branch_y], s=600, c=BG, edgecolors=PLAYER_2, linewidths=2, zorder=3)
    ax.scatter([branch_x], [-branch_y], s=250, c=PLAYER_2, alpha=0.9, zorder=4)
    ax.text(TREE_X + 0.15, -branch_y/2 - 0.1, "Defect", color=FG, fontsize=11,
            alpha=0.8, rotation=-25, zorder=5)
    
    # Player 2's responses (terminal nodes with payoffs)
    term_x = 3.1
    outcomes = [
        (branch_x, branch_y, term_x, branch_y + 0.25, "(3, 3)", PLAYER_2, "C"),
        (branch_x, branch_y, term_x, branch_y - 0.25, "(0, 5)", PLAYER_2, "D"),
        (branch_x, -branch_y, term_x, -branch_y + 0.25, "(5, 0)", PLAYER_2, "C"),
        (branch_x, -branch_y, term_x, -branch_y - 0.25, "(1, 1)", PLAYER_2, "D"),
    ]
    
    for x0, y0, x1, y1, payoff, color, action in outcomes:
        ax.plot([x0, x1], [y0, y1], c=color, lw=1.5, alpha=0.6, zorder=1)
        # Terminal node
        ax.scatter([x1], [y1], s=400, c=BG, edgecolors=ACCENT, linewidths=1.5, zorder=3)
        ax.scatter([x1], [y1], s=150, c=ACCENT, alpha=0.8, zorder=4)
        # Payoff text
        ax.text(x1 + 0.25, y1, payoff, color=FG, fontsize=10, ha='left', va='center',
                fontfamily='monospace', alpha=0.9, zorder=5)
        # Action label
        ax.text((x0 + x1)/2, y1, action, color=FG, fontsize=9, alpha=0.7, zorder=5)
    
    # Add a chance node visualization in the upper left
    chance_x = 0.8
    chance_y = 0.8
    ax.scatter([chance_x], [chance_y], s=700, c=BG, edgecolors=CHANCE, 
               linewidths=2.5, marker='D', zorder=3)
    ax.scatter([chance_x], [chance_y], s=250, c=CHANCE, alpha=0.9, marker='D', zorder=4)
    
    # Probability branches from chance node
    prob_angles = [30, -30]
    prob_labels = ["p = 0.7", "p = 0.3"]
    for angle, label in zip(prob_angles, prob_labels):
        rad = math.radians(angle)
        end_x = chance_x + 0.4 * math.cos(rad)
        end_y = chance_y + 0.4 * math.sin(rad)
        ax.plot([chance_x, end_x], [chance_y, end_y], c=CHANCE, lw=1.5, 
                alpha=0.6, zorder=1, linestyle='--')
        ax.text(end_x + 0.05, end_y, label, color=FG, fontsize=9, 
                alpha=0.75, zorder=5)
    
    # Payoff matrix in lower left
    matrix_x = 0.6
    matrix_y = -0.75
    cell_w = 0.35
    cell_h = 0.25
    
    # Draw matrix cells
    for i in range(2):
        for j in range(2):
            x = matrix_x + j * cell_w
            y = matrix_y - i * cell_h
            rect = mpatches.Rectangle((x, y), cell_w, cell_h, 
                                       linewidth=1.5, edgecolor=FG, 
                                       facecolor=BG, alpha=0.3, zorder=2)
            ax.add_patch(rect)
    
    # Matrix values
    matrix_values = [
        [(3, 3), (0, 5)],
        [(5, 0), (1, 1)]
    ]
    
    for i in range(2):
        for j in range(2):
            x = matrix_x + j * cell_w + cell_w/2
            y = matrix_y - i * cell_h + cell_h/2
            v1, v2 = matrix_values[i][j]
            ax.text(x, y, f"{v1}, {v2}", color=FG, fontsize=11,
                    ha='center', va='center', fontfamily='monospace',
                    alpha=0.85, zorder=5)
    
    # Matrix labels
    ax.text(matrix_x - 0.15, matrix_y - 0.125, "C", color=PLAYER_1, 
            fontsize=10, ha='right', va='center', fontweight='bold', zorder=5)
    ax.text(matrix_x - 0.15, matrix_y - 0.375, "D", color=PLAYER_1,
            fontsize=10, ha='right', va='center', fontweight='bold', zorder=5)
    ax.text(matrix_x + 0.175, matrix_y + 0.05, "C", color=PLAYER_2,
            fontsize=10, ha='center', va='bottom', fontweight='bold', zorder=5)
    ax.text(matrix_x + 0.525, matrix_y + 0.05, "D", color=PLAYER_2,
            fontsize=10, ha='center', va='bottom', fontweight='bold', zorder=5)
    
    # Title block on the left
    TITLE_X = -1.9
    ax.text(TITLE_X, 0.38, "201", color=ACCENT, fontsize=48,
            ha="center", va="center", fontweight="bold", family="monospace")
    ax.text(TITLE_X, 0.05, "Computational Reconstruction of", color=FG, fontsize=16,
            ha="center", va="center", alpha=0.85, family="serif", style="italic")
    ax.text(TITLE_X, -0.20, "Zhang's Marxian Formalization", color=FG, fontsize=17,
            ha="center", va="center", alpha=0.9, family="serif", fontweight="medium")
    ax.text(TITLE_X, -0.50, "Game Theory · Probability · Cybernetics", color=FG,
            fontsize=13, ha="center", va="center", alpha=0.75, family="serif",
            style="italic")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=200)
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()