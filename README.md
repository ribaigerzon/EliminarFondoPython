# EliminarFondoPython

Este script en Python permite recortar automáticamente el espacio vacío (transparente) que rodea una imagen PNG. Es ideal para preparar íconos, ilustraciones o recursos gráficos que necesiten un marco ajustado a su contenido real.

🚀 Funcionalidad

El script:

- Permite al usuario seleccionar una imagen PNG desde el explorador de archivos de Windows.
- Recorta automáticamente los bordes transparentes de la imagen.
- Guarda la imágen recortada en una carpeta de destino elegida por el usuario.

Mantiene la transparencia (canal alfa) y el formato PNG.

🧰 Requisitos

Este script requiere:

- Python 3.6 o superior
- Las bibliotecas: Pillow y tkinter

Puedes instalar Pillow con:

  pip install Pillow
  
tkinter suele estar incluido en las instalaciones estándar de Python para Windows.

🖥️ ¿Cómo usarlo?

- Clona este repositorio:

git clone https://github.com/tu-usuario/recortador-imagenes-png.git
cd recortador-imagenes-png

- Ejecuta el script:

python recortar_png.py

- Selecciona las imágenes PNG que deseas recortar.

- Selecciona la carpeta donde deseas guardar las imágenes recortadas.

¡Listo! Las imágenes procesadas se guardarán con el mismo nombre, en la carpeta que elegiste.

📦 Versión ejecutable (Windows)
También puedes descargar y ejecutar el archivo .exe sin necesidad de instalar Python. Descarga el ejecutable que se encuentra en mi Drive:

https://drive.google.com/file/d/1eRFmSpQbG4I7MT11TklZMjz2TDlUI9yw/view?usp=sharing

📷 Ejemplo visual

Antes	

<img width="1080" height="1080" alt="2" src="https://github.com/user-attachments/assets/2833c65a-4585-4fdb-9f51-b7108c99c393" />

Después

<img width="1080" height="1080" alt="2_sin_fondo" src="https://github.com/user-attachments/assets/eb905b5f-5d4b-48f9-a4db-f6c14d4bbba3" />



📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.
