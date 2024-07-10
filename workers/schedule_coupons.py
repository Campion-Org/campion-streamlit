import requests
import json
import datetime

class Campaign:

    def __init__(self, username: str, backend_url: str):
        self.username = username
        self.backend_url = backend_url
        
    def schedule_campaign(self, coupon_name, coupon_code, expiration_date, message_content, scheduled_date):
        response = requests.post(
            f"{self.backend_url}/sms/schedule?api_key={self.username}&coupon_name={coupon_name}&coupon_code={coupon_code}&expiration_date={expiration_date}&message_content={message_content}&scheduled_date={scheduled_date}")
        return response.json()
    
    def get_scheduled_campaigns(self):
        # Get scheduled campaigns
        response = requests.get(f"{self.backend_url}/sms/get/{self.username}")        
        print(response.json())
        campaigns = response.json()
        table = []
        for campaign in campaigns:
            # Use fromisoformat for ISO 8601 formatted strings
            expiration_date = datetime.datetime.fromisoformat(campaign["expiration_date"].rstrip("Z"))
            expiration_date_ymd = expiration_date.strftime('%Y-%m-%d')
            table.append([campaign["coupon_name"], campaign["coupon_code"], expiration_date_ymd, campaign["content"], campaign["scheduled_date"]])
        return table