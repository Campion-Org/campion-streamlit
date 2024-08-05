#######################
# Import libraries
import streamlit as st
import altair as alt
import streamlit_shadcn_ui as ui

#######################
# Page configuration
# Page configuration
st.set_page_config(page_title="Campion Coupon", page_icon="🏂", layout="wide")

# Enable dark theme for Altair charts
#alt.themes.enable("dark")


# Custom CSS to enhance appearance, including buttons
st.markdown("""
    <style>
    .coupon-code { font-weight: bold; font-size: 20px; color: #FF4B4B; }
    .validity { font-style: italic; }
    .button-custom { margin: 10px 0; }
    /* Style buttons */
    .stButton>button {
        border: 2px solid #4CAF50; /* Green border */
        background-color: #4CAF50; /* Green background */
        color: white;
        padding: 10px 24px;
        cursor: pointer;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green background */
    }
    </style>
    """, unsafe_allow_html=True)

#######################
# Check if 'coupon_redeemed' key exists in session_state, if not initialize it to False

#if 'coupon_redeemed' not in st.session_state:
#    st.session_state.coupon_redeemed = False

# Redeem Coupon Section
#if st.button("Redeem Coupon", key="redeem_button", help="Click to redeem your coupon"):
#    st.session_state.coupon_redeemed = True

#if st.session_state.coupon_redeemed:
st.success("Coupon redeemed from _Capitol Pizza, Littleton_! **Please copy the code below.**")
coupon_code = "BOGO50"
st.markdown("Code: "+ f"<div class='coupon-code'>{coupon_code}</div>", unsafe_allow_html=True)
# Line break
st.markdown("---")
st.markdown("**Buy 1, Get 1 50% Off on 10\" and 14\" Pizza!**", unsafe_allow_html=True)
st.markdown("***Valid only till August 08, 2024 11:59 PM.***", unsafe_allow_html=True)

    
#if st.session_state.coupon_redeemed:
    # Line break
st.markdown("---")

# Columns for additional actions
col1, col2 = st.columns(2)

# Go to the Website Button
with col1:
    # Using markdown to create a clickable link that looks like a button with a blue color scheme
    st.markdown("<a href='https://order.toasttab.com/online/capitol-pizza-littleton-new' target='_blank'><button style='color: white; background-color: #007BFF; padding: 10px 24px; border: none; border-radius: 5px; cursor: pointer;'>Order Online!</button></a>", unsafe_allow_html=True)
    #st.markdown("You will be redirected to the website of Capitol Pizza, Littleton", unsafe_allow_html=True)

# Call the Store Button
with col2:
    # Using markdown to create a clickable link that looks like a button with a red color scheme
    st.markdown("<a href='tel:+1 (720) 459-8049'><button style='color: white; background-color: #DC3545; padding: 10px 24px; border: none; border-radius: 5px; cursor: pointer;'>Call Store</button></a>", unsafe_allow_html=True)
    #st.markdown("Clicking the button will attempt to open your phone app to call Capitol Pizza, Littleton.", unsafe_allow_html=True)