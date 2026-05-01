"""Generate the Postcapitalism After AI research-track cover (legacy: blockchain network visualization, retained from the prior crypto-course stub).

Run from the project directory:
    uv run python make-cover.py

Writes to assets/images/cover.png. The cover visualizes a decentralized
blockchain network with blocks, merkle trees, and distributed consensus nodes,
representing the cryptographic and ecosocialist planning aspects.
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
BLOCK_COLOR = "#2d5f5d"
VALIDATED = "#26de81"
PENDING = "#fd9644"
MERKLE = "#a29bfe"

def draw_block(ax, x, y, label, validated=True):
    """Draw a blockchain block with header and merkle root."""
    color = VALIDATED if validated else PENDING
    
    # Block outline
    rect = mpatches.Rectangle((x - 0.15, y - 0.12), 0.3, 0.24,
                               linewidth=2, edgecolor=color,
                               facecolor=BG, alpha=0.4, zorder=2)
    ax.add_patch(rect)
    
    # Block number
    ax.text(x, y + 0.05, label, color=FG, fontsize=9,
            ha='center', va='center', fontfamily='monospace',
            fontweight='bold', alpha=0.9, zorder=5)
    
    # Hash visualization (horizontal lines)
    for i, offset in enumerate([-0.04, 0, 0.04]):
        ax.plot([x - 0.10, x + 0.10], [y + offset - 0.06, y + offset - 0.06],
                c=color, lw=1, alpha=0.6, zorder=3)

def main() -> None:
    # 2.5:1 aspect ratio (3000x1200 at dpi=200)
    fig = plt.figure(figsize=(15, 6), dpi=200)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_facecolor(BG)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-1.4, 1.4)
    ax.set_axis_off()

    # Blockchain chain - positioned on the right
    CHAIN_Y = 0.4
    block_positions = [1.2, 1.8, 2.4, 3.0]
    block_labels = ["#1729", "#1730", "#1731", "#1732"]
    
    for i, (x, label) in enumerate(zip(block_positions, block_labels)):
        draw_block(ax, x, CHAIN_Y, label, validated=(i < 3))
        
        # Chain links
        if i > 0:
            prev_x = block_positions[i-1]
            ax.plot([prev_x + 0.15, x - 0.15], [CHAIN_Y, CHAIN_Y],
                    c=VALIDATED, lw=2.5, alpha=0.7, zorder=1)
            # Arrow head
            ax.plot([x - 0.15, x - 0.20], [CHAIN_Y, CHAIN_Y + 0.04],
                    c=VALIDATED, lw=2.5, alpha=0.7, zorder=1)
            ax.plot([x - 0.15, x - 0.20], [CHAIN_Y, CHAIN_Y - 0.04],
                    c=VALIDATED, lw=2.5, alpha=0.7, zorder=1)
    
    # Merkle tree structure in the middle
    MERKLE_X = 1.8
    MERKLE_Y = -0.3
    
    # Root hash
    ax.scatter([MERKLE_X], [MERKLE_Y], s=500, c=BG, edgecolors=MERKLE,
               linewidths=2, marker='s', zorder=3)
    ax.scatter([MERKLE_X], [MERKLE_Y], s=200, c=MERKLE, alpha=0.8,
               marker='s', zorder=4)
    ax.text(MERKLE_X, MERKLE_Y, "MR", color=BG, fontsize=9,
            ha='center', va='center', fontweight='bold', zorder=5)
    
    # Second level
    level2_y = MERKLE_Y - 0.35
    level2_x = [MERKLE_X - 0.25, MERKLE_X + 0.25]
    for x in level2_x:
        ax.plot([MERKLE_X, x], [MERKLE_Y - 0.08, level2_y + 0.08],
                c=MERKLE, lw=1.5, alpha=0.5, zorder=1)
        ax.scatter([x], [level2_y], s=350, c=BG, edgecolors=MERKLE,
                   linewidths=1.5, marker='s', zorder=3)
        ax.scatter([x], [level2_y], s=150, c=MERKLE, alpha=0.7,
                   marker='s', zorder=4)
    
    # Leaf nodes (transactions)
    leaf_y = level2_y - 0.35
    leaf_x = [MERKLE_X - 0.45, MERKLE_X - 0.15, MERKLE_X + 0.15, MERKLE_X + 0.45]
    for i, x in enumerate(leaf_x):
        parent_x = level2_x[i // 2]
        ax.plot([parent_x, x], [level2_y - 0.08, leaf_y + 0.06],
                c=MERKLE, lw=1.5, alpha=0.5, zorder=1)
        ax.scatter([x], [leaf_y], s=250, c=BG, edgecolors=MERKLE,
                   linewidths=1.5, marker='s', zorder=3)
        ax.scatter([x], [leaf_y], s=100, c=MERKLE, alpha=0.6,
                   marker='s', zorder=4)
    
    # Distributed network nodes in the upper left
    network_center_x = 0.6
    network_center_y = 0.7
    n_nodes = 6
    radius = 0.45
    
    angles = np.linspace(0, 2 * np.pi, n_nodes, endpoint=False)
    node_positions = []
    
    for i, angle in enumerate(angles):
        x = network_center_x + radius * math.cos(angle)
        y = network_center_y + radius * math.sin(angle)
        node_positions.append((x, y))
        
        # Node
        ax.scatter([x], [y], s=400, c=BG, edgecolors=ACCENT,
                   linewidths=2, marker='o', zorder=3)
        ax.scatter([x], [y], s=150, c=ACCENT, alpha=0.8, zorder=4)
    
    # Connect nodes in a mesh (each node connects to 2-3 neighbors)
    for i, (x1, y1) in enumerate(node_positions):
        # Connect to next node
        next_i = (i + 1) % n_nodes
        x2, y2 = node_positions[next_i]
        ax.plot([x1, x2], [y1, y2], c=ACCENT, lw=1.2, alpha=0.4, zorder=1)
        
        # Connect to node two steps ahead
        if i % 2 == 0:
            next2_i = (i + 2) % n_nodes
            x3, y3 = node_positions[next2_i]
            ax.plot([x1, x3], [y1, y3], c=ACCENT, lw=1.2, alpha=0.3, zorder=1)
    
    # Network label
    ax.text(network_center_x, network_center_y - 0.65, "Consensus Network",
            color=FG, fontsize=10, ha='center', va='center',
            alpha=0.75, style='italic', zorder=5)
    
    # Add mining/energy efficiency symbol in lower left
    energy_x = 0.6
    energy_y = -0.9
    
    # Leaf symbol (representing green energy)
    leaf_points = np.array([
        [0, 0.15],
        [-0.08, 0.05],
        [-0.05, -0.05],
        [0, -0.15],
        [0.05, -0.05],
        [0.08, 0.05],
        [0, 0.15]
    ])
    leaf_points[:, 0] += energy_x
    leaf_points[:, 1] += energy_y
    
    leaf_patch = mpatches.Polygon(leaf_points, closed=True,
                                  edgecolor=VALIDATED, facecolor=VALIDATED,
                                  alpha=0.6, linewidth=1.5, zorder=3)
    ax.add_patch(leaf_patch)
    
    ax.text(energy_x, energy_y - 0.25, "Ecosocialist\nPlanning",
            color=FG, fontsize=9, ha='center', va='center',
            alpha=0.7, style='italic', zorder=5)

    # Title block on the left
    TITLE_X = -1.85
    ax.text(TITLE_X, 0.45, "The Crypto", color=FG, fontsize=34,
            ha="center", va="center", fontweight="bold", family="serif")
    ax.text(TITLE_X, 0.10, "Calculation Course", color=ACCENT, fontsize=36,
            ha="center", va="center", fontweight="bold", family="serif")
    ax.text(TITLE_X, -0.20, "Cryptocurrency, Blockchain,", color=FG, fontsize=15,
            ha="center", va="center", alpha=0.85, family="serif", style="italic")
    ax.text(TITLE_X, -0.42, "and the Ecosocialist Planning System", color=FG,
            fontsize=15, ha="center", va="center", alpha=0.85,
            family="serif", style="italic")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, facecolor=BG, dpi=200)
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()