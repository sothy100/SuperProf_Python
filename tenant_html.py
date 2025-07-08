# ************************************************************
# tenant_html.py ----> fichier principal
# login_aci.py ----> contient APIC_URL, USERNAME, PASSWORD
# aci_session.py ----> contient la classe ACI avec get_session()
# ************************************************************

from flask import Flask, render_template, request
from login_aci import APIC_URL
from aci_session import ACI
import urllib3

# Désactiver les avertissements SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialiser l'application Flask
app = Flask(__name__)

# Route principale pour afficher ou traiter le formulaire
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        tenant = request.form["tenant"]
        aci_instance = ACI()
        session = aci_instance.get_session()

        if not session:
            message = "❌ Échec de l'authentification."
        else:
            # Vérifier si le tenant existe déjà
            check_url = f"{APIC_URL}/api/node/mo/uni/tn-{tenant}.json"
            check_response = session.get(check_url, verify=False)

            if check_response.status_code == 200 and check_response.json().get("imdata"):
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

# Lancer le serveur Flask
if __name__ == "__main__":
    app.run(debug=True)  # Accès via http://127.0.0.1:5000
