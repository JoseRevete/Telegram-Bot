# **Telegram Bot para Automatización de Tareas**

---

## **Descripción**

Este proyecto es un bot de Telegram que automatiza tareas mediante Selenium y Telegram API, facilitando la interacción con aplicaciones web y la gestión de notificaciones a los usuarios a través de comandos personalizados. Entre las funciones principales, el bot permite consultar saldos en una página web específica, enviar mensajes a todos los usuarios, y manejar archivos (aunque algunas de estas funcionalidades están en construcción).

---

## **Requisitos**

Antes de comenzar, asegúrate de tener instalados los siguientes programas y bibliotecas:

### **1. Python 3.x**
   - Asegúrate de tener Python 3.x instalado en tu sistema.
   - Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### **2. Google Chrome**
   - El bot utiliza Selenium con Google Chrome, por lo que necesitas tener instalado este navegador.
   - Descárgalo desde [Google Chrome](https://www.google.com/chrome/).

### **3. ChromeDriver**
   - Necesitas ChromeDriver, que es el controlador que permite a Selenium interactuar con Google Chrome.
   - Asegúrate de que la versión de ChromeDriver coincida con la versión de tu navegador Chrome.
   - Descárgalo desde [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) y asegúrate de añadir su ubicación al PATH de tu sistema operativo.

### **4. Bibliotecas de Python**
   - Para instalar todas las bibliotecas necesarias, utiliza `pip`:

   ```sh
   pip install selenium python-telegram-bot apscheduler pyautogui
   ```

Estas bibliotecas son esenciales para el funcionamiento del bot:

- **Selenium:**  Interactúa con navegadores web de manera automatizada.
- **python-telegram-bot:** Interfaz para interactuar con la API de Telegram.
- **APSscheduler:** Para programar tareas periódicas en el bot.
- **pyautogui:** Para automatizar la interfaz gráfica (si es necesario).

### **5. Cuenta de Telegram Bot**
Necesitas crear un bot en Telegram y obtener un token para interactuar con la API de Telegram.
Puedes crear tu bot usando BotFather en Telegram. Sigue esta guía (https://origendata.com/2023/05/05/como-crear-un-bot-en-telegram/) para obtener tu token.

### **6. Clonar el Repositorio:**

```sh
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

    Ademas, recuerda colocar tus credenciales

## **Uso del Bot**

### **1. Ejecutar el Bot**

Para iniciar el bot, sigue estos pasos:

1. Asegúrate de haber configurado correctamente tus credenciales y haber instalado todas las dependencias necesarias.
2. Navega hasta el directorio raíz del proyecto donde se encuentra el archivo `bot.py`.
3. Ejecuta el siguiente comando en la terminal para iniciar el bot:

   ```sh
   python bot.py
   ```

### **2. Comandos Disponibles**

A continuación, se listan los comandos que puedes utilizar con este bot de Telegram, junto con una breve descripción de cada uno:

- **`/start`**: 
  - **Descripción**: Inicia la interacción con el bot.
  - **Uso**: Simplemente escribe `/start` para que el bot te salude y esté listo para recibir otros comandos.

- **`/help`**: 
  - **Descripción**: Muestra una lista de todos los comandos disponibles junto con sus descripciones.
  - **Uso**: Escribe `/help` para ver los comandos que puedes utilizar con el bot.

- **`/send_to_all [mensaje]`**: 
  - **Descripción**: Envía un mensaje a todos los usuarios registrados en el bot.
  - **Uso**: Escribe `/send_to_all` seguido del mensaje que deseas enviar. Ejemplo: `/send_to_all Hola a todos!`.

- **`/obtener_id`**: 
  - **Descripción**: Muestra tu ID de usuario de Telegram.
  - **Uso**: Escribe `/obtener_id` para recibir tu ID único de usuario en Telegram, lo cual es útil para configuraciones específicas.

- **`/cobreTads`**: 
  - **Descripción**: Consulta y muestra el saldo del vehículo asociado en el sistema Cobremex.
  - **Uso**: Escribe `/cobreTads` para recibir el saldo actual de tu vehículo.

- **`/avisar`**: 
  - **Descripción**: Envía una notificación a todos los usuarios registrados, indicando un mensaje predefinido.
  - **Uso**: Escribe `/avisar` para enviar un mensaje como "Ya voy subiendo" a todos los usuarios.

- **`/almacenar_en_pc`**: 
  - **Descripción**: Permite almacenar un archivo en tu PC.
  - **Estado**: *Este comando está en construcción*.
  - **Uso**: Actualmente en desarrollo.

- **`/obtener_archivo`**: 
  - **Descripción**: Permite obtener un archivo almacenado en tu PC y enviarlo a través de Telegram.
  - **Estado**: *Este comando está en construcción*.
  - **Uso**: Actualmente en desarrollo.