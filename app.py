#######################
# Import libraries
import streamlit as st
import altair as alt
import streamlit_shadcn_ui as ui

#######################
# Page configuration
st.set_page_config(
    page_title="Campion Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")


#######################
# Load data
#df_reshaped = pd.read_csv('data/us-population-2010-2019-reshaped.csv')


#######################



#######################
# Sidebar
with st.sidebar:
    st.title("Campion")
    # Break line
    st.write("---")

    # User profile with image and name on the side
    col = st.columns([2.5, 2])

    with col[0]:
        st.image("https://avatars.githubusercontent.com/u/8320180?v=4", width=100)
    with col[1]:
        # Space to align the text
        st.write("")
        st.write("Sudeep Dhakal")
        st.write("_Capitol Pizza, Litteton_")


    setting_button = ui.button(text="Settings", key="settings")

    ui.alert_dialog(show=setting_button, title="Settings", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")


# Card 1

col = st.columns(2)

#######################
# Calendar and Coupon Schedule
with col[0]:
    with ui.card(key="card2", title="Calendar"):
        with ui.card(key="card3", title="Coupon Schedule"):
            ui.date_picker(key="date_picker", label="Date")

#######################
# Dashboard Main Panel
with col[1]:
    with ui.card(key="card5", title="Add Coupons"):
        # TODO: Add coupon form here
        # with coupon name, discount, and expiry date
        # Also allows to refine and send messages.
        pass
        
    with ui.card(key="card6", title="Retention Rate"):
        # TODO: Retention rate chart here with toggle to change the time period
        pass