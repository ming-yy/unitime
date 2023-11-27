import flet as ft
import pages.inicioSesion as iniSes
import middleware.cambiarContrasenya as CambiarContrasenya

class nuevaContrasenya:
    def __init__(self, page: ft.Page,email,user):

        # Pagina de Inicio
        self.paginaInicio = None
        self.user = user
        self.email = email

        self.page = page
        self.passwd = None
        self.passwdConf = None

        # Manejadores de campos de contraseñas
        self.CampoContraseña.controls[0].on_change=self.on_passwrd_init
        self.CampoContraseña2.controls[0].on_change=self.on_passwrd_confirm

        # Manejador de cambio de contraseña
        self.BotonCambiar.controls[1].on_click = self.on_change_click

        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        fondoPantallaInicioSesion = '../assets/images/bgSesion.png'
        pantalla = ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        bgcolor='#8986FF',
                        border_radius=10,
                        width=450,
                        height=400,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.TituloContra,
                                self.CampoContraseña,
                                self.CampoContraseña2,
                                self.BotonCambiar,
                                self.ErrorCambio,
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

    def on_passwrd_init(self,e):
        self.passwd = self.CampoContraseña.controls[0].value

    def on_passwrd_confirm(self,e):
        self.passwdConf = self.CampoContraseña2.controls[0].value

    def on_change_click(self, e):
        if self.passwd == self.passwdConf and self.passwd is not None and self.passwdConf is not None:
            CambiarContrasenya.update_password(self.email, self.passwd)     # Actualizamos contraseña
            self.page.clean()
            self.paginaInicioSesion = iniSes.inicioSesion(self.page)
            self.page.add(self.paginaInicioSesion.Pantalla)
        else:
            self.ErrorCambio.controls[0].visible=True
        self.page.update()
    
    TituloContra = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Cambiar mi contraseña\n", size=30, color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_600),
                            ]
                        )
    CampoContraseña = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Contraseña nueva", text_align=ft.TextAlign.LEFT,
                                             password=True, can_reveal_password=True,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2,
                                             focused_border_color=ft.colors.WHITE, color='#000000'),
                            ],
                        )
    CampoContraseña2 = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Confirmar nueva contraseña", text_align=ft.TextAlign.LEFT,
                                             password=True, can_reveal_password=True,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2,
                                             focused_border_color=ft.colors.WHITE, color='#000000'),
                            ],
                        )
    
    BotonCambiar = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Container(height=125),
                                ft.ElevatedButton(
                                    "     Cambiar     ",
                                    width=200,
                                    height=40,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.BLACK,
                                        bgcolor={ft.MaterialState.DEFAULT: '#FEC456'},
                                        side={ft.MaterialState.DEFAULT:
                                                ft.BorderSide(3, '#CB9D45')},
                                        shape={
                                            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
                                        },          
                                    ),
                                )
                            ],   
                        )
    ErrorCambio = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=43,
                            controls=[
                                ft.Text("Las contraseñas no coinciden o estan vacias", size=15, color=ft.colors.RED_ACCENT_400,
                                        weight=ft.FontWeight.W_500, visible=False),
                            ],
                        )