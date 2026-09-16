import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'cle-secrete-flask'

# Chemin absolu vers votre fichier Excel dans le sous-dossier generate_sql
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, 'generate_sql', 'appels_offres_depuis_id_2459.xlsx')


def get_excel_data():
    """Lit le fichier Excel et renvoie la liste des clients sous forme de liste de tuples/éléments."""
    if not os.path.exists(EXCEL_PATH):
        print(f"Fichier non trouvé au chemin : {EXCEL_PATH}")
        return []
    
    try:
        # Lecture du fichier Excel
        df = pd.read_excel(EXCEL_PATH)
        
        # Remplacer les valeurs manquantes/NaN par None pour Jinja2
        df = df.where(pd.notnull(df), None)
        
        # S'assurer qu'une colonne ID existe à l'index 0 (sinon insérer un index dynamique 1, 2, 3...)
        cols = [str(c).lower().strip() for c in df.columns]
        if 'id' not in cols:
            df.insert(0, 'id', range(1, len(df) + 1))
            
        return df.values.tolist()
    except Exception as e:
        print(f"Erreur de lecture du fichier Excel: {e}")
        return []


# ---------------------- DASHBOARD ----------------------

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


# ---------------------- ADMINISTRATION ----------------------

@app.route('/administration')
def administration():
    return render_template('administration.html')


# ---------------------- CLIENTS / OPÉRATIONS ----------------------

@app.route('/operation', methods=['GET', 'POST'])
def operation():
    all_clients = get_excel_data()

    # ---- RÉCUPÉRATION DES CATÉGORIES DISTINCTES ----
    categories = sorted(list(set(
        str(c[4]) for c in all_clients 
        if len(c) > 4 and c[4] is not None and str(c[4]).strip() != ''
    )))

    # ---- FILTRAGE DES CLIENTS ----
    search_id = request.args.get('search_id', '').strip()
    search_cat = request.args.get('search_cat', '').strip()

    filtered_clients = all_clients

    # Filtre par ID (index 0)
    if search_id and search_id.isdigit():
        filtered_clients = [c for c in filtered_clients if str(c[0]) == search_id]

    # Filtre par Catégorie (index 4)
    if search_cat:
        filtered_clients = [c for c in filtered_clients if len(c) > 4 and str(c[4]) == search_cat]

    return render_template(
        'operation.html', 
        clients=filtered_clients, 
        categories=categories, 
        search_id=search_id, 
        search_cat=search_cat
    )


# ---------------------- MODIFIER UN CLIENT ----------------------

@app.route('/operation/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    if not os.path.exists(EXCEL_PATH):
        flash("Fichier Excel introuvable.", "error")
        return redirect(url_for('operation'))

    df = pd.read_excel(EXCEL_PATH)
    cols = [str(c).lower().strip() for c in df.columns]
    if 'id' not in cols:
        df.insert(0, 'id', range(1, len(df) + 1))

    # Trouver la ligne correspondant à l'ID
    row_idx = df[df['id'] == client_id].index
    if len(row_idx) == 0:
        flash("Client introuvable.", "error")
        return redirect(url_for('operation'))

    idx = row_idx[0]

    if request.method == 'POST':
        # Mettre à jour les données dans le DataFrame Pandas
        if 'reference' in df.columns:
            df.loc[idx, 'reference'] = request.form.get('reference')
        if 'libelle' in df.columns:
            df.loc[idx, 'libelle'] = request.form.get('libelle')
        if 'client' in df.columns:
            df.loc[idx, 'client'] = request.form.get('client')
        if 'categorie' in df.columns:
            df.loc[idx, 'categorie'] = request.form.get('categorie')
        if 'estimation' in df.columns:
            df.loc[idx, 'estimation'] = request.form.get('estimation')
        if 'date_remise' in df.columns:
            df.loc[idx, 'date_remise'] = request.form.get('date_remise')
        
        # Sauvegarder les modifications dans le fichier Excel
        df.to_excel(EXCEL_PATH, index=False)
        flash("Client modifié avec succès !", "success")
        return redirect(url_for('operation'))

    # Convertir la ligne en dictionnaire pour l'afficher dans le formulaire de modification
    client = df.loc[idx].to_dict()
    return render_template('edit_client.html', client=client)


# ---------------------- SUPPRIMER UN CLIENT ----------------------

@app.route('/operation/delete/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    if not os.path.exists(EXCEL_PATH):
        flash("Fichier Excel introuvable.", "error")
        return redirect(url_for('operation'))

    df = pd.read_excel(EXCEL_PATH)
    cols = [str(c).lower().strip() for c in df.columns]
    if 'id' not in cols:
        df.insert(0, 'id', range(1, len(df) + 1))

    # Filtrer le DataFrame pour exclure la ligne à supprimer
    df = df[df['id'] != client_id]
    
    # Enregistrer le fichier mis à jour
    df.to_excel(EXCEL_PATH, index=False)
    flash("Client supprimé avec succès !", "success")
    return redirect(url_for('operation'))


# ---------------------- AUTRES PAGES ----------------------

@app.route('/banque')
def banque():
    return render_template('banque.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')


if __name__ == '__main__':
    app.run(debug=True)