# aci_session.py

import requests
from login_aci import APIC_URL, USERNAME, PASSWORD

def get_session():
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
    #verifiy=false ---> desactive la verification SSL
    if response.status_code == 200:
        return session
    else:
        return None
