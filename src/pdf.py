from fpdf import FPDF

pdf = FPDF()

# Agregamos página.
pdf.add_page()

# Establecemos la fuente a utilizar.
pdf.set_font('Arial', 'B', 16)

# Establecemos el color del fondo de la página.
pdf.set_fill_color(255,0,0)
pdf.rect(0,0,210,297,"F")

# Agregamos un texto introducido dentro de una celda.
pdf.cell(60, 3, "NINTENDO EN LOS ÚLTIMOS 10 AÑOS")

# Seleccionamos imágenes .png que queremos insertar.
pdf.image(f"../outputs/barh.png", 20, pdf.get_y()+5, w=170)
pdf.image(f"../outputs/box.png", 20, pdf.get_y()+210, w=170)
pdf.image(f"../inputs/nintendo.png", 150, 0, w=36)

# Exportamos el documento a la carpeta deseada.
pdf.output("../outputs/Nintendo.pdf", "F")


