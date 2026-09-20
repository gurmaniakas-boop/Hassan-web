import streamlit as st
import random
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="To My Dearest Hassan Abbas Baloch",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. ROMANTIC STYLING & CUSTOM CSS (LOVE THEME) ---
st.markdown("""
    <style>
    /* Main Background with Romantic Gradient */
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 50%, #ffb3c1 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header Container */
    .hero-header {
        background: rgba(255, 255, 255, 0.85);
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 10px 25px rgba(225, 29, 72, 0.15);
        border: 2px solid #ff4d6d;
        margin-bottom: 25px;
    }
    
    .hero-title {
        color: #c9184a;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 5px;
    }
    
    .hero-subtitle {
        color: #ff4d6d;
        font-size: 1.2rem;
        font-weight: 600;
    }

    /* Cards Styling */
    .content-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4d6d;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Button Customization */
    .stButton>button {
        background: linear-gradient(90deg, #ff4d6d 0%, #c9184a 100%);
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 10px rgba(201, 24, 74, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(201, 24, 74, 0.5) !important;
    }

    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 20px;
        margin-top: 40px;
        border-top: 1px solid rgba(255, 77, 109, 0.3);
        color: #800f2f;
        font-weight: bold;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HERO HEADER ---
st.markdown("""
    <div class="hero-header">
        <div class="hero-title">💖 Forever & Always 💖</div>
        <div class="hero-subtitle">A Special Gift for Hassan Abbas Baloch</div>
        <p style="color: #590d22; margin-top: 10px; font-style: italic;">
            "Every day with you is my favorite adventure."
        </p>
    </div>
""", unsafe_allow_html=True)

# --- 4. NAVIGATION TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["💌 Love Letter", "📸 Gallery", "⏳ Memories", "🎮 Surprise Game"])

# --- TAB 1: LOVE LETTER & QUOTES ---
with tab1:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.subheader("🌹 Dearest Hassan,")
    st.write("""
    To the man who fills my world with happiness, comfort, and unconditional love — this app is dedicated entirely to you!
    
    Thank you for being my strength, my best friend, and my lifelong partner. Every single moment with you is a memory I treasure deeply.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("✨ Daily Love Quote Generator")
    
    quotes = [
        "In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine.",
        "I look at you and see the rest of my life in your eyes.",
        "You are my today and all of my tomorrows, Hassan.",
        "Loved you yesterday, love you still, always have, always will.",
        "Home isn't a place, it's a person — and for me, it's you."
    ]
    
    if st.button("💖 Generate Love Note"):
        st.balloons()
        selected_quote = random.choice(quotes)
        st.info(f"*{selected_quote}*")

# --- TAB 2: PHOTO GALLERY ---
with tab2:
    st.subheader("🖼️ Our Precious Moments")
    st.write("Replace these sample photos with your real photos with Hassan!")
    
    col1, col2 = st.columns(2)
    
    # NOTE: You can replace these image links with real photo URLs or local file paths (e.g., 'images/hassan1.jpg')
    with col1:
        st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=500", caption="Unforgettable Moments 💕", use_container_width=True)
        st.image("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=500", caption="Hand in Hand Forever 🤝", use_container_width=True)
        
    with col2:
        st.image("https://images.unsplash.com/photo-1522673607200-164d1b6ce486?w=500", caption="Smiles & Laughter 😊", use_container_width=True)
        st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500", caption="My Heart & Soul ❤️", use_container_width=True)

# --- TAB 3: MEMORY TIMELINE ---
with tab3:
    st.subheader("⏳ Our Beautiful Journey")
    
    st.markdown("""
    * **📍 The Day We Met:** The start of something magical that changed my world forever.
    * **💍 Saying 'Yes':** Stepping into a beautiful future side by side.
    * **✈️ Our Favorite Trip:** Laughter, adventures, and endless joy together.
    * **🏡 Building Our Home:** Creating a peaceful life filled with warm love.
    """)
    
    st.divider()
    
    st.subheader("🔥 Love Compatibility Meter")
    love_percent = st.slider("How much do Akas & Hassan love each other?", 0, 100, 100)
    
    if love_percent == 100:
        st.success("100% - Infinite, Unconditional & Eternal Love! ❤️")
    else:
        st.warning("Needs to be set to 100%! Try moving it to the max! 😉")

# --- TAB 4: SURPRISE GAME ---
with tab4:
    st.subheader("🎯 How Well Do You Know Us?")
    
    answer = st.radio(
        "What is Akas's favorite thing about Hassan?",
        ["His kind heart & warm smile", "His intelligence & guidance", "His jokes & humor", "All of the above! ❤️"]
    )
    
    if st.button("Submit Answer"):
        if answer == "All of the above! ❤️":
            st.snow()
            st.success("Correct! You mean the absolute absolute world to me, Hassan!")
        else:
            st.write("Close! But the real answer is **All of the above! ❤️**")

# --- 5. FOOTER ---
st.markdown("""
    <div class="footer">
        Developed by : Akas Gurmani 💖
    </div>
""", unsafe_allow_html=True)
