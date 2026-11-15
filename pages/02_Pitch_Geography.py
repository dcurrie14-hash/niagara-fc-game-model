
import streamlit as st
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import apply_css, sidebar_brand, get_img

st.set_page_config(
    page_title="Pitch Geography | Niagara FC",
    page_icon="🗺️",
    layout="wide"
)

apply_css()
sidebar_brand()

st.markdown("# PITCH GEOGRAPHY")

st.markdown(
    "<div class='quote-block'>"
    "Pitch geography provides shared reference points "
    "for positioning, support, spacing and decision-making. "
    "It helps us recognise where space exists and "
    "how to use it."
    "</div>",
    unsafe_allow_html=True
)

tabs = st.tabs([
    "📏 Horizontal Zones",
    "🔀 Vertical Channels",
    "🗺️ Zones & Channels"
])

with tabs[0]:
    st.markdown("### HORIZONTAL ZONES")

    img = get_img("pitch_horizontal_zones.png")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.warning("Horizontal Zones image not found.")

    c1, c2 = st.columns(2)

    with c1:
        zones = [
            (
                "ZONE 1 — BUILD",
                "Create passing options, recognise pressure "
                "and find ways to progress beyond the first line."
            ),
            (
                "ZONE 2 — PROGRESS",
                "Break lines through passing, carrying "
                "or combinations. Create and exploit overloads."
            ),
            (
                "ZONE 3 — CREATE",
                "Find space between and behind defenders. "
                "Combine, penetrate and create chances."
            ),
            (
                "ZONE 4 — FINISH",
                "Attack the box with appropriate numbers "
                "and timing. Support the final action, "
                "anticipate rebounds and finish decisively."
            )
        ]

        for title, detail in zones:
            st.markdown(
                f"<div class='card'>"
                f"<b>{title}</b><br>"
                f"<small>{detail}</small>"
                f"</div>",
                unsafe_allow_html=True
            )

    with c2:
        st.markdown(
            "<div class='quote-block'>"
            "<b>THINK FORWARD · PLAY FORWARD · "
            "RUN FORWARD</b>"
            "<br><br>"
            "Pitch geography gives us reference points. "
            "Our principles guide the decisions we make."
            "</div>",
            unsafe_allow_html=True
        )



with tabs[1]:
    st.markdown("### VERTICAL CHANNELS")

    img = get_img("pitch_vertical_channels.png")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.warning("Vertical Channels image not found.")

    c1, c2 = st.columns(2)

    with c1:
        channels = [
            (
                "LEFT & RIGHT WIDE CHANNELS",
                "Provide width to stretch the opposition. "
                "Create space inside and opportunities "
                "to receive, advance or deliver."
            ),
            (
                "LEFT & RIGHT HALF-SPACES",
                "Recognise opportunities to receive "
                "between lines, combine, turn and "
                "penetrate towards goal."
            ),
            (
                "CENTRAL CHANNEL",
                "Connect players across the pitch. "
                "Recognise when central progression "
                "is available and when to move the ball "
                "to create a better opportunity."
            )
        ]

        for title, detail in channels:
            st.markdown(
                f"<div class='card'>"
                f"<b>{title}</b><br>"
                f"<small>{detail}</small>"
                f"</div>",
                unsafe_allow_html=True
            )

    with c2:
        st.markdown(
            "<div class='quote-block'>"
            "Width stretches the opposition. "
            "Movement creates space. "
            "Intelligent positioning creates "
            "opportunities to penetrate."
            "<br><br>"
            "We use all five channels to create "
            "passing options and challenge "
            "the opposition's defensive structure."
            "</div>",
            unsafe_allow_html=True
        )



with tabs[2]:
    st.markdown("### ZONES & CHANNELS")

    img = get_img("pitch_zones_channels.png")
    if img:
        st.image(img, use_container_width=True)
    else:
        st.warning("Combined Zones & Channels image not found.")

    st.markdown(
        "<div class='quote-block'>"
        "Horizontal zones help us recognise "
        "where we are progressing towards goal. "
        "Vertical channels help us recognise "
        "where we can create space across the pitch."
        "<br><br>"
        "Together, they provide reference points "
        "for positioning, support and decision-making."
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### HOW WE USE PITCH GEOGRAPHY")

    examples = [
        (
            "BUILDING THROUGH ZONE 1",
            "Our centre backs and goalkeeper create "
            "passing options to overcome pressure. "
            "The #6 provides support while teammates "
            "recognise opportunities to receive beyond "
            "the opposition's first line."
        ),
        (
            "PROGRESSING THROUGH ZONE 2",
            "A fullback receives in the wide channel. "
            "The winger provides depth, the #8 offers "
            "a passing option in the half-space, "
            "and the #6 supports underneath. "
            "The player on the ball recognises "
            "the best option to progress."
        ),
        (
            "CREATING IN ZONE 3",
            "A midfielder receives between the lines "
            "in a half-space. The #9 threatens "
            "the space behind while the winger "
            "provides width or makes a penetrating run. "
            "Their movements create different "
            "solutions for the player on the ball."
        ),
        (
            "FINISHING IN ZONE 4",
            "Players attack the penalty area with "
            "appropriate timing and numbers. "
            "Supporting players provide options "
            "for combinations, cutbacks and rebounds, "
            "while others maintain defensive balance."
        )
    ]

    for title, detail in examples:
        st.markdown(
            f"<div class='card'>"
            f"<b>{title}</b><br>"
            f"<small>{detail}</small>"
            f"</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "<b>THE PRINCIPLE</b>"
        "<br><br>"
        "Understand the space. Recognise the opportunity. "
        "Make the decision."
        "<br><br>"
        "We want intelligent players who understand "
        "the game, not players who simply follow "
        "pre-determined movements."
        "</div>",
        unsafe_allow_html=True
    )
