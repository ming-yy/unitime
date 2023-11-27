import flet as ft
import re
import pages.inicioSesion as iniSes
import middleware.registrarse as Reg
from db.models.user import User


class registrar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.paginaInicioSesion = None
        self.email = None
        self.user = None
        self.passwd = None
        self.passwdConf = None
        # Manejador de boton de registro
        self.BotonRegistrarse.controls[0].on_click=self.on_register_click

        # Manejador de campo user
        self.CampoUsuario.controls[0].on_change=self.on_user_init
        # Manejador de campo email
        self.CampoEmail.controls[0].on_change=self.on_email_init
        # Manejadores de campos de contraseñas
        self.CampoContraseña.controls[0].on_change=self.on_passwrd_init
        self.CampoContraseña2.controls[0].on_change=self.on_passwrd_confirm

    def es_correo_valido(self):
        # Expresión regular para validar un correo electrónico
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, self.email) is not None
    
    def es_correo_registrado(self):
        # Buscar correo en base de datos
        if Reg.get_usuario(self.email) is not None:
            return True
        else:
            return False
        
    def on_register_click(self, e):   
        # Si no son variables vacias
        if all([self.email, self.user, self.passwd, self.passwdConf]):
            # Si el correo es valido y no esta registrado
            if self.es_correo_valido() and not self.es_correo_registrado():
                if self.passwd == self.passwdConf:
                    newUser = User(email=self.email, username=self.user, password=self.passwd)
                    Reg.add_usuario(newUser)
                    self.page.clean()
                    self.paginaInicioSesion = iniSes.inicioSesion(self.page)
                    self.page.add(self.paginaInicioSesion.Pantalla)
                else:
                    self.ErrorRegistro.controls[0].visible=True
                    self.ErrorRegistro.controls[0].value = "Las contraseñas no coinciden"
            else:
                self.ErrorRegistro.controls[0].visible=True
                self.ErrorRegistro.controls[0].value = "El correo es invalido o ya esta registrado."
        else:
            self.ErrorRegistro.controls[0].visible=True
            self.ErrorRegistro.controls[0].value = "Todos los campos son obligatorios"
        self.page.update()


    def on_user_init(self,e):
        self.user = self.CampoUsuario.controls[0].value

    def on_email_init(self,e):
        self.email = self.CampoEmail.controls[0].value

    def on_passwrd_init(self,e):
        self.passwd = self.CampoContraseña.controls[0].value

    def on_passwrd_confirm(self,e):
        self.passwdConf = self.CampoContraseña2.controls[0].value
        


    TituloRegistrar = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Registrarse", size=30, color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_600),
                            ]
                        )
    CampoUsuario = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Usuario", text_align=ft.TextAlign.LEFT,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2,
                                             focused_border_color=ft.colors.GREY, color='#000000'),
                            ],
                        )
    CampoEmail = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Email", text_align=ft.TextAlign.LEFT,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2, 
                                             focused_border_color=ft.colors.GREY, color='#000000'),
                            ],
                        )
    CampoContraseña = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Contraseña", text_align=ft.TextAlign.LEFT,
                                             password=True, can_reveal_password=True,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2,
                                             focused_border_color=ft.colors.GREY, color='#000000'),
                            ],
                        )
    CampoContraseña2 = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Confirmar contraseña", text_align=ft.TextAlign.LEFT,
                                             password=True, can_reveal_password=True,
                                             bgcolor=ft.colors.WHITE, border_radius=10,
                                             border_color=ft.colors.GREY, width=300,
                                             height=40, border=ft.InputBorder.OUTLINE,
                                             border_width=2, 
                                             focused_border_color=ft.colors.GREY, color='#000000'),
                            ],
                        )
    BotonRegistrarse = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    "     Registrarse     ",
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
    ErrorRegistro = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=43,
                            controls=[
                                ft.Text(size=15, color=ft.colors.RED_ACCENT_400,
                                        weight=ft.FontWeight.W_500, visible=False),
                            ],
                        )
    
    pantalla=ft.Container(
            bgcolor='#8986FF',
            border_radius=10,
            alignment=ft.alignment.center,
            width=450,
            height=400,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    TituloRegistrar,
                    CampoUsuario,
                    CampoEmail,
                    CampoContraseña,
                    CampoContraseña2,                                
                    ErrorRegistro,
                    BotonRegistrarse,
                ],
            )
    )
