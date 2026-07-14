import pywikibot
from datetime import datetime, timezone
from pywikibot.exceptions import LockedPageError, EditConflictError, PageSaveRelatedError

def publier_message_ads_bistro():
    site = pywikibot.Site('fr', 'wikipedia')
    
    mois_fr = ["janvier", "février", "mars", "avril", "mai", "juin", 
               "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    
    maintenant = datetime.now(timezone.utc)
    jour = maintenant.day
    mois = mois_fr[maintenant.month - 1]
    annee = maintenant.year
    
    titre_cible = f"Wikipédia:Le Bistro/{jour} {mois} {annee}"
    page = pywikibot.Page(site, titre_cible)
    
    wikicode_message = f"""

{{{{subst:Wikipédia:Article de la semaine/Annonce dans le Bistro}}}} ~~~~
"""
    
    texte_actuel = page.text
    page.text = texte_actuel + wikicode_message
    
    try:
        page.save(summary="Bot : Publication automatique de l'Article de la semaine")
        print(f"Le message a été publié avec succès sur {titre_cible} !")
        
    except LockedPageError:
        print(f"Erreur : La page {titre_cible} est protégée (verrouillée) !")
    except EditConflictError:
        print(f"Erreur : Conflit d'édition sur {titre_cible} !")
    except PageSaveRelatedError as e:
        print(f"Une erreur est survenue lors de la sauvegarde : {e}")
    except Exception as e:
        print(f"Une erreur système inattendue est survenue : {e}")

if __name__ == "__main__":
    publier_message_ads_bistro()
