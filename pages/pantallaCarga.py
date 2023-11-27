import flet as ft
import pages.inicioSesion as Inicio
import time
from math import radians

class pantallaCarga:
    def __init__(self, page: ft.Page):
        self.page = page

        # User interface
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        fondoPantallaInicioSesion = '../assets/images/bgSesion.png'
        pantalla = ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        bgcolor='#8986FF',
                        border_radius=10,
                        alignment=ft.alignment.center,
                        width=450,
                        height=400,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.TextoAviso,
                            ],
                        )
                    ),
                ],
            ),
            alignment=ft.alignment.center,
            image_src=fondoPantallaInicioSesion,
            image_fit=ft.ImageFit.COVER,
            expand = True,
        )
        self.Pantalla = pantalla





    Loading = '../assets/icons/loading.png'

    TextoAviso = ft.Column(
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "Se envió un email a su\ncuenta, por favor\nverifique que es el dueño\nde la cuenta para\nproceder\n",
                size=25,
                color=ft.colors.BLACK,
                weight=ft.FontWeight.W_600,
                text_align=ft.TextAlign.CENTER,
            ),
        ft.ProgressRing(color=ft.colors.BLACK,width=60,height=60),
        ],
    )

    def rotate_image(self, sender):
        self.rotation_angle += 5  # Aumenta la rotación en 5 grados
        if self.rotation_angle >= 360:
            self.rotation_angle = 0  # Restablece la rotación

        # Actualiza la imagen con la nueva rotación
        self.TextoAviso.controls[1] = ft.Image(
            src=self.Loading,
            width=200,
            height=200,
            transform=ft.Transform.rotate(radians(self.rotation_angle))
        )
        self.page.update()