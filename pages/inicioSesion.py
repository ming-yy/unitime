import flet as ft
import pages.baseHorarios as basHor
import pages.registrarse as Reg
import middleware.inicioSesion as iniSesion
import pages.cambiarContrasenya as Change

# Correo adds@abc.com
# Contraseña abc
class inicioSesion:
    def __init__(self, page: ft.Page):
        # Inicializa el atributo 'page'
        self.page = page 
        page.route="/inicioSesion"

        # Distintas paginas en relacion con Iniciar Sesion
        self.paginaBaseHorarios = None

        self.paginaRegis = None

        self.paginaChange = None

        # Manejador de login
        self.BotonInicioSesion.controls[0].on_click = self.on_login_click
        # Manejador de registro
        self.BotonRegistrar.controls[1].on_click = self.on_register_click
        # Manejador de cambio de contraseña
        self.OpcionRecordarOlvidona.controls[1].on_click = self.on_remember_click
        # Layout de la app
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
                                self.TituloInicioSesion,
                                self.CampoUsuario,
                                self.CampoContraseña,
                                self.OpcionRecordarOlvidona,
                                self.ErrorInicioSesion,
                                self.BotonInicioSesion,
                                self.BotonRegistrar,
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

    def inicializarBaseHorarios(self,email,contrasenya):
        if self.paginaBaseHorarios is None:
            self.paginaBaseHorarios = basHor.baseHorarios(self.page,email,contrasenya)
        

    def on_login_click(self, e):
        # Obtenemos email y contraseña
        direccion = self.Pantalla.content.controls[0].content
        email = direccion.controls[1].controls[0].value
        contrasenya = direccion.controls[2].controls[0].value
        respuesta = iniSesion.autentificar_usuario(email, contrasenya)
        if respuesta:
            self.inicializarBaseHorarios(email,contrasenya)
            self.page.add(self.paginaBaseHorarios.Pantalla)
            self.page.update()
        else:  # Opcionalmente puedes mostrar un mensaje de error si las credenciales son incorrectas
            self.ErrorInicioSesion.controls[0].visible = True
            self.page.update()

    def on_register_click(self, e):
        self.Pantalla.content.controls[0].clean()
        self.paginaRegis = Reg.registrar(self.page)
        self.Pantalla.content.controls.append(self.paginaRegis.pantalla)
        self.page.update()

    def on_remember_click(self, e):
        self.page.clean()
        self.paginaChange = Change.cambiarContrasenya(self.page)
        self.page.add(self.paginaChange.Pantalla)
        self.page.update()
    
    TituloInicioSesion = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Iniciar Sesión\n", size=30, color=ft.colors.BLACK,
                                        weight=ft.FontWeight.W_600),
                            ]
                        )
    CampoUsuario = ft.Row(
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
    OpcionRecordarOlvidona = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=43,
                            controls=[
                                ft.Checkbox(label="Recuérdame", value=False,
                                            fill_color=ft.colors.WHITE,
                                            check_color=ft.colors.BLACK),
                                ft.TextButton(text="Olvidé la contraseña",
                                              style=ft.ButtonStyle(color=ft.colors.BLACK))
                            ],
                        )
    BotonInicioSesion = ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    "     Iniciar sesión     ",
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
                                ft.Text("Email o contraseña no correctos", size=15, color=ft.colors.RED_ACCENT_400,
                                        weight=ft.FontWeight.W_500, visible=False),
                            ],
                        )

    BotonRegistrar = ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                        controls=[
                            ft.Text("¿No estás registrado?", size=15, color=ft.colors.BLACK,),
                            ft.TextButton(text="Registrarse",
                                            style=ft.ButtonStyle(color=ft.colors.BLACK))
                        ],
                    )
