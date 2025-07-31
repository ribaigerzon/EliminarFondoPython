"""
    Crear un entorno virtual con python 3.10
        py -3.10 -m venv env
    Activar el entorno virtual
        env\Scripts\activate
    Instalar paquetes
        pip install --upgrade pip
        pip install rembg pillow
"""

from rembg import remove
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_imagen():
    """Abre el explorador para seleccionar una imagen."""
    return filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp *.webp *.tiff")]
    )

def seleccionar_carpeta_salida():
    """Abre el explorador para seleccionar la carpeta de destino."""
    return filedialog.askdirectory(title="Seleccionar carpeta de destino")

def remover_fondo_y_guardar_png(ruta_entrada, carpeta_salida):
    try:
        if not ruta_entrada or not carpeta_salida:
            print("⚠️ Proceso cancelado por el usuario.")
            return

        nombre_archivo = os.path.splitext(os.path.basename(ruta_entrada))[0] + "_sin_fondo.png"
        ruta_salida = os.path.join(carpeta_salida, nombre_archivo)

        # Abrir y procesar imagen
        input_image = Image.open(ruta_entrada)
        output_image = remove(input_image)

        # Guardar como PNG
        output_image.save(ruta_salida, format="PNG")

        messagebox.showinfo("¡Éxito!", f"Imagen guardada sin fondo:\n{ruta_salida}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter

    print("\n📸 Removedor de Fondo de Imágenes (con explorador gráfico)\n")

    if messagebox.askyesno("Removedor de Fondo", "¿Deseas seleccionar una imagen para remover su fondo?"):
        ruta_entrada = seleccionar_imagen()
        carpeta_salida = seleccionar_carpeta_salida()
        remover_fondo_y_guardar_png(ruta_entrada, carpeta_salida)
    else:
        print("🚫 Operación cancelada por el usuario.")

