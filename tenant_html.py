#************************************************************
#tenant_html.py ----> fichier principal
#login_aci.py ----> les variables APIC_URL, USERNAME, PASSWORD
#aci_session.py
#***********************************************************
#modif par la branch
from flask import Flask, render_template, request
from login_aci import APIC_URL, USERNAME, PASSWORD
#from aci_session import get_session
import requests
import urllib3
urllib3.disable_warnings()

#initialiser la gestion de la page html
app = Flask(__name__)

#pointer le chemin de la page web index
@app.route("/", methods=["GET", "POST"])

def index():
    message = ""

    if request.method == "POST":
        tenant = request.form["tenant"]
        session = get_session()

        if not session:
            message = "❌ Échec de l'authentification."
        else:
            # Vérifier si le tenant existe déjà
            check_url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant}.json"
            check_response = session.get(check_url, verify=False)

            if check_response.status_code == 200 and check_response.json()["imdata"]:
                message = f"⚠️ Le tenant '{tenant}' existe déjà."
            else:
                # Créer le tenant
                create_url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant}.json"
                payload = {
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
                response = session.post(create_url, json=payload, verify=False)
                if response.status_code == 200:
                    message = f"✅ Tenant '{tenant}' créé avec succès."
                else:
                    message = f"❌ Erreur lors de la création : {response.status_code}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)   #Execute la page web http://127.0.0.1:5000
