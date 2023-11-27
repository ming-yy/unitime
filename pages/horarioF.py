import flet as ft
from db.daos.asignaturaDao import asignatura_dao

class horario():
    def __init__(self, page: ft.Page, horaIni, horaFin, asignaturas):
        self.horaIni = horaIni
        self.horaFin = horaFin
        self.page = page
        self.MAX_ANCHURA = 6
        self.contenido = ["", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
        

        self.semanas = {}   
        for x in asignaturas:     # Guardamos las semanas de cada asignatura
            self.semanas[x['codigo']] = asignatura_dao.get_semana_by_code(x['codigo'])
        
        self.generarHorario(asignaturas)


    def generarHorario(self,asignaturas):
        #self.Horario.content.controls = None    # Limpiamos lo que hubiese antes
        #self.generarCabecera()
        self.generarHorasYAsignaturas(asignaturas)


    def generarCabecera(self):
        direccionHorario = self.Horario.content
        #direccionHorario.controls.append(ft.ResponsiveRow(spacing=0))
        for i in range(self.MAX_ANCHURA):
            #celda = self.ContainerCabecera.content=ft.Text(self.contenido[i],
            #        size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER)
            direccionHorario.controls[0].controls[i].content.value=self.contenido[i]


    def generarHorasYAsignaturas(self,asignaturas):
        #direccionHorario = self.Horario.content.controls
        #direccionHorario.append(ft.ResponsiveRow(spacing=0))
        
        self.generarColumnaHoras()

        #direccionColumna = self.Horario.content.controls[1]
        #direccionColumna.controls.append(ft.Column(spacing=0, col=2,))
        

        for dia in range(self.MAX_ANCHURA-1):       # Generamos las columnas de los días
            direccionColumna = self.Horario.content.controls[1].controls[dia+1].controls
            i = 0
            for hora0 in range(self.horaIni,self.horaFin+1):
                nombreAsignaturas = self.getNombresAsignaturas(dia, hora0,asignaturas)
                #aux = self.ContainerAsignatura.content=ft.Text(nombreAsignaturas ,size=18,
                #    color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER)
                #print(direccionColumna[i].content)
                direccionColumna[i].content.value = nombreAsignaturas
                i += 1

    def getNombresAsignaturas(self, dia, horaInicio,asignaturas):
        retVal = ""
        for i in asignaturas:      # Para cada asignatura
            cod = i['codigo']
            nombre = i['nombre']
            semanaActual = self.semanas[cod]
            for clase in semanaActual['dias'][dia]:     # Para cada clase de ese dia
                if clase:
                    if horaInicio >= clase['horaIni'] and horaInicio < clase['horaFin']:
                        retVal += nombre + "\n"
                        break

        return retVal

    def generarColumnaHoras(self):
        #direccionColumna = self.Horario.content.controls[1]
        #direccionColumna.controls.append(ft.Column(spacing=0,col=2,))
        direccionColumna = self.Horario.content.controls[1].controls[0].controls
        numHoras = self.horaFin-self.horaIni
        hora = self.horaIni
        for i in range(numHoras+1):
            nuevaHora = str(hora)+":00h"
            #aux = self.ContainerAsignatura.content=ft.Text(nuevaHora,size=18,
            #        color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER)
            #direccionColumna.append(aux)
            direccionColumna[i].content.value=nuevaHora
            hora += 1


    BarraNombre = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextField(hint_text="Horario sin título", autofocus=False,
                    height=50, text_size=12),
            ],
        ),
        padding= 20,
        bgcolor='#8986FF',
        border_radius=15,
        height=70,
    )
    
    Horario = ft.Container(
            content=ft.Column(
                controls=[
                    # Primer row con los días
                    ft.ResponsiveRow(
                        controls=[
                            # Primer espacio esquina superior izquierda
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content = ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Lunes",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Martes",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Miércoles",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Jueves",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Viernes",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                        ],
                        spacing=0,
                    ),
                    # Segundo row con las columnas de horas y horarios de asignaturas
                    ft.ResponsiveRow(
                        controls=[
                            # Columna de containers de horas
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                ],
                                spacing=0,
                                col=2,
                            ),
                            # Columna de containers de asignaturas de lunes
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("14:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                ],
                                spacing=0,
                                col=2,
                            ),
                            # Columna de containers de asignaturas de martes
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("14:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                ],
                                spacing=0,
                                col=2,
                            ),
                            # Columna de containers de asignaturas de miércoles
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("14:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                ],
                                spacing=0,
                                col=2,
                            ),
                            # Columna de containers de asignaturas de jueves
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("14:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                ],
                                spacing=0,
                                col=2,
                            ),
                            # Columna de containers de asignaturas de viernes
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("14:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=18,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                ],
                                spacing=0,
                                col=2,
                            ),
                        ],
                        spacing=0,
                    ),
                ],
                scroll=ft.ScrollMode.ADAPTIVE,
                spacing=0,
            ),
            bgcolor='#FFFFFF',
            height=500,
            expand=True,
        )
    
