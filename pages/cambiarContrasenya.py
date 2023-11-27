import flet as ft
import time
import pages.nuevaContrasenya as Inicio
import pages.pantallaCarga as Email_send
import middleware.cambiarContrasenya as Change
import smtplib

class cambiarContrasenya:
    def __init__(self, page: ft.Page):
        self.page = page
        self.user = None
        self.email = None
        # Pagina de envio de email
        self.paginaEmail = None
        # Pagina de Inicio
        self.paginaInicio = None
        # Manejador de cambio de contraseña
        self.BotonCambiar.controls[1].on_click = self.on_change_click
        # Manejador de campo email
        self.CampoEmail.controls[0].on_change=self.on_email_init

        # Email de la aplicacion y contraseña
        self.email_app= "unitimecontactapp@gmail.com"
        self.password = "yyoo crzb ckji mwfk"

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
                        width=450,
                        height=400,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                self.TituloContra,
                                self.CampoEmail,
                                self.BotonCambiar,
                                self.ErrorInicioSesion,
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

    def es_correo_registrado(self):
        # Buscar correo en base de datos
        if Change.get_usuario(self.email) is not None:
            return True
        else:
            return False

    def on_email_init(self,e):
        self.email = self.CampoEmail.controls[0].value

    def on_change_click(self, e):
        if self.es_correo_registrado():
            self.page.clean()
            self.paginaChange = Email_send.pantallaCarga(self.page)
            self.page.add(self.paginaChange.Pantalla)
            self.page.update()
            # Se muestra un aviso del email
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()

            s.login(self.email_app,self.password)

            message = f'Subject: {"Recuperacion de cuenta"} \n\n {"Para recuperar la cuenta responda a este correo"} '

            s.sendmail(from_addr=self.email_app, 
                       to_addrs=self.email, 
                       msg=message)
            s.quit()

            time.sleep(5)
            # Se vuelve al estado inicial tras el aviso
            self.page.clean()
            self.user= Change.get_usuario(self.email)
            self.paginaInicio = Inicio.nuevaContrasenya(self.page,self.email,self.user['username'])
            self.page.add(self.paginaInicio.Pantalla)
        else:
            self.ErrorInicioSesion.controls[0].visible=True
        self.page.update()
    
    TituloContra = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Cambiar mi contraseña\n", size=30, color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_600),
                            ]
                        )
    CampoEmail = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Email", text_align=ft.TextAlign.LEFT,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2, focused_border_width=7,
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
    ErrorInicioSesion = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=43,
                            controls=[
                                ft.Text("Email no registrado o incorrecto", size=15, color=ft.colors.RED_ACCENT_400,
                                        weight=ft.FontWeight.W_500, visible=False),
                            ],
                        )