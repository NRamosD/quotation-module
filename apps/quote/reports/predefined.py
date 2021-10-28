from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        # Logo
        self.image('logo.png', x = 10, y = 10, w = 15, h = 15)

        # Arial bold 25
        self.set_font('Arial', 'B', 25)

        # Title
        self.cell(w = 0, h = 15, txt = 'Encabezado', border = 1, ln=1,
                align = 'C', fill = 0)   

        # Line break
        self.ln(5)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}', border = 1,
                align = 'C', fill = 0)   

"""
# IMAGEN (jpg/png) -----

url = 'https://github.com/ALEX7320'

pdf.image('logo.png',
        x= 50, y= 120,
        w = 60, h = 60,
        link = url)


pdf.output('hoja.pdf', 'F')"""

#PARA ESTILOS https://github.com/ALEX7320/guia-pdf-python/tree/master/9%20Establecer%20estilos
def reportUser(allUsers):
        # datos para usar
        usersList = []
        for x in allUsers:
                #                 cédula,    nombre,        apellido,   correo,    celular,      ciudad
                usersList.append((x.id_card, x.first_name, x.last_name, x.email, x.mobile_phone, x.city))

        dataInTuple = tuple(usersList)

        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.add_page()

        # TEXTO
        pdf.set_font('Arial', '', 15)

        # titulo
        pdf.cell(w = 0, h = 15, txt = 'Reporte de Usuarios', border = 1, ln=1,
                align = 'C', fill = 0)


        # TEXTO
        pdf.set_font('Arial', '', 12)
        # encabezado cédula,    nombre,        apellido,   correo,    celular,      ciudad
        pdf.cell(w = 30, h = 10, txt = 'Cédula', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 35, h = 10, txt = 'Nombres', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 35, h = 10, txt = 'Apellidos', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 35, h = 10, txt = 'Correo', border = 1,
                align = 'C', fill = 0)

        pdf.cell(w = 30, h = 10, txt = 'Celular', border = 1,
                align = 'C', fill = 0)

        pdf.multi_cell(w = 0, h = 10, txt = 'Ciudad', border = 1,
                align = 'C', fill = 0)

        
        # TEXTO
        pdf.set_font('Arial', '', 8)
        # valores
        for valor in dataInTuple:
                pdf.cell(w = 30, h = 7, txt = str(valor[0]), border = 1, align = 'C', fill = 0)
                pdf.cell(w = 35, h = 7, txt = valor[1], border = 1, align = 'C', fill = 0)
                pdf.cell(w = 35, h = 7, txt = valor[2], border = 1, align = 'C', fill = 0)
                pdf.cell(w = 35, h = 7, txt = valor[3], border = 1, align = 'C', fill = 0)
                pdf.cell(w = 30, h = 7, txt = valor[4], border = 1, align = 'C', fill = 0)
                pdf.multi_cell(w = 0, h = 7, txt = valor[5], border = 1, align = 'C', fill = 0)

        #elDato = pdf.output('hoja.pdf','D')
        #print(f"plano  -> {elDato}")
        #print(f'el tipo {type(elDato)}')
        pdf.output(f'./files/ReporteUsuarios.pdf','F')










"""
    data = (
        ("First name", "Last name", "Age", "City"),
        ("Jules", "Smith", "34", "San Juan"),
        ("Mary", "Ramos", "45", "Orlando"),
        ("Carlson", "Banks", "19", "Los Angeles"),
        ("Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
    )

    def reportUser(allUsers):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", size=10)

        line_height = pdf.font_size * 2.5
        col_width = pdf.epw / 4  # distribute content evenly
        usersList = []
        for x in allUsers:
            usersList.append((x.first_name, x.last_name, x.email, x.country))
        
        dataInTuple = tuple(usersList)

        
        for row in dataInTuple:
            #eso = (row.first_name, row.last_name, row.email, row.country)
            #pdf.multi_cell(col_width, line_height, eso, border=1, ln=3, max_line_height=pdf.font_size)
            #print(f"eso -> {row.first_name} {row.last_name} {row.email} {row.country}")
            #dataInTuple = ((row.first_name, row.last_name, row.email, row.country))
            #print(f"tipo {type(dataInTuple)}")
            #print(f"ahi ta -> {eso}")
            #pdf.multi_cell(col_width, line_height,row, border=1, ln=3, max_line_height=pdf.font_size)
            for dataInCell in row:
                #dataInTuple = (datarow.first_name, datarow.last_name, datarow.email, datarow.country)
                #print(f"ahi ta -> {datarow}")
                pdf.multi_cell(col_width, line_height, dataInCell, border=1, ln=3, max_line_height=pdf.font_size)
            pdf.ln(line_height)

        print("Listo el pdf")
        pdf.output('D', 'firstReport.pdf')



    # def reportUser(allUsers):
    #     pdf = FPDF()
    #     pdf.add_page()
    #     pdf.set_font("Times", size=10)
    #     line_height = pdf.font_size * 2.5
    #     col_width = pdf.epw / 4  # distribute content evenly
    #     for row in data:
    #         for datum in row:
    #             pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
    #         pdf.ln(line_height)
    #     pdf.output('firstReport.pdf')

"""
