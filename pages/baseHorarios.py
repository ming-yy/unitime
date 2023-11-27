import flet as ft
import pages.inicioSesion as iniSes
import middleware.baseHorarios as baseSesion
import pages.horarioF as Horario
from pages.plantillas.plantillas import plantillas
from db.models.misAsignaturas import misAsignaturas
from db.models.horario import Horario as horarioNuevo


class baseHorarios():
    def __init__(self, page: ft.Page, email, contrasenya):
        # Inicializa el atributo 'page' 
        self.page = page
        self.page.clean()
        self.page.route="/baseHorarios"
        self.page.bgcolor = ft.colors.WHITE
        self.cuenta = baseSesion.get_usuario(email)
        self.usuario = self.cuenta['username']
        self.email = self.cuenta['email']
        self.contrasenya = self.cuenta['password']
        self.admin = self.cuenta['soyAdmin']     
        self.horarios = self.cuenta['horarios']

        self.listaAsignaturas = []
        self.listaInicio = []
        self.listaFin = []

        #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        #page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.Anyadir.controls[0].on_click = self.on_create_click

        self.Opciones.content.controls[1].content.on_click=self.on_next_click
        self.Opciones.content.controls[0].content.on_click=self.on_clear_click

        self.SeleccionHorario.content.controls[1].controls[0].controls[1].on_change= self.dropdown_changed
        self.SeleccionHorario.content.controls[1].controls[1].controls[1].on_change= self.dropdown_changed

        self.paginaHorario = Horario.horario(self.page,0,0,[])
        self.page.update()

        self.dialog = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Configuración",size=40,color=ft.colors.BLACK,text_align=ft.MainAxisAlignment.CENTER),
                            ft.IconButton(
                                icon=ft.icons.CLOSE,
                                icon_color="black",
                                icon_size=50,
                                tooltip="Cerrar Configuración",
                                on_click=self.close_dialog,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(value="Cambiar nombre",size=30,color=ft.colors.BLACK,text_align=ft.MainAxisAlignment.CENTER),
                            ft.TextField(hint_text="Nuevo nombre", autofocus=False,
                            width=400, height=40, text_size=20,),
                            ft.ElevatedButton(
                                "Confirmar",
                                width=130,
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
                            ),
                            ft.Container(width=20),
                            ft.Text(value="Cambiar contraseña",size=30,color=ft.colors.BLACK,text_align=ft.MainAxisAlignment.CENTER),
                            ft.TextField(hint_text="Nueva contraseña", autofocus=False,
                            width=400, height=40, text_size=20,can_reveal_password=True,password=True),
                            ft.TextField(hint_text="Confirmar nueva contraseña", autofocus=False,
                            width=400, height=40, text_size=20,can_reveal_password=True,password=True),
                            ft.ElevatedButton(
                                "Confirmar",
                                width=130,
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
                            ),
                        ],
                    ),
                ],
            ),
            bgcolor='#8986FF',
            expand=True,
            padding=20,
        )

        # Asignar esta función al evento on_click del botón de configuración
        config_button = self.Usuario.controls[0].items[1].content
        config_button.on_click = self.open_config_dialog

        logoutButton = self.Usuario.controls[0].items[2].content
        logoutButton.on_click = self.on_logOut_click

        primer_container = ft.Container(
            content=ft.Column(
                        controls=[
                            ft.Column(
                                controls=[
                                    self.Usuario,
                                    self.separador,
                                    self.Recientes,
                                    self.separador,
                                    self.Anyadir,
                                ],
                            ),
                        ],
                    ),
            width=250,
            height=1000,
            bgcolor='#DCDBFF',
        )

        # Si es admin poner el Panel de administrador
        if self.admin is True:
            primer_container.content.controls[0].controls.insert(3,self.Panel)

        self.visualizar_horarios()

        # Crear un Stack para el GridView y el AlertDialog
        self.stack = ft.Container(
            content= ft.Stack( # Para que se ponga encima configuracion
                controls=[
                    self.ColeccionHorarios  # Añadir primero el GridView
                ],
                expand=True
            ),
            expand=True
        )

        self.SeccionPrincipal = ft.Container(
            content= ft.Column(
                controls=[
                    self.BarraBusqueda,
                    self.stack,
                ],
            ),
            expand=True,
            height=1000,
            bgcolor='#FFFFFF'
        )

        self.CreacionHorario = ft.Container(
            content= ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            self.SeleccionHorario,
                            self.EstadoSistema,
                            self.SeleccionAsignaturas,
                            self.separador,
                            self.Opciones,
                        ],
                    ),  
                ],
            ),
            expand=True,
            height=1000,
            bgcolor='#FFFFFF'
        )

        self.FinHorario = ft.Container(
            content= ft.Stack(
                controls=[
                    ft.Column(
                        controls=[
                            self.paginaHorario.BarraNombre,
                            self.paginaHorario.Horario,
                            self.separador,
                            self.Opciones,
                        ],
                        spacing=20,
                    ),  
                ],
            ),
            padding=20,
            expand=True,
            height=1000,
            bgcolor='#FFFFFF',
        )

        # Pantalla (Container) que incluye ambos Stacks
        pantalla = ft.Container(
            content=ft.Row(
                controls=[
                    primer_container,
                    self.SeccionPrincipal,
                ],
                #vertical_alignment=ft.MainAxisAlignment.START,
            ),
        )
        self.Pantalla = pantalla

        #Poner nombre de usuario correcto
        self.userName(self.usuario)

    def anyadir_horario(self, asig, horaIn, horaFin):
        ids = []
        for x in asig:     # Guardamos los ids de cada asignatura
            ids.append(x['_id'])
        
        # Se crea a la base de datos los datos de misAsignaturas
        newMisAsig = misAsignaturas(misAsignaturas = ids)

        # Se sube misAsignaturas y se obtiene el id de misAsignaturas recién subido
        idAsignaturas = str(baseSesion.add_misAsignaturas(newMisAsig))

        # Se crea a la base de datos los datos de horario
        newHorario = horarioNuevo(nombre = "Horario sin nombre", misAsignaturas = idAsignaturas, horaFin = horaFin, horaIni = horaIn)
        
        # Se sube horario y se obtiene el id de horario recién subido
        idHorario = baseSesion.add_horario_user(newHorario)

        # Se añade a la lista de horarios de usuario
        self.horarios.append(idHorario)

        baseSesion.update_horario(idHorario,self.email)
        
        #self.Pantalla.content.controls[1].content.controls[1].content.controls.append(
            #ft.ElevatedButton(text="123", height=200, width=200, bgcolor=ft.colors.AMBER_400, style=(ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=10)))),
        #)
        

    def visualizar_horarios(self):
        # Recuperar id del user
        # Hacer consulta de su array de horarios
        # Teniendo el id del horario, recoger el array de mis asignaturas
        # en mis asinaturas obtener el array de misAsignaturas obteniendo la
        # lista completa de ids de asignaturas.
        # A partir de ahi generar un array con el objeto a que apunta cada asignatura
        self.ColeccionHorarios.content.controls = []       

        lista=[]
        for i in self.horarios:
            horario = baseSesion.get_mi_horario(i)
            claveMisAsignaturas= horario['misAsignaturas']
            misAsig = baseSesion.get_misAsig(str(claveMisAsignaturas))
            listaAsignaturas = []
            
            for i in misAsig['misAsignaturas']:
                listaAsignaturas.append(baseSesion.get_asig(str(i)))

            def mostrarMiHorario(e):
                self.paginaHorario=Horario.horario(self.page,horario['horaIni'],horario['horaFin'],listaAsignaturas)


            boton=ft.ElevatedButton(on_click=mostrarMiHorario, text=horario['nombre'], height=200, width=200, bgcolor=ft.colors.AMBER_400, style=(ft.ButtonStyle(shape=ft.ContinuousRectangleBorder(radius=10))),)
            self.ColeccionHorarios.content.controls.append(boton)
        
            

    def userName(self,usuario):
        if usuario is not None:
            self.Pantalla.content.controls[0].content.controls[0].controls[0].controls[0].content.controls[1].value=self.usuario
            self.Pantalla.content.controls[0].content.controls[0].controls[0].controls[0].items[0].content.controls[1].value=self.usuario

    def open_config_dialog(self, e):
        # Llamar a esta función para mostrar el diálogo
        if self.dialog not in self.stack.content.controls:
            self.stack.content.controls.append(self.dialog)
            self.page.update()

        if self.CreacionHorario in self.Pantalla.content.controls:
            if self.dialog not in self.CreacionHorario.content.controls:
                self.CreacionHorario.content.controls.append(self.dialog)
                self.page.update()

        if self.FinHorario in self.Pantalla.content.controls:
            if self.dialog not in self.FinHorario.content.controls:
                self.FinHorario.content.controls.append(self.dialog)
                self.page.update()

    def close_dialog(self, e):
            # Llamar a esta función para cerrar el diálogo
            if self.dialog in self.stack.content.controls:
                self.stack.content.controls.remove(self.dialog)
                self.page.update()

            if self.dialog in self.CreacionHorario.content.controls:
                self.CreacionHorario.content.controls.remove(self.dialog)
                self.page.update()

            if self.dialog in self.FinHorario.content.controls:
                self.FinHorario.content.controls.remove(self.dialog)
                self.page.update()

    def on_create_click(self, e):
        
        self.Pantalla.content.controls.remove(self.SeccionPrincipal)

        self.Pantalla.content.controls.append(self.CreacionHorario)

        self.page.update()

    def on_clear_click(self, e):
        print("Hola")
        dlg=ft.Container(
            content= ft.AlertDialog(
                title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
            ),
            height=200,
            width=200,
            bgcolor='#DCDBFF'
        ),
        self.Pantalla.content.controls[1].content.controls.append(dlg)
        pass

    def on_logOut_click(self, e):
        # Limpiar la página actual
        self.page.controls.clear()

        # Cargar la página de inicio de sesión
        # Asegúrate de que 'inicioSesion' esté importado correctamente y se pueda instanciar aquí
        self.page.add(iniSes.inicioSesion(self.page).Pantalla)
        #self.page.remove()

        
        # Actualizar la página
        self.page.update()

    def on_next_click(self, e):
        # Cambiar manejador de evento en el boton de siguiente
        self.Opciones.content.controls[1].content.on_click=self.on_next_click2

        # Vaciar lista de controles
        self.Pantalla.content.controls[1].content.controls[0].controls.remove(self.SeleccionAsignaturas)

        self.SeleccionAsignaturas.content.controls = []
        
        # Meter el container con grupos en vez de asignaturas
        self.Pantalla.content.controls[1].content.controls[0].controls.insert(2,self.SeleccionAsignaturas)

        planEstudio = self.Pantalla.content.controls[1].content.controls[0].controls[0].content.controls[1].controls[0].controls[1].value
        aux = baseSesion.get_numCursos(planEstudio)
        for i in range(1,aux['numCursos']+1):
                # Consulta para saber las asignaturas por el plan de estudio, año y semestre seleccionado
                aux2 = baseSesion.get_grupo_carrera_curso(planEstudio, i)
                # Lista vacia donde se meteran los botones de cada asignatura de cada año
                mondongo = []
                for a in aux2:
                    # Creacion de boton por asignatura en el año
                    mondongo.append(plantillas.obtenerGrupoCarrera(str(a['codigo']),str(a['horaInicio']),str(a['horaFin']),self.listaInicio,self.listaFin))
                # Creacion del container con el año de la carrera y sus asignaturas
                containerAnyoCarrera = self.Pantalla.content.controls[1].content.controls[0].controls[2].content.controls

                Anyo = plantillas.obtenerAnyoCarrera(self.page,i, mondongo,containerAnyoCarrera)
                
                containerAnyoCarrera.append(Anyo)

        # Actualizar estado sistema
        self.Pantalla.content.controls[1].content.controls[0].controls[1].content.controls[1].bgcolor="#D3DCE3"
        self.Pantalla.content.controls[1].content.controls[0].controls[1].content.controls[2].bgcolor="#D3DCE3"

        self.page.update()

    def on_next_click2(self, e):
        # Actualizar estado sistema
        self.Pantalla.content.controls[1].content.controls[0].controls[1].content.controls[1].bgcolor=None
        self.Pantalla.content.controls[1].content.controls[0].controls[1].content.controls[2].bgcolor=None
        # Eliminar la creacion de Horario de los controles
        self.SeleccionAsignaturas.content.controls = []
        
        self.Pantalla.content.controls.remove(self.CreacionHorario)

        self.Opciones.content.controls[1].content.on_click=self.on_finish_click
        self.Opciones.content.controls[1].content.text="     Crear Horario     "
        self.Opciones.content.controls[0].content.visible=False

        if self.listaInicio == [] or self.listaFin == []:
            self.paginaHorario = Horario.horario(self.page,14,20,self.listaAsignaturas)
        else:
            self.paginaHorario = Horario.horario(self.page,int(min(self.listaInicio)),int(max(self.listaFin)),self.listaAsignaturas)
        

        self.Pantalla.content.controls.append(self.FinHorario)

        self.page.update()

    def on_finish_click(self,e):    
        self.Pantalla.content.controls.remove(self.FinHorario)

        # Reasignacion de las acciones normales del boton
        self.Opciones.content.controls[1].content.on_click=self.on_next_click
        self.Opciones.content.controls[1].content.text="     Siguiente     "
        self.Opciones.content.controls[0].content.visible=True

        self.Pantalla.content.controls.append(self.SeccionPrincipal)
        listaAsig = self.listaAsignaturas
        horaIn = int(min(self.listaInicio))
        horaFi = int(max(self.listaFin))
        self.listaAsignaturas = []
        self.listaFin = []
        self.listaInicio = []

        self.anyadir_horario(listaAsig, horaIn ,horaFi)

        self.page.update()

    def dropdown_changed(self, e):
        planEstudio = self.Pantalla.content.controls[1].content.controls[0].controls[0].content.controls[1].controls[0].controls[1].value
        periodoAcademico = self.Pantalla.content.controls[1].content.controls[0].controls[0].content.controls[1].controls[1].controls[1].value

        aux = {}
        if planEstudio and periodoAcademico:
            # Numero de años de la carrera
            aux = baseSesion.get_numCursos(planEstudio)

            # Creacion del container con el año de la carrera y sus asignaturas
            containerAnyoCarrera = self.Pantalla.content.controls[1].content.controls[0].controls[2].content.controls= []

            for i in range(1,aux['numCursos']+1):
                # Consulta para saber las asignaturas por el plan de estudio, año y semestre seleccionado
                aux2 = baseSesion.get_asignatura_carrera_curso_semestre(planEstudio, i, periodoAcademico)
                # Lista vacia donde se meteran los botones de cada asignatura de cada año
                mondongo = []
                for a in aux2:
                    # Creacion de boton por asignatura en el año
                    mondongo.append(plantillas.obtenerAsignaturaCarrera(str(a['nombre']),str(a['codigo']),self.listaAsignaturas))

                Anyo = plantillas.obtenerAnyoCarrera(self.page,i, mondongo,containerAnyoCarrera)
                
                containerAnyoCarrera.append(Anyo)

        self.page.update()

    searchbar = ft.TextField(hint_text="Buscar Horarios ...", autofocus=False,
                            width=200, height=40, text_size=12,),
    
    Search_icon = '../assets/icons/search_icon.png'
    Filter_icon = '../assets/icons/filter_icon.png'

    ColeccionHorarios = ft.Container(
        content=ft.GridView(
            expand=True,
            max_extent=150,
            child_aspect_ratio=1
        ),
        expand=True,
    )

    BarraBusqueda = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(width=10),
                #ft.Image(src=Search_icon, width=30, height=30,),
                ft.ElevatedButton(

                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(src=Search_icon, width=40, height=40),
                        ],
                    ),
                ),
                ft.Container(width=10),
                ft.TextField(hint_text="Buscar Horarios ...", autofocus=False,
                    expand=True, height=50, text_size=12),
                ft.Container(width=10),
                ft.IconButton(
                    width=60,
                    height=60,
                    style=ft.ButtonStyle(
                        shape=ft.BeveledRectangleBorder(),
                    ),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Image(src=Filter_icon, width=60, height=60),
                        ],
                    ),
                ),
                ft.Container(width=10),
            ],
        ),
        bgcolor='#8986FF',
        border_radius=15,
        height=70,
    )

    User_icon = '../assets/icons/icon.png'

    Usuario = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        width=250,
        height=90,
        controls=[
            ft.PopupMenuButton(
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=User_icon, width=70, height=70,
                        ),
                        ft.Text(value="Username", size=25,color=ft.colors.BLACK,),
                    ]
                ),
                expand=True,
                items=[
                    ft.PopupMenuItem(
                        content=ft.Row(
                            controls=[
                                ft.Image(src=User_icon, width=70, height=70),
                                ft.Text("Username", size=25, color=ft.colors.BLACK),
                            ],
                        ),
                    ),
                    ft.PopupMenuItem(
                        content=ft.TextButton(
                            content=ft.Row(
                                controls=[
                                    ft.Text(value="Configuración", style="labelMedium",
                                    text_align="center",size=20,color=ft.colors.BLACK, width=230),                                    
                                ],
                            ),
                        ),
                    ),
                    ft.PopupMenuItem(
                        content=ft.TextButton(
                            content=ft.Row(
                                controls=[
                                    ft.Text(value="Cerrar sesión", style="labelMedium",
                                    text_align="center",size=20,color=ft.colors.BLACK, width=230),
                                ],
                            ),
                        ),
                    ),
                ]
            ),
        ]   
    )

    Recent_icon = '../assets/icons/home_icon.png'
    
    Recientes = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.IconButton(
                width=250,
                height=80,
                style=ft.ButtonStyle(
                    shape=ft.BeveledRectangleBorder(),
                ),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=Recent_icon, width=40, height=40),
                        ft.Text("Home", size=25, color=ft.colors.BLACK,),
                    ],
                ),
            ),
        ],
    )

    Panel_icon = '../assets/icons/admin_icon.png'

    Panel = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.IconButton(
                width=250,
                height=80,
                style=ft.ButtonStyle(
                    shape=ft.BeveledRectangleBorder(),
                ),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=Panel_icon, width=40, height=40),
                        ft.Text("Panel de admin", size=25, color=ft.colors.BLACK,),
                    ],
                ),
            ),
        ],
    )

    Ayadir_icon = '../assets/icons/add_icon.png'
    
    Anyadir = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                width=250,
                height=80,
                style=ft.ButtonStyle(
                    shape=ft.CircleBorder(), 
                ),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=Ayadir_icon, width=80, height=80),
                    ],
                ),
                
            ),
        ],
    )
    
    # Definición del separador (línea azul)
    separador = ft.Container(
        height=2,  # Ajusta el alto para el grosor de la línea
        bgcolor="#0041E9",  # Color de fondo azul
    )

    
    SeleccionHorario = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Horarios: 2023/2024",size=40,color=ft.colors.BLACK,text_align=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    controls=[
                         ft.Column(
                            controls=[
                                ft.Text("Plan de estudio",size=30,color=ft.colors.BLACK,text_align=ft.MainAxisAlignment.CENTER),
                                #ft.TextField(hint_text="Plan de estudio...", autofocus=False,
                                #    width=500, height=40, text_size=20,on_change=),
                                ft.Dropdown(
                                    hint_text="Plan de estudio",
                                    options=[
                                        ft.dropdown.Option("Ingeniería Informática"),
                                        ft.dropdown.Option("Ingeniería Electronica"),
                                        ft.dropdown.Option("Ingeniería Espacial"),
                                    ],
                                    autofocus=True,
                                ),
                            ],
                         ),
                         ft.Column(
                            controls=[
                                ft.Text("Periodo académico",size=30,color=ft.colors.BLACK,text_align=ft.MainAxisAlignment.CENTER),
                                #ft.TextField(hint_text="Periodo académico...", autofocus=False,
                                #    width=500, height=40, text_size=20,on_change= ),
                                ft.Dropdown(
                                    hint_text="Numero de cuatrimestre",
                                    options=[
                                        ft.dropdown.Option("1"),
                                        ft.dropdown.Option("2"),
                                    ],
                                    autofocus=True,
                                ),
                            ],
                         ),
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor='#8986FF',
        border_radius=15,
        padding=20,
    )


    EstadoSistema = ft.Container(
        padding=10,
        content= ft.Row(
             controls=[
                ft.Text(
                    "Selección de asignaturas",
                    size=20,
                    color=ft.colors.BLACK,
                    bgcolor="#D3DCE3"
                ),

                ft.Icon(
                    name=ft.icons.ARROW_FORWARD_IOS,
                    color="black",
                    size=20,
                ),
                
                ft.Text(
                    "Selección de grupos",
                    size=20,
                    color=ft.colors.BLACK
                ),
            ],
        ),
    )

    AsignaturaCarrera=ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                "Programacion 1",
                width=150,
                height=50,
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                    bgcolor={ft.MaterialState.DEFAULT: '#1B7746'},
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
                    },
                ),
            ),
        ],
    )

    SeleccionAsignaturas=ft.Container(
        padding=10,
        height=600,
        content=ft.Column(
                spacing=20,
                controls=[
                       
                ],
                scroll=ft.ScrollMode.AUTO,
            )
    )

    Opciones=ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.ElevatedButton(
                        text="     Limpiar     ",
                        height=60,
                        style=ft.ButtonStyle(
                            color=ft.colors.BLACK,
                            bgcolor={ft.MaterialState.DEFAULT: '#F24822'},
                            side={ft.MaterialState.DEFAULT:
                                    ft.BorderSide(3, '#C13A1B')},
                            shape={
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
                            },          
                        ),
                        visible=False
                    ),
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="     Siguiente     ",
                        height=60,
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
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
    )

    
