import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Clase para gestionar el historial del chat
class ChatManager:
    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=self.API_KEY)
        
        # Instrucciones de configuración inicial del sistema
        self.agents_general = [
            {"role": "system", "content": "Eres un programador experimentado en la parte de frontend y tienes mucha creatividad para el diseño UI"},
            {"role": "system", "content": "Tu trabajo es generar componentes nativos solo con html y css de acuerdo a especificaciones"},
            {"role": "system", "content": "Siempre tienes que enviar el codigo del componente dentro de una etiqueta div que este centrada correctamente y este siempre dentro de su padre, no utilices medidas con vh vw en el componente, solo con relacion al div"},
            {"role": "system", "content": "Siempre debes responder solo el codigo, ninguna descripcion ni saludo ni nada mas que solo el codigo."},
            {"role": "system", "content": "Procura ser creativo, revisa la armonia de colores y no escatimes en hacer animaciones css"},
            {"role": "system", "content": "Haz al componente muy grande ya que solo se mostrara este componente"},
            {"role": "system", "content": "Añadele mucho javascript"},

        ]
        
        # Historial de mensajes
        self.mensajes_historial = self.agents_general.copy()  # Copiamos las instrucciones iniciales

    async def chat_with_agent(self, mensajes):
        print("Procesando petición...")
        chat_completion = await self.client.chat.completions.create(
            model="gpt-4o-mini",  # O el modelo que estés utilizando
            messages=mensajes,
        )
        response = chat_completion.choices[0].message.content
        print("Respuesta recibida.")
        return response

    async def preguntar_a_openai(self, mensaje):
        # Agregar el mensaje del usuario al historial
        self.mensajes_historial.append({"role": "user", "content": f'Mejora la ultima version con estas instrucciones: {mensaje}'})
        
        # Obtener la respuesta del modelo con el historial actualizado
        respuesta = await self.chat_with_agent(self.mensajes_historial)
        print(f"Respuesta generada: {respuesta}")
        
        return respuesta

    def agregar_mejora(self, mejora):
        # Añadir una mejora al historial
        self.mensajes_historial.append({"role": "user", "content": f"Mejora la respuesta con lo siguiente: {mejora}"})
        print("Mejora añadida al historial.")

    def añadir_ultima_version(self, ultiVersion):
        self.mensajes_historial.append({"role": "user", "content": f"Esta es la ultima version del componente: {ultiVersion}"})
        print("Ultima version en area de analisis")


# Ejemplo de uso:
async def main():
    chat_manager = ChatManager()

    # Primera llamada: inicializa el chat y envía el primer mensaje
    mensaje_inicial = "Hola, ¿cómo puedo responder a este foro?"
    respuesta_inicial = await chat_manager.preguntar_a_openai(mensaje_inicial)
    
    # Si no estás conforme con la respuesta, puedes pedir una mejora
    usuario_conforme = input("¿Estás conforme con la respuesta? (sí/no): ").strip().lower()
    
    if usuario_conforme == "no":
        mejora = input("¿Qué mejorarías en la respuesta?: ").strip()
        chat_manager.agregar_mejora(mejora)
        
        # Enviar la mejora y obtener la nueva respuesta
        nueva_respuesta = await chat_manager.preguntar_a_openai(mensaje_inicial)
        print(f"Nueva respuesta después de la mejora: {nueva_respuesta}")
    else:
        print("Respuesta finalizada.")

# Ejecutar la función principal
#asyncio.run(main())
