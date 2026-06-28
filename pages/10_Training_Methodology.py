import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import apply_css, sidebar_brand, get_img, ROYAL, RED, GOLD, NAVY, WHITE

st.set_page_config(page_title="Training Methods | Niagara FC", page_icon="🏃", layout="wide")
apply_css(); sidebar_brand()

st.markdown("# TRAINING METHODOLOGY & DESIGN")
st.markdown("<div class='quote-block'>We design the problem, not just the solution. Our role is to create environments that encourage players to perceive information, make decisions, and discover effective solutions within realistic game situations.</div>", unsafe_allow_html=True)

tabs = st.tabs(["📚 Methodology","📋 SCORE & Constraints","🏟️ Session Example","📸 Session Drills","🔢 Environment Design"])

# ═══════════════════════════════════════════════════
# TAB 1 — METHODOLOGY
# ═══════════════════════════════════════════════════
with tabs[0]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:0.95em;color:#FFD700;letter-spacing:1px;margin-bottom:12px;'>Our training methodology is guided by the game model, the specific game moment, and the needs of the players. Practice formats, methodologies, and constraints are selected to create the learning environment best suited to achieving the objective.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>WHOLE — PART — WHOLE</div>", unsafe_allow_html=True)
        st.markdown("""<div class='card'>
        Most game moments are best learned within the context of the game. Whole-Part-Whole is therefore my preferred methodology.
        Players first encounter the game problem in a realistic game environment before key learning moments are isolated when necessary.
        They then return to the game where solutions must be recognised and executed under realistic pressure.<br><br>
        I rarely stop sessions to provide answers immediately. Instead, I prefer to manipulate the environment and allow players
        to discover solutions through repetition, discussion, and guided questioning.
        </div>""", unsafe_allow_html=True)

        st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>WHEN I ADAPT THE METHODOLOGY</div>", unsafe_allow_html=True)

        st.markdown("""<div class='card card-blue'><b>Progressive Part Method</b><br><br>
        If players repeatedly struggle with a specific tactical moment, I may isolate and repeat that situation before returning to the full game.<br><br>
        For example, if midfield players are not recognising opportunities to support underneath the #9 during attacking organisation,
        I may create a Progressive Part activity that increases repetition of that specific moment before progressing back into a larger game.
        </div>""", unsafe_allow_html=True)

        st.markdown("""<div class='card'><b>Whole Method</b><br><br>
        When introducing a new game problem — for example, our pressing structure in a new system — I'll often start with an 11v11 or large-sided game
        and let players experience it with minimal intervention. This shows me what they already understand before I decide where to coach.
        </div>""", unsafe_allow_html=True)

        st.markdown("""<div class='card'><b>Part Method</b><br><br>
        Part Method is used sparingly — mainly for set-piece organisation or isolated technical detail, such as our short corner routine,
        where precise repetition matters more than game realism.
        </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>HOW I SELECT PRACTICE FORMATS</div>", unsafe_allow_html=True)
        st.markdown("""<div class='card card-gold'>
        The format is chosen by what the moment demands. To work on the relationship between the #6 and centre backs,
        I'll use a Functional Practice — fewer players, more repetitions of that specific connection.
        To develop our pressing triggers as a team, I'll use Phase of Play or an 8v8, where the picture is closer to a real game.
        Small-Sided Games are my go-to for raw decision-making reps — more touches, more transitions, more problems to solve.
        </div>""", unsafe_allow_html=True)

        st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>HOW I USE CONSTRAINTS</div>", unsafe_allow_html=True)
        st.markdown("""<div class='card' style='margin-bottom:0.5rem;'>
        Training activities are influenced by the Constraints-Led Approach. Rather than prescribing solutions,
        I manipulate the environment to encourage players to discover effective actions and behaviours.
        Constraints are not used to restrict players — they are used to guide attention, influence behaviour,
        and create realistic problems that players must solve.
        </div>""", unsafe_allow_html=True)

        for item in [
            "To encourage quicker forward play in Zone 2, I may reduce support around the ball or create a numerical disadvantage — forcing players to recognise forward passing opportunities earlier.",
            "To increase penetration in attacking organisation, I may reward line-breaking passes or goals scored within a set number of actions.",
            "To improve transition reactions, I may introduce time constraints that require players to win the ball back or play forward immediately after regaining possession.",
        ]:
            st.markdown(f"<div class='card card-green'>→ {item}</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 2 — SCORE & CONSTRAINTS
# ═══════════════════════════════════════════════════
with tabs[1]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>SCORE PRINCIPLES IN PRACTICE</div>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>Every session at Niagara FC is designed using the SCORE principles. If it does not look like the game, we change it.</div>", unsafe_allow_html=True)

    for letter, word, detail, clr in [
        ("S","Soccer Problem","Every session begins with a game moment taken directly from our game model. The problem comes from the game — not the coach.","card-red"),
        ("C","Challenge","Constraints and conditions encourage players to solve problems and make decisions under realistic pressure.","card-orange"),
        ("O","Opposition","The opposition provides the information players must perceive and respond to — not a prescribed drill pattern.","card-gold"),
        ("R","Realism","Activities reflect the demands and complexity of the game. If it wouldn't happen on a Saturday, we question whether it belongs in training.","card-blue"),
        ("E","Enjoyment","Players are challenged, engaged, and motivated to compete. Enthusiasm for the game is never sacrificed for organisation.","card-green"),
    ]:
        st.markdown(f"<div class='{clr}' style='color:white !important;'><span style='font-size:1.8em;font-weight:900;color:white;'>{letter}</span> <b style='color:white;'>{word}</b> <span style='color:white;'>— {detail}</span></div>", unsafe_allow_html=True)

    st.divider()
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>EXAMPLES FROM MY ENVIRONMENT</div>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>By manipulating the practice environment, constraints guide attention and shape behaviour, allowing players to discover solutions rather than being given them.</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='card card-red'>
        <b>Attacking Organisation</b> <span style='color:#ccc;font-size:0.78em;font-style:italic;'>(numerical constraint)</span><br><br>
        To encourage quicker forward play in Zone 2, I may reduce support around the ball or create a numerical disadvantage.
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='card card-gold'>
        <b>Transition to Attack</b> <span style='color:#ccc;font-size:0.78em;font-style:italic;'>(time / scoring constraint)</span><br><br>
        To reinforce our "play forward, run forward" principle, I may reward goals scored within a set number of seconds after regaining possession.
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='card card-blue'>
        <b>Defensive Organisation</b> <span style='color:#ccc;font-size:0.78em;font-style:italic;'>(space constraint)</span><br><br>
        To improve compactness, I may reduce the width of the playing area and reward regains in central areas.
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 3 — SESSION EXAMPLE
# ═══════════════════════════════════════════════════
with tabs[2]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>SESSION EXAMPLE — CHANGING THE POINT OF ATTACK</div>", unsafe_allow_html=True)
    st.markdown("<div style='background:#0D1B2A;border-left:4px solid #1E56D6;padding:12px 18px;border-radius:0 8px 8px 0;margin-bottom:16px;'><b style='color:#1E56D6;'>OBJECTIVE:</b> <span style='color:#F5F5F5;'>Develop players' ability to recognise when and why to switch the point of attack to create space and attack more effectively.</span><br><b style='color:#F5C518;'>MOMENT:</b> <span style='color:#F5F5F5;'>Attacking Organisation — Zones 2 & 3</span></div>", unsafe_allow_html=True)

    st.markdown("**B Licence Format — System / Strategy / Tactics / Skill Set**")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div class='card'><b>SYSTEM</b><br>1-4-3-3<br>Attacking & Defensive</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card card-blue'><b>STRATEGY</b><br>Switch play to disrupt the opposition shape and create space to attack quickly.</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card card-gold'><b>TACTICS</b><br>Change point of attack through wide neutrals. Combine centrally to attract pressure. Play quickly to the far side.</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='card card-green'><b>SKILL SET</b><br>Quick short passes · Positive first touch away from pressure · Scanning & Decision Making · Movement and rotations</div>", unsafe_allow_html=True)

    st.markdown("#### What / Where / Who / When / How")
    for what, where, who, when, how in [
        ("Switch the point of attack","Zone 2 & 3 — central and wide channels","6, 8, 10, 7, 11, 2, 3","When central spaces are overloaded or defended","Pass quickly to the wide neutral — first touch forward — attack the space"),
        ("Fullback underlaps to support centrally","Zone 3 — as ball travels","2, 3, 4, 5","When the wide forward holds width and a central underlap is on","Read the wide forward's position, time the underlapping run, receive between the lines"),
        ("Third-man combination to break lines","Between lines, Zone 2 transition","6, 8, 10, 9","When first receiver is pressed — look for the player beyond","Quality first pass to feet, immediate movement, third player times run beyond"),
    ]:
        with st.expander(f"**{what}**"):
            tbl = "| | |\n|-|-|\n| **Where** | " + str(where) + " |\n| **Who** | " + str(who) + " |\n| **When** | " + str(when) + " |\n| **How** | " + str(how) + " |"
            st.markdown(tbl)

    st.divider()
    st.markdown("#### 3-Part Whole-Part-Whole Structure")

    st.markdown("""<div class='card' style='margin-bottom:0.5rem;'>
    <b style='color:#1E56D6;'>PART ONE — WHOLE</b> — <b>3v3+2 Four Goal Game</b><br><br>
    Players immediately experience the game problem. With four scoring options available, players must constantly scan,
    perceive pressure, and recognise opportunities to change the point of attack rather than forcing play into crowded areas.<br><br>
    <i style='color:#aaa;'>Why this activity? The game naturally presents switching opportunities without prescribing solutions.
    Players experience the tactical problem before coaching intervention occurs.</i>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class='card' style='margin-bottom:0.5rem;'>
    <b style='color:#1E56D6;'>PART TWO — PART</b> — <b>4v4+3 Open the Pitch Game</b><br><br>
    Wide locked neutrals and a central neutral create repeated opportunities to switch play. Players are encouraged to use width
    to move the opposition before attacking quickly into space.<br><br>
    <i style='color:#aaa;'>Why this activity? This environment increases repetition of the specific tactical moment while maintaining
    opposition, decision making, and realism. If players are struggling to recognise when to switch play, this activity creates
    more frequent opportunities to practise that decision.</i>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div class='card' style='margin-bottom:0.5rem;'>
    <b style='color:#1E56D6;'>PART THREE — WHOLE</b> — <b>8v8+2 Width & Switching Game</b><br><br>
    Players return to a larger, more realistic game where they must recognise switching opportunities within a full team context.
    Two neutrals support the team in possession and encourage circulation, while the larger space creates realistic attacking problems.<br><br>
    <i style='color:#aaa;'>Why this activity? Success is measured by improved recognition and decision making rather than perfect execution.
    We observe whether players are more likely to recognise, attempt, and successfully use switches of play when the opportunity emerges.</i>
    </div>""", unsafe_allow_html=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Coaching Focus")
        for item in [
            "Perceive pressure and congestion",
            "Scan before receiving",
            "Recognise opportunities to switch play",
            "Recognise when NOT to switch play",
            "Use width to move the opposition",
            "Attack quickly once space has been created",
        ]:
            st.markdown(f"<div class='card card-blue'>→ {item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### Constraints Used")
        for item in [
            "Neutral players to create width and support",
            "Multiple scoring options to encourage scanning",
            "Positional advantages that reward switching behaviour",
            "Scoring incentives following successful switches",
        ]:
            st.markdown(f"<div class='card card-gold'>→ {item}</div>", unsafe_allow_html=True)

    st.markdown("""<div class='quote-block' style='margin-top:0.5rem;'>
    <b>Coach Reflection:</b> If players are still forcing play into pressure, I may increase the value of goals scored following
    a switch or create additional width through neutral players. If players are switching automatically without reading the game,
    I may progressively remove constraints and allow the game to present more realistic decisions.
    </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════
# TAB 4 — SESSION DRILLS
# ═══════════════════════════════════════════════════
with tabs[3]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>SESSION DRILL IMAGES</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        img = get_img("8v6_Runs_behind.png")
        if img: st.image(img, caption="8v6 — Runs Behind. Attacking organisation in Zone 3 & 4. Timing runs to get in behind the defensive line.", use_container_width=True)
        img = get_img("Counter_Attack_in_Final_third.png")
        if img: st.image(img, caption="Counter Attack in Final Third. Transition to attack — arrive with numbers, attack before they set.", use_container_width=True)
    with c2:
        img = get_img("8v8_Pressing_Half_Field.png")
        if img: st.image(img, caption="8v8 Pressing — Half Field. Defensive organisation and press triggers. Team pressing as a connected unit.", use_container_width=True)
        img = get_img("Phase_of_Play_8v8_counter.png")
        if img: st.image(img, caption="Phase of Play 8v8 — Counter. Defensive transition into immediate counter-attack. React first, attack second.", use_container_width=True)

# ═══════════════════════════════════════════════════
# TAB 5 — ENVIRONMENT DESIGN
# ═══════════════════════════════════════════════════
with tabs[4]:
    st.markdown("<div style='font-family:Oswald,sans-serif;font-size:1.2em;color:#F5F5F5;letter-spacing:1px;margin:16px 0 8px;'>ENVIRONMENT DESIGN FRAMEWORK</div>", unsafe_allow_html=True)
    st.markdown("<div class='quote-block'>Every training environment is a decision. The design determines what players experience and what they learn.</div>", unsafe_allow_html=True)

    for section, items, clr in [
        ("EXPERIENCES — OBJECTIVES — LEARNING INTENTIONS",
         ["What do we want players to experience?",
          "Every session objective is taken directly from our game model and focuses on developing behaviours rather than isolated techniques.",
          "Learning intentions describe what players should recognise, attempt, and improve — not simply what activity they complete."],
         "#111"),
        ("ORGANISATION — STRUCTURE — ACTIVITIES",
         ["How is the session structured?",
          "What activities achieve the objective?",
          "What progressions are planned?"],
         "#1E56D6"),
    ]:
        st.markdown(f"<div style='background:{clr};border:1px solid #1E56D6;border-radius:6px;padding:12px;margin:8px 0;'><b style='color:white;'>{section}</b></div>", unsafe_allow_html=True)
        for item in items:
            st.markdown(f"<div class='card'>→ {item}</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### DESIGN")
        for item, clr in [
            ("Pitch — size, shape, zones","card-red"),
            ("Parameters — rules, constraints","card-red"),
            ("Players — numbers, roles, positions","card-red"),
        ]:
            st.markdown(f"<div class='{clr}'>{item}</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("#### DEMANDS")
        for item, clr in [
            ("Reward — how do we score points?","card-green"),
            ("Relate — how does it connect to the game?","card-green"),
            ("Restrict — what constraints create the problem?","card-green"),
        ]:
            st.markdown(f"<div class='{clr}'>{item}</div>", unsafe_allow_html=True)
