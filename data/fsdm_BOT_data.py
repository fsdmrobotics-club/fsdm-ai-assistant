# FILE: core/fsdm_data.py
import datetime

def get_fsdm_context():
    """
    Returns the static knowledge base for the Faculty of Sciences Dhar El Mahraz (FSDM).
    Contains: General Info, Academics, Library, Transport, Social Aids, Campus Life, and Higher Education.
    """
    # Dynamically generate the current timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%A, %B %d, %Y %I:%M %p") # e.g., "Friday, December 12, 2025 11:30 PM"
    
    return f"""
    [OFFICIAL FSDM CONTEXT]
    [CURRENT TIME: {timestamp}]
    
    === FICHE D'IDENTITÉ FSDM ===
    - Nom Complet : Faculté des Sciences Dhar El Mahraz (كلية العلوم ظهر المهراز)
    - Abréviation : FSDM
    - Université : Université Sidi Mohamed Ben Abdellah (USMBA)
    - Date de création : 1980
    - Adresse : B.P. 1796 Fès-Atlas, 30003, Fès, Maroc
    - Localisation : Quartier Atlas (Campus Dhar El Mahraz)
    - Lien Google Maps : https://maps.app.goo.gl/YkFq4wJz7j4z8z8z9
    
    [LEADERSHIP & CONTACT]
    - Doyen : Mr. Mohammed BELKASMI
    - Vice-Doyen (Pédagogie) : Mr. Hicham AMAKDOUF
    - Vice-Doyen (Recherche) : Mr. Mohammed Nabil KABBAJ
    - Secrétaire Général : Mr. Hamid ZAHID
    - Téléphone Décanat : +212 535 64 23 98
    - Fax : +212 535 64 25 00
    - Email Support : support.fsdm@usmba.ac.ma
    - Site Web Officiel : https://www.fsdm.usmba.ac.ma

    [DÉPARTEMENTS & CHEFS]
    - Biologie : Pr. BENYAHYA Mohammed
    - Chimie : Pr. OUARSAL RACHID (Bureau: Bâtiment Chimie, RDC)
    - Géologie : Pr. TEKIOUT BRAHIM
    - Informatique : Pr. TAIRI Hamid
    - Mathématiques : Pr. ZGUITTI HASSANE (Bureau: Bâtiment principal, Aile gauche)
    - Physique : Pr. FILALI MOHAMMED (Bureau: Près des Amphis D, E)

    === 1. ADMINISTRATION & SCOLARITÉ ===
    
    🕒 HORAIRES D’OUVERTURE
    - Guichets : Du lundi au jeudi (09h00 - 13h30), le vendredi (09h00 - 13h00).
    - Service Scolarité : De 09h00 à 16h30.
    - Note : Fermé le week-end et les jours fériés.

    📍 LOCALISATION
    - Le service de scolarité se trouve à gauche de l’entrée principale.
    - Les guichets sont en face (entre le département de Géologie et la bibliothèque).

    📄 PROCÉDURES ADMINISTRATIVES
    - Attestation de Scolarité : Demande sur place au guichet de votre filière (délai 2-3h, CNE requis).
    - Relevé de Notes : Demande sur place au guichet de scolarité (délai 2-3h).
    - Carte Étudiant (Perte) : Nécessite une déclaration de perte (Police) ou un engagement sur l’honneur.
    - Retrait du Baccalauréat : Le retrait définitif entraîne la radiation de la faculté.

    === 2. SYSTÈME PÉDAGOGIQUE (VALIDATION & NOTES) ===

    ✅ VALIDATION D'UN MODULE
    - Condition : Obtenir une moyenne de 10/20 ou plus.
    - Calcul : La note finale est la moyenne des notes des Travaux Pratiques (TP) et de l'examen final.

    ⚖️ COMPENSATION DES MODULES
    - Principe : Un module avec une note entre 5.00 et 9.99 peut être validé si un autre module du même semestre a une note supérieure à 10.
    - Condition Clé : La moyenne générale du semestre doit être égale ou supérieure à 10/20.

    🚫 NOTE ÉLIMINATOIRE
    - Seuil : Une note inférieure à 5/20 dans un module est éliminatoire.
    - Conséquence : Le module ne peut pas être compensé et doit obligatoirement être passé au rattrapage.
    - Absence : L'absence à un examen final est considérée comme une note éliminatoire.

    🔄 SESSION DE RATTRAPAGE
    - Éligibilité : Pour les étudiants ayant une note de module entre 0 et 9.99 (et non-absents à l'examen initial).
    - Règle : La note la plus élevée entre la session normale et la session de rattrapage est conservée.

    🏆 MENTIONS DE FIN DE CYCLE
    - Passable : 10 à 11.99
    - Assez Bien : 12 à 13.99
    - Bien : 14 à 15.99
    - Très Bien : 16 et plus

    === 3. BIBLIOTHÈQUE (BIBLIO) ===

    🕒 HORAIRES
    - Ouverture : 08h00 | Fermeture : 18h00.
    - Samedi : Ouvert.
    - Période de préparation (Exams) : Ouvert jusqu’à 23h00.

    🔑 ACCÈS & EMPRUNT
    - Documents requis : Aucun.
    - Emprunt de livres : Se fait via une réservation en ligne.


    === 4. GUIDE TRANSPORT & ACCÈS ===

    🚌 BUS (City Bus)
    - Ligne 06 (Principale) : Centre-ville -> Bab EL GHOL -> Devant la Fac (2.50 DH).
    - Ligne 51 : Sidi Boujida -> Sidi Brahim -> Al-Nourjiss (3.50 DH). Arrêt Sidi Brahim.
    - Ligne 54 : Al Rassif -> Sidi Brahim -> Mont Fleury -> Al Zohour (3.50 DH). Arrêt Sidi Brahim.
    - Abonnement Étudiant : 100 DH (2 lignes) ou 80 DH (1 ligne). Dépôt à l'agence Barcelo ou Sidi Brahim.

    🚖 PETIT TAXI (Rouge)
    - Gare de Train : ~12-14 DH.
    - Centre Ville (VN) : ~10-12 DH.

    === 5. AIDES SOCIALES (BOURSE, LOGEMENT, AMO) ===

    💰 BOURSE MINHATY (Min7a)
    - Site officiel : https://www.minhaty.ma
    - Décision : Ministère / Wilaya (la faculté est un intermédiaire).
    - Réclamation : Service des bourses (Bloc Administratif).
    - Versements (Indicatifs) : Tranche 1 (Déc-Jan), Tranche 2 (Mars-Avr), Tranche 3 (Mai-Juin).

    🏠 CITÉ UNIVERSITAIRE (Dhar El Mahraz)
    - Inscription : En ligne sur https://logement.onousc.ma (fin août/début sept).
    - Critères : Éloignement, revenus faibles, priorité aux nouveaux étudiants.
    - Restauration (Resto U) : Ticket ≈ 1.40 DH.

    🏥 COUVERTURE MÉDICALE (AMO Étudiant)
    - Site officiel : https://amo.etudiant.ma
    - Inscription : En ligne recommandée. Dépôt de dossier aux agences CNOPS.
    
    === 6. LIEUX DE VIE SUR LE CAMPUS ===

    ☕ BUVETTE (CAFÉTÉRIA)
    - Localisation : Derrière le Département de Géologie (près des salles L).
    - Offre : Café (2 DH), Thé (3 DH), Eau (3 DH), Soda (4 DH), Snacks.

    🕌 MOSQUÉE (SALLE DE PRIÈRE)
    - Localisation : Derrière le Département d'Informatique.
    - Installations : Tapis, espace ablutions extérieur, section pour femmes.

    🖨️ CENTRE DE PHOTOCOPIE (TIREUSE)
    - Localisation : À côté de la Buvette.
    - Services : Impression (0,50 DH/copie N&B), vente de fournitures.

    🚽 SANITAIRES (TOILETTES)
    - Filles : RDC Géologie et RDC Mathématiques.
    - Hommes : RDC Chimie.

    🎭 CLUBS ÉTUDIANTS
    - Exemples : ENACTUS (Entrepreneuriat), IT&AI, Robotique, EPEDD (Environnement).
    - Soutenir/Rejoindre : Contacter directement les clubs via leurs réseaux sociaux.

    === 7. FORMATIONS SUPÉRIEURES (MASTERS & DOCTORAT) ===

    🎓 MASTERS (Par Département)
    - INFORMATIQUE : MQL (Qualité Logiciel), MID (Web Intelligence/Data Science), MLAIM (Machine Learning), MBDSI (Big Data).
    - MATHÉMATIQUE : MASI (Maths Appliquées), MMP (Maths Pures), MSSD (Modélisation Stochastique).
    - PHYSIQUE : M2A (Matériaux Avancés), MAER (Automatique/Énergies Renouvelables), 2ESI (Électronique Embarquée), PNOMER (Physique Nouveaux Matériaux), MSI (Smart Industry).
    - CHIMIE : CAE (Chimie Analytique/Environnement), CMI (Chimie Matériaux Innovants).
    - BIOLOGIE : BEVP (Biotechnologie/Écologie), BAMQ (Biotechnologie Alimentaire/Qualité).

    📝 ADMISSION MASTER (Procédure Typique)
    1. Pré-inscription : En ligne sur le site de la FSDM.
    2. Sélection : Étude de dossier, puis concours écrit et/ou oral.
    3. Inscription Finale : Au service de scolarité.

    🔬 DOCTORAT (Recherche)
    - Gestion : Centre d'Études Doctorales (CED) "Sciences et Technologies".
    - Laboratoires de recherche : LASIMA (Maths), LIMAS (Ingénierie), LESSI (Électronique), LM2A (Matériaux), L3IA (IA), LGERA (Biotechnologie), LIEME (Électrochimie), LPS (Physique du Solide).
    """