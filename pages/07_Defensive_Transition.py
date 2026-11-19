
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Defensive Transition | Niagara FC",
    page_icon="🔒",
    layout="wide"
)

apply_css()
sidebar_brand()

st.markdown("# DEFENSIVE TRANSITION")

st.markdown(
    "<div style='font-family:Oswald,sans-serif;font-size:1em;"
    "color:#E53935;letter-spacing:1px;margin-bottom:12px;'>"
    "TEAM INTENTION: Regain possession immediately after losing the ball, "
    "preventing the opposition from exploiting the transition."
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='font-family:Oswald,sans-serif;font-size:0.95em;"
    "color:#F5C518;letter-spacing:1px;margin-bottom:12px;'>"
    "STRATEGY: Counter-press immediately. Close forward options. Protect central "
    "spaces. If effective pressure is no longer possible, recover quickly into "
    "our defensive structure.</div>",
    unsafe_allow_html=True
)


# ==================================================
# DEFENSIVE TRANSITION DIAGRAM
# ==================================================

img = get_img("def_transition_new.png")

if img:
    st.image(img, use_container_width=True)
else:
    st.warning("Defensive transition diagram not found.")


# ==================================================
# COUNTER-PRESSING AND IMMEDIATE PRIORITIES
# ==================================================

c1, c2 = st.columns(2)

with c1:
    st.markdown("### COUNTER-PRESSING — COACHING DETAIL")

    coaching_points = [
        "React immediately when possession is lost. Recognise whether we can regain "
        "the ball before the opposition progresses.",

        "The player best positioned applies immediate pressure to the ball carrier.",

        "Nearby players close forward passing lanes and restrict the opposition's options.",

        "Press collectively. Support the first player with cover, balance and coordinated movements.",

        "The #6 protects central spaces and provides balance behind the press.",

        "If #6 steps forward, another player must immediately protect the space left behind.",

        "Players behind the ball recover to protect central spaces and prevent forward penetration.",

        "Recognise when effective pressure is no longer possible. Recover quickly rather than chasing the ball.",

        "Reorganise into a compact defensive structure when the immediate transition has ended.",
    ]

    for item in coaching_points:
        st.markdown(
            f"<div class='card card-red'>→ {item}</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "React to the moment first. Protect central spaces "
        "and recover into our structure when necessary."
        "</div>",
        unsafe_allow_html=True
    )


with c2:
    st.markdown("### IMMEDIATE PRIORITIES")

    priorities = [
        (
            "REACT",
            "Recognise the loss of possession immediately. "
            "The first few actions are critical.",
            "card-red"
        ),
        (
            "COUNTER-PRESS",
            "Apply collective pressure to regain possession. "
            "Close forward options and support the player pressing.",
            "card-orange"
        ),
        (
            "PROTECT CENTRAL",
            "Players behind the press protect central spaces "
            "and prevent the opposition playing forward.",
            "card-gold"
        ),
        (
            "RECOVER & REORGANISE",
            "If the opposition escapes pressure, recover quickly "
            "into a compact defensive structure.",
            "card-blue"
        ),
    ]

    for priority, detail, clr in priorities:
        st.markdown(
            f"<div class='card {clr}'>"
            f"<b>{priority}</b><br>"
            f"<small>{detail}</small></div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "REACT. PRESS. REGAIN. "
        "If we cannot regain, recover and reorganise."
        "</div>",
        unsafe_allow_html=True
    )


# ==================================================
# REAL GAME REFERENCES
# ==================================================

st.divider()

st.markdown("### REAL GAME REFERENCES — DEFENSIVE TRANSITION")

st.markdown("#### Individual Defensive Transition — NFC #2 Recovery")

c1, c2 = st.columns(2)

with c1:
    img = get_img("def_trans1.png")
    if img:
        st.image(
            img,
            caption=(
                "Niagara FC — #2 reacts immediately after possession is lost, "
                "making a recovery sprint to get goal-side and win the ball back."
            ),
            use_container_width=True
        )

with c2:
    img = get_img("def_trans2.png")
    if img:
        st.image(
            img,
            caption=(
                "Niagara FC — #2 wins the footrace and regains possession. "
                "Immediate individual defensive transition — react, recover, regain."
            ),
            use_container_width=True
        )

st.divider()

st.markdown("#### Team Defensive Transition — Counter-Pressing & Recovery")

img = get_img("team_def_transition.png")

if img:
    st.image(
        img,
        caption=(
            "Niagara FC — #8 loses possession. Nearby players react immediately "
            "to counter-press and restrict forward passing options. Players behind "
            "the ball provide cover and protect central spaces, preparing to recover "
            "into shape if the press is unsuccessful."
        ),
        use_container_width=True
    )
