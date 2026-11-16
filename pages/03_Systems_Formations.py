
import streamlit as st
import sys
import os
import matplotlib.pyplot as plt

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import (
    apply_css,
    sidebar_brand,
    fig_formation,
    FORMATIONS
)

st.set_page_config(
    page_title="Systems & Formations | Niagara FC",
    page_icon="📐",
    layout="wide"
)

apply_css()
sidebar_brand()

# ==========================================
# PAGE INTRODUCTION
# ==========================================

st.markdown("# SYSTEMS & FORMATIONS")

st.markdown(
    "<div class='quote-block'>"
    "The formation organises the team. "
    "Our principles give players the freedom "
    "to solve problems, adapt to the game, "
    "and make intelligent decisions."
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "The positions shown represent our starting structure. "
    "Responsibilities and relationships change as the game develops."
)

# ==========================================
# FORMATION SELECTOR
# ==========================================

c1, _ = st.columns([1, 3])

with c1:
    sel = st.selectbox(
        "Formation",
        list(FORMATIONS.keys())
    )

# ==========================================
# FORMATION DIAGRAM
# ==========================================

st.markdown("### BASE STRUCTURE")

fig = fig_formation(sel)

st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)

st.divider()

# ==========================================
# POSITIONAL RESPONSIBILITIES
# ==========================================

st.markdown("### POSITIONAL RESPONSIBILITIES")

st.markdown(
    "Each position has specific responsibilities within "
    "our Game Model. Players must recognise how those "
    "responsibilities change with the ball, the opposition "
    "and the movements of teammates."
)

cols = st.columns(3, gap="medium")

for i, (role, desc) in enumerate(
    FORMATIONS[sel]["roles"].items()
):
    with cols[i % 3]:

        st.markdown(
            f"<div class='card'>"
            f"<b>{role}</b><br>"
            f"<small>{desc}</small>"
            f"</div>",
            unsafe_allow_html=True
        )
