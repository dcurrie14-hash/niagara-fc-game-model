
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
    fig_pentagon,
    PROFILES
)

st.set_page_config(
    page_title="Player Skill-Sets | Niagara FC",
    page_icon="👤",
    layout="wide"
)

apply_css()
sidebar_brand()

CAT_COLORS = {
    "Technical": "#4169E1",
    "Tactical": "#FFD700",
    "Physical": "#E53935",
    "Mental & Social": "#FF8C00",
    "NFC Non-Negotiables": "#00BFFF",
}

# Page-specific styling
st.markdown("""
<style>
/* Headings */
[data-testid="stMain"] h1,
[data-testid="stMain"] h2,
[data-testid="stMain"] h3,
[data-testid="stMain"] h4 {
    color: #EAF2FF !important;
}

/* Expander container */
[data-testid="stExpander"] {
    background: #0B1B2D !important;
    border: 1px solid #28405D !important;
    border-radius: 8px !important;
    overflow: hidden;
    margin-bottom: 10px;
}

/* Expander header: normal, hover and expanded */
[data-testid="stExpander"] details > summary,
[data-testid="stExpander"] details > summary:hover,
[data-testid="stExpander"] details[open] > summary,
[data-testid="stExpander"] details[open] > summary:hover {
    background: #10243A !important;
    color: #FFFFFF !important;
}

/* Text and icons inside headers */
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span,
[data-testid="stExpander"] summary svg {
    color: #FFFFFF !important;
    fill: currentColor;
}

/* Expander content */
[data-testid="stExpander"] details > div {
    background: #071522 !important;
}

/* Tab readability */
[data-testid="stTabs"] button {
    white-space: nowrap;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# PLAYER SKILL-SETS")

st.markdown(
    "<div class='quote-block'>"
    "We build intelligent players who can play in any system "
    "because they understand the game — not just our game."
    "</div>",
    unsafe_allow_html=True
)

st.markdown("### NIAGARA FC — IDEAL POSITIONAL PROFILES")

st.markdown(
    "<div class='card'>"
    "These profiles describe the qualities, decisions and "
    "behaviours we aim to develop in each position. "
    "The scores illustrate the relative demands of the role "
    "across five development areas — they are not ratings "
    "of individual players. Every position requires a "
    "strong foundation in all five areas."
    "</div>",
    unsafe_allow_html=True
)



# ==================================================
# POSITIONAL PROFILES
# ==================================================

tabs = st.tabs(list(PROFILES.keys()))

for tab, (pos, profile) in zip(tabs, PROFILES.items()):

    with tab:

        st.markdown(
            f"<div class='quote-block'>{profile['intro']}</div>",
            unsafe_allow_html=True
        )

        col_chart, col_detail = st.columns(
            [1, 1.4],
            gap="large"
        )

        # ==========================================
        # LEFT COLUMN — IDEAL POSITIONAL PROFILE
        # ==========================================

        with col_chart:

            st.markdown("#### IDEAL POSITIONAL PROFILE")

            fig = fig_pentagon(pos)

            st.pyplot(
                fig,
                use_container_width=True
            )

            plt.close(fig)

            st.markdown("#### POSITIONAL DEMANDS")

            cats = list(CAT_COLORS.keys())
            scores = profile["scores"]

            for cat, score in zip(cats, scores):

                clr = CAT_COLORS[cat]
                bar_pct = int((score / 5) * 100)

                st.markdown(
                    f"""
                    <div style="
                        display:flex;
                        align-items:center;
                        gap:10px;
                        margin:10px 0;
                    ">
                        <span style="
                            color:{clr};
                            font-weight:700;
                            font-size:0.82em;
                            min-width:145px;
                        ">{cat}</span>

                        <div style="
                            flex:1;
                            background:#1A2E4A;
                            border-radius:5px;
                            height:9px;
                            overflow:hidden;
                        ">
                            <div style="
                                width:{bar_pct}%;
                                background:{clr};
                                height:100%;
                                border-radius:5px;
                            "></div>
                        </div>

                        <span style="
                            color:{clr};
                            font-weight:700;
                            min-width:32px;
                            text-align:right;
                        ">{score:.1f}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                "<div class='card' style='margin-top:20px;'>"
                "<strong>Understanding the Profile</strong>"
                "<br><br>"
                "Higher scores indicate greater emphasis "
                "within this positional profile. "
                "They do not represent a player's current "
                "ability or limit their development."
                "</div>",
                unsafe_allow_html=True
            )


        # ==========================================
        # RIGHT COLUMN — DEVELOPMENT ATTRIBUTES
        # ==========================================

        with col_detail:

            st.markdown("#### PLAYER DEVELOPMENT EXPECTATIONS")

            for cat, attrs in profile["attrs"].items():

                clr = CAT_COLORS.get(cat, "#4169E1")

                with st.expander(
                    cat,
                    expanded=(cat == "NFC Non-Negotiables")
                ):

                    for attr in attrs:

                        st.markdown(
                            f"""
                            <div class='card' style="
                                border-left:3px solid {clr};
                                margin:5px 0;
                            ">
                                → {attr}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            st.markdown(
                "<div class='card' style='"
                "border-left:3px solid #4169E1;"
                "margin-top:18px;'>"
                "<strong>Development Focus</strong><br><br>"
                "These are qualities to develop through "
                "training, match experiences, feedback "
                "and individual reflection. "
                "Progress is demonstrated through "
                "consistent decisions and behaviours, "
                "not simply individual actions."
                "</div>",
                unsafe_allow_html=True
            )
