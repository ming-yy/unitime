import flet as ft
from db.daos.asignaturaDao import asignatura_dao

class horario():
    def __init__(self, page: ft.Page):
        self.page = page
        """
        self.asignaturas = asignatura_dao.get_all()
        for i in asignaturas:
            self.semanas[i['codigo']] = semanas_dao.get_semana_by_code(i['codigo'])
        """

    Horario = ft.Container(
            content=ft.Column(
                controls=[
                    # Primer row con los días
                    ft.ResponsiveRow(
                        controls=[
                            # Primer espacio esquina superior izquierda
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Lunes",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Martes",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Miércoles",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Jueves",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                #width=150,
                                height=50,
                                col=2,
                            ),
                            ft.Container(
                                border= ft.border.all(3, ft.colors.GREY),
                                content=ft.Text("Viernes",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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
                                        content=ft.Text("14:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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
                                        content=ft.Text("14:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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
                                        content=ft.Text("14:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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
                                        content=ft.Text("14:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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
                                        content=ft.Text("14:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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
                                        content=ft.Text("14:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("15:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("16:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("17:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("18:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("19:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                                        width=300,
                                        height=100,
                                    ),
                                    ft.Container(
                                        border= ft.border.all(3, ft.colors.GREY),
                                        content=ft.Text("20:00",size=30,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
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

    BarraNombre = ft.Container(
        content=ft.Row(
            controls=[
                ft.TextField(hint_text="Introducir nombre de horario... ...", autofocus=False,
                    expand=True, height=50, text_size=12),
            ],
        ),
        padding= 20,
        bgcolor='#8986FF',
        border_radius=15,
        height=70,
    )