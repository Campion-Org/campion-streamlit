#######################
# Import libraries
import streamlit as st
import pandas as pd
from utils import utils
from streamlit_calendar import calendar
#######################
# Page configuration
st.set_page_config(
    page_title="Campion Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")


cols = st.columns([1, 1])

with cols[0]:
    st.title("Schedule New Campaign")

    st.subheader("Coupon Details")
    # Add coupon form
    coupon_name = st.text_input("Coupon Name", help="Enter the name of the coupon")
    coupon_code = st.text_input("Coupon Code", help="Enter the coupon code")
    expiration_date = st.date_input("Expiration Date", help="Select the validity of the coupon")

    st.subheader("Content Details")
    # Add content form
    message_content = st.text_area("Message Content", help="Enter the content of the message", height=200)
    scheduled_date = st.date_input("Schedule Date", help="Select the date to schedule the campaign")

    add_campaign = st.button("Add Campaign", help="Click to schedule the campaign")
    if add_campaign:
        # Check if all fields are filled
        if not coupon_name or not coupon_code or not expiration_date or not message_content or not scheduled_date:
            st.warning("Please fill all the fields")
        else:
            utils.campaign.schedule_campaign(coupon_name, coupon_code, expiration_date, message_content, scheduled_date)
            st.success(f"Campaign with {coupon_name} scheduled at {scheduled_date} successfully!")
    # Reset the form
    coupon_name = ""
    coupon_code = ""
    expiration_date = ""
    message_content = ""
    date_time = ""





calendar_options = {
    "editable": "true",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "18:00:00",
}
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""


with cols[1]:
    st.title("Scheduled Coupons List")
    # Get scheduled campaigns
    # Get scheduled campaigns
    scheduled_campaigns = utils.campaign.get_scheduled_campaigns()
    if scheduled_campaigns:
        # Convert list to DataFrame
        df_scheduled_campaigns = pd.DataFrame(scheduled_campaigns)
        df_scheduled_campaigns.columns = ['Coupon Name', 'Coupon Code', 'Expiration Date', 'Message Content', 'Scheduled Date']
        # Convert DataFrame to HTML without index
        html = df_scheduled_campaigns.to_html(index=False, border=0, classes='table table-striped')
        calendar = calendar(events=scheduled_campaigns, options=calendar_options, custom_css=custom_css)
        st.write(calendar)
    else:
        st.warning("No scheduled campaigns found")
