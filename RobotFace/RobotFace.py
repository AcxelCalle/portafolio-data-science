import warnings
warnings.filterwarnings("ignore")

import flet as ft
import flet.canvas as cv
import cv2
import mediapipe as mp
import face_recognition
import pyttsx3
import threading
import time
import random
import os
import asyncio 

# --- CONFIGURACIÓN ---
SCALE = 4.0 
COLOR_OJOS = "cyan"
COLOR_FONDO = "black"

# Configura tu voz
# Con este ID identificamos la voz en español de México
# instalado en el Sistema Operativo.
VOZ_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"

# Colección de fotos para reconocimiento facial
# la clave es el nombre, el valor es el archivo de imagen

DB_FOTOS = {
     "Acxel": "acxel.jpg",
    # "Carlos": "carlos.jpg",
    # "Ana": "ana.jpg",
    # "Luis": "luis.jpg",
    # Agregar más según sea necesario
}

# --- BACKEND: VISIÓN ---
class VisionSystem:
    def __init__(self):
        # Intentar cámara 1, si no la 0
        self.cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) 
        if not self.cap.isOpened():
             self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1, refine_landmarks=True,
            min_detection_confidence=0.5, min_tracking_confidence=0.5
        )

        self.known_encodings = []
        self.known_names = []
        self._cargar_db()

        self.target_x = 0.0
        self.target_y = 0.0
        self.running = True
        self.ultimo_saludo = {}
        self.frame_count = 0

    def _cargar_db(self):
        print("--- Inicializando Biometría ---")
        for nombre, archivo in DB_FOTOS.items():
            if os.path.exists(archivo):
                try:
                    img = face_recognition.load_image_file(archivo)
                    enc = face_recognition.face_encodings(img)[0]
                    self.known_encodings.append(enc)
                    self.known_names.append(nombre)
                    print(f"✅ Cargado: {nombre}")
                except: pass

    def hablar_async(self, texto, jarvis_ui):
        def _worker():
            try:
                jarvis_ui.happy() 
                engine = pyttsx3.init()
                try: engine.setProperty('voice', VOZ_ID)
                except: pass
                engine.setProperty('rate', 160)
                engine.say(texto)
                engine.runAndWait()
                time.sleep(0.5)
                jarvis_ui.normal() 
            except: pass
        threading.Thread(target=_worker, daemon=True).start()

    def procesar_datos(self, jarvis_ui):
        """
        Este método corre en un HILO SECUNDARIO.
        Por eso podemos usar cv2.imshow aquí sin congelar Flet.
        """
        # Configuramos la ventana de OpenCV
        window_name = "SISTEMA VISUAL (BACKEND)"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(window_name, 400, 300)

        while self.running:
            success, frame = self.cap.read()
            if not success:
                time.sleep(0.1)
                continue
            
            # Espejo para efecto espejo
            frameInv = cv2.flip(frame, 1)
            
            # --- VISUALIZACIÓN EN VENTANA NATIVA (EL CAMBIO) ---
            # Mostramos el frame ANTES de reducirlo para procesar, para que se vea bien
            cv2.imshow(window_name, frameInv)
            
            # OBLIGATORIO: El corazón que mantiene viva la ventana de OpenCV
            # Si quitas esto, la ventana se pone gris y se cuelga.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break
            # ---------------------------------------------------

            # Procesamiento matemático (usamos una versión pequeña para velocidad)
            small_frame = cv2.resize(frame, (320, 240))
            rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            
            results = self.face_mesh.process(rgb_small)
            hay_cara = False
            
            if results.multi_face_landmarks:
                hay_cara = True
                nose = results.multi_face_landmarks[0].landmark[1]
                # Invertimos X para efecto espejo
                x_real = 1 - nose.x 
                self.target_x = max(-1.2, min(1.2, (x_real - 0.5) * 3.0))
                self.target_y = max(-1.0, min(1.0, (nose.y - 0.5) * 3.0))
            else:
                self.target_x = 0.0
                self.target_y = 0.0

            self.frame_count += 1
            # Reconocimiento facial cada 30 frames
            if self.frame_count % 30 == 0 and self.known_encodings and hay_cara:
                threading.Thread(target=self._verificar_identidad, args=(rgb_small, jarvis_ui)).start()

            # Pequeña pausa para no saturar la CPU
            time.sleep(0.01)
        
        # Limpieza al salir
        self.cap.release()
        cv2.destroyAllWindows()

    def _verificar_identidad(self, frame, jarvis_ui):
        try:
            # Encuentra todas las caras en el frame
            locs = face_recognition.face_locations(frame)
            # Toma los pixeles de la cara detectada y los convierte
            # en una lista de 128 números únicos (un vector). 
            # Es como convertir tu cara en una "contraseña
            # biométrica" matemática.
            encs = face_recognition.face_encodings(frame, locs) 
            for enc in encs:
                # Compara los números de la cara actual (enc)
                # contra tu base de datos de 
                # caras conocidas (self.known_encodings).
                matches = face_recognition.compare_faces(self.known_encodings, enc, 0.55)
                if True in matches:
                    nombre = self.known_names[matches.index(True)]
                    ahora = time.time()

                    # Saluda solo si no ha saludado en los últimos 20 segundos

                    if nombre not in self.ultimo_saludo or (ahora - self.ultimo_saludo[nombre] > 20):
                        frases = [f"Bienvenido {nombre}. Sistemas en línea y listos para trabajar.", 
                          f"Hola {nombre}, todo listo para comenzar.",
                          f"Es bueno tenerlo de vuelta jefe {nombre}",
                          f"{nombre}, los sistemas están operativos y esperando tus órdenes.",
                          f"Saludos {nombre}, todo está preparado para iniciar."]
                        self.hablar_async(random.choice(frases), jarvis_ui)
                        self.ultimo_saludo[nombre] = ahora
        except: pass

    def stop(self):
        self.running = False

# --- FRONTEND: JARVIS UI ---
class JarvisBrain:
    def __init__(self):
        self.current_look_x = 0.0
        self.current_look_y = 0.0
        self.blink_state = 0
        self.next_blink = time.time() + 2
        
        self.eye_w = 40 * SCALE
        self.eye_h = 40 * SCALE
        self.radius = 10 * SCALE
        
        self.canvas = cv.Canvas(shapes=[], content=ft.Container(expand=True))
        self.is_happy = False

    def _rect(self, x, y, w, h, r, color):
        return cv.Rect(x, y, w, h, r, ft.Paint(color=color))
    
    def _circle(self, x, y, r, color):
        return cv.Circle(x, y, r, ft.Paint(color=color))

    def update(self, target_x, target_y, cx, cy):
        self.current_look_x += (target_x - self.current_look_x) * 0.1
        self.current_look_y += (target_y - self.current_look_y) * 0.1
        
        off_x = self.current_look_x * (60 * SCALE)
        off_y = self.current_look_y * (40 * SCALE)
        space = 10 * SCALE

        lx = cx - (self.eye_w * 0.6) - (space / 2) + off_x
        ly = cy + off_y
        rx = cx + (self.eye_w * 0.6) + (space / 2) + off_x
        ry = cy + off_y

        self._blink_logic()
        self._draw(lx, ly, rx, ry)

    def _blink_logic(self):
        now = time.time()
        speed = 10 * SCALE
        if self.blink_state == 0 and now > self.next_blink: self.blink_state = 1
        
        if self.blink_state == 1: 
            self.eye_h -= speed
            if self.eye_h <= 2 * SCALE: 
                self.eye_h = 2 * SCALE
                self.blink_state = 2
        elif self.blink_state == 2:
            self.eye_h += speed
            if self.eye_h >= 40 * SCALE:
                self.eye_h = 40 * SCALE
                self.blink_state = 0
                self.next_blink = now + random.randint(2, 6)

    def _draw(self, lx, ly, rx, ry):
        safe_r = min(self.radius, min(self.eye_w, self.eye_h)/2) if min(self.eye_w, self.eye_h)/2 >= 1 else 0
        
        shapes = [
            self._rect(lx - self.eye_w/2, ly - self.eye_h/2, self.eye_w, self.eye_h, safe_r, COLOR_OJOS),
            self._rect(rx - self.eye_w/2, ry - self.eye_h/2, self.eye_w, self.eye_h, safe_r, COLOR_OJOS)
        ]
        
        if self.is_happy:
            offset_y = self.eye_h * 0.5 
            shapes.append(self._circle(lx, ly + offset_y, self.eye_w * 0.9, COLOR_FONDO))
            shapes.append(self._circle(rx, ry + offset_y, self.eye_w * 0.9, COLOR_FONDO))

        self.canvas.shapes = shapes
        self.canvas.update() 
        
    def happy(self): self.is_happy = True
    def normal(self): self.is_happy = False


# --- APP PRINCIPAL (ASYNC) ---
async def main(page: ft.Page):
    page.title = "Jarvis Async Core + Visual Feedback"
    page.bgcolor = "black"
    page.padding = 0
    page.window_width = 800
    page.window_height = 600
    
    jarvis_brain = JarvisBrain()
    vision_system = VisionSystem()

    main_container = ft.Container(
        content=jarvis_brain.canvas,
        expand=True,
        bgcolor="black",
        # Un borde cyan para que se vea genial
        border=ft.border.all(2, "cyan") 
    )

    page.add(main_container)

    # 1. Hilo de Visión (Ahora con ventana propia)
    t_vision = threading.Thread(
        target=vision_system.procesar_datos, 
        args=(jarvis_brain,)
    )
    t_vision.daemon = True
    t_vision.start()

    # 2. Bucle Asíncrono de UI
    print("👁️ Jarvis Iniciado. Busca la segunda ventana 'SISTEMA VISUAL'...")
    
    try:
        while True:
            w = page.width if page.width else 800
            h = page.height if page.height else 600
            
            jarvis_brain.update(vision_system.target_x, vision_system.target_y, w/2, h/2)
            
            # Cede el control para que Flet respire
            await asyncio.sleep(0.016) 
            
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"Error: {e}")
    finally:
        vision_system.stop()

if __name__ == "__main__":
    ft.app(target=main)