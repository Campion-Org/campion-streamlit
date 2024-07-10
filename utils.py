import os
from workers.schedule_coupons import Campaign


BACKEND_URL="https://campion.onrender.com"
#BACKEND_URL="http://localhost:8088"
backend_url = BACKEND_URL

#st.title("!")

# Text box to enter the user's name
#user_name = st.text_input("Enter your name", key="name")
user_name = "Capitol_Pizza_Littleton"


class Utils:
    def __init__(self):
        self.user_name = user_name
        self.campaign = Campaign(user_name, backend_url=backend_url)

utils = Utils()