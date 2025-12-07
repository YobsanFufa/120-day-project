# ==========================================
# Web App: Password Generator (Streamlit)
# ==========================================
import streamlit as st
from generator import build_character_pool, generate_password
from utils import check_strength

# Page Configuration
st.set_page_config(page_title="Secure Password Gen", page_icon="🔒", layout="centered")

# Custom CSS for a "Premium" look
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px;
    }
    .password-display {
        font-family: 'Courier New', monospace;
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px;
        border: 2px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🔒 Professional Password Generator")
    st.markdown("Generate strong, secure passwords instantly.")
    st.markdown("---")

    # --- Sidebar Settings ---
    st.sidebar.header("⚙️ Settings")
    
    length = st.sidebar.slider("Password Length", min_value=4, max_value=64, value=16)
    
    st.sidebar.subheader("Character Types")
    use_upper = st.sidebar.checkbox("A-Z (Uppercase)", value=True)
    use_lower = st.sidebar.checkbox("a-z (Lowercase)", value=True)
    use_digits = st.sidebar.checkbox("0-9 (Digits)", value=True)
    use_symbols = st.sidebar.checkbox("!@# (Symbols)", value=True)
    
    st.sidebar.markdown("---")
    exclude_ambiguous = st.sidebar.checkbox("Exclude Ambiguous Chars (e.g. l, 1, O, 0)", value=False)

    # --- Main Area ---
    
    if st.button("Generate Password ⚡"):
        try:
            # reuse our logic from generator.py
            pool = build_character_pool(use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous)
            password = generate_password(length, pool)
            
            # Display Password
            st.markdown(f'<div class="password-display">{password}</div>', unsafe_allow_html=True)
            
            # Strength Meter
            strength = check_strength(password)
            st.text(f"Strength Estimate: {strength}")
            
            # Visual Strength Indicator
            if "Very Strong" in strength:
                st.progress(100)
                st.balloons()
            elif "Strong" in strength:
                st.progress(75)
            elif "Medium" in strength:
                st.progress(50)
            else:
                st.progress(25)
                st.warning("Consider increasing length or variety for better security.")
                
            # Note about clipboard
            st.info("💡 Copy manually or use the CLI version for auto-clipboard features.")
            
        except ValueError as e:
            st.error(f"Error: {e}")

    # Footer
    st.markdown("---")
    st.caption("Day 001 - 120 Days of Code Challenge | Built with Python & Streamlit")

if __name__ == "__main__":
    main()
