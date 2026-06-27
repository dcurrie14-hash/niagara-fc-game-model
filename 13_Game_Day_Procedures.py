import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand

st.set_page_config(page_title="Game Day Procedures | Niagara FC", page_icon="📋", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# GAME DAY PROCEDURES")
st.markdown("<div class='quote-block'>Match day is not where we introduce new ideas. The work has already been completed. Match day is an opportunity for players to apply what they have learned, solve problems independently, and express themselves within the game model.</div>", unsafe_allow_html=True)

tabs = st.tabs(["📋 Pre-Match","🔄 Selection & Subs","🏃 Warm-Up","⏸️ Half-Time","📊 Post-Match"])

# ═══════════════════════════════════════════════════
# TAB 1 — PRE-MATCH
# ═══════════════════════════════════════════════════
with tabs[0]:

    st.markdown("""
    <div style='background:#0D1B2A;border-left:6px solid #FFD700;padding:18px 24px;
    border-radius:0 8px 8px 0;margin:16px 0;'>
    <div style='font-family:Oswald,sans-serif;font-size:1.3em;color:#FFD700;
    font-weight:700;letter-spacing:1px;'>🎯 OBJECTIVE</div>
    <div style='color:#F5F5F5;font-size:1.05em;margin-top:8px;line-height:1.6;'>
    The objective is to create clarity rather than pressure.
    </div></div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### MATCH STAFF RESPONSIBILITIES")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown("#### Manager")
        for item in ["Administration","Team sheets","Match paperwork"]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)
    with s2:
        st.markdown("#### Assistant Coach")
        for item in ["Bench management","Substitutions","Player communication"]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)
    with s3:
        st.markdown("#### Medical Staff")
        for item in ["Player treatment","Readiness","Injury management"]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)
    with s4:
        st.markdown("#### Head Coach")
        for item in ["Players","Match management","Decision making"]:
            st.markdown(f"<div class='card card-gold'>→ {item}</div>", unsafe_allow_html=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🗣 Discussion")
        st.markdown("**Revisit the Weekly Objective**")
        for item in [
            "What did we work on this week?",
            "What problem were we trying to solve?",
            "What does success look like today?",
        ]:
            st.markdown(f"<div class='card'>→ {item}</div>", unsafe_allow_html=True)

        st.markdown("**⚽ Key Principles**")
        for item in [
            "Play forward, run forward",
            "Protect the middle",
            "Counter-press after loss",
            "Arrive with numbers",
            "Attack before they recover",
        ]:
            st.markdown(f"<div class='card card-gold'>→ {item}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("#### 🧠 Mindset")
        st.markdown("**Unit Discussions**")
        for item in [
            "Role-specific responsibilities",
            "Match-specific tactical reminders",
            "Opposition considerations",
            "Questions and player clarification",
        ]:
            st.markdown(f"<div class='card card-green'>→ {item}</div>", unsafe_allow_html=True)

        st.markdown("**Players Leave Knowing**")
        for item in [
            "Their role within today's game plan",
            "The key behaviours we are looking for",
            "The principles that guide their decisions",
            "The confidence to apply what they have practised",
        ]:
            st.markdown(f"<div class='card'>→ {item}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("#### Staff Preparation")
    for item in [
        "Confirm match administration and environment are ready",
        "Confirm Veo is functioning before kick-off",
        "Assistant coach and manager operate independently — coaching staff focus on players",
    ]:
        st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 2 — SELECTION & SUBS
# ═══════════════════════════════════════════════════
with tabs[1]:

    st.markdown("""
    <div style='background:#0D1B2A;border-left:6px solid #FFD700;padding:18px 24px;
    border-radius:0 8px 8px 0;margin:16px 0;'>
    <div style='font-family:Oswald,sans-serif;font-size:1.3em;color:#FFD700;
    font-weight:700;letter-spacing:1px;'>🎯 OBJECTIVE</div>
    <div style='color:#F5F5F5;font-size:1.05em;margin-top:8px;line-height:1.6;'>
    A player not starting is not a player being punished. Every player is expected to remain engaged,
    support teammates, and be fully prepared to influence the game when called upon.
    </div></div>""", unsafe_allow_html=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### 🗣 Individual Conversations")
        st.markdown("Every player not starting receives a brief 1-on-1 before the game. No player is left guessing.")
        for item in [
            "The reason for the decision",
            "Their role within today's game plan",
            "What I need from them when they enter",
            "The impact they can have on the game",
        ]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("#### ⚽ Substitution Philosophy")
        st.markdown("Substitutions are planned, but always influenced by the needs of the game.")
        for item in [
            "Match demands and game state",
            "Physical load and fatigue",
            "Tactical requirements",
            "Player development opportunities",
            "Training attendance and commitment",
            "Team standards",
        ]:
            st.markdown(f"<div class='card'>→ {item}</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 3 — WARM-UP
# ═══════════════════════════════════════════════════
with tabs[2]:

    st.markdown("""
    <div style='background:#0D1B2A;border-left:6px solid #FFD700;padding:18px 24px;
    border-radius:0 8px 8px 0;margin:16px 0;'>
    <div style='font-family:Oswald,sans-serif;font-size:1.3em;color:#FFD700;
    font-weight:700;letter-spacing:1px;'>🎯 OBJECTIVE</div>
    <div style='color:#F5F5F5;font-size:1.05em;margin-top:8px;line-height:1.6;'>
    The objective is to allow players to take ownership of their own readiness.
    </div></div>""", unsafe_allow_html=True)

    st.divider()
    for phase, title, desc, clr in [
        ("Phase 1","Movement Preparation","Dynamic mobility, activation, and injury prevention.","card-red"),
        ("Phase 2","Technical Preparation","Ball mastery, scanning, and decision-making.","card-blue"),
        ("Phase 3","Football Actions","Position-specific actions linked to the game plan.","card-gold"),
        ("Phase 4","Match Intensity","Short competitive actions — prepare for the speed and intensity of the game.","card-green"),
    ]:
        st.markdown(f"<div class='{clr}'><b>{phase} — {title}</b><br><small>{desc}</small></div>", unsafe_allow_html=True)

    st.markdown("""<div class='card' style='margin-top:0.5rem;'>
    <b>Phase 5 — Player Ownership</b><br><br>
    The final five minutes belong to the players. Each player completes the preparation they feel they need —
    extra touches, passing, shooting, stretching, or mental preparation.
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 4 — HALF-TIME
# ═══════════════════════════════════════════════════
with tabs[3]:

    st.markdown("""
    <div style='background:#0D1B2A;border-left:6px solid #FFD700;padding:18px 24px;
    border-radius:0 8px 8px 0;margin:16px 0;'>
    <div style='font-family:Oswald,sans-serif;font-size:1.3em;color:#FFD700;
    font-weight:700;letter-spacing:1px;'>🎯 OBJECTIVE</div>
    <div style='color:#F5F5F5;font-size:1.05em;margin-top:8px;line-height:1.6;'>
    The goal is not simply to provide answers — it is to develop players who can recognise problems
    and adapt independently within the game.
    </div></div>""", unsafe_allow_html=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Half-Time Process")
        for phase, title, desc, clr in [
            ("Phase 1","Recovery","Physical and emotional recovery — give players space.","card-blue"),
            ("Phase 2","Player Reflection","Players speak first — coaches listen.","card-gold"),
            ("Phase 3","Coaching Adjustments","Key observations and no more than 2-3 team messages.","card-red"),
            ("Phase 4","Unit Discussions","Role-specific adjustments in smaller groups where needed.","card-green"),
        ]:
            st.markdown(f"<div class='{clr}'><b>{phase} — {title}</b><br><small>{desc}</small></div>", unsafe_allow_html=True)

    with c2:
        st.markdown("#### 🗣 Player Reflection Questions")
        for item in [
            "How do you feel?",
            "What are they giving us?",
            "What are you seeing?",
            "What is working?",
            "What problems are we facing?",
            "What solutions do you see?",
        ]:
            st.markdown(f"<div class='card card-gold'>→ {item}</div>", unsafe_allow_html=True)

        st.markdown("#### 🧠 Half-Time Principles")
        for item in [
            "Focus on solutions, not mistakes",
            "Player input before coach input",
            "Reinforce what is working",
            "Clarity over quantity",
            "No more than 2-3 key messages",
        ]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 5 — POST-MATCH
# ═══════════════════════════════════════════════════
with tabs[4]:

    st.markdown("""
    <div style='background:#0D1B2A;border-left:6px solid #FFD700;padding:18px 24px;
    border-radius:0 8px 8px 0;margin:16px 0;'>
    <div style='font-family:Oswald,sans-serif;font-size:1.3em;color:#FFD700;
    font-weight:700;letter-spacing:1px;'>🎯 OBJECTIVE</div>
    <div style='color:#F5F5F5;font-size:1.05em;margin-top:8px;line-height:1.6;'>
    The match provides information. The result may influence emotions, but the review process focuses
    on behaviours, decisions, and learning opportunities that support long-term player development.
    </div></div>""", unsafe_allow_html=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Immediate Post-Match")
        st.markdown("Intentionally brief — emotions run high, information won't land.")
        for item in [
            "Acknowledge effort and commitment",
            "Reinforce one or two key positives",
            "Thank players, staff, opponents, and officials",
            "Establish the next point of contact",
        ]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("#### Formal Review — Following Day")
        st.markdown("Using match footage, coaching observations, and player reflections:")
        for item in [
            "The weekly objective",
            "Application of our game model",
            "Tactical principles and key moments",
            "Individual and collective learning opportunities",
        ]:
            st.markdown(f"<div class='card card-green'>→ {item}</div>", unsafe_allow_html=True)

    st.markdown("""<div class='quote-block' style='margin-top:1.5rem;'>
    Players are encouraged to reflect on their own performance before receiving detailed feedback.
    Creating space between the match and the analysis process leads to more productive conversations
    and more objective reflection.
    </div>""", unsafe_allow_html=True)