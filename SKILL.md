---
name: unsplash-search
description: >
  Recherche des images sur Unsplash via leur API et retourne les résultats
  sous forme de liste avec URLs, descriptions et métadonnées. Utilise ce skill
  dès que l'utilisateur mentionne "cherche une image", "trouve une photo sur
  Unsplash", "image de [sujet]", ou toute demande de recherche visuelle.
---

# Unsplash Image Search

Permet de chercher des images sur Unsplash à partir d'un descriptif textuel.

## Quand utiliser ce skill

- Recherche d'images ou de photos sur Unsplash
- L'utilisateur donne un mot-clé ou une description visuelle
- L'utilisateur veut récupérer une URL d'image directement utilisable

## Workflow

1. Appelle le script `scripts/unsplash_search.py` avec le descriptif
2. Affiche les résultats : première image OU liste de plusieurs options
3. Propose les URLs de téléchargement et les métadonnées

## Utilisation du script

```bash
# Retourne la 1ère image uniquement
python ~/.claude/skills/unsplash-search/scripts/unsplash_search.py "chien dans la neige"

# Retourne les N premières images (ex: 5)
python ~/.claude/skills/unsplash-search/scripts/unsplash_search.py "chien dans la neige" --count 5
```

## Variables d'environnement requises

- `UNSPLASH_ACCESS_KEY` : ta clé API Unsplash (Access Key)

## Format de sortie

Le script retourne un JSON avec :
- `total` : nombre de résultats trouvés
- `results` : liste d'images avec `id`, `description`, `url_regular`, 
  `url_thumb`, `download_url`, `photographer`, `photographer_url`

## Comportement attendu de Claude

- Si `--count 1` (défaut) → affiche la meilleure image directement
- Si `--count > 1` → présente un tableau des options avec vignettes et métadonnées
- Toujours proposer l'URL `url_regular` pour l'usage et `download_url` pour le téléchargement
