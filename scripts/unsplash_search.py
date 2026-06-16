#!/usr/bin/env python3
"""
Unsplash Image Search — Claude Code Skill
Recherche des images sur Unsplash et retourne du JSON exploitable par Claude.
Usage:
    python unsplash_search.py "descriptif de l'image" [--count N]
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

UNSPLASH_API_BASE = "https://api.unsplash.com"


def search_images(query: str, count: int = 1) -> dict:
    """Appelle l'API Unsplash et retourne les résultats en JSON."""
    access_key =  os.environ.get("UNSPLASH_ACCESS_KEY")
    if not access_key:
        print(json.dumps({
            "error": "Variable d'environnement UNSPLASH_ACCESS_KEY manquante.",
            "hint": "Exporte-la avec : export UNSPLASH_ACCESS_KEY=ton_access_key"
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    params = urllib.parse.urlencode({
        "query": query,
        "per_page": min(count, 30),  # max 30 par appel Unsplash
        "page": 1,
        "orientation": "landscape"   # optionnel, tu peux retirer
    })
    url = f"{UNSPLASH_API_BASE}/search/photos?{params}"

    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Client-ID {access_key}",
            "Accept-Version": "v1"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            raw = json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(json.dumps({
            "error": f"Erreur HTTP {e.code}",
            "detail": body
        }, ensure_ascii=False, indent=2))
        sys.exit(1)
    except urllib.error.URLError as e:
        print(json.dumps({
            "error": f"Impossible de joindre l'API Unsplash : {e.reason}"
        }, ensure_ascii=False, indent=2))
        sys.exit(1)

    total = raw.get("total", 0)
    photos = raw.get("results", [])

    results = []
    for photo in photos:
        results.append({
            "id": photo.get("id"),
            "description": photo.get("description") or photo.get("alt_description") or "(aucune description)",
            "width": photo.get("width"),
            "height": photo.get("height"),
            "color": photo.get("color"),
            "url_thumb": photo.get("urls", {}).get("thumb"),
            "url_regular": photo.get("urls", {}).get("regular"),
            "url_full": photo.get("urls", {}).get("full"),
            "download_url": photo.get("links", {}).get("download"),
            "page_url": photo.get("links", {}).get("html"),
            "photographer": photo.get("user", {}).get("name"),
            "photographer_url": photo.get("user", {}).get("links", {}).get("html"),
            "likes": photo.get("likes"),
        })

    return {
        "query": query,
        "total_available": total,
        "returned": len(results),
        "results": results
    }


def main():
    parser = argparse.ArgumentParser(
        description="Recherche d'images Unsplash pour Claude Code"
    )
    parser.add_argument(
        "query",
        help="Descriptif de l'image à rechercher (ex: 'chien dans la neige')"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Nombre d'images à retourner (défaut: 1, max: 30)"
    )
    args = parser.parse_args()

    data = search_images(args.query, args.count)
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
