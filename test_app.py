import unittest
# Importamos la instancia de Flask 'app' desde tu archivo app.py
from app import app 

class TestApplication(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba."""
        # Crea un cliente de pruebas de Flask para simular peticiones HTTP sin levantar el servidor
        self.app = app.test_client()
        self.app.testing = True

    def test_1_home_status_code(self):
        """
        CRITERIO 3: Verifica que la ruta principal '/' responde con 200 OK.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_2_home_content(self):
        """
        CRITERIO 3: Verifica que el contenido de la página principal contiene el mensaje esperado.
        
        NOTA: Para evitar errores de codificación ASCII, la verificación se hace solo sobre la parte
        del mensaje que es ASCII simple, ya que la '¡' causaba conflicto.
        """
        response = self.app.get('/')
        # Verifica la parte ASCII del mensaje. Tu app.py devuelve: "¡Hola Mundo desde Flask con Traefik! 🚀"
        # Verificamos la parte: "Hola Mundo desde Flask con Traefik!" (sin el signo de apertura)
        expected_message_ascii = b"Hola Mundo desde Flask con Traefik!"
        self.assertIn(expected_message_ascii, response.data)
        
    def test_3_nonexistent_route_404(self):
        """
        CRITERIO 3: Verifica que cualquier ruta que NO exista (incluyendo /predict) 
        responde correctamente con 404 Not Found.
        """
        # Ya que /predict no está en app.py, debe devolver 404.
        response = self.app.get('/predict') 
        self.assertEqual(response.status_code, 404)