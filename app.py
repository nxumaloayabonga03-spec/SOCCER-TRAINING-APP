import streamlit as st

# TOUCHLINE ACADEMY
# Python version of the player + coach development prototype.
# Run locally with:
#   pip install streamlit
#   streamlit run touchline_academy.py

st.set_page_config(
    page_title="Touchline Academy",
    page_icon="⚽",
    layout="wide",
)

st.markdown("""
<style>
.stApp { background: #08130f; color: #f4f8f3; }
[data-testid="stSidebar"] { background: #10221a; }
h1, h2, h3 { color: #d8f6c1; }
div[data-testid="stMetric"] {
    background: #10221a; border: 1px solid #294638;
    padding: 14px; border-radius: 12px;
}
.stButton > button {
    background: #a8f06a; color: #102015; border: 0;
    border-radius: 9px; font-weight: 700;
}
.notice {
    background: #2b2417; border-left: 4px solid #ffc46b;
    padding: 12px; border-radius: 6px; color: #ffe2b5;
    }
.plan {
    background: #10221a; border: 1px solid #294638;
    padding: 18px; border-radius: 14px; min-height: 310px;
}
</style>
""", unsafe_allow_html=True)

st.title("⚽ TOUCHLINE ACADEMY")
st.caption("Train smarter. Play braver. Coach better.")
st.write("A football development hub for players and coaches.")

if "membership" not in st.session_state:
    st.session_state.membership = "FREE"

page = st.sidebar.radio(
    "NAVIGATION",
    ["Player workspace", "Coach tactical lab", "Games & tryouts", "Membership"]
)

# ---------------- PLAYER WORKSPACE ----------------
if page == "Player workspace":
    st.header("🏃 Player workspace")
    left, right = st.columns(2)

    with left:
        st.subheader("Player profile")
        position = st.selectbox(
            "Playing position",
       ["Winger", "Striker", "Central midfielder",
             "Defensive midfielder", "Centre-back", "Full-back", "Goalkeeper"]
        )
        focus = st.selectbox(
            "Development focus",
            ["Ball control & first touch", "Passing & vision", "Finishing",
             "Speed & agility", "Defending", "Goalkeeping"]
        )

        drills = {
            "Ball control & first touch": [
                "Wall passes: 3 × 2 minutes, alternate feet",
                "Receive across your body: 3 × 8 each side",
                "Cone close-control course: 4 relaxed rounds",
            ],
            "Passing & vision": [
                "Two-touch wall passing: 4 × 90 seconds",
                "Scan before receiving: 3 × 8 repetitions",
                "Pass-and-move triangles: 4 × 2 minutes",
            ],
            "Finishing": [
                "Settle then finish: 3 × 6 each foot",
                "One-touch finishing technique: 3 × 5",
                "Accuracy targets: 3 × 5 attempts",
            ],
            "Speed & agility": [
                "Dynamic warm-up: 8 minutes",
                "Short accelerations with full recovery: 4–6 reps",
                "Controlled change-of-direction patterns: 3 × 3 each side",
            ],
            "Defending": [
                "Side-on jockeying footwork: 3 × 45 seconds",
                "Track a partner at controlled pace: 4 × 30 seconds",
                "Passing-lane awareness: 3 × 2 minutes",
            ],
        "Goalkeeping": [
                "Set position and footwork: 3 × 45 seconds",
                "Catching technique with a partner: 3 × 8",
                "Distribution to a target: 3 × 6",
            ],
        }

        if st.button("Build my practice session"):
            st.session_state.practice = drills[focus]

        if "practice" in st.session_state:
            st.success(f"Practice plan for: {focus}")
            for drill in st.session_state.practice:
                st.write("•", drill)

    with right:
        st.subheader("🥗 Everyday fuel guide")
        st.write(
            "Use a balanced, flexible approach to support training and recovery. "
            "This is general education, not a personalised diet."
        )
        st.write("- Eat regular meals with carbohydrates, protein, fruit or vegetables, and healthy fats.")
        st.write("- Before training, choose a familiar meal or snack that gives you energy.")
        st.write("- After training, have food containing carbohydrates and protein.")
        st.write("- Drink water regularly and bring a bottle to training.")
        st.write("- Include a variety of foods; avoid restrictive diets.")
        st.markdown(
            '<div class="notice">If you are still growing, avoid restrictive diets or supplement plans. '
            'Ask a parent/guardian and a registered sports dietitian for individual advice.</div>',
            unsafe_allow_html=True,
        )

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("💪 Training session")
        st.write("1. Warm-up — 8–10 minutes of easy movement, mobility and ball touches.")
        st.write("2. Skill block — 15–20 minutes focused on one technical theme.")
        st.write("3. Movement — age-appropriate bodyweight strength, balance and controlled acceleration.")
        st.write("4. Cool-down — walk, breathe and gently move through comfortable ranges.")
        st.caption("Adapt sessions to age, experience and coach/guardian guidance. Stop if you feel pain or unwell.")
    with c2:
        st.subheader("🌙 Recovery & rest")
        st.write("- Keep a consistent sleep routine; teens generally need 8–10 hours.")
        st.write("- Schedule at least one easier or rest day each week.")
        st.write("- Do not stack hard sessions when unusually tired or sore.")
        st.write("- Eat enough, hydrate and tell a trusted adult/coach if recovery is not going well.")

    st.divider()
    st.subheader("🎯 Match & tryout preparation")
    a, b, c = st.columns(3)
    a.info("**7 days before**\n\nConfirm venue, kickoff, transport and kit. Practise key role-specific skills.")
    b.info("**1 day before**\n\nPrepare boots, shin guards, water and documents. Eat familiar meals and sleep well.")
    c.info("**On the day**\n\nArrive early, warm up progressively, communicate and show teamwork.")

# ---------------- COACH TACTICAL LAB ----------------
elif page == "Coach tactical lab":
    st.header("🧠 Coach tactical lab")
    formations = {
        "4-3-3": {
            "shape": "4 defenders · 3 midfielders · 3 forwards",
            "benefits": [
                "Natural width and several attacking options",
                "Can press high with a coordinated front three",
                "Midfield triangle supports possession",
            ],
            "drawbacks": [
                "Space can open beside the single defensive midfielder",
                "Wide forwards and full-backs need clear coordination",
                "Can be vulnerable in transition if many players attack",
            ],
            "roles": {
                "Goalkeeper": "Communication, handling, positioning and distribution",
                "Centre-backs": "Aerial ability, anticipation, communication and passing",
                "Full-backs": "Recovery pace, stamina, 1v1 defending and crossing",
                "Number 6": "Scanning, positioning, tackling and press resistance",
                "Number 8s": "Engine, support angles, passing range and timing",
                "Wingers": "Acceleration, 1v1 skill, creativity and tracking back",
                "Striker": "Movement, finishing, link-up play and pressing",
            },
        },
        "4-2-3-1": {
            "shape": "4 defenders · 2 holding midfielders · 3 attacking midfielders · 1 striker",
            "benefits": [
                "Two deeper midfielders can protect the centre",
                "Flexible attacking midfield line",
                 "Useful structure for counter-pressing",
            ],
            "drawbacks": [
                "Can leave the striker isolated",
                "Needs disciplined distances between the pivots and front four",
                "Wide attackers must contribute defensively",
            ],
            "roles": {
                "Double pivot": "Positioning, communication, ball recovery and secure passing",
                "Number 10": "Awareness, creativity, quick decisions and close control",
                "Wide attackers": "Pace, 1v1 ability, pressing and combination play",
                "Striker": "Hold-up play, finishing, movement and work rate",
                "Back four and goalkeeper": "Defensive organisation, recovery and distribution",
            },
        },
        "4-4-2": {
            "shape": "4 defenders · 4 midfielders · 2 strikers",
            "benefits": [
                "Clear defensive lines and compactness",
                "Two forwards can combine and occupy centre-backs",
                "Straightforward roles for a developing team",
            ],
            "drawbacks": [
                "Central midfield can be outnumbered",
                "Wide midfielders cover large distances",
                "Can lack a natural link player between midfield and attack",
            ],
            "roles": {
                "Two strikers": "Complementary movement, finishing, pressing and link-up",
                "Central midfielders": "Work rate, positioning, duels and passing",
                "Wide midfielders": "Stamina, crossing, tracking runners and 1v1 skill",
                "Back four and goalkeeper": "Communication, discipline and recovery ability",
            },
        },
        "3-5-2": {
            "shape": "3 centre-backs · 2 wing-backs · 3 central midfielders · 2 forwards",
            "benefits": [
                "Can create a midfield numerical advantage",
               "Two forwards provide central attacking presence",
                "Wing-backs offer width and can adjust their height",
            ],
            "drawbacks": [
                "Wing-backs need high stamina and tactical awareness",
                "Wide centre-backs must defend channels",
                "Switches of play can expose the far side",
            ],
            "roles": {
                "Centre-backs": "Covering, communication, defending space and passing",
                "Wing-backs": "Stamina, pace, crossing and 1v1 defending",
                "Central midfielders": "Scanning, mobility, ball retention and pressing",
                "Two forwards": "Combination play, movement and finishing",
            },
        },
        "3-4-3": {
            "shape": "3 centre-backs · 4 midfielders · 3 forwards",
            "benefits": [
                "Strong front-line pressing potential",
                "Natural width from wide forwards and wing-backs",
                "Can pin an opponent's back line",
            ],
            "drawbacks": [
                "Midfield can be stretched if distances are poor",
                "Wing-backs face demanding two-way work",
                "Needs coordinated pressing triggers",
            ],
            "roles": {
                "Back three": "Pace in covering spaces, communication and distribution",
                "Wing-backs": "Engine, positioning, crossing and recovery",
                "Central midfielders": "Awareness, mobility and passing under pressure",
                "Front three": "Pressing coordination, pace, creativity and finishing",
            },
        },
        "4-1-4-1": {
            "shape": "4 defenders · 1 holding midfielder · 4 midfielders · 1 striker",
            "benefits": [
                "Compact defensive block",
                "Good protection of central areas",
                "Can transition quickly through wide midfielders",
            ],
            "drawbacks": [
                "Striker may become isolated",
                "Single holding midfielder needs positional support",
                "Wide midfielders have significant recovery duties",
            ],
            "roles": {
                "Number 6": "Scanning, discipline, anticipation and passing",
                "Four midfielders": "Work rate, compactness, support angles and tactical awareness",
                "Striker": "Hold-up play, movement, finishing and pressing",
                "Back four and goalkeeper": "Organisation, communication and defending space",
            },
        },
    }

    chosen = st.selectbox("Choose a formation", list(formations.keys()))
    data = formations[chosen]
 st.subheader(chosen + " — " + data["shape"])
    x, y = st.columns(2)
    with x:
        st.markdown("#### ✅ Potential benefits")
        for item in data["benefits"]:
            st.write("•", item)
    with y:
        st.markdown("#### ⚠️ Potential drawbacks")
        for item in data["drawbacks"]:
            st.write("•", item)

    st.markdown("#### Position qualities required")
    for role, qualities in data["roles"].items():
        with st.expander(role):
            st.write(qualities)

    st.divider()
    st.subheader("How to test a new formation")
    st.write("1. Set one clear objective: press higher, protect central space or create width.")
    st.write("2. Walk players through starting positions and responsibilities.")
    st.write("3. Run a short, controlled phase of play against a realistic opponent shape.")
    st.write("4. Observe spacing, passing options, transitions and communication.")
    st.write("5. Change one variable at a time and compare what improves.")
    st.warning("A formation is a starting structure, not a fixed answer. Adapt it to your players and opponent.")

# ---------------- GAMES AND TRYOUTS ----------------
elif page == "Games & tryouts":
    st.header("🏟️ Games & tryouts")
    country = st.selectbox(
        "Choose country",
        ["South Africa", "England", "Spain", "Germany", "Nigeria", "United States"]
    )

    st.subheader("Professional football resources")
    country_resources = {
        "South Africa": [
            ("SAFA — South African Football Association", "https://www.safa.net/"),
            ("Premier Soccer League", "https://www.psl.co.za/"),
        ],
        "England": [
            ("The FA", "https://www.thefa.com/"),
            ("Premier League", "https://www.premierleague.com/"),
        ],
        "Spain": [
            ("Royal Spanish Football Federation", "https://rfef.es/"),
            ("LaLiga", "https://www.laliga.com/"),
        ],
        "Germany": [
            ("German Football Association", "https://www.dfb.de/"),
            ("Bundesliga", "https://www.bundesliga.com/"),
        ],
        "Nigeria": [
            ("Nigeria Football Federation", "https://thenff.com/"),
        ],
        "United States": [
           ("U.S. Soccer", "https://www.ussoccer.com/"),
            ("Major League Soccer", "https://www.mlssoccer.com/"),
        ],
    }

    for label, url in country_resources[country]:
        st.markdown(f"- [{label}]({url})")

    st.subheader("Find academy trials")
    st.write("Use official club and association channels. Verify age group, eligibility, fees, venue and closing date.")
    search_url = (
        "https://www.google.com/search?q="
        + country.replace(" ", "+")
        + "+football+academy+trials+official"
    )
    st.markdown(f"[Search official academy trial announcements for {country}]({search_url})")
    st.markdown(
        '<div class="notice">This prototype does not have a verified live tryout feed. '
        'Never pay an unofficial agent or share identity documents with an unverified account. '
        'Take a parent/guardian into trial arrangements.</div>',
        unsafe_allow_html=True,
    )
    st.caption("Live fixtures and confirmed trials require a trusted, regularly updated data source.")

# ---------------- MEMBERSHIP ----------------
elif page == "Membership":
    st.header("⭐ TOUCHLINE ACADEMY Membership")
    st.write("Start with FREE. Paid plans are previews until secure billing is integrated.")
    st.info("Your current selection: " + st.session_state.membership)

    free, pro, expert = st.columns(3)

    with free:
        st.markdown('<div class="plan">', unsafe_allow_html=True)
        st.subheader("FREE")
        st.metric("Price", "R0 / month")
        st.write("- Basic player training plans")
        st.write("- Skills and practice drills")
        st.write("- General nutrition and recovery guidance")
        st.write("- Match and tryout checklist")
        st.write("- Basic formation library")
        if st.button("Use FREE", key="free_plan"):
            st.session_state.membership = "FREE"
               st.success("FREE membership selected.")
        st.markdown("</div>", unsafe_allow_html=True)

    with pro:
        st.markdown('<div class="plan">', unsafe_allow_html=True)
        st.subheader("PRO")
        st.metric("Price", "Coming soon")
        st.write("- Personalised training-plan builder")
        st.write("- Player progress and goal tracking")
        st.write("- Detailed match preparation")
        st.write("- Advanced skill-development library")
        st.write("- Player development reports")
        st.button("PRO — coming soon", disabled=True, key="pro_plan")
        st.markdown("</div>", unsafe_allow_html=True)

    with expert:
        st.markdown('<div class="plan">', unsafe_allow_html=True)
        st.subheader("EXPERT")
        st.metric("Price", "Coming soon")
        st.write("- Advanced tactical analysis")
        st.write("- Squad and position planning")
        st.write("- Team performance reports")
        st.write("- Custom team training programmes")
        st.write("- Expanded coaching resources")
        st.button("EXPERT — coming soon", disabled=True, key="expert_plan")
        st.markdown("</div>", unsafe_allow_html=True)

st.warning(
        "PRO and EXPERT payments are not active. This prototype does not collect "
        "card details or start subscriptions. Before charging users, add secure "
        "accounts, a backend entitlement check and the correct Google Play Billing "
        "integration for Android digital subscriptions."
    )

st.divider()
st.caption(
    "TOUCHLINE ACADEMY • Educational football development prototype. "
    "Training, nutrition and recovery guidance should be adapted to each player "
    "with appropriate coach, parent/guardian and qualified professional support."
  )
