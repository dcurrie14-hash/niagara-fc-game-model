
import streamlit as st
import sys
import os
from html import escape

sys.path.insert(
    0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from utils import apply_css, sidebar_brand

st.set_page_config(
    page_title="Game Day Procedures | Niagara FC",
    page_icon="📋",
    layout="wide"
)

apply_css()
sidebar_brand()

# Page-specific styling
st.markdown("""
<style>
.gd-objective {
    background: #0D1B2A;
    border-left: 4px solid #4169E1;
    padding: 15px 20px;
    border-radius: 0 6px 6px 0;
    margin: 12px 0 22px;
}
.gd-objective-title {
    font-family: 'Oswald', sans-serif;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 1px;
    color: #C1C7CE;
    margin-bottom: 7px;
}
.gd-objective-text {
    color: #F5F5F5;
    line-height: 1.65;
    font-size: 0.95rem;
}
.gd-panel {
    background: #0D1B2A;
    border-left: 3px solid #4169E1;
    padding: 14px 17px;
    border-radius: 0 6px 6px 0;
    margin: 8px 0 14px;
    color: #F5F5F5;
}
.gd-panel-title {
    font-family: 'Oswald', sans-serif;
    font-size: 1.12rem;
    color: #D0D5DA;
    margin-bottom: 8px;
    font-weight: 600;
}
.gd-list {
    margin: 0;
    padding-left: 18px;
    line-height: 1.85;
    font-size: 0.88rem;
}
.gd-list li {
    padding: 2px 0;
    color: #F5F5F5;
}
.gd-panel-text {
    font-size: 0.88rem;
    line-height: 1.7;
    color: #F5F5F5;
}
.gd-phase {
    background: #0D1B2A;
    border-left: 3px solid #4169E1;
    border-radius: 0 6px 6px 0;
    padding: 13px 17px;
    margin: 8px 0;
}
.gd-phase-title {
    font-weight: 600;
    font-size: 0.93rem;
    color: #F5F5F5;
    margin-bottom: 4px;
}
.gd-phase-desc {
    color: #C1C7CE;
    font-size: 0.87rem;
    line-height: 1.6;
}
.gd-section {
    font-family: 'Oswald', sans-serif;
    font-size: 1.3rem;
    color: #D0D5DA;
    letter-spacing: 0.5px;
    margin: 8px 0 12px;
}
</style>
""", unsafe_allow_html=True)


# Reusable components

def objective(text):
    st.markdown(
        "<div class='gd-objective'>"
        "<div class='gd-objective-title'>OBJECTIVE</div>"
        f"<div class='gd-objective-text'>{escape(text)}</div>"
        "</div>",
        unsafe_allow_html=True
    )


def panel(title, items):
    rows = "".join(
        f"<li>{escape(item)}</li>"
        for item in items
    )
    st.markdown(
        "<div class='gd-panel'>"
        f"<div class='gd-panel-title'>{escape(title)}</div>"
        f"<ul class='gd-list'>{rows}</ul>"
        "</div>",
        unsafe_allow_html=True
    )


def phase(number, title, description):
    st.markdown(
        "<div class='gd-phase'>"
        f"<div class='gd-phase-title'>"
        f"Phase {number} — {escape(title)}</div>"
        f"<div class='gd-phase-desc'>"
        f"{escape(description)}</div>"
        "</div>",
        unsafe_allow_html=True
    )


def section(title):
    st.markdown(
        f"<div class='gd-section'>{escape(title)}</div>",
        unsafe_allow_html=True
    )


# PAGE HEADER

st.markdown("# GAME DAY PROCEDURES")

st.markdown(
    "<div class='quote-block'>"
    "Match day is not where we introduce new ideas. "
    "The work has already been completed. "
    "Match day is an opportunity for players to apply "
    "what they have learned, solve problems independently, "
    "and express themselves within the game model."
    "</div>",
    unsafe_allow_html=True
)

tabs = st.tabs([
    "Pre-Match",
    "Selection & Subs",
    "Warm-Up",
    "Half-Time",
    "Post-Match"
])


# ==================================================
# TAB 1 — PRE-MATCH
# ==================================================

with tabs[0]:

    objective(
        "The objective is to create clarity rather than pressure."
    )

    st.markdown("### MATCH STAFF RESPONSIBILITIES")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        panel("Manager", [
            "Administration",
            "Team sheets",
            "Match paperwork"
        ])

    with s2:
        panel("Assistant Coach", [
            "Bench management",
            "Substitutions",
            "Player communication"
        ])

    with s3:
        panel("Medical Staff", [
            "Player treatment",
            "Readiness",
            "Injury management"
        ])

    with s4:
        panel("Head Coach", [
            "Players",
            "Match management",
            "Decision making"
        ])

    st.divider()

    c1, c2 = st.columns(2, gap="large")

    with c1:

        section("Discussion")

        panel("Revisit the Weekly Objective", [
            "What did we work on this week?",
            "What problem were we trying to solve?",
            "What does success look like today?"
        ])

        panel("Key Principles", [
            "Play forward, run forward",
            "Protect the middle",
            "Counter-press after loss",
            "Arrive with numbers",
            "Attack before they recover"
        ])

    with c2:

        section("Mindset")

        panel("Unit Discussions", [
            "Role-specific responsibilities",
            "Match-specific tactical reminders",
            "Opposition considerations",
            "Questions and player clarification"
        ])

        panel("Players Leave Knowing", [
            "Their role within today's game plan",
            "The key behaviours we are looking for",
            "The principles that guide their decisions",
            "The confidence to apply what they have practised"
        ])

    st.divider()

    section("Staff Preparation")

    panel("Match-Day Preparation", [
        "Confirm match administration and environment are ready",
        "Confirm Veo is functioning before kick-off",
        "Assistant coach and manager operate independently — coaching staff focus on players"
    ])


# ==================================================
# TAB 2 — SELECTION & SUBS
# ==================================================

with tabs[1]:

    objective(
        "A player not starting is not a player being punished. "
        "Every player is expected to remain engaged, "
        "support teammates, and be fully prepared to influence "
        "the game when called upon."
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:

        section("Individual Conversations")

        st.markdown(
            "Every player not starting receives a brief "
            "1-on-1 before the game. No player is left guessing."
        )

        panel("Conversation Focus", [
            "The reason for the decision",
            "Their role within today's game plan",
            "What I need from them when they enter",
            "The impact they can have on the game"
        ])

    with c2:

        section("Substitution Philosophy")

        st.markdown(
            "Substitutions are planned, but always influenced "
            "by the needs of the game."
        )

        panel("Considerations", [
            "Match demands and game state",
            "Physical load and fatigue",
            "Tactical requirements",
            "Player development opportunities",
            "Training attendance and commitment",
            "Team standards"
        ])


# ==================================================
# TAB 3 — WARM-UP
# ==================================================

with tabs[2]:

    objective(
        "The objective is to allow players to take "
        "ownership of their own readiness."
    )

    phase(
        1,
        "Movement Preparation",
        "Dynamic mobility, activation, and injury prevention."
    )

    phase(
        2,
        "Technical Preparation",
        "Ball mastery, scanning, and decision-making."
    )

    phase(
        3,
        "Football Actions",
        "Position-specific actions linked to the game plan."
    )

    phase(
        4,
        "Match Intensity",
        "Short competitive actions — prepare for the "
        "speed and intensity of the game."
    )

    phase(
        5,
        "Player Ownership",
        "The final five minutes belong to the players. "
        "Each player completes the preparation they feel "
        "they need — extra touches, passing, shooting, "
        "stretching, or mental preparation."
    )


# ==================================================
# TAB 4 — HALF-TIME
# ==================================================

with tabs[3]:

    objective(
        "The goal is not simply to provide answers — "
        "it is to develop players who can recognise problems "
        "and adapt independently within the game."
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:

        section("Half-Time Process")

        phase(
            1,
            "Recovery",
            "Physical and emotional recovery — give players space."
        )

        phase(
            2,
            "Player Reflection",
            "Players speak first — coaches listen."
        )

        phase(
            3,
            "Coaching Adjustments",
            "Key observations and no more than 2-3 team messages."
        )

        phase(
            4,
            "Unit Discussions",
            "Role-specific adjustments in smaller groups where needed."
        )

    with c2:

        section("Player Reflection")

        panel("Reflection Questions", [
            "How do you feel?",
            "What are they giving us?",
            "What are you seeing?",
            "What is working?",
            "What problems are we facing?",
            "What solutions do you see?"
        ])

        panel("Half-Time Principles", [
            "Focus on solutions, not mistakes",
            "Player input before coach input",
            "Reinforce what is working",
            "Clarity over quantity",
            "No more than 2-3 key messages"
        ])


# ==================================================
# TAB 5 — POST-MATCH
# ==================================================

with tabs[4]:

    objective(
        "The match provides information. The result may "
        "influence emotions, but the review process focuses "
        "on behaviours, decisions, and learning opportunities "
        "that support long-term player development."
    )

    c1, c2 = st.columns(2, gap="large")

    with c1:

        section("Immediate Post-Match")

        st.markdown(
            "Intentionally brief — emotions run high, "
            "information won't land."
        )

        panel("Immediate Priorities", [
            "Acknowledge effort and commitment",
            "Reinforce one or two key positives",
            "Thank players, staff, opponents, and officials",
            "Establish the next point of contact"
        ])

    with c2:

        section("Formal Review — Following Day")

        st.markdown(
            "Using match footage, coaching observations, "
            "and player reflections:"
        )

        panel("Review Focus", [
            "The weekly objective",
            "Application of our game model",
            "Tactical principles and key moments",
            "Individual and collective learning opportunities"
        ])

    st.markdown(
        "<div class='quote-block' style='margin-top:1.5rem;'>"
        "Players are encouraged to reflect on their own "
        "performance before receiving detailed feedback. "
        "Creating space between the match and the analysis "
        "process leads to more productive conversations "
        "and more objective reflection."
        "</div>",
        unsafe_allow_html=True
    )
