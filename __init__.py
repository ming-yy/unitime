import flet as ft
import pages.inicioSesion as iniSes
#import pages.baseHorarios as basHor
#import pages.cambiarContrasenya as camCon
#import pages.pantallaCarga as loadPage
#import pages.nuevaContrasenya as newCon
#import pages.registrarse as regis

class App():
    def __init__(self, pg: ft.Page):
        paginaInicioSesion = iniSes.inicioSesion(pg)
        #paginaBaseHorarios = basHor.baseHorarios(pg)
        #paginaCambiarCon = camCon.cambiarContrasenya(pg)
        #paginaCarga = loadPage.pantallaCarga(pg)
        #paginaNewCon = newCon.nuevaContrasenya(pg)
        #paginaRegis = regis.registrar(pg)

        pg.add(paginaInicioSesion.Pantalla)
        #pg.add(paginaBaseHorarios.Pantalla)
        #paginaBaseHorarios.anyadir_horarios()
        #pg.add(paginaCambiarCon.Pantalla)
        #pg.add(paginaCarga.Pantalla)
        #pg.add(paginaNewCon.Pantalla)
        #pg.add(paginaRegis.Pantalla)
        pg.update()
        


ft.app(target=App)