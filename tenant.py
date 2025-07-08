#******************* RECUPERER A PARTIR
# method: POST
# url: https://sandboxapicdc.cisco.com/api/node/mo/uni/tn-Test_tenant.json
# payload: {"fvTenant":{"attributes":{"dn":"uni/tn-Test_tenant","name":"Test_tenant","rn":"tn-Test_tenant","status":"created"},"children":[]}}
#**************************************************************************************************************

import requests
import urllib3
urllib3.disable_warnings()  # Pour ignorer les warnings SSL

# --- Paramètres ---
apic_url = "https://sandboxapicdc.cisco.com"
username = "admin"
password = "!v3G@!4@Y"  # ✅ mot de passe correct pour le sandbox

# --- Étape 1 : Authentification ---
login_url = f"{apic_url}/api/aaaLogin.json"
login_payload = {
    "aaaUser": {
        "attributes": {
            "name": username,
            "pwd": password
        }
    }
}

session = requests.Session()
login_response = session.post(login_url, json=login_payload, verify=False)

if login_response.status_code != 200:
    print("❌ Échec de l'authentification :", login_response.status_code)
    exit()

print("✅ Authentifié avec succès")

# --- Saisie du nom du tenant ---
#tenant = input("Quel est le tenant à créer ? ")
tenant = "Tenant_8_juillet"
# --- Vérifier si le tenant existe déjà ---
check_url = f"{apic_url}/api/node/mo/uni/tn-{tenant}.json"
check_response = session.get(check_url, verify=False)

if check_response.status_code == 200 and check_response.json()["imdata"]:
    print(f"⚠️ Le tenant '{tenant}' existe déjà.")
else:
    # --- Créer le tenant ---
    create_url = f"{apic_url}/api/node/mo/uni/tn-{tenant}.json"
    tenant_payload = {
        "fvTenant": {
            "attributes": {
                "dn": f"uni/tn-{tenant}",
                "name": tenant,
                "rn": f"tn-{tenant}",
                "status": "created"
            },
            "children": []
        }
    }

    response = session.post(create_url, json=tenant_payload, verify=False)

    # --- Affichage des résultats ---
    print("✅ Tenant créé avec succès.")
    print("Code HTTP :", response.status_code)
    print("Réponse JSON :")
    print(response.json())
