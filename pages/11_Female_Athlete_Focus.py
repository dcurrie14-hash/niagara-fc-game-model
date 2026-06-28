import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, CYCLE_PHASES, NAVY

st.set_page_config(page_title="Female Athlete Focus | Niagara FC", page_icon="♀", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# FEMALE ATHLETE FOCUS")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;color:#4169E1;letter-spacing:2px;margin-bottom:16px;'>COACHING THE COMPLETE FEMALE ATHLETE</div>", unsafe_allow_html=True)

tabs = st.tabs(["🧠 Coaching Philosophy","💬 Communication","🏃 Physical Development","📊 Cycle Awareness"])

# ═══════════════════════════════════════════════════
# TAB 1 — COACHING PHILOSOPHY
# ═══════════════════════════════════════════════════
with tabs[0]:
    st.markdown("<div class='quote-block'>Effective coaching begins by understanding the individual athlete. Female footballers experience unique physiological, psychological, and social demands that influence development, but coaching decisions should always be based on the player in front of you — not assumptions.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### COACHING PRINCIPLES")
        for item in [
            "Create a psychologically safe environment where players feel comfortable taking risks and making mistakes",
            "Build confidence through competence, ownership, and success experiences",
            "Provide high challenge with high support",
            "Develop intrinsic motivation — players who love the game, not just the result",
            "Use questioning and guided discovery to develop independent thinkers",
            "Celebrate courage — reward the attempt, not only the outcome",
            "Coach the athlete in front of you, not assumptions about gender",
        ]:
            st.markdown(f"<div class='card'>✔ {item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("### DEVELOPMENT PRIORITIES")
        for item, cls in [
            ("Technical confidence — comfort on the ball under pressure","card"),
            ("Tactical intelligence — recognise and solve problems independently","card"),
            ("Physical capability — strength, speed, power, and resilience","card-orange"),
            ("Psychological resilience — respond positively to mistakes and setbacks","card"),
            ("Leadership — every player can influence the environment in different ways","card"),
            ("Identity — pride in the collective, belief in herself","card-orange"),
        ]:
            st.markdown(f"<div class='{cls}' style='color:white !important;'>⚡ <span style='color:white;'>{item}</span></div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 2 — COMMUNICATION
# ═══════════════════════════════════════════════════
with tabs[1]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### ✅ Effective Behaviours")
        for item in [
            "Use questioning and guided discovery over direct instruction",
            "Be consistent — players thrive when expectations are clear",
            "Give specific, actionable feedback",
            "Address behaviours rather than personalities",
            "Address the group before the individual in difficult moments",
            "Acknowledge effort, learning, and process",
            "Use player names and build individual relationships",
            "Check in regularly through informal conversations",
            "Listen first when players communicate concerns",
        ]:
            st.markdown(f"<div class='card'>✔ {item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### ❌ Behaviours to Avoid")
        for item in [
            "Public criticism or embarrassment",
            "Comparing players negatively",
            "Focusing only on mistakes",
            "Sarcasm that damages trust",
            "Dismissing emotional responses",
            "Making assumptions about confidence, motivation, or commitment",
        ]:
            st.markdown(f"<div class='card card-red'>✗ {item}</div>", unsafe_allow_html=True)

    st.markdown("""<div class='quote-block' style='margin-top:1rem;'>
    Female athletes are not a homogeneous group. Strong coaching relationships are built through communication, trust,
    and understanding the individual needs of each player.
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 3 — PHYSICAL DEVELOPMENT
# ═══════════════════════════════════════════════════
with tabs[2]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### ⚠️ Injury Prevention")
        for item in [
            "ACL injury risk is 3–6× higher in female athletes — warm-up is non-negotiable",
            "FIFA 11+ or similar prevention warm-up every session",
            "Emphasise landing mechanics, change of direction, and knee alignment",
            "Strengthen hip abductors and glutes — they protect the knee joint",
            "Joint laxity increases around ovulation — monitor individual response",
        ]:
            st.markdown(f"<div class='card card-red'>⚠️ {item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### 💪 Developing Powerful Female Footballers")
        for item in [
            "Strength training is a performance tool, not just an injury-prevention strategy",
            "Build strength foundations through squatting, lunging, hinging, pushing, and pulling",
            "Develop speed through acceleration, deceleration, and sprint mechanics",
            "Train power through jumping, landing, and change-of-direction activities",
            "Recovery is part of performance — sleep, nutrition, hydration, and stress management matter",
            "High standards and high support should exist together",
        ]:
            st.markdown(f"<div class='card'>💪 {item}</div>", unsafe_allow_html=True)

    st.markdown("""<div class='quote-block' style='margin-top:1rem;'>
    Female athletes should not be protected from challenge. They should be prepared for it through appropriate
    physical development and progressive exposure to training demands.
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 4 — CYCLE AWARENESS
# ═══════════════════════════════════════════════════
with tabs[3]:
    st.markdown("### MENSTRUAL CYCLE & PERFORMANCE")
    st.markdown("""<div class='quote-block'>
    Understanding the menstrual cycle helps us support players, manage training load, and reduce injury risk.
    Individual responses vary significantly, and the athlete's experience always takes priority over predicted phase responses.
    Training adapts to the player — not the other way around.
    </div>""", unsafe_allow_html=True)

    ph_cols = st.columns(4)
    for col, (ph, data) in zip(ph_cols, CYCLE_PHASES.items()):
        with col:
            label = ph.split("(")[0].strip()
            days  = "(" + ph.split("(")[1] if "(" in ph else ""
            intensity = data['intensity']
            if ph.startswith("🟡"):
                intensity = "High (monitor individual response)"
            if ph.startswith("🟡") and "Peak" in data['focus']:
                focus_display = "Peak — coordination and power may be highest"
            else:
                focus_display = data['energy']
            st.markdown(f"<div style='background:{NAVY};border-top:4px solid {data['color']};border-radius:6px;padding:12px;height:100%;'><div style='font-family:Oswald,sans-serif;font-size:0.9em;font-weight:700;color:{data['color']};margin-bottom:8px;'>{label}<br><span style='font-size:0.8em;opacity:0.8;'>{days}</span></div><div style='font-size:0.8em;color:#ccc;margin-bottom:6px;'>⚡ {focus_display}</div><div style='font-size:0.8em;color:white;font-weight:600;margin-bottom:6px;'>{data['focus']}</div><div style='font-size:0.75em;color:#aaa;'>Intensity: {intensity}</div></div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("#### Coach-Athlete Communication")
    for item in [
        "Normalise the conversation — create an environment where athletes can speak openly",
        "Never make assumptions — some athletes have irregular cycles or hormonal conditions",
        "A simple weekly check-in ('How's your energy this week?') goes a long way",
        "Encourage athletes to track their cycle — awareness is the first step",
        "Adjust training loads and communication style based on what athletes tell you",
        "Respect privacy — individual conversations, not group discussions",
    ]:
        st.markdown(f"<div class='card card-blue'>♀ {item}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("#### Athlete Ownership")
    for item in [
        "Players are encouraged to understand their own bodies and performance patterns",
        "Wellness conversations are collaborative rather than coach-directed",
        "Players are educated about recovery, readiness, and training load",
        "Communication is always optional, confidential, and player-led",
        "Individual experience is more important than textbook expectations",
    ]:
        st.markdown(f"<div class='card card-gold'>♀ {item}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("""<div class='quote-block'>
    Every player develops differently. Our role is not to coach female footballers as a group, but to coach each athlete
    as an individual while understanding the demands unique to the female game.<br><br>
    <strong>Coach the athlete in front of you. Use research to inform your decisions, but never let it replace the individual.</strong>
    </div>""", unsafe_allow_html=True)
