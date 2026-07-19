from crewai import Task
from app.models.articulo import ArticuloBlogger

class AppTasks:
    
    def tarea_investigar_y_redactar(self, agente, categorias: str) -> Task:
        """
        Tarea 1: Investigar de forma autónoma tendencias recientes, seleccionar la de mayor relevancia
        y redactar un borrador de artículo estructurado.
        """
        description = f"""
        Identifica de forma autónoma las tendencias tecnológicas y de desarrollo de software más actuales y con mayor relevancia/impacto de esta semana (año 2026).
        
        Debes actuar como el responsable de seleccionar de manera completamente independiente el tema del artículo de esta semana, evaluando criterios como:
        - Actualidad y frescura de la noticia.
        - Popularidad y nivel de interés.
        - Impacto en la industria del software.
        - Utilidad práctica para programadores y profesionales de TI.

        Una vez que hayas seleccionado autónomamente el mejor tema del ámbito de tecnología (por ejemplo: Inteligencia Artificial, Agentes Autónomos, LLMs, Cloud Computing, DevOps, Ciberseguridad, etc.), realiza una investigación y redacta un borrador inicial de altísimo valor editorial.

        REGLAS DE INVESTIGACIÓN Y ACTUALIDAD:
        1. El borrador DEBE basarse en información ACTUAL y RECIENTE de este año (2026).
        2. Incluye referencias temporales ("En 2026", "Recientemente", "Actualmente", etc.).
        3. El borrador debe tener una introducción sólida, explicación del tema, contexto, beneficios, casos de uso, ejemplos cuando sea posible, conclusiones y referencias utilizadas.
        4. Debe tener una extensión mínima de 500 palabras y estar formateado en HTML válido (usa solo <h2>, <p>, <ul>, <ol>, <strong>, <em>, <blockquote>). No insertes imágenes en el HTML.

        SELECCIÓN DE CATEGORÍAS:
        Analiza las categorías del blog y selecciona únicamente los IDs numéricos que correspondan al tema elegido:
        {categorias}

        PROMPTS DE IMAGEN:
        1. Diseña un 'featured_image_prompt' detallado y cinemático para la tendencia seleccionada, escrito estrictamente en INGLÉS.
        2. Diseña un 'featured_image_alt' descriptivo y natural en ESPAÑOL (máximo 125 caracteres), ideal para accesibilidad de WordPress.
        """

        return Task(
            description=description,
            expected_output=(
                "Un borrador estructurado del artículo tecnológico seleccionado autónomamente que contenga: "
                "título propuesto, categorías seleccionadas, contenido redactado en HTML (mínimo 500 palabras), "
                "prompt en inglés de la imagen y alt text en español."
            ),
            agent=agente,
        )

    def tarea_humanizar_y_formatear(self, agente, tarea_borrador: Task) -> Task:
        """
        Tarea 2: Tomar el borrador del periodista, reescribirlo y humanizarlo para que no parezca IA,
        manteniendo el HTML y estructurando la salida en el JSON final requerido.
        """
        description = f"""
        Analiza el borrador del artículo de tendencia tecnológica generado en la tarea anterior. 
        
        Tu objetivo es pulir la redacción, el título y el extracto (excerpt) para que el texto final suene completamente natural, humano y cercano, como si fuera una investigación o artículo escrito en primera persona o por un autor humano experto (autoría propia), y no por una IA.

        REGLAS CRÍTICAS DE HUMANIZACIÓN:
        1. Elimina modismos y clichés típicos de IA (por ejemplo: "En resumen", "En conclusión", "Es crucial", "El dinámico mundo", "A medida que...", transiciones excesivamente formales o repetitivas).
        2. Simplifica palabras complejas u oraciones demasiado densas. Usa un lenguaje claro, directo y fluido que sea fácil de entender para cualquier persona, pero manteniendo el rigor profesional.
        3. Escribe de manera que se sienta que el autor tiene experiencia de primera mano con lo que está describiendo.
        4. Conserva el formato HTML en la propiedad 'content' (usando obligatoriamente <h2>, <p>, <ul>, <ol>, <strong>, <em>, <blockquote>) y asegúrate de que mantenga el mínimo de 500 palabras.
        5. No insertes imágenes en el HTML.
        6. Mantén el 'featured_image_prompt' en INGLÉS y el 'featured_image_alt' en ESPAÑOL tal y como vienen en el borrador (o mejóralos si es necesario respetando el idioma).
        7. El extracto (excerpt) debe ser un resumen SEO muy natural de máximo 160 caracteres.

        FORMATO DE RESPUESTA OBLIGATORIO:
        Debes estructurar la salida exactamente en base al modelo Pydantic suministrado (ArticuloBlogger).
        """

        return Task(
            description=description,
            expected_output="Un objeto JSON válido estructurado según el modelo ArticuloBlogger, que represente el artículo totalmente humanizado y formateado.",
            agent=agente,
            context=[tarea_borrador],
            output_json=ArticuloBlogger
        )
