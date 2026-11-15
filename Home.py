
import streamlit as st
import sys
import os

sys.path.insert(
    0,
    os.path.dirname(os.path.abspath(__file__))
)

from utils import (
    apply_css, sidebar_brand, get_img,
    ROYAL, NAVY, WHITE, RED, GOLD, ORANGE, LBLUE
)

st.set_page_config(
    page_title="Niagara FC Game Model",
    page_icon="🔵",
    layout="wide"
)

apply_css()
sidebar_brand()

logo = get_img("nfc.png")

c_logo, c_title = st.columns([1, 5])

with c_logo:
    if logo:
        st.image(logo, width=120)

with c_title:
    st.markdown("# GAME MODEL")

    st.markdown(
        "<div style='font-family:Oswald,sans-serif;"
        "font-size:1em;letter-spacing:2px;'>"
        "<span style='color:#FFFFFF;font-weight:700;'>"
        "DAVIE CURRIE</span> "
        "<span style='color:#89B4FF;'>"
        "· NIAGARA FC OPDL ·</span> "
        "<span style='color:#FFFFFF;font-weight:700;'>"
        "CONCACAF B DIPLOMA</span></div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div style='font-family:Oswald,sans-serif;"
        "font-size:1.1em;color:#1E56D6;letter-spacing:2px;'>"
        "INTENSITY · AGGRESSION · PURPOSE · "
        "FREEDOM WITHIN STRUCTURE"
        "</div>",
        unsafe_allow_html=True
    )

st.markdown(
    "<div class='quote-block'>"
    "\"The only expectation is to work hard and be all in. "
    "Development is the priority, but we still compete to win. "
    "We love players that hate to lose.\""
    "</div>",
    unsafe_allow_html=True
)

c1, c2 = st.columns([3, 2])

with c1:
    st.markdown("### OUR FOOTBALL IDENTITY")

    identity = [
        "Aggressive and forward-thinking — "
        "high tempo in and out of possession",

        "Brave in possession — play through pressure, "
        "not away from it",

        "Compact and connected defensively — "
        "protect central spaces first",

        "Competitive in every moment — "
        "love to win, hate to lose",

        "Freedom within structure — "
        "players solve problems, not coaches",

        "Structured without becoming robotic — "
        "intelligence over patterns"
    ]

    for item in identity:
        st.markdown(
            f"<div class='card'>⚡ {item}</div>",
            unsafe_allow_html=True
        )

    st.markdown(
        "<div class='quote-block'>"
        "\"We build intelligent players who can play "
        "in any system because they understand the game, "
        "not just our game.\""
        "</div>",
        unsafe_allow_html=True
    )

with c2:
    st.markdown("### WHAT WE VALUE")

    values = [
        "Intensity",
        "Accountability",
        "Courage",
        "Problem Solving",
        "Communication",
        "Leadership",
        "Coachability",
        "Resilience"
    ]

    for value in values:
        st.markdown(
            f"<span class='identity-word'>{value}</span>",
            unsafe_allow_html=True
        )



st.divider()

st.markdown("### THE 5 MOMENTS OF THE GAME")

st.markdown(
    "<div style='font-family:Oswald,sans-serif;"
    "font-size:0.95em;color:#89B4FF;"
    "letter-spacing:1px;margin-bottom:12px;'>"
    "The principles stay the same, "
    "even when the moment changes."
    "</div>",
    unsafe_allow_html=True
)

# Updated five moments diagram
img = get_img("five_moments_new.png")

if img:
    st.image(img, use_container_width=True)
else:
    st.warning(
        "Five Moments diagram not found. "
        "Upload five_moments_new.png to the main GitHub folder."
    )

st.markdown("#### OUR PRINCIPLES IN EACH MOMENT")

moments = [
    (
        "1",
        "IN POSSESSION",
        "Control and progress the ball with tempo and purpose. "
        "Play forward whenever possible.",
        ROYAL
    ),
    (
        "2",
        "DEFENSIVE TRANSITION",
        "React immediately after losing possession. "
        "Win it back on the first action or recover into shape.",
        RED
    ),
    (
        "3",
        "OUT OF POSSESSION",
        "Remain compact and connected. "
        "Deny central penetration and force play wide.",
        RED
    ),
    (
        "4",
        "ATTACKING TRANSITION",
        "Exploit the opposition's disorganisation. "
        "Recognise opportunities to play and run forward.",
        GOLD
    ),
    (
        "5",
        "SET PIECES",
        "Create and defend opportunities with organisation, "
        "purpose, and attention to detail.",
        LBLUE
    )
]

columns = st.columns(5)

for col, (num, moment, desc, clr) in zip(columns, moments):
    with col:
        st.markdown(
            f"""
            <div style='
                background:{NAVY};
                border-top:4px solid {clr};
                padding:12px;
                border-radius:6px;
                min-height:175px;
            '>
                <div style='
                    color:{clr};
                    font-weight:700;
                    font-size:0.85em;
                    margin-bottom:8px;
                '>
                    {num}. {moment}
                </div>
                <div style='
                    color:#D6DFEA;
                    font-size:0.8em;
                    line-height:1.5;
                '>
                    {desc}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )



st.divider()

st.markdown("### NON-NEGOTIABLES")

c1, c2 = st.columns(2)

with c1:
    for item in [
        "React immediately to losing possession — "
        "regain or recover.",

        "Look forward first. Recognise when to play "
        "forward and when to secure possession.",

        "Be brave on the ball. Take responsibility "
        "and find solutions under pressure."
    ]:
        st.markdown(
            f"<div class='card card-red'>🔴 {item}</div>",
            unsafe_allow_html=True
        )

with c2:
    for item in [
        "Communicate with purpose — organise, "
        "inform and support teammates.",

        "Compete with intensity and purpose — "
        "in training and matches.",

        "Anticipate, react and compete "
        "for every second ball."
    ]:
        st.markdown(
            f"<div class='card card-red'>🔴 {item}</div>",
            unsafe_allow_html=True
        )
