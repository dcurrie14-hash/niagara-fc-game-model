import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img

st.set_page_config(page_title="Set Pieces | Niagara FC", page_icon="🎯", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# SET PIECES & RESTARTS")
st.markdown("<div class='quote-block'>Set pieces are not a break in the game — they are another opportunity to impose ourselves on the opposition.</div>", unsafe_allow_html=True)

tabs = st.tabs(["⚽ Attacking Corners", "🎯 Attacking Free Kicks", "🛡️ Defending Set Pieces", "🔄 Throw-Ins & Restarts"])

# ═══════════════════════════════════════════════════
# TAB 1 — ATTACKING CORNERS
# ═══════════════════════════════════════════════════
with tabs[0]:
    st.markdown("<div class='quote-block'>Attack space. Attack the ball. Attack rebounds.</div>", unsafe_allow_html=True)

    st.markdown("### CORNER PRINCIPLES")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("""<div class='card'>⚽ <strong>Delivery & First Contact</strong><br><br>Primary aerial target is free to attack the delivery. Surround the goalkeeper aggressively.</div>""", unsafe_allow_html=True)
    with p2:
        st.markdown("""<div class='card'>⚽ <strong>Box Movement</strong><br><br>Two back-post runners attack through the six-yard box towards the front-post zone — arrive first and create chaos around the goalkeeper.</div>""", unsafe_allow_html=True)
    with p3:
        st.markdown("""<div class='card'>⚽ <strong>Second Ball & Cover</strong><br><br>One midfielder secures the top of the box while the delivery-side fullback provides cover — protect against counter-attacks and attack second balls.</div>""", unsafe_allow_html=True)

    st.markdown("""<div class='card' style='margin-top:0.5rem;'>⚽ <strong>Short Corner</strong> — If the option is available, play it and attack quickly.</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### NFC In Action")
    i1, i2 = st.columns(2)
    with i1:
        img_routine = get_img("corner_routine.png")
        if img_routine:
            st.image(img_routine, caption="NFC — Attacking corner routine", use_container_width=True)
        else:
            st.warning("corner_routine.png not found in Game Model folder.")
    with i2:
        img_nfc = get_img("attacking_corner.png")
        if img_nfc:
            st.image(img_nfc, caption="Niagara FC — Two back-post runners attack through the six-yard box to disrupt defenders and create space around the goalkeeper. The primary aerial target attacks the first delivery while one midfielder secures the edge of the box, protecting against transition and attacking second balls. This reflects our principles of aggressive movement, first contact, and immediate reactions to the second action.", use_container_width=True)

    st.markdown("---")
    st.markdown("### Professional Reference")
    r1, r2 = st.columns(2)
    with r1:
        img_ger = get_img("Corner_att_example.png")
        if img_ger:
            st.image(img_ger, caption="Professional Reference – Germany Women (Olympics): Similar use of back-post movement through the six-yard box to create space for the primary aerial target while maintaining balance outside the box.", use_container_width=True)
    with r2:
        img_esp = get_img("attack_set-piece.jpg")
        if img_esp:
            st.image(img_esp, caption="Olympics — Spain corner sequence", use_container_width=True)

# ═══════════════════════════════════════════════════
# TAB 2 — ATTACKING FREE KICKS
# ═══════════════════════════════════════════════════
with tabs[1]:
    st.markdown("<div class='quote-block'>⚽ Make intelligent decisions — speed when it's on, patience when it's not.</div>", unsafe_allow_html=True)

    st.markdown("### ATTACKING FREE KICKS")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class='card'>🔴 <strong>Zones 1 & 2</strong><br><br>Play immediately if it's on. First available option wins.</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='card'>🔴 <strong>Zone 3</strong><br><br>Play quickly if possible. If not, organise and deliver into the box.</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class='card'>🔴 <strong>Zone 4</strong><br><br>Slow down, assess the situation, choose between a shot or service. Only play short when the opposition have failed to organise.</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Game Model in Action")
    i1, i2 = st.columns(2)
    with i1:
        img_att0 = get_img("att_free-kick.png")
        if img_att0:
            st.image(img_att0, caption="NFC — Attacking free kick shape and delivery", use_container_width=True)
        img_att1 = get_img("att_free-kick_zone4.png")
        if img_att1:
            st.image(img_att1, caption="NFC — Attacking free kick, Zone 4", use_container_width=True)
    with i2:
        img_att2 = get_img("quick_att_freekick_zone3.png")
        if img_att2:
            st.image(img_att2, caption="Zone 3 — Immediate restart exploiting a disorganised defensive line.", use_container_width=True)
        img_att3 = get_img("free_kick_zone3_pass.png")
        if img_att3:
            st.image(img_att3, caption="Immediate switch of play to exploit weak-side space before defensive recovery.", use_container_width=True)

# ═══════════════════════════════════════════════════
# TAB 3 — DEFENDING SET PIECES
# ═══════════════════════════════════════════════════
with tabs[2]:
    st.markdown("<div class='quote-block'>Win the first ball. Win the second ball. Win the moment.</div>", unsafe_allow_html=True)

    st.markdown("### DEFENSIVE CORNERS")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class='card'>🛡️ <strong>Zones Occupied</strong><br><br>
        Four zones always filled — no matter what the opposition do:<br><br>
        <strong>#3</strong> — Near post<br>
        <strong>#5</strong> — Central protection<br>
        <strong>#2</strong> — Primary aerial defender attacks the first contact<br>
        <strong>#9</strong> — High outlet
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card'>🛡️ <strong>Player-Oriented Marking</strong><br><br>All other players mark opponents directly — stay connected. Stay goal-side. Stay alert. No ball-watching.</div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='card'>🛡️ <strong>Short Corners</strong><br><br>Front-edge 6-yard player and nearest defender press together immediately. We never allow a 1v2 against us.</div>""", unsafe_allow_html=True)

    st.markdown("""<div class='card' style='margin-top:0.5rem;'>🛡️ <strong>GK Wins the Ball</strong> — Release #9 long as quickly as possible.</div>""", unsafe_allow_html=True)
    st.markdown("""<div class='card'>🛡️ <strong>Ball Stays Live</strong> — Defend the box with intensity. Do not let the ball bounce in our 18-yard box. Clear long, reorganise, and deal with the next action.</div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Defensive Principles in Action")
    i1, i2 = st.columns(2)
    with i1:
        img_shape = get_img("def_corner_shape.png")
        if img_shape:
            st.image(img_shape, caption="NFC — Defensive corner shape, zones occupied, player-oriented marking", use_container_width=True)
    with i2:
        img_win = get_img("def_corner_strongdef_free_to_win.png")
        if img_win:
            st.image(img_win, caption="NFC — Primary aerial defender released from her zone to attack the first contact", use_container_width=True)

    st.markdown("---")
    st.markdown("### DEFENSIVE FREE KICKS")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class='card'>🛡️ <strong>Zones 3 & 4</strong><br><br>
        Recover into defensive structure immediately.<br>
        Do not turn your back on play while recovering.<br>
        Get organised first, then rest.<br>
        Protect central spaces and force play wide.<br>
        Constant communication throughout.</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='card'>🛡️ <strong>Zones 1 & 2</strong><br><br>
        Nearest player immediately stands over the ball.<br>
        Delay the restart — allow the team to recover shape.<br>
        Do not allow quick free kicks.<br>
        Recover quickly behind the ball and organise.</div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class='card'>🛡️ <strong>Zone 1 Wide — Defend as a Corner</strong><br><br>
        Protect central spaces first.<br>
        Attack the first ball aggressively.<br>
        No free headers inside the penalty area.<br>
        Clear danger long and reorganise until the threat is over.</div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class='quote-block'>
    🔴 Recover immediately &nbsp;·&nbsp; 🔴 Protect central spaces &nbsp;·&nbsp;
    🔴 Communicate constantly &nbsp;·&nbsp; 🔴 Attack the first ball &nbsp;·&nbsp;
    🔴 Clear danger and reorganise
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Defensive Principles in Action")
    d1, d2 = st.columns(2)
    with d1:
        img_def1 = get_img("def_freekick_zone1.png")
        if img_def1:
            st.image(img_def1, caption="NFC — Zone 1 defensive free kick shape", use_container_width=True)
        img_def3 = get_img("def_freekick_zone3.png")
        if img_def3:
            st.image(img_def3, caption="NFC — Zone 2 compact defensive block", use_container_width=True)
    with d2:
        img_def2 = get_img("def_deep_freekick_zone2.png")
        if img_def2:
            st.image(img_def2, caption="NFC — Zone 2 defensive shape, compactness from a different angle", use_container_width=True)
        img_def4 = get_img("def_freekick_zone4_Back_in_shape.png")
        if img_def4:
            st.image(img_def4, caption="NFC — Zone 4 defensive free kick, immediate recovery into compact defensive structure.", use_container_width=True)

# ═══════════════════════════════════════════════════
# TAB 4 — THROW-INS & RESTARTS
# ═══════════════════════════════════════════════════
with tabs[3]:
    st.markdown("<div class='quote-block'>High tempo never stops. If it's on — play it.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Throw-In Principles")
        for item in [
            "Assess the quick restart before the opposition can organise",
            "Throw to feet whenever possible — receive, turn, and play forward",
            "Create support angles around the ball — make the throw-in easy to receive",
            "Movement starts before the throw, not after it",
            "Nearest players create options, far players create space",
            "In own half, secure possession first while maintaining a forward mindset",
            "Throw-ins in advanced Zones 3 and 4 are treated as attacking set pieces",
        ]:
            st.markdown(f"<div class='card'>⚽ {item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### Restart Mentality")
        for item in [
            "Recognise when to play quickly and when to control the moment",
            "Be organised before the restart and ruthless after it",
            "Use every restart to shift momentum — play with purpose, not just possession",
            "Every restart is an opportunity to create an advantage",
        ]:
            st.markdown(f"<div class='card card-gold'>⚽ {item}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Game Model in Action — Long Throw Routine")
    st.markdown("<div class='card'>⚽ <strong>Long Throw in Zones 3 & 4</strong> — Crowd the six-yard box, deliver into the danger area, attack the first contact aggressively, and arrive late for second balls.</div>", unsafe_allow_html=True)

    st.markdown("##### Example 1 — Midfielder arrives late, picks up second ball, scores from edge of box")
    img_2nd = get_img("picking_up_2nd_ball_from_long_throw.png")
    if img_2nd:
        st.image(img_2nd, caption="NFC — Midfielder arrives late, picks up second ball, scores from edge of box", use_container_width=True)

    st.markdown("##### Example 2 — Long throw creates first-contact pressure, NFC score from the second action")
    l1, l2, l3 = st.columns(3)
    with l1:
        img_lt1 = get_img("long_throw_1.png")
        if img_lt1:
            st.image(img_lt1, caption="Long throw delivered into the danger area", use_container_width=True)
    with l2:
        img_lt2 = get_img("long_throw_2.png")
        if img_lt2:
            st.image(img_lt2, caption="First contact creates pressure around the goalkeeper", use_container_width=True)
    with l3:
        img_lt3 = get_img("long_throw_3.png")
        if img_lt3:
            st.image(img_lt3, caption="NFC score from the second action", use_container_width=True)