import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, fig_pentagon, PROFILES, ROYAL, GOLD, NAVY, WHITE
import matplotlib.pyplot as plt

st.set_page_config(page_title="Player Skill-Sets | Niagara FC", page_icon="👤", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# PLAYER SKILL-SETS")
st.markdown("<div class='quote-block'>We build intelligent players who can play in any system because they understand the game — not just our game.</div>", unsafe_allow_html=True)

CAT_COLORS = {
    "Technical":           "#4169E1",
    "Tactical":            "#FFD700",
    "Physical":            "#E53935",
    "Mental & Social":     "#FF8C00",
    "NFC Non-Negotiables": "#00BFFF",
}

tabs = st.tabs(list(PROFILES.keys()))

for tab, (pos, profile) in zip(tabs, PROFILES.items()):
    with tab:
        st.markdown(f"<div class='quote-block'>{profile['intro']}</div>",
                    unsafe_allow_html=True)

        col_chart, col_detail = st.columns([1, 1.4])

        with col_chart:
            fig = fig_pentagon(pos)
            st.pyplot(fig, use_container_width=True)
            plt.close()

            st.markdown("#### Score Summary")
            cats  = list(CAT_COLORS.keys())
            scores = profile["scores"]
            for cat, score in zip(cats, scores):
                clr = CAT_COLORS[cat]
                bar_pct = int((score / 5) * 100)
                st.markdown(f"""
                <div style='display:flex;align-items:center;margin:6px 0;gap:10px;'>
                    <span style='color:{clr};font-weight:700;font-size:0.8em;min-width:150px;'>{cat}</span>
                    <div style='flex:1;background:#1a2e4a;border-radius:4px;height:8px;'>
                        <div style='width:{bar_pct}%;background:{clr};height:8px;border-radius:4px;'></div>
                    </div>
                    <span style='color:{clr};font-weight:700;font-size:0.9em;min-width:28px;text-align:right;'>{score}</span>
                </div>""", unsafe_allow_html=True)

        with col_detail:
            for cat, attrs in profile["attrs"].items():
                clr = CAT_COLORS[cat]
                with st.expander(f"**{cat}**", expanded=False):
                    for attr in attrs:
                        st.markdown(
                            f"<div class='card' style='border-left:3px solid {clr};margin:3px 0;'>→ {attr}</div>",
                            unsafe_allow_html=True)
