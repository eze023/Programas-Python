from wx import *
from wx.dataview import *
from datetime import *
from wx.adv import *
import sqlite3


class MyApp(App):
    def OnInit(self):
        self.lista = lista = ["Clientes", "Articulos/Stock", "Ventas"]
        self.f = f = MyFrame("Punto de Venta", (50, 60), (1366, 750))
        gbs = GridBagSizer(0, 0)
        for i in range(len(lista)):
            b = Button(f, label=lista[i])
            gbs.Add(b, pos=(0, i))
            if lista[i] == "Clientes":
                b.Bind(EVT_BUTTON, self.clientes)
            elif lista[i] == "Articulos/Stock":
                b.Bind(EVT_BUTTON, self.stock)
            elif lista[i] == "Ventas":
                b.Bind(EVT_BUTTON, self.ventas)
        f.SetSizer(gbs)
        f.Show()
        self.SetTopWindow(f)
        return True

#------------------------------Clientes------------------------------ f1, p1, dvlc1, f2, p2, gbs2
    def clientes(self, event):
        self.f1 = f1 = Frame(None, -1, "Agregar clientes", size=(800, 600))
        self.p1 = p1 = Panel(f1, -1)
        self.dvlc1 = dvlc1 = DataViewListCtrl(p1)
        encabezado1 = [('ID Cliente', 100), ('Apellido', 150), ('Nombre', 150), ('DNI', 100), ('Cuit/Cuil', 100), ('Categoria', 150), ('Codigo Postal', 100), ('Domicilio', 100), ('Localidad', 100), ('Telefono', 100), ('Correo Electronico', 150)]
        for i in encabezado1:
            dvlc1.AppendTextColumn(i[0], width=i[1])
        sizerV1 = BoxSizer(VERTICAL)
        sizerV1.Add(dvlc1, 1, EXPAND)
        sizerH1 = BoxSizer(HORIZONTAL)
        bAgrC = Button(p1, -1, "Agregar Cliente")
        sizerH1.Add(bAgrC)
        blisC = Button(p1, -1, "Listar Clientes")
        sizerH1.Add(blisC)
        bBus = Button(p1, -1, "Buscar Cliente")
        sizerH1.Add(bBus)
        bCeC = Button(p1, -1, "Cerrar")
        sizerH1.Add(bCeC)
        sizerV1.Add(sizerH1)
        bAgrC.Bind(EVT_BUTTON, self.agregarCliente)
        blisC.Bind(EVT_BUTTON, self.mostrarClientes)
        bBus.Bind(EVT_BUTTON, self.buscarCliente)
        bCeC.Bind(EVT_BUTTON, self.cerrarCliente)
        p1.SetSizer(sizerV1)
        f1.Show()

    def agregarCliente(self, event):
        self.f2 = f2 = Frame(None, -1, "Agregar Cliente", size=(500, 425))
        self.p2 = p2 = Panel(f2, -1, style=TAB_TRAVERSAL)
        gbs2 = GridBagSizer(5, 20)
#Tipo de IVA
        tpC = StaticText(p2, -1, "Tipo de IVA")
        gbs2.Add(tpC, pos=(1, 1))
        tipoC = ["Consumidor Final", "Responsable Inscripto", "Resp. Monotributista", "Excento", "Exportador", "Hoteleria o Servicios"]
        self.tipoC = combo1 = ComboBox(p2, -1, "Emisor", (0, 0), (190, 25), tipoC, CB_DROPDOWN | TE_PROCESS_ENTER)
        combo1.Bind(EVT_KILL_FOCUS, self.killFocus)
        gbs2.Add(self.tipoC, pos=(1, 2))
#Apellido
        aPe = StaticText(p2, -1, "Apellido")
        gbs2.Add(aPe, pos=(2, 1))
        ape = self.ape = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(ape, pos=(2, 2))
        ape.Disable()
#Nombre
        nOm = StaticText(p2, -1, "Nombre")
        gbs2.Add(nOm, pos=(3, 1))
        nom = self.nom = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(nom, pos=(3, 2))
        nom.Disable()
#DNI
        dNi = StaticText(p2, -1, "DNI")
        gbs2.Add(dNi, pos=(4, 1))
        dni = self.dni = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(dni, pos=(4, 2))
        dni.Disable()
#Cuil/Cuit
        cuil = StaticText(p2, -1, "Cuil/Cuit")
        gbs2.Add(cuil, pos=(5, 1))
        cuit = self.cuit = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(cuit, pos=(5, 2))
        cuit.Disable()
#Codigo Postal
        cP = StaticText(p2, -1, "Código Postal")
        gbs2.Add(cP, pos=(6, 1))
        cp = self.cp = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(cp, pos=(6, 2))
        cp.Disable()
#Direccion
        dire = StaticText(p2, -1, "Domicilio")
        gbs2.Add(dire, pos=(7, 1))
        dire2 = self.dire2 = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(dire2, pos=(7, 2))
        dire2.Disable()
#Localidad
        local = StaticText(p2, -1, "Localidad")
        gbs2.Add(local, pos=(8, 1))
        local2 = self.local2 = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(local2, pos=(8, 2))
        local2.Disable()
#Telefono
        tel = StaticText(p2, -1, "Numero de Teléfono")
        gbs2.Add(tel, pos=(9, 1))
        tel2 = self.tel2 = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(tel2, pos=(9, 2))
        tel2.Disable()
#Correo Electronico
        corre = StaticText(p2, -1, "Correo Electronico")
        gbs2.Add(corre, pos=(10, 1))
        corre2 = self.corre2 = TextCtrl(p2, -1, size=(190, 25))
        gbs2.Add(corre2, pos=(10, 2))
        corre2.Disable()
#Agregar boton Guardar
        guar = Button(p2, -1, "&Guardar")
        gbs2.Add(guar, pos=(11, 3))
        guar.Bind(EVT_BUTTON, self.guardarCliente)
        cance = Button(p2, -1, "&Cancelar")
        gbs2.Add(cance, pos=(11, 1))
        cance.Bind(EVT_BUTTON, self.cerrarAgregaCliente)
        p2.SetSizer(gbs2)
        f2.Show()

    def guardarCliente(self, event):
        lista = []
        listasql = []
        ide = ""
        self.tC = tC = self.tipoC.GetValue()
        lista.append((ide, self.ape.GetValue(), self.nom.GetValue(), self.dni.GetValue(), self.cuit.GetValue(), self.tC, self.cp.GetValue(), self.dire2.GetValue(), self.local2.GetValue(), self.tel2.GetValue(), self.corre2.GetValue()))
        listasql.append((self.ape.GetValue(), self.nom.GetValue(), self.dni.GetValue(), self.cuit.GetValue(), self.tC, self.cp.GetValue(), self.dire2.GetValue(), self.local2.GetValue(), self.tel2.GetValue(), self.corre2.GetValue()))
        for i in lista:
            self.dvlc1.AppendItem(i)
        self.cargarClienteSql(listasql)
        self.mostrarClientes(EVT_BUTTON)            #Ejecuta la funcion para mostrar todos los clientes inlcuyendo el ultimo agregado
        self.f2.Close()

    def cerrarCliente(self, event):
        self.f1.Close()

    def cerrarAgregaCliente(self, event):
        self.f2.Close()

    def killFocus(self, event):
        self.tC = self.tipoC.GetValue()
        self.ape.Enable()
        self.nom.Enable()
        self.dni.Enable()
        self.cuit.Enable()
        self.cp.Enable()
        self.dire2.Enable()
        self.local2.Enable()
        self.tel2.Enable()
        self.corre2.Enable()
        event.Skip()

    def cargarClienteSql(self, lista):
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            Apellido NVARCHAR NOT NULL,
            Nombre NVARCHAR NOT NULL,
            Dni NVARCHAR UNIQUE NOT NULL,
            Cuit NVARCHAR UNIQUE NOT NULL,
            Iva NVARCHAR NOT NULL,
            Cp NVARCHAR NOT NULL,
            Domicilio NVARCHAR NOT NULL,
            Localidad NVARCHAR NOT NULL,
            Telefono NVARCHAR NOT NULL,
            Correo NVARCHAR NOT NULL)''')
        except:
            pass
        try:
            cur.executemany("INSERT INTO clientes VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", lista,)
        except:
            self.dialogo(EVT_BUTTON)
        con.commit()
        con.close()

    def mostrarClientes(self, event):
        self.dvlc1.DeleteAllItems()
        lista = self.recuperoDBclientes()
        for i in lista:
            self.dvlc1.AppendItem(i)

    def recuperoDBclientes(self):
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM clientes ORDER BY id")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            e[0] = str(e[0])
        con.close()
        return listaA

    def dialogo(self, event):
        self.dialogo = dialogo = Dialog(None, -1, "ERROR", size=(600, 150))
        box = BoxSizer(VERTICAL)
        ate = StaticText(dialogo, -1, label="Error el DNI o CUIT de la persona ingresada ya se encuentra en el sistema")
        box.Add(ate, 0, ALIGN_CENTER | ALL, 10)
        bCancel = Button(dialogo, -1, label="Cerrar")
        box.Add(bCancel, 0, ALIGN_CENTER | ALL, 10)
        bCancel.Bind(EVT_BUTTON, self.cerrarDialogo)
        dialogo.SetSizer(box)
        dialogo.Show()

    def cerrarDialogo(self, event):
        self.dialogo.Close()

#------------------------------Buscador de Clientes------------------------------

    def buscarCliente(self, event):
        self.buscar = buscar = Frame(None, -1, "Buscar Cliente", size=(800, 600))
        self.pa1 = pa1 = Panel(buscar, -1, style=TAB_TRAVERSAL)
        self.dvelc = dvelc = DataViewListCtrl(pa1)
        grbs = GridBagSizer(5, 5)
        bx = BoxSizer(VERTICAL)
        bx.Add(grbs)
        bx.Add(dvelc, 1, EXPAND)
        encabezado = [('ID Cliente', 100), ('Apellido', 150), ('Nombre', 150), ('DNI', 100), ('Cuit/Cuil', 100), ('IVA', 150), ('Codigo Postal', 100), ('Domicilio', 100), ('Localidad', 100), ('Telefono', 100), ('Correo Electronico', 150)]
        for i in encabezado:
            dvelc.AppendTextColumn(i[0], width=i[1])
        bsca = StaticText(pa1, -1, "Llene uno de los campos para buscar")
        grbs.Add(bsca, pos=(1, 3))
#Buscamos por Id
        ide = StaticText(pa1, -1, "Id")
        grbs.Add(ide, pos=(2, 2))
        self. ideb = ideb = TextCtrl(pa1, -1, size=(190, 25))
        grbs.Add(ideb, pos=(2, 3))
#Buscamos por DNI
        dni = StaticText(pa1, -1, "Dni")
        grbs.Add(dni, pos=(3, 2))
        self.dni2 = dni2 = TextCtrl(pa1, -1, size=(190, 25))
        grbs.Add(dni2, pos=(3, 3))
#Buscamos por CUIT
        cuit = StaticText(pa1, -1, "Cuit")
        grbs.Add(cuit, pos=(4, 2))
        self.cuit2 = cuit2 = TextCtrl(pa1, -1, size=(190, 25))
        grbs.Add(cuit2, pos=(4, 3))
#Buscamos por Nombre
        nom = StaticText(pa1, -1, "Nombre")
        grbs.Add(nom, pos=(5, 2))
        self.nom2 = nom2 = TextCtrl(pa1, -1, size=(190, 25))
        grbs.Add(nom2, pos=(5, 3))
#Buscamos por Apellido
        ape = StaticText(pa1, -1, "Apellido")
        grbs.Add(ape, pos=(6, 2))
        self.ape2 = ape2 = TextCtrl(pa1, -1, size=(190, 25))
        grbs.Add(ape2, pos=(6, 3))
#Agregamos Boton Buscar y Cancelar
        bs = Button(pa1, -1, "Buscar")
        grbs.Add(bs, pos=(8, 2))
        bs.Bind(EVT_BUTTON, self.buscarSql)
        bCan = Button(pa1, -1, "Cancelar")
        grbs.Add(bCan, pos=(8, 4))
        bCan.Bind(EVT_BUTTON, self.canBusqueda)
        sep = StaticText(pa1, -1, "")
        grbs.Add(sep, pos=(9, 1))
        pa1.SetSizer(bx)
        buscar.Show()
        dvelc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.editoCliente)

    def canBusqueda(self, event):
        self.buscar.Close()

    def buscarSql(self, event):
        self.dvelc.DeleteAllItems()
        lista = self.buscarClienteSql()
        for i in lista:
            self.dvelc.AppendItem(i)

    def buscarClienteSql(self):
        Id = self.ideb.GetValue()
        dni = self.dni2.GetValue()
        cuit = self.cuit2.GetValue()
        nom = self.nom2.GetValue()
        ape = self.ape2.GetValue()
        lista = []
        if len(Id) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = Id
            sentencia = "SELECT * FROM Clientes WHERE id LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        if len(dni) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = dni
            sentencia = "SELECT * FROM Clientes WHERE Dni LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        if len(cuit) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = cuit
            sentencia = "SELECT * FROM Clientes WHERE Cuit LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        if len(nom) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = nom
            sentencia = "SELECT * FROM Clientes WHERE Nombre LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        if len(ape) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = ape
            sentencia = "SELECT * FROM Clientes WHERE Apellido LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        return lista

#------------------------------Editor de Clientes------------------------------

    def editoCliente(self, event):
        ide, ap, no, dn, cu, tip, cop, di, lo, te, cor = self.buscoeditoCliente()
        self.frame = frame = Frame(None, -1, "Editor de clientes", size=(450, 500))
        panel = Panel(frame, -1, style=TAB_TRAVERSAL)
        gridbag = GridBagSizer(5, 5)
#Boton Editar
        bEditC = Button(panel, -1, "Editar")
        gridbag.Add(bEditC, pos=(1, 1))
        bEditC.Bind(EVT_BUTTON, self.habilitoEdicion)
#Boton Guardar Edicion
        bGuE = Button(panel, -1, "Guardar")
        gridbag.Add(bGuE, pos=(1, 3))
        bGuE.Bind(EVT_BUTTON, self.guardoEdicion)
#Mostramos ID
        idee = StaticText(panel, -1, "ID")
        gridbag.Add(idee, pos=(3, 1))
        idee2 = self.idee2 = TextCtrl(panel, -1, value=ide, size=(190, 25))
        gridbag.Add(idee2, pos=(3, 2))
        idee2.Disable()
#Mostramos Apellido
        ape = StaticText(panel, -1, "Apellido")
        gridbag.Add(ape, pos=(4, 1))
        apee2 = self.apee2 = TextCtrl(panel, -1, value=ap, size=(190, 25))
        gridbag.Add(apee2, pos=(4, 2))
        apee2.Disable()
#Mostramos Nombre
        nom = StaticText(panel, -1, "Nombre")
        gridbag.Add(nom, pos=(5, 1))
        nome2 = self.nome2 = TextCtrl(panel, -1, value=no, size=(190, 25))
        gridbag.Add(nome2, pos=(5, 2))
        nome2.Disable()
#DNI
        dNi = StaticText(panel, -1, "DNI")
        gridbag.Add(dNi, pos=(6, 1))
        dnie = self.dnie = TextCtrl(panel, -1, value=dn, size=(190, 25))
        gridbag.Add(dnie, pos=(6, 2))
        dnie.Disable()
#Cuil/Cuit
        cuil = StaticText(panel, -1, "Cuil/Cuit")
        gridbag.Add(cuil, pos=(7, 1))
        cuite = self.cuite = TextCtrl(panel, -1, value=cu, size=(190, 25))
        gridbag.Add(cuite, pos=(7, 2))
        cuite.Disable()
#Codigo Postal
        cP = StaticText(panel, -1, "Código Postal")
        gridbag.Add(cP, pos=(8, 1))
        cpe = self.cpe = TextCtrl(panel, -1, value=cop, size=(190, 25))
        gridbag.Add(cpe, pos=(8, 2))
        cpe.Disable()
#Direccion
        dire = StaticText(panel, -1, "Domicilio")
        gridbag.Add(dire, pos=(9, 1))
        diree2 = self.diree2 = TextCtrl(panel, -1, value=di, size=(190, 25))
        gridbag.Add(diree2, pos=(9, 2))
        diree2.Disable()
#Localidad
        local = StaticText(panel, -1, "Localidad")
        gridbag.Add(local, pos=(10, 1))
        locale2 = self.locale2 = TextCtrl(panel, -1, value=lo, size=(190, 25))
        gridbag.Add(locale2, pos=(10, 2))
        locale2.Disable()
#Telefono
        tel = StaticText(panel, -1, "Numero de Teléfono")
        gridbag.Add(tel, pos=(11, 1))
        tele2 = self.tele2 = TextCtrl(panel, -1, value=te, size=(190, 25))
        gridbag.Add(tele2, pos=(11, 2))
        tele2.Disable()
#Correo Electronico
        corre = StaticText(panel, -1, "Correo Electronico")
        gridbag.Add(corre, pos=(12, 1))
        corree2 = self.corree2 = TextCtrl(panel, -1, value=cor, size=(190, 25))
        gridbag.Add(corree2, pos=(12, 2))
        corree2.Disable()
#Tipo de IVA
        tpC = StaticText(panel, -1, "Tipo de IVA")
        gridbag.Add(tpC, pos=(13, 1))
        tipoCe = self.tipoCe = TextCtrl(panel, -1, value=tip, size=(190, 25))
        gridbag.Add(self.tipoCe, pos=(13, 2))
        tipoCe.Disable()
#Boton Eliminar
        bEli = Button(panel, -1, "Eliminar")
        gridbag.Add(bEli, pos=(14, 1))
        bEli.Bind(EVT_BUTTON, self.eliminaCliente)
        panel.SetSizer(gridbag)
        frame.Show()

    def buscoeditoCliente(self):
        lista = []
        listaE = []
        fila = self.dvelc.GetSelectedRow()
        ide = self.dvelc.GetTextValue(fila, 0)
        if len(ide) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = ide
            sentencia = "SELECT * FROM Clientes WHERE id LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        for i in lista:
            listaE+=i
        ides, ap, no, dn, cu, tip, cop, di, lo, te, cor = listaE
        return ides, ap, no, dn, cu, tip, cop, di, lo, te, cor

    def habilitoEdicion(self, event):
        self.apee2.Enable()
        self.nome2.Enable()
        self.dnie.Enable()
        self.cuite.Enable()
        self.cpe.Enable()
        self.diree2.Enable()
        self.locale2.Enable()
        self.tele2.Enable()
        self.corree2.Enable()
        self.tipoCe.Enable()

    def guardoEdicion(self, event):
        id = self.idee2.GetValue()
        ape = self.apee2.GetValue()
        nom = self.nome2.GetValue()
        dni = self.dnie.GetValue()
        cuit = self.cuite.GetValue()
        cp = self.cpe.GetValue()
        dire = self.diree2.GetValue()
        local = self.locale2.GetValue()
        tel = self.tele2.GetValue()
        corre = self.corree2.GetValue()
        iva = self.tipoCe.GetValue()
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute("UPDATE clientes SET Apellido = ?, Nombre = ?, Dni = ?, Cuit = ?, Iva = ?, Cp = ?, Domicilio = ?, Localidad = ?, Telefono = ?, Correo = ? WHERE id= ?",(ape, nom, dni, cuit, iva, cp, dire, local, tel, corre, id))
        except:
            self.dialogo(EVT_BUTTON)
        con.commit()
        con.close()
        self.edf.Close()
        self.frame.Close()

    def eliminaCliente(self, event):
        self.dialo = dialo = Dialog(None, -1, "Eliminar Cliente", size=(475,125))
        pan = Panel(dialo)
        gbrs2 = GridBagSizer(5, 5)
        alerta = StaticText(pan, -1, "¿Esta seguro que quiere elminar este cliente?")
        gbrs2.Add(alerta, pos=(1,2))
        bSi = Button(pan, -1, "Si")
        gbrs2.Add(bSi, pos=(2,1))
        bSi.Bind(EVT_BUTTON, self.eliminaSql)
        bNo = Button(pan, -1, "No")
        gbrs2.Add(bNo, pos=(2,3))
        bNo.Bind(EVT_BUTTON, self.noElimina)
        pan.SetSizer(gbrs2)
        dialo.Show()

    def eliminaSql(self, event):
        id = self.idee2.GetValue()
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM clientes WHERE id = ?",(id))
        except:
            pass
        con.commit()
        con.close()
        self.dialo.Destroy()
        self.frame.Close()

    def noElimina(self, event):
        self.dialo.Destroy()
        self.frame.Close()

#------------------------------Cierra Clientes------------------------------

#------------------------------Articulos/Stock------------------------------ f3, p2, dvlc2, f4, p3, gbs3
    def stock(self, event):
        self.f3 = f3 = Frame(None, -1, "Articulos/Stock", size=(800, 600))
        p2 = self.p2 = Panel(f3, -1)
        dvlc2 = self.dvlc2 = DataViewListCtrl(p2)
        encabezado = [('Id', 100), ('Codigo', 150), ('Tipo', 150), ('Descripción', 150), ('Cantidad', 150), ('Precio Neto Unitario', 150), ('Precio Publico', 150)]
        for i in encabezado:
            dvlc2.AppendTextColumn(i[0], width=i[1])
        sizerV2 = BoxSizer(VERTICAL)
        sizerV2.Add(dvlc2, 1, EXPAND)
        sizerH2 = BoxSizer(HORIZONTAL)
        bAgrA = Button(p2, -1, "Agregar Articulos")
        sizerH2.Add(bAgrA)
        bEdiA = Button(p2, -1, "Editar Articulos/Agregar Stock")
        sizerH2.Add(bEdiA)
        bMart = Button(p2, -1, "Mostrar Articulos")
        sizerH2.Add(bMart)
        bCerr = Button(p2, -1, "Cerrar")
        sizerH2.Add(bCerr)
        bAgrA.Bind(EVT_BUTTON, self.agregaArticulo)
        bEdiA.Bind(EVT_BUTTON, self.buscaArticulo)
        bMart.Bind(EVT_BUTTON, self.mostrarArticulos)
        bCerr.Bind(EVT_BUTTON, self.cerrarStock)
        sizerV2.Add(sizerH2)
        p2.SetSizer(sizerV2)
        f3.Show()

    def agregaArticulo(self, event):
        self.f4 = f4 = Frame(None, -1, "Agregar Articulos", size=(490, 325))
        self.p3 = p3 = Panel(f4, -1, style=TAB_TRAVERSAL)
        gbs3 = GridBagSizer(5, 20)
#Agregamos Codigo del Articulos/stock
        cOd = StaticText(p3, -1, "Codigo")
        gbs3.Add(cOd, pos=(1, 1))
        cod = self.cod = TextCtrl(p3, -1, size=(190, 25))
        gbs3.Add(cod, pos=(1, 2))
#Agregamos tipo
        tiP = StaticText(p3, -1, "Tipo")
        gbs3.Add(tiP, pos=(2, 1))
        tip = self.tip = TextCtrl(p3, -1, size=(190, 25))
        gbs3.Add(tip, pos=(2, 2))
#Agregamos Descripción
        desC = StaticText(p3, -1, "Marca")
        gbs3.Add(desC, pos=(3, 1))
        des = self.des = TextCtrl(p3, -1, size=(190, 25))
        gbs3.Add(des, pos=(3, 2))
#Agregamos cantidad
        can = StaticText(p3, -1, "Cantidad")
        gbs3.Add(can, pos=(4, 1))
        cant = self.cant = TextCtrl(p3, -1, size=(190, 25))
        gbs3.Add(cant, pos=(4, 2))
#Agregamos Precio Neto
        pNet = StaticText(p3, -1, "Precio Neto Unidad")
        gbs3.Add(pNet, pos=(5, 1))
        pnet = self.pnet = TextCtrl(p3, -1, size=(190, 25))
        gbs3.Add(pnet, pos=(5, 2))
#Agregamos % de ganancia al producto
        pgan = StaticText(p3, -1, "% Ganancia")
        gbs3.Add(pgan, pos=(6, 1))
        pgana = self.pgana = TextCtrl(p3, -1, size=(190, 25))
        gbs3.Add(pgana, pos=(6, 2))
#Agregamos Boton Guardar
        guard = Button(p3, -1, "&Guardar")
        gbs3.Add(guard, pos=(8, 3))
        guard.Bind(EVT_BUTTON, self.guardarArt)
        canc = Button(p3, -1, "&Cancelar")
        gbs3.Add(canc, pos=(8, 1))
        canc.Bind(EVT_BUTTON, self.cerrarArt)
        p3.SetSizer(gbs3)
        f4.Show()

    def guardarArt(self, event):
        listaArt = []
        listaSql = []
        ide = ""
        self.pet = pet = self.pnet.GetValue()
        gan = gan = self.pgana.GetValue()
        g = int(gan)
        p = int(pet)
        gano = p + (p*(g/100))
        self.gano = gano = str(gano)
        listaArt.append((ide, self.cod.GetValue(), self.tip.GetValue(), self.des.GetValue(), self.cant.GetValue(), self.pnet.GetValue(), self.gano))
        listaSql.append((self.cod.GetValue(), self.tip.GetValue(), self.des.GetValue(), self.cant.GetValue(), self.pnet.GetValue(), self.gano))
        for i in listaArt:
            self.dvlc2.AppendItem(i)
        self.cargarArticulosSql(listaSql)
        self.mostrarArticulos(EVT_BUTTON)

    def cerrarStock(self, event):
        self.f3.Close()

    def cerrarArt(self, event):
        self.f4.Close()

    def cargarArticulosSql(self, lista):
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute('''CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            Codigo NVARCHAR NOT NULL,
            Tipo NVARCHAR NOT NULL,
            Descripcion NVARCHAR NOT NULL,
            Cantidad NVARCHAR NOT NULL,
            PrecioUnitario NVARCHAR NOT NULL,
            PrecioPublico NVARCHAR NOT NULL)''')
        except:
            pass
        cur.executemany("INSERT INTO articulos VALUES (NULL,?,?,?,?,?,?)", lista,)
        con.commit()
        con.close()

    def mostrarArticulos(self, event):
        self.dvlc2.DeleteAllItems()
        lista = self.recuperoDBarticulos()
        for i in lista:
            self.dvlc2.AppendItem(i)

    def recuperoDBarticulos(self):
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM articulos ORDER BY id")
        tuplas = cur.fetchall()
        listaA = [list(e) for e in tuplas]
        for e in listaA:
            e[0] = str(e[0])
        con.close()
        return listaA

    def buscaArticulo(self, event):
        fr3 = self.fr3 = Frame(None, -1, "Buscar Articulos", size=(450, 500))
        pa2 = self.pa2 = Panel(fr3, -1, style=TAB_TRAVERSAL)
        grid = GridBagSizer(5, 5)
        self.dtvlc = dtvlc = DataViewListCtrl(pa2)
        bx2 = BoxSizer(VERTICAL)
        bx2.Add(grid)
        bx2.Add(dtvlc, 1, EXPAND)
#Agrego Buscador
        art = StaticText(pa2, -1, "Buscador de Articulos")
        grid.Add(art, pos=(1, 1))
        iD = StaticText(pa2, -1, "Tipo")
        grid.Add(iD, pos=(3, 1))
        self.busca = busca = SearchCtrl(pa2, -1, size=(190, 25))
        grid.Add(busca, pos=(3, 2))
        sep = StaticText(pa2, -1, "")
        grid.Add(sep, pos=(5, 5))
        busca.Bind(EVT_SEARCHCTRL_SEARCH_BTN, self.devuelvolistaArt)
#Agrego al dataview
        encabezado = [('Id', 100), ('Codigo', 150), ('Tipo', 150), ('Descripción', 150), ('Cantidad', 150), ('Precio Neto Unitario', 150), ('Precio Publico', 150)]
        for i in encabezado:
            dtvlc.AppendTextColumn(i[0], width=i[1])
        pa2.SetSizer(bx2)
        fr3.Show()
        dtvlc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.modificoArt)

    def devuelvolistaArt(self, event):
        self.dtvlc.DeleteAllItems()
        lista = self.buscarArtSql()
        for i in lista:
            self.dtvlc.AppendItem(i)

    def buscarArtSql(self):
        lista = []
        tipo = self.busca.GetValue()
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        parte = tipo
        sentencia = "SELECT * FROM Articulos WHERE Tipo LIKE '%" + parte + "%'"
        cur.execute(sentencia)
        tuplas = cur.fetchall()
        lista = [list(e) for e in tuplas]
        for e in lista:
            e[0] = str(e[0])
        con.close()
        return lista

    def modificoArt(self, event):
        id, co, ti, ma, ca, pn, pp = self.modificaoeliminaArt()
        self.frameArt = frameArt = Frame(None, -1, "Modifico Articulo")
        pArt = Panel(frameArt, -1, style=TAB_TRAVERSAL)
        gArt = GridBagSizer(5, 5)
#Boton Editar
        bEditA = Button(pArt, -1, "Editar")
        gArt.Add(bEditA, pos=(1, 1))
        bEditA.Bind(EVT_BUTTON, self.habilitaEdicionArt)
#Boton Guardar
        bGuarA = Button(pArt, -1, "Guardar")
        gArt.Add(bGuarA, pos=(1, 3))
        bGuarA.Bind(EVT_BUTTON, self.guardoEdicionArticulo)
#Agrego ID
        idArt = StaticText(pArt, -1, "ID")
        gArt.Add(idArt, pos=(2, 1))
        idArt2 = self.idArt2 = TextCtrl(pArt, -1, value=id, size=(190, 25))
        gArt.Add(idArt2, pos=(2, 2))
        idArt2.Disable()
#Agrego Codigo
        coArt = StaticText(pArt, -1, "Codigo")
        gArt.Add(coArt, pos=(3, 1))
        coArt2 = self.coArt2 = TextCtrl(pArt, -1, value=co, size=(190, 25))
        gArt.Add(coArt2, pos=(3, 2))
        coArt2.Disable()
#Agrego Tipo
        tArt = StaticText(pArt, -1, "Tipo")
        gArt.Add(tArt, pos=(4, 1))
        tArt2 = self.tArt2 = TextCtrl(pArt, -1, value=ti, size=(190, 25))
        gArt.Add(tArt2, pos=(4, 2))
        tArt2.Disable()
#Agrego Marca
        mArt = StaticText(pArt, -1, "Descripción")
        gArt.Add(mArt, pos=(5, 1))
        mArt2 = self.mArt2 = TextCtrl(pArt, -1, value=ma, size=(190, 25))
        gArt.Add(mArt2, pos=(5, 2))
        mArt2.Disable()
#Agrego Cantidad
        cArt = StaticText(pArt, -1, "Cantidad")
        gArt.Add(cArt, pos=(6, 1))
        cArt2 = self.cArt2 = TextCtrl(pArt, -1, value=ca, size=(190, 25))
        gArt.Add(cArt2, pos=(6, 2))
        cArt2.Disable()
#Agrego Precio Neto
        pnArt = StaticText(pArt, -1, "Precio Neto")
        gArt.Add(pnArt, pos=(7, 1))
        pnArt2 = self.pnArt2 = TextCtrl(pArt, -1, value=pn, size=(190, 25))
        gArt.Add(pnArt2, pos=(7, 2))
        pnArt2.Disable()
#Agrego Precio Publico
        ppArt = StaticText(pArt, -1, "Precio Publico")
        gArt.Add(ppArt, pos=(8, 1))
        ppArt2 = self.ppArt2 = TextCtrl(pArt, -1, value=pp, size=(190, 25))
        gArt.Add(ppArt2, pos=(8, 2))
        ppArt2.Disable()
#Agrego Boton Eliminar
        bElimiArt = Button(pArt, -1, "Eliminar")
        gArt.Add(bElimiArt, pos=(9, 1))
        bElimiArt.Bind(EVT_BUTTON, self.eliminaArticulo)
#Fin Frame
        pArt.SetSizer(gArt)
        frameArt.Show()

    def modificaoeliminaArt(self):
        lista = []
        listaE = []
        fila = int(self.dtvlc.GetSelectedRow())
        ide = self.dtvlc.GetTextValue(fila, 0)
        if len(ide) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = ide
            sentencia = "SELECT * FROM Articulos WHERE id LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        for i in lista:
            listaE += i
        return listaE

    def habilitaEdicionArt(self, event):
        self.coArt2.Enable()
        self.tArt2.Enable()
        self.mArt2.Enable()
        self.cArt2.Enable()
        self.pnArt2.Enable()
        self.ppArt2.Enable()

    def guardoEdicionArticulo(self, event):
        id = self.idArt2.GetValue()
        co = self.coArt2.GetValue()
        ti = self.tArt2.GetValue()
        ma = self.mArt2.GetValue()
        ca = self.cArt2.GetValue()
        pn = self.pnArt2.GetValue()
        pp = self.ppArt2.GetValue()
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute("UPDATE articulos SET Codigo = ?, Tipo = ?, Descripcion = ?, Cantidad = ?, PrecioUnitario = ?, PrecioPublico = ? WHERE id= ?",(co, ti, ma, ca, pn, pp, id))
        except:
            pass
        con.commit()
        con.close()
        self.frameArt.Close()

    def eliminaArticulo(self, event):
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        try:
            cur.execute("DELETE FROM articulos WHERE id = ?",(id))
        except:
            pass
        con.commit()
        con.close()

#------------------------------Cierra Articulos/Stock------------------------------

#------------------------------Ventas------------------------------ f4, p3, dvlc3, f5, p4, gbs4

    def ventas(self, event):
        self.centinela = centinela = True
        self.listafactura = listafactura = []
        self.acumulador = acumulador = 0
        self.f4 = f4 = Frame(None, -1, "Venta", size=(800, 600))
        p3 = self.p3 = Panel(f4, -1)
        dvlc3 = self.dvlc3 = DataViewListCtrl(p3)
        encabezado = [('Id', 100), ('Codigo', 150), ('Tipo', 150), ('Descripción', 150), ('Cantidad', 150), ('Precio Neto Unitario', 150), ('Precio Neto Publico', 150), ('Importe', 150)]
        for i in encabezado:
            dvlc3.AppendTextColumn(i[0], width=i[1])
        sizerV3 = BoxSizer(VERTICAL)
        sizerV3.Add(dvlc3, 1, EXPAND)
        sizerH3 = BoxSizer(HORIZONTAL)
        aCarro = Button(p3, -1, "Agregar al Carro")
        sizerH3.Add(aCarro)
        aCarro.Bind(EVT_BUTTON, self.agregarCarro)
        factura = Button(p3, -1, "Factura")
        sizerH3.Add(factura)
        factura.Bind(EVT_BUTTON, self.facturacion)
        bCrr = Button(p3, -1, "Cerrar")
        bCrr.Bind(EVT_BUTTON, self.CerrarVentas)
        sizerH3.Add(bCrr)
        sizerV3.Add(sizerH3)
        p3.SetSizer(sizerV3)
        f4.Show()

    def CerrarVentas(self, event):
        self.f4.Close()

    def agregarCarro(self, event):
        self.faCarro = faCarro = Frame(None, -1, "Buscar Articulo para Agregar", size=(800, 600))
        self.acPanel = acPanel = Panel(faCarro, -1, style=TAB_TRAVERSAL)
        self.acdvelc = acdvelc = DataViewListCtrl(acPanel)
        acgrbs = GridBagSizer(5, 5)
        bx = BoxSizer(VERTICAL)
        bx.Add(acgrbs)
        bx.Add(acdvelc, 1, EXPAND)
        encabezado = [('Id', 100), ('Codigo', 150), ('Tipo', 150), ('Descripción', 150), ('Stock', 150), ('Precio Neto Unitario', 150), ('Precio Neto Publico', 150)]
        for i in encabezado:
            acdvelc.AppendTextColumn(i[0], width=i[1])
        bsca = StaticText(acPanel, -1, "Busqueda")
        acgrbs.Add(bsca, pos=(1, 3))
#Buscamos por Tipo
        tip = StaticText(acPanel, -1, "Tipo")
        acgrbs.Add(tip, pos=(3, 2))
        self.tip2 = tip2 = TextCtrl(acPanel, -1, size=(190, 25))
        acgrbs.Add(tip2, pos=(3, 3))
#Agregamos Boton Buscar y Aceptar
        bs = Button(acPanel, -1, "Buscar")
        acgrbs.Add(bs, pos=(6, 2))
        bs.Bind(EVT_BUTTON, self.buscarcarroSql)
        bCan = Button(acPanel, -1, "Aceptar")
        acgrbs.Add(bCan, pos=(6, 4))
        bCan.Bind(EVT_BUTTON, self.canBusq)
        sep = StaticText(acPanel, -1, "")
        acgrbs.Add(sep, pos=(7, 1))
        acPanel.SetSizer(bx)
        faCarro.Show()
        acdvelc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.agregoVentas)

    def buscarcarroSql(self, event):
        self.acdvelc.DeleteAllItems()
        lista = self.carroArtSql()
        for i in lista:
            self.acdvelc.AppendItem(i)

    def carroArtSql(self):
        lista = []
        tipo = self.tip2.GetValue()
        con = sqlite3.connect("puntodeventa.db")
        cur = con.cursor()
        parte = tipo
        sentencia = "SELECT * FROM Articulos WHERE Tipo LIKE '%" + parte + "%'"
        cur.execute(sentencia)
        tuplas = cur.fetchall()
        lista = [list(e) for e in tuplas]
        for e in lista:
            e[0] = str(e[0])
        con.close()
        return lista
    
    def canBusq(self, event):
        self.faCarro.Close()

    def agregoVentas(self, event):
        ide, co, ti, de, ca, pn, pp = self.buscoArticuloCarro()
        agVentas = self.agVentas = Frame(None, -1, "Agregar al Carro", size=(400, 400))
        panel = Panel(agVentas, -1, style=TAB_TRAVERSAL)
        aGridbag = GridBagSizer(5, 5)
#Boton Guardar
        bGuardar = Button(panel, -1, "Aceptar")
        aGridbag.Add(bGuardar, pos=(10, 1))
        bGuardar.Bind(EVT_BUTTON, self.guardoProducto)
#Boton Cancelar
        bCancel = Button(panel, -1, "Cancelar")
        aGridbag.Add(bCancel, pos=(10, 3))
        bCancel.Bind(EVT_BUTTON, self.cancelProducto)
#Mostramos ID
        idPro = StaticText(panel, -1, "ID")
        aGridbag.Add(idPro, pos=(2, 1))
        idPro2 = self.idPro2 = TextCtrl(panel, -1, value=ide, size=(190, 25))
        aGridbag.Add(idPro2, pos=(2, 2))
        idPro2.Disable()
#Mostramos Codigo
        codPro = StaticText(panel, -1, "Codigo")
        aGridbag.Add(codPro, pos=(3, 1))
        codPro2 = self.codPro2 = TextCtrl(panel, -1, value=co, size=(190, 25))
        aGridbag.Add(codPro2, pos=(3, 2))
        codPro2.Disable()
#Mostramos Tipo
        tipPro = StaticText(panel, -1, "Tipo")
        aGridbag.Add(tipPro, pos=(4, 1))
        tipPro2 = self.tipPro2 = TextCtrl(panel, -1, value=ti, size=(190, 25))
        aGridbag.Add(tipPro2, pos=(4, 2))
        tipPro2.Disable()
#Mostramos Descripción
        desPro = StaticText(panel, -1, "Descripción")
        aGridbag.Add(desPro, pos=(5, 1))
        desPro2 = self.desPro2 = TextCtrl(panel, -1, value=de, size=(190, 25))
        aGridbag.Add(desPro2, pos=(5, 2))
        desPro2.Disable()
#Mostramos la Cantidad
        canPro = StaticText(panel, -1, "Cantidad")
        aGridbag.Add(canPro, pos=(6, 1))
        canPro2 = self.canPro2 = TextCtrl(panel, -1, size=(190, 25))
        aGridbag.Add(canPro2, pos=(6, 2))
#Mostramos Precio Neto
        pnPro = StaticText(panel, -1, "Precio Neto")
        aGridbag.Add(pnPro, pos=(7, 1))
        pnPro2 = self.pnPro2 = TextCtrl(panel, -1, value=pn, size=(190, 25))
        aGridbag.Add(pnPro2, pos=(7, 2))
        pnPro2.Disable()
#Mostramos Precio Publico
        ppPro = StaticText(panel, -1, "Precio Publico")
        aGridbag.Add(ppPro, pos=(8, 1))
        ppPro2 = self.ppPro2 = TextCtrl(panel, -1, value=pp, size=(190, 25))
        aGridbag.Add(ppPro2, pos=(8, 2))
        ppPro2.Disable()
        panel.SetSizer(aGridbag)
        agVentas.Show()

    def buscoArticuloCarro(self):
        lista = []
        listaE = []
        fila = self.acdvelc.GetSelectedRow()
        ide = self.acdvelc.GetTextValue(fila, 0)
        if len(ide) > 0:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = ide
            sentencia = "SELECT * FROM Articulos WHERE id LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
        for i in lista:
            listaE+=i
        ide, co, ti, de, ca, pn, pp = listaE
        return ide, co, ti, de, ca, pn, pp

    def guardoProducto(self, event):
        lista = []
        listaf = []
        can = self.canPro2.GetValue()
        pp = self.ppPro2.GetValue()
        cantidad = int(can)
        precioPu = float(pp)
        total = (cantidad*precioPu)
        self.to = to = str(total)
        lista.append((self.idPro2.GetValue(), self.codPro2.GetValue(), self.tipPro2.GetValue(), self.desPro2.GetValue(), self.canPro2.GetValue(), self.pnPro2.GetValue(), self.ppPro2.GetValue(), self.to))
        listaf.append((self.idPro2.GetValue(), self.codPro2.GetValue(), self.tipPro2.GetValue(), self.desPro2.GetValue(), self.canPro2.GetValue(), self.ppPro2.GetValue(), self.to))
        for i in lista:
            self.dvlc3.AppendItem(i)
        self.pasoaFactura(listaf)
        self.agVentas.Close()

    def cancelProducto(self, event):
        self.agVentas.Close()

    def pasoaFactura(self, lista):
        self.listafactura += lista
        print(self.listafactura)

    def facturacion(self, event):
        facFrame = self.facFrame = Frame(None, -1, "Factura", size=(1024, 768))
        self.panel = panel = Panel(facFrame, -1, style=TAB_TRAVERSAL)
        self.facDvelc = facDvelc = DataViewListCtrl(panel)
        facGridbag = GridBagSizer(5, 0)
        bx = BoxSizer(HORIZONTAL)
        bx.Add(facGridbag)
        bx.Add(facDvelc, 1, EXPAND)
        encabezado = [('Id', 50), ('Codigo', 100), ('Tipo', 100), ('Descripción', 100), ('Cantidad', 100), ('Precio Neto Unitario', 150), ('Precio Neto Publico', 150)]
        for i in encabezado:
            facDvelc.AppendTextColumn(i[0], width=i[1])
        nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv = self.devuelvodatosFactura()
        nomOrg = StaticText(panel, -1, "Nombre Organizacion: ")
        facGridbag.Add(nomOrg, pos= (1, 1))
        nomOrg2 = StaticText(panel, -1, label = nop)
        facGridbag.Add(nomOrg2, pos=(1, 2))
        cuitOrg = StaticText(panel, -1, "C.U.I.T. Nro: ")
        facGridbag.Add(cuitOrg, pos=(2, 1))
        cuitOrg2 = StaticText(panel, -1, label = cu)
        facGridbag.Add(cuitOrg2, pos=(2, 2))
        ingbOrg = StaticText(panel, -1, "Ing. Brutos: ")
        facGridbag.Add(ingbOrg, pos=(3, 1))
        ingbOrg2 = StaticText(panel, -1, label = ing)
        facGridbag.Add(ingbOrg2, pos=(3, 2))
        cpOrg = StaticText(panel, -1, "Codigo Postal: ")
        facGridbag.Add(cpOrg, pos=(4, 1))
        cpOrg2 = StaticText(panel, -1, label = cp)
        facGridbag.Add(cpOrg2, pos=(4, 2))
        diOrg = StaticText(panel, -1, "Domicilio: ")
        facGridbag.Add(diOrg, pos=(5, 1))
        diOrg2 = StaticText(panel, -1, label=di)
        facGridbag.Add(diOrg2, pos=(5, 2))
        loOrg = StaticText(panel, -1, "Localidad: ")
        facGridbag.Add(loOrg, pos=(6, 1))
        loOrg2 = StaticText(panel, -1, label =lo)
        facGridbag.Add(loOrg2, pos=(6, 2))
        prvOrg = StaticText(panel, -1, "Provincia: ")
        facGridbag.Add(prvOrg, pos=(7, 1))
        prvOrg2 = StaticText(panel, -1, label = pr)
        facGridbag.Add(prvOrg2, pos=(7, 2))
        iniOrg = StaticText(panel, -1, "Inicio de Actividades: ")
        facGridbag.Add(iniOrg, pos=(8, 1))
        iniOrg2 = StaticText(panel, -1, label = inac)
        facGridbag.Add(iniOrg2, pos=(8, 2))
        ivaOrg = StaticText(panel, -1, "Categoria: ")
        facGridbag.Add(ivaOrg, pos=(9, 1))
        ivaOrg2 = StaticText(panel, -1, label = iva)
        facGridbag.Add(ivaOrg2, pos=(9, 2))
        habmOrg = StaticText(panel, -1, "Habilitacion Municipal: ")
        facGridbag.Add(habmOrg, pos=(10, 1))
        habmOrg2 = StaticText(panel, -1, label= habm)
        facGridbag.Add(habmOrg2, pos=(10, 2))
        facCate = StaticText(panel, -1, "Categoria: ")
        facGridbag.Add(facCate, pos=(11, 1))
        tipoCate = ["Consumidor Final", "Responsable Inscripto", "Resp. Monotributista"]
        self.facopt = facopt = RadioBox(panel, -1, choices = tipoCate, style = RA_SPECIFY_COLS | NO_BORDER, size=(450, 50))
        facopt.Bind(EVT_RADIOBOX, self.killcombo)
        opfac = self.facopt.GetStringSelection()
        print(opfac)
        facGridbag.Add(facopt, pos=(11, 2))
        tiqOrg = StaticText(panel, -1, "Factura: ")
        facGridbag.Add(tiqOrg, pos=(13, 1))
        if iva == "Resp. Monotributista" and opfac == "Consumidor Final":
            tiqOrg2 = StaticText(panel, -1, label= "C")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Resp. Monotributista" and opfac == "Responsable Inscripto":
            tiqOrg2 = StaticText(panel, -1, label= "C")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Resp. Monotributista" and opfac == "Resp. Monotributista":
            tiqOrg2 = StaticText(panel, -1, label= "C")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Resp. Monotributista" and opfac == "Excento":
            tiqOrg2 = StaticText(panel, -1, label= "C")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Responsabe Inscripto" and opfac == "Responsable Inscripto":
            tiqOrg2 = StaticText(panel, -1, label= "A")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Responsable Inscripto" and opfac == "Consumidor Final":
            tiqOrg2 = StaticText(panel, -1, label= "B")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Responsable Inscripto" and opfac == "Resp. Monotributista":
            tiqOrg2 = StaticText(panel, -1, label= "B")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        elif iva == "Responsable Inscripto" and opfac == "Excento":
            tiqOrg2 = StaticText(panel, -1, label= "B")
            facGridbag.Add(tiqOrg2, pos=(13, 2))
        fyh = StaticText(panel, -1, "Fecha y Hora: ")
        facGridbag.Add(fyh, pos=(14, 1))
        fyh2 = StaticText(panel, -1, label = datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        facGridbag.Add(fyh2, pos=(14, 2))
        if self.centinela == True:
            self.total = total = self.cargaFactura(self.listafactura)
            totalOrg = StaticText(panel, -1, "TOTAL: ", size=(200, 30))
            facGridbag.Add(totalOrg, pos=(15, 1))
            self.totalOrg2 = totalOrg2 = TextCtrl(panel, -1, value = str(self.total), size=(150,30))
            facGridbag.Add(totalOrg2, pos=(15, 2))
        elif self.centinela == False:
            self.total = total = self.cargaFactura(self.listafactura)
            totalOrg = StaticText(panel, -1, "TOTAL: ", size=(200, 30))
            facGridbag.Add(totalOrg, pos=(16, 1))
            self.totalOrg2 = totalOrg2 = TextCtrl(panel, -1, value = str(self.total), size=(150,30))
            facGridbag.Add(totalOrg2, pos=(16, 2))
        bCancel = Button(panel, -1, "Cancelar")
        facGridbag.Add(bCancel, pos=(17,2))
        bCancel.Bind(EVT_BUTTON, self.cerrarFactura)
        bAceptar = Button(panel, -1, "Aceptar")
        facGridbag.Add(bAceptar, pos=(17, 1))
        bAceptar.Bind(EVT_BUTTON, self.aceptaFactura)
        facDvelc.Bind(EVT_DATAVIEW_ITEM_ACTIVATED, self.editoFactura)
        panel.SetSizer(bx)
        facFrame.Show()

    def killcombo(self, event):
        opcion = self.facopt.GetStringSelection()

    def devuelvodatosFactura(self):
        listaE = []
        try:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = "1"
            sentencia = "SELECT * FROM personaldata WHERE id LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
            for i in lista:
                listaE+=i
            ide, nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv = listaE
        except:
            nop = ""
            cu = ""
            ing = ""
            cp = ""
            di = ""
            lo = ""
            pr = ""
            inac = ""
            iva = ""
            habm = ""
            pv = ""
        return nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv

    def cargaFactura(self, lista):
        self.facDvelc.DeleteAllItems()
        for i in lista:
            self.facDvelc.AppendItem(i)
        for x in lista:
            for i in range(len(x)):
                num=x[6]
            self.acumulador += float(num)
        return self.acumulador

    def cerrarFactura(self, event):
        self.facFrame.Close()
        self.f4.Close()

    def aceptaFactura(self, event):
        self.facFrame.Close()
        self.f4.Close()
        boxdlg = BoxSizer(VERTICAL)
        self.dlg = dlg = Dialog(None, -1, size=(400, 200))
        panel = Panel(dlg, -1, style=TAB_TRAVERSAL)
        gracias = StaticText(panel, -1, "GRACIAS POR SU COMPRA!")
        boxdlg.Add(gracias, 0, ALIGN_CENTER | ALL, 50)
        boAceptar = Button(panel, -1, "Aceptar", size=(190, 25))
        boxdlg.Add(boAceptar, 0, ALIGN_CENTER | ALL, 0)
        boAceptar.Bind(EVT_BUTTON, self.cerrarDialogo)
        panel.SetSizer(boxdlg)
        dlg.ShowModal()
    
    def cerrarDialogo(self, event):
        self.dlg.Destroy()

    def editoFactura(self, event):
        boxdlgedFa = BoxSizer(VERTICAL)
        self.dlgedFa = dlgedFa = Dialog(None, -1, size=(400,200))
        panel = Panel(dlgedFa, -1, style=TAB_TRAVERSAL)
        opcion = StaticText(panel, -1, "¿Desea eliminar este item?")
        boxdlgedFa.Add(opcion, 0, ALIGN_CENTER | ALL, 50)
        boSi = Button(panel, -1, "Aceptar", size=(190, 25))
        boxdlgedFa.Add(boSi, 0, ALIGN_CENTER | ALL, 0)
        boSi.Bind(EVT_BUTTON, self.siborro)
        boNo = Button(panel, -1, "Cancelar", size=(190, 25))
        boxdlgedFa.Add(boNo, 0, ALIGN_CENTER | ALL, 0)
        boNo.Bind(EVT_BUTTON, self.noborro)
        panel.SetSizer(boxdlgedFa)
        dlgedFa.ShowModal()

    def noborro(self, event):
        self.dlgedFa.Destroy()

    def siborro(self, event):
        self.centinela = False
        self.acumulador = 0
        fila = int(self.facDvelc.GetSelectedRow())
        self.listafactura.pop(fila)
        self.facFrame.Close()
        self.facturacion(event)
        self.dlgedFa.Destroy()

#------------------------------Cierre Ventas------------------------------

#------------------------------Menu--------------------------------

class MyFrame(Frame):
    def __init__(self, title, pos, size):
        Frame.__init__(self, None, -1, title, pos, size)
        menuFile = Menu()
        menuFile.Append(1, "&Información del Sistema")
        menuFile.AppendSeparator()
        menuFile.Append(2, "&Información Personal")
        menuFile.AppendSeparator()
        menuFile.Append(3, "&Salir")
        menuBar = MenuBar()
        menuBar.Append(menuFile, "&Archivo")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("Bienvenido al sistema de Facturación")
        self.Bind(EVT_MENU, self.OnAbout, id=1)
        self.Bind(EVT_MENU, self.PersonalData, id=2)
        self.Bind(EVT_MENU, self.OnQuit, id=3)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        MessageBox("Sistema de Facturación", "Sistema de Facturación 2019", OK | ICON_INFORMATION, self)

    def PersonalData(self, event):
        self.prFrame = prFrame = Frame(None, -1, "Datos Personales", (50, 60), (800, 600))
        nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv = self.devuelvoPr()
        prPanel = Panel(prFrame, -1, style=TAB_TRAVERSAL)
        prGbs = GridBagSizer(5, 5)
#Boton Nuevo
        bNuevo = Button(prPanel, -1, "Nuevo")
        prGbs.Add(bNuevo, pos=(1, 1))
        if len(nop)==0:
            bNuevo.Bind(EVT_BUTTON, self.habilitaEdicionPr)
#Boton Modifica
        bModifi = Button(prPanel, -1, "Modifica")
        prGbs.Add(bModifi, pos=(1, 3))
        bModifi.Bind(EVT_BUTTON, self.habilitaEdicionPr)
#Boton Guardar
        bGuar = Button(prPanel, -1, "Guardar")
        prGbs.Add(bGuar, pos=(11, 3))
        bGuar.Bind(EVT_BUTTON, self.guardoPr)
#Agregamos Nombre de la Organizacion
        prNomo = StaticText(prPanel, -1, "Nombre de la Organizacion")
        prGbs.Add(prNomo, pos=(2, 1))
        prNomo2 = self.prNomo2 = TextCtrl(prPanel, -1, value=nop, size=(190, 25))
        prGbs.Add(prNomo2, pos=(2, 2))
        prNomo2.Disable()
#Agregamos CUIT
        prCuit = StaticText(prPanel, -1, "CUIT")
        prGbs.Add(prCuit, pos=(3, 1))
        self.prCuit2 = prCuit2 = TextCtrl(prPanel, -1, value=cu, size=(190, 25))
        prGbs.Add(prCuit2, pos=(3, 2))
        prCuit2.Disable()
#Agregamos Ingresos Brutos
        prIngr = StaticText(prPanel, -1, "Ingresos Brutos")
        prGbs.Add(prIngr, pos=(4, 1))
        self.prIngr2 = prIngr2 = TextCtrl(prPanel, -1, value=ing, size=(190, 25))
        prGbs.Add(prIngr2, pos=(4, 2))
        prIngr2.Disable()
#Agregamos Codigo Postal
        prCp = StaticText(prPanel, -1, "Codigo Postal")
        prGbs.Add(prCp, pos=(5, 1))
        prCp2 = self.prCp2 = TextCtrl(prPanel, -1, value=cp, size=(190, 25))
        prGbs.Add(prCp2, pos=(5, 2))
        prCp2.Disable()
#Agregamos Direccion
        prDire = StaticText(prPanel, -1, "Domicilio")
        prGbs.Add(prDire, pos=(6, 1))
        prDire2 = self.prDire2 = TextCtrl(prPanel, -1, value=di, size=(190, 25))
        prGbs.Add(prDire2, pos=(6, 2))
        prDire2.Disable()
#Agregamos Localidad
        prLocal = StaticText(prPanel, -1, "Localidad")
        prGbs.Add(prLocal, pos=(7, 1))
        prLocal2 = self.prLocal2 = TextCtrl(prPanel, -1, value=lo, size=(190, 25))
        prGbs.Add(prLocal2, pos=(7, 2))
        prLocal2.Disable()
#Agregamos Provincia
        prProvin = StaticText(prPanel, -1, "Provincia")
        prGbs.Add(prProvin, pos=(8, 1))
        prProvin2 = self.prProvin2 = TextCtrl(prPanel, -1, value=pr, size=(190, 25))
        prGbs.Add(prProvin2, pos=(8, 2))
        prProvin2.Disable()
#Agregamos Inicio de Actividades
        prInAct = StaticText(prPanel, -1, "Inicio de Actividades")
        prGbs.Add(prInAct, pos=(9, 1))
        self.dpc = dpc = DatePickerCtrl(prPanel, -1, style = DP_DROPDOWN | DP_SHOWCENTURY | DP_ALLOWNONE)
        self.dpc.Bind(EVT_DATE_CHANGED, self.OnDateChanged, dpc)
        prGbs.Add(dpc, pos=(9, 2))
        self.dpc.Disable()
#Agregamos AFIP
        prTiva = StaticText(prPanel, -1, "Categoria")
        prGbs.Add(prTiva, pos=(10, 1))
        optList = ["Responsable Inscripto", "Resp. Monotributista", "Excento"]
        self.opt = opt = RadioBox(prPanel, -1, choices = optList)
        prGbs.Add(opt, pos=(10, 2))
        self.opt.Bind(EVT_RADIOBOX, self.optRadio)
        opt.Disable()
#Agregamos Habilitacion Municipal
        prHabm = StaticText(prPanel, -1, "Habilitacion Municipal")
        prGbs.Add(prHabm, pos=(11, 1))
        self.prHabm2 = prHabm2 = TextCtrl(prPanel, -1, value=habm, size=(190, 25))
        prGbs.Add(prHabm2, pos=(11, 2))
        prHabm2.Disable()
#Agregamos Punto de Venta
        prPventa = StaticText(prPanel, -1, "Punto de Venta Nº: ")
        prGbs.Add(prPventa, pos=(12, 1))
        self.prPventa2 = prPventa2 = TextCtrl(prPanel, -1, value=pv, size=(190, 25))
        prGbs.Add(prPventa2, pos=(12, 2))
        prPventa2.Disable()
#Cierro Frame 
        prPanel.SetSizer(prGbs)
        prFrame.Show()

    def optRadio(self, event):
        opcion = self.opt.GetStringSelection()
        print(opcion)
        self.tIva = tIva = opcion

    def OnDateChanged(self, event):
        seleccion = self.dpc.GetValue()
        print(seleccion)
        self.prInAct2 = prInAct2 = str(seleccion)

    def guardoPr(self, event):
        listasql = []
        listasql.append((self.prNomo2.GetValue(), self.prCuit2.GetValue(), self.prIngr2.GetValue(), self.prCp2.GetValue(), self.prDire2.GetValue(), self.prLocal2.GetValue(), self.prProvin2.GetValue(), self.prInAct2, self.tIva, self.prHabm2.GetValue(), self.prPventa2.GetValue()))
        self.modificaPr(listasql)
        self.prFrame.Close()

    def devuelvoPr(self):
        listaE = []
        try:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            parte = "1"
            sentencia = "SELECT * FROM personaldata WHERE id LIKE '%" + parte + "%'"
            cur.execute(sentencia)
            tuplas = cur.fetchall()
            lista = [list(e) for e in tuplas]
            for e in lista:
                e[0] = str(e[0])
            con.close()
            for i in lista:
                listaE+=i
            ide, nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv = listaE
        except:
            nop = ""
            cu = ""
            ing = ""
            cp = ""
            di = ""
            lo = ""
            pr = ""
            inac = ""
            iva = ""
            habm = ""
            pv = ""
        return nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv

    def habilitaEdicionPr(self, event):
        self.prNomo2.Enable()
        self.prCuit2.Enable()
        self.prIngr2.Enable()
        self.prCp2.Enable()
        self.prDire2.Enable()
        self.prLocal2.Enable()
        self.prProvin2.Enable()
        self.opt.Enable()
        self.dpc.Enable()
        self.prHabm2.Enable()
        self.prPventa2.Enable()

    def modificaPr(self, lista):
        listaEdit = []
        listaF = []
        try:
            listaEdit = [list(elem) for elem in lista]
            for i in listaEdit:
                listaF += i
            id = "1"
            nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv = listaF
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            cur.execute("UPDATE personaldata SET NombreOrganizacion = ?, CUIT = ?, IngresosBrutos = ?, CodigoPostal = ?, Domicilio = ?, Localidad = ?, Provincia = ?, InicioActividades = ?, Categoria = ?, HabilitacionMunicipal = ?, PuntoVenta = ? WHERE id= ?",(nop, cu, ing, cp, di, lo, pr, inac, iva, habm, pv, id))
            con.commit()
            con.close() 
        except:
            con = sqlite3.connect("puntodeventa.db")
            cur = con.cursor()
            try:
                cur.execute('''CREATE TABLE IF NOT EXISTS personaldata (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                NombreOrganizacion NVARCHAR NOT NULL,
                CUIT NVARCHAR NOT NULL,
                IngresosBrutos NVARCHAR NOT NULL,
                CodigoPostal NVARCHAR NOT NULL,
                Domicilio NVARCHAR NOT NULL,
                Localidad NVARCHAR NOT NULL,
                Provincia NVARCHAR NOT NULL,
                InicioActividades NVARCHAR NOT NULL,
                Categoria NVARCHAR NOT NULL,
                HabilitacionMunicipal NVARCHAR NOT NULL,
                PuntoVenta NVARCHAR NOT NULL)''')
            except:
                print("No se creo la tabla")
            cur.executemany("INSERT INTO personaldata VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)", lista,)
            con.commit()
            con.close()       

app = MyApp()
app.MainLoop()