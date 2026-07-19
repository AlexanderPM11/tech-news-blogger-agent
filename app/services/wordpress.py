import requests
from app.core.config import settings

def obtener_categorias_wordpress() -> str:
    """
    Realiza una consulta a la API REST de WordPress para obtener la lista de categorías
    en formato 'ID - Nombre' excluyendo aquellas que contengan un guión bajo '_'. 
    En caso de error, retorna un listado fallback limpio.
    """
    base_url = settings.WORDPRESS_CATEGORIES_URL
    url = f"{base_url}?per_page=100" if "?" not in base_url else f"{base_url}&per_page=100"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        categories = response.json()
        formatted = []
        for cat in categories:
            cat_id = cat.get("id")
            cat_name = cat.get("name")
            if cat_id is not None and cat_name is not None:
                # Filtrar categorías que contengan un guión bajo '_' (ej: _highlights, _servicesonly)
                if "_" in cat_name:
                    continue
                formatted.append(f"{cat_id} - {cat_name}")
        return ", ".join(formatted)
    except Exception as e:
        print(f"[WARN] Error al obtener categorías de WordPress: {e}. Usando fallback de categorías.")
        return (
            "13 - (P) - Aplicaciones Web, 14 - (P) - Ecommerce, 19 - aaPanel, 5 - Bases de Datos, "
            "18 - Corporativo, 3 - Desarrollo Web, 4 - DevOps y Cloud, 9 - Educación y Tecnología, "
            "16 - Finanzas, 6 - Frameworks y Librerías, 27 - Habilidades, 17 - Inmobiliaria, "
            "21 - Mail, 22 - n8n, 10 - Noticias y Actualizaciones, 12 - projects, "
            "8 - Proyectos y Casos Prácticos, 7 - Seguridad y Redes, 15 - Social, 23 - Tech Semanal, "
            "11 - Tips y Snippets, 1 - Uncategorized, 20 - WebMail"
        )
