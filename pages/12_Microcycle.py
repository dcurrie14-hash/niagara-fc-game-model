import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img, fig_microcycle_timeline, CYCLE_PHASES, DAYS, MICRO_SCHEDULE, NAVY, ROYAL, RED, GOLD, LBLUE
import matplotlib.pyplot as plt

st.set_page_config(page_title="Microcycle | Niagara FC", page_icon="📅", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# WEEKLY MICROCYCLE")
st.markdown("""<div style='font-family:Oswald,sans-serif;font-size:1em;letter-spacing:1px;margin-bottom:16px;color:#aaa;'>
<span style='color:#E53935;font-weight:700;'>Game</span>: Sunday &nbsp;•&nbsp;
<span style='color:#89B4FF;font-weight:700;'>Recovery</span>: Monday &nbsp;•&nbsp;
<span style='color:#666;font-weight:700;'>Off</span>: Tuesday &nbsp;•&nbsp;
<span style='color:#E53935;font-weight:700;'>Main Training</span>: Wednesday &nbsp;•&nbsp;
<span style='color:#F5C518;font-weight:700;'>Tactical Application</span>: Thursday &nbsp;•&nbsp;
<span style='color:#89B4FF;font-weight:700;'>Optional Technical</span>: Friday &nbsp;•&nbsp;
<span style='color:#666;font-weight:700;'>Off</span>: Saturday
</div>""", unsafe_allow_html=True)

tabs = st.tabs(["📆 Week Structure","📊 RPE Targets","🔬 Cycle Phase Integration"])

with tabs[0]:
    fig = fig_microcycle_timeline()
    st.pyplot(fig, use_container_width=True)
    plt.close()

    st.markdown("---")
    for day in DAYS:
        d = MICRO_SCHEDULE[day]
        with st.expander(f"{d['icon']}  **{day} — {d['title']}**", expanded=(day=="Sunday")):
            st.markdown(f"<span style='color:{d['color']};font-weight:700;'>{d['rpe']}</span>", unsafe_allow_html=True)
            st.markdown(f"<div class='card' style='border-left:3px solid {d['color']};'>{d['desc']}</div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("### COACHING NOTE")
    st.markdown("""<div class='quote-block'>
    Training load is adapted based on player readiness, school sport commitments, wellness surveys, RPE feedback, and fixture congestion.
    The Canada Soccer microcycle framework provides a guide; however, session intensity and volume are adjusted to meet the realities
    of youth football and the individual needs of players.<br><br>
    Load is manipulated through activity design, including player numbers, pitch dimensions, work-to-rest ratios, constraints,
    and tactical objectives. The goal is not simply to increase running volume, but to develop football-specific capacity
    while supporting long-term player development and wellbeing.
    </div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.9em;color:#89B4FF;letter-spacing:0.5px;margin-bottom:8px;'>Training intensity and demands are adapted across the menstrual cycle. See Female Athlete Focus for full phase guidance and athlete communication principles.</div>", unsafe_allow_html=True)
    st.markdown("### Select Current Cycle Phase")
    phase_key = st.radio("", list(CYCLE_PHASES.keys()), horizontal=True, label_visibility="collapsed")
    phase = CYCLE_PHASES[phase_key]
    st.markdown(f"<div style='background:{phase['bg']};border-left:5px solid {phase['color']};padding:12px 18px;border-radius:8px;margin:10px 0 18px;'><span style='color:{phase['color']};font-size:1em;font-weight:700;'>{phase_key}</span><br><span style='color:#ccc;font-size:0.85em;'>Energy: {phase['energy']}</span> | <span style='color:white;font-weight:600;'>Intensity: </span><span style='color:{phase['color']};font-weight:700;'>{phase['intensity']}</span><br><span style='color:#aaa;font-size:0.8em;'>Focus: {phase['focus']}</span></div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("### RPE TARGETS — RATE OF PERCEIVED EXERTION")
    st.markdown("<div class='quote-block'>The RPE you should aim for with each session in the microcycle depends on the type of training, the goals of the microcycle, and considerations of when match day occurs — allowing for recovery or preparation.</div>", unsafe_allow_html=True)
    img = get_img("RPE_info_graph_.png")
    if img: st.image(img, caption="Canada Soccer — Soccer Microcycle RPE Example. Our schedule follows the Consistent Professional Schedule model.", use_container_width=True)
    st.markdown("#### Our RPE Schedule")
    for day in DAYS:
        d = MICRO_SCHEDULE[day]
        st.markdown(f"<div class='card' style='border-left:3px solid {d['color']};'><b>{day} — {d['title']}</b> — <span style='font-weight:700;color:{d['color']};'>{d['rpe']}</span> — <small>{d['desc']}</small></div>", unsafe_allow_html=True)

with tabs[2]:
    st.markdown("### MENSTRUAL CYCLE PHASE INTEGRATION")
    st.markdown("<div class='quote-block'>Understanding the menstrual cycle allows us to train smarter, support our players better, and reduce injury risk. Training adapts to the body — not the other way around.</div>", unsafe_allow_html=True)
    for ph, data in CYCLE_PHASES.items():
        with st.expander(f"**{ph}**  ·  Intensity: {data['intensity']}"):
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"**Energy:** {data['energy']}"); st.markdown(f"**Focus:** {data['focus']}")
                for tip in data["tips"]:
                    st.markdown(f"<div class='card'>✔ {tip}</div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div style='background:{data['bg']};border:1px solid {data['color']};border-radius:8px;padding:14px;'><b style='color:{data['color']};'>Avoid:</b><br><span style='color:#ccc;font-size:0.88em;'>{data['avoid']}</span></div>", unsafe_allow_html=True)
