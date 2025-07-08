#************************
# aci_session.py
#*************************
import requests
import urllib3
from login_aci import APIC_URL, USERNAME, PASSWORD

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class ACI:
    def __init__(self):
        self.session = None
    def get_session(self):
        session = requests.Session()
        login_url = f"{APIC_URL}/api/aaaLogin.json"
        login_payload = {
            "aaaUser": {
                "attributes": {
                    "name": USERNAME,
                    "pwd": PASSWORD
                }
            }
        }

        response = session.post(login_url, json=login_payload, verify=False)
        if response.status_code == 200:
            self.session = session
            return session
        else:
            print(f"❌ Erreur de connexion : {response.status_code}")
            return None
