import flet as ft
import middleware.baseHorarios as Base

class Plantillas:
    def obtenerAnyoCarrera(self, page: ft.Page, anyo, asignaturas, pantalla):

        self.page = page
        def on_click_anyo(e):
            aux = pantalla[anyo-1].content.controls[1].visible
            pantalla[anyo-1].content.controls[1].visible=not aux
            self.page.update()

        AnyoCarrera=ft.Container(
            height=200,
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text=str(anyo) + " º",
                        width=200,
                        height=200,
                        style=ft.ButtonStyle(
                            color=ft.colors.BLACK,
                            bgcolor={ft.MaterialState.DEFAULT: '#FEC456'},
                            side={ft.MaterialState.DEFAULT:
                                    ft.BorderSide(3, '#CB9D45')},
                            shape={
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
                            },
                        ),
                    ), 
                    ft.Container(
                        content=ft.Row(
                            controls= asignaturas,
                            scroll=ft.ScrollMode.AUTO,
                            expand=True,
                            alignment=ft.MainAxisAlignment.SPACE_AROUND
                        ),
                        padding=20,
                        bgcolor="#FFCB83",
                        expand=True,
                        border_radius=15,
                    )
                ],
            ),
        )

        AnyoCarrera.content.controls[0].on_click=on_click_anyo

        return AnyoCarrera
    
    def obtenerAsignaturaCarrera(self, nombre, codigo, lista):

        def on_asignatura_click(e):
            res = Base.get_asignatura_by_codeId(codigo)
            lista.append(res)
            
        AsignaturaGrupoCarrera=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(
                    text=nombre,
                    width=150,
                    height=50,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor={ft.MaterialState.DEFAULT: '#1B7746'},
                        shape={
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
                        },
                    ),
                    on_click=on_asignatura_click
                ),

            ],
        )
        return AsignaturaGrupoCarrera
    
    def obtenerGrupoCarrera(self, codigo, horaInicio, horaFin, listaInicio, listaFin):

        def on_grupo_click(e):
            listaInicio.append(horaInicio)
            listaFin.append(horaFin)
            
        AsignaturaGrupoCarrera=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(
                    text=codigo,
                    width=150,
                    height=50,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor={ft.MaterialState.DEFAULT: '#1B7746'},
                        shape={
                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
                        },
                    ),
                    on_click=on_grupo_click
                ),

            ],
        )
        return AsignaturaGrupoCarrera

plantillas = Plantillas()