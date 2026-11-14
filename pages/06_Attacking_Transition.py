
import streamlit as st
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Attacking Transition | Niagara FC",
    page_icon="⚡",
    layout="wide"
)

apply_css()
sidebar_brand()

st.markdown("# ATTACKING TRANSITION")

st.markdown(
    "<div style='font-family:Oswald,sans-serif;"
    "font-size:1em;color:#F5C518;letter-spacing:1px;"
    "margin-bottom:12px;'>"
    "TEAM INTENTION: Exploit the opposition's disorganisation "
    "immediately after regaining possession."
    "</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div style='font-family:Oswald,sans-serif;"
    "font-size:0.95em;color:#FFD700;letter-spacing:1px;"
    "margin-bottom:12px;'>"
    "STRATEGY: Play forward whenever possible. "
    "Break lines quickly. Support the attack with forward runs."
    "</div>",
    unsafe_allow_html=True
)

# New tactical diagram
img = get_img("att_transition_new.png")

if img:
    st.image(img, use_container_width=True)
else:
    st.warning(
        "Attacking Transition diagram not found. "
        "Check that att_transition_new.png is uploaded "
        "to the main GitHub folder."
    )



c1, c2 = st.columns(2)

with c1:
    st.markdown("### COACHING DETAIL")

    coaching_points = [
        "React immediately when possession is regained. "
        "Recognise the opportunity before the opposition reorganises.",

        "Look forward first. Can we pass, carry, combine, "
        "or run forward to break a line?",

        "Recognise the positioning of #7, #9, and #11. "
        "Exploit space ahead of or behind the opposition.",

        "#9 provides a forward option. Check to receive, "
        "turn, combine, hold the ball, or threaten space behind.",

        "Wide players provide width and depth. "
        "Recognise when to run behind or receive to feet.",

        "#8 and #10 support the attack with forward runs, "
        "creating options around and beyond the ball.",

        "#6 provides support underneath and helps maintain "
        "balance behind the attack.",

        "Fullbacks recognise opportunities to advance "
        "while maintaining defensive security.",

        "Attack the space, not simply the direction. "
        "A quick switch may be the best way forward.",

        "If forward progression is not available, "
        "secure possession and establish attacking organisation."
    ]

    for item in coaching_points:
        st.markdown(
            f"<div class='card card-gold'>→ {item}</div>",
            unsafe_allow_html=True
        )

with c2:
    for word in ["REGAIN.", "RECOGNISE.", "EXPLOIT."]:
        st.markdown(
            f"<span class='identity-word'>{word}</span>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "Play forward when the opportunity is there. "
        "Run forward to create the opportunity."
        "</div>",
        unsafe_allow_html=True
    )



st.divider()

st.markdown(
    "### REAL GAME REFERENCES — ATTACKING TRANSITION"
)

c1, c2 = st.columns(2)

with c1:
    img = get_img("LB_providing_width_on_AT.png")

    if img:
        st.image(
            img,
            caption=(
                "Niagara FC — #8 wins the second ball and "
                "immediately switches play to the fullback "
                "providing width. A quick switch exploits "
                "space before the opposition reorganises."
            ),
            use_container_width=True
        )

    img = get_img("attacking_transition1.png")

    if img:
        st.image(
            img,
            caption=(
                "WEURO — Germany regain possession and "
                "play forward quickly. Two runners attack "
                "the space behind Austria's defensive line."
            ),
            use_container_width=True
        )

with c2:
    img = get_img("Attacking_transitions2.png")

    if img:
        st.image(
            img,
            caption=(
                "NWSL — possession is regained and play "
                "is switched immediately to exploit width. "
                "A runner attacks space on the far side "
                "before the defence recovers."
            ),
            use_container_width=True
        )
