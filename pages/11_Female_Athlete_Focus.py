
import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, NAVY

st.set_page_config(page_title="Female Athlete Focus | Niagara FC", page_icon="♀", layout="wide")
apply_css()
sidebar_brand()


def cards(items, css_class="card", symbol="✔"):
    for item in items:
        st.markdown(f"<div class='{css_class}'>{symbol} {item}</div>", unsafe_allow_html=True)


st.markdown("# FEMALE ATHLETE FOCUS")
st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1em;color:#4169E1;letter-spacing:2px;margin-bottom:16px;'>COACHING THE COMPLETE FEMALE FOOTBALLER</div>", unsafe_allow_html=True)

st.markdown("""<div class='quote-block'>
We aim to develop confident, capable, intelligent, and resilient female footballers. We combine high expectations with individual support, recognising that every athlete develops differently. Our approach challenges players to compete, take ownership of their development, and support the growth of those around them.
</div>""", unsafe_allow_html=True)

tabs = st.tabs([
    "🧠 Coaching Philosophy",
    "💬 Communication & Wellbeing",
    "🏃 Physical Development",
    "📊 Menstrual Health",
    "🥗 Fuel & Recovery",
])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### COACHING PRINCIPLES")
        cards([
            "Psychological safety — players can ask questions, take risks, and learn from mistakes",
            "High challenge, high support — demanding standards with the guidance needed to succeed",
            "Confidence through competence — build belief through preparation, progress, and meaningful success",
            "Player ownership — take responsibility for decisions, effort, and development",
            "Competitive excellence — earn opportunities and raise the standards of teammates",
            "Resilience — respond constructively to setbacks, feedback, and adversity",
            "Guided discovery — ask questions that develop independent thinkers",
        ])
    with c2:
        st.markdown("### DEVELOPMENT PRIORITIES")
        cards([
            "Technical confidence — execute skills under pressure",
            "Tactical intelligence — recognise problems and make effective decisions",
            "Physical capability — strength, speed, power, and movement quality",
            "Psychological resilience — manage setbacks and keep learning",
            "Leadership — positively influence teammates and the environment",
            "Identity and enjoyment — pride in the team and a lasting connection to football",
        ], "card", "⚡")
    st.markdown("<div class='quote-block'>We develop the footballer and the person. A supportive environment and a competitive environment are not opposites — players need both.</div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("""<div class='quote-block'>Players deserve a voice in their development. Clear expectations, honest feedback, respectful relationships, and appropriate privacy help athletes communicate what they need while remaining accountable for their growth.</div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### OUR COACHING COMMITMENTS")
        cards([
            "Listen without judgment when players raise concerns",
            "Give clear, specific feedback about actions and decisions — not personalities",
            "Explain expectations and help players understand the reasons behind training",
            "Challenge every player while recognising individual circumstances",
            "Discuss sensitive health and wellbeing concerns privately and appropriately",
            "Never require athletes to share menstrual information or other private health details to justify playing time",
        ], "card card-blue")
    with c2:
        st.markdown("### PLAYER OWNERSHIP")
        cards([
            "Communicate honestly about readiness, discomfort, or concerns",
            "Ask questions and seek support when needed",
            "Respond to feedback and take responsibility for improvement",
            "Respect teammates' experiences and privacy",
            "Build healthy habits around preparation, recovery, and wellbeing",
            "Understand that support and accountability can exist together",
        ], "card card-gold")
    st.markdown("""<div class='quote-block'>Personal health information should be handled discreetly, with safeguarding and medical support when appropriate. Privacy is respected, while recognising that serious safety concerns may need to be shared with the appropriate people.</div>""", unsafe_allow_html=True)


with tabs[2]:
    st.markdown("""<div class='quote-block'>Female footballers should not be protected from physical challenge; they should be prepared for it. Well-designed, progressive training develops performance and helps reduce avoidable injury risk.</div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### BUILDING PERFORMANCE")
        cards([
            "Strength — develop the capacity to sprint, jump, shield, and compete in duels",
            "Speed — practise acceleration, sprint mechanics, and efficient deceleration",
            "Power — progressively develop jumping, landing, and explosive movement",
            "Movement quality — practise balance, cutting, coordination, and change of direction",
            "Individual progression — consider growth, maturation, experience, and readiness",
        ])
    with c2:
        st.markdown("### REDUCING INJURY RISK")
        cards([
            "Female footballers have an elevated ACL injury risk in many comparable playing settings",
            "Use a consistent, structured neuromuscular warm-up, such as FIFA 11+ or an age-appropriate equivalent",
            "Include strength, balance, landing, deceleration, and change-of-direction training",
            "Progress training demands appropriately and respond to fatigue, pain, and recovery needs",
            "Injury prevention is a consistent team practice, not something reserved for players with symptoms",
        ], "card card-blue", "✓")
    st.markdown("""<div class='quote-block'>Our goal is to develop strong, powerful, adaptable footballers. Strength training is a performance tool as well as one part of injury-risk reduction.</div>""", unsafe_allow_html=True)

with tabs[3]:
    st.markdown("### MENSTRUAL HEALTH & PERFORMANCE")
    st.markdown("""<div class='quote-block'>The menstrual cycle is a normal part of health and development. Experiences vary between players and from month to month. A predicted cycle phase does not reliably tell us how an athlete will perform or what training intensity she should complete. We listen to the individual and respond to symptoms, readiness, and wellbeing.</div>""", unsafe_allow_html=True)

    phases = [
        ("Menstrual", "Period begins", "#5B9CF5", "Some players experience cramps, fatigue, or discomfort. Others train and compete normally."),
        ("Follicular", "Before ovulation", "#5CCF91", "Hormone levels change through this phase. Energy and performance responses vary between individuals."),
        ("Ovulation", "Timing varies", "#F7C64B", "Ovulation is a normal hormonal event, not a reliable predictor of peak performance or injury risk."),
        ("Luteal", "After ovulation", "#FB9562", "Some players notice changes in mood, sleep, energy, or physical comfort; others notice little change."),
    ]
    cols = st.columns(4)
    for col, (name, timing, colour, description) in zip(cols, phases):
        with col:
            st.markdown(f"""<div style='background:{NAVY};border-top:4px solid {colour};border-radius:6px;padding:14px;min-height:205px;'>
            <div style='font-family:Oswald,sans-serif;font-weight:700;color:{colour};font-size:1.1em;'>{name}</div>
            <div style='color:#c5d1df;font-size:0.8em;margin:6px 0 12px;'>{timing}</div>
            <div style='color:white;font-size:0.88em;line-height:1.55;'>{description}</div>
            </div>""", unsafe_allow_html=True)
    st.caption("This is a simplified educational overview. Cycle length and phase timing vary, particularly during adolescence; hormonal contraception can also change cycle patterns.")
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### OUR APPROACH")
        cards([
            "Ask about overall wellness and readiness without making assumptions",
            "Respond to significant symptoms and individual training needs",
            "Keep menstrual conversations private, respectful, and optional",
            "Never require cycle tracking or disclosure as a condition of participation or selection",
        ], "card card-blue")
    with c2:
        st.markdown("### WHAT PLAYERS SHOULD KNOW")
        cards([
            "Your experience may differ from teammates' experiences",
            "Tracking personal patterns is optional and should remain under your control",
            "Severe pain, persistent symptoms, or absent or very irregular periods deserve medical advice",
            "You can seek support without discussing personal details with the whole team",
        ], "card card-gold")
    st.markdown("""<div class='quote-block'>Coach the athlete in front of you. Research informs our decisions, but never replaces listening to the individual.</div>""", unsafe_allow_html=True)


with tabs[4]:
    st.markdown("""<div class='quote-block'>Athletes need enough energy to support football, recovery, and healthy growth. Fuel, hydration, sleep, and rest are essential parts of development — not optional extras.</div>""", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### FUEL TO PERFORM")
        cards([
            "Eat enough to support both training demands and ongoing growth",
            "Regular meals and snacks help provide energy across the day",
            "Carbohydrates support football activity; protein supports growth and recovery",
            "Hydration matters before, during, and after training",
            "Focus on health, strength, and performance — not weight or appearance",
        ])
    with c2:
        st.markdown("### RECOVER TO DEVELOP")
        cards([
            "Prioritise sufficient sleep and consistent sleep routines",
            "Balance demanding sessions with appropriate recovery",
            "Recognise that school, stress, illness, and other commitments affect readiness",
            "Persistent fatigue, repeated injuries, or menstrual changes can signal a need for health support",
            "Low energy availability can affect health and performance; seek qualified medical or sports nutrition guidance for concerns",
        ], "card card-blue")
    st.markdown("""<div class='quote-block'>Coaches encourage healthy habits and recognise concerns; they do not diagnose medical conditions or prescribe restrictive diets.</div>""", unsafe_allow_html=True)

st.divider()
st.markdown("### OUR COMMITMENT TO PLAYERS & FAMILIES")
st.markdown("""<div class='quote-block'>We challenge our players to meet high standards while recognising their individual developmental needs. We aim to create an environment where female footballers feel informed, respected, supported, and empowered to take ownership of their development.</div>""", unsafe_allow_html=True)

with st.expander("📚 Research & Further Reading"):
    st.markdown("""
- [IOC consensus statement on Relative Energy Deficiency in Sport (REDs), 2023](https://bjsm.bmj.com/content/57/17/1073)
- [Systematic review: injury prevention in female football](https://pubmed.ncbi.nlm.nih.gov/32253193/)
- [FIFA 11+ injury prevention resources](https://www.fifamedicalnetwork.com/)

These resources provide background information; individual health concerns should be discussed with qualified professionals.
""")


