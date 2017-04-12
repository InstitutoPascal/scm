# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from consultas.py")

#consultas completas (sin parametros)

def listadoClientes():
    datosClientes = db().select(db.clientes.ALL)
    i=0
    tablafinal=[]
    for x in datosClientes:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Codigo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Sexo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Localidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Número de calle',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Teléfono',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' Clientes',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.sexo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosClientes]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoProductos():
    datosProductos = db(db.articulos.proveedores == db.proveedores.id).select(db.articulos.ALL, db.proveedores.nombre_empresa)
    i=0
    tablafinal=[]
    for x in datosProductos:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Equipo',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Descripción',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Código de barras',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Precio de compra',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Precio de venta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Stock',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Proveedor',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Producto',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.producto.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.producto.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.codigo_barra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.precio_compra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.stock,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.proveedor.nombre_empresa,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosProductos]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoProveedor():
    datosProveedor = db().select(db.proveedores.ALL)
    i=0
    tablafinal=[]
    for x in datosProveedor:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:100px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre de empresa',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Localidad',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Calle',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Numero de calle',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Teléfono',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('E-mail',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Proveedor',_style='width:160px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.nombre_empresa,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.numero_calle,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.telefono,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosProveedor]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoVendedor():
    datosVendedor = db().select(db.vendedores.ALL)
    i=0
    tablafinal=[]
    for x in datosVendedor:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:100px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Dni',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Nombre',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Apellido',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Contraseña',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Vendedores',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.id,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.dni,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.nombre,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.password,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosVendedor]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)

def listadoVentas():
    datosVentas = db((db.ventas.vendedores==db.vendedores.id)&(db.ventas.clientes==db.clientes.id)&(db.ventas.equipo==db.articulos.id)).select(db.ventas.ALL ,db.vendedores.nombre, db.vendedores.apellido, db.clientes.nombre, db.clientes.apellido, db.articulos.equipo)
    i=0
    tablafinal=[]
    for x in datosVentas:
         i=i+1
    lista=[]
    lista.append(TABLE(TR(TH('Código',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Vendedor',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Cliente',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Equipo',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Fecha de venta',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Número de factura',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Cantidad',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('Total',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,'Ventas',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
     *[TR(TD(x.ventas.id,_style='width:100px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.vendedores.nombre, ' ', x.vendedores.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
     TD(x.clientes.nombre, ' ', x.clientes.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.producto.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.fecha_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.numero_factura,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.cantidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.ventas.total,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
     for x in datosVentas]),))
    tablafinal = DIV(lista)
    return dict (tabla=tablafinal, cantidad=i)




#Consultas (con parametros)

def clientes_ciudad():
    subtitulo=T('Listado de Clientes por ciudad')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Ciudad:",INPUT(_type="text",_name="ciudad",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.localidad==form.vars.ciudad).count()==0:
            form.errors.codigo="La ciudad ingresada no se encuentra registrada"
            response.flash = 'La ciudad ingresada no se encuentra registrada'
        else:
            listado =db(db.clientes.localidad==form.vars.ciudad).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DNI',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def clientes_dni():
    subtitulo=T('Listado de Clientes por dni')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Dni:",INPUT(_type="text",_name="dni",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.clientes.dni==form.vars.dni).count()==0:
            form.errors.codigo="El dni ingresado no se encuentra registrado"
            response.flash = 'El dni ingresado no se encuentra registrado'
        else:
            listado =db(db.clientes.dni==form.vars.dni).select(db.clientes.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DNI',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.nombre,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.apellido,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.dni,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#--------------------------------------------------------Productos--------------------------------------------------------#
    
def productos_codigo():
    subtitulo=T('Listado de Productos por codigo')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Codigo a buscar:",INPUT(_type="text",_name="codigo",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.codigo_barra==form.vars.codigo).count()==0:
            form.errors.codigo="El codigo de barra ingresado no se encuentra registrado"
            response.flash = 'El codigo de barra ingresado no se encuentra registrado'
        else:
            listado =db(db.producto.codigo_barra==form.vars.codigo).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('CODIGO DE BARRA',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('EQUIPO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('STOCK',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.codigo_barra,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.equipo,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.stock,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_superiores_venta():
    subtitulo=T('Listado de Productos superiores')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Precio de venta:",INPUT(_type="text",_name="precio",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.precio_venta > form.vars.precio).count()==0:
            form.errors.codigo="No hay productos con precios de venta mayores al ingresado"
            response.flash = 'No hay productos con precios de venta mayores al ingresado'
        else:
            listado =db(db.producto.precio_venta > form.vars.precio).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DESCRIPCION',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE VENTA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTOS',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_inferiores_venta():
    subtitulo=T('Listado de Productos')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Menos a:",INPUT(_type="text",_name="precio",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.precio_venta < form.vars.precio).count()==0:
            form.errors.codigo="No hay productos con precios de venta menores al ingresado"
            response.flash = 'No hay productos con precios de venta menores al ingresado'
        else:
            listado =db(db.producto.precio_venta < form.vars.precio).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DESCRIPCION',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE VENTA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
           
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
         response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_entre_venta():
    subtitulo=T('Listado de Productos')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Precio inferior:",INPUT(_type="integer",_name="precio1",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("Precio superior:",INPUT(_type="integer",_name="precio2",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db((db.producto.precio_venta >= form.vars.precio1) & (db.producto.precio_venta <= form.vars.precio2)).count()==0:
            form.errors.codigo="No hay productos con precio de venta entre los precios ingresados"
            response.flash = 'No hay productos con precio de venta entre los precios ingresados'
        else:
            listado =db((db.producto.precio_venta >= form.vars.precio1) & (db.producto.precio_venta <= form.vars.precio2)).select(db.producto.ALL, orderby=db.producto.precio_venta)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DESCRIPCION',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE VENTA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
           
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
         response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_superiores_compra():
    subtitulo=T('Listado de Productos superiores')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Precio de compra:",INPUT(_type="text",_name="precio",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.precio_compra > form.vars.precio).count()==0:
            form.errors.codigo="No hay productos con precios de compra mayores al ingresado"
            response.flash = 'No hay productos con precios de compra mayores al ingresado'
        else:
            listado =db(db.producto.precio_compra > form.vars.precio).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DESCRIPCION',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE COMPRA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTOS',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.precio_compra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_inferiores_compra():
    subtitulo=T('Listado de Productos')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Menos a:",INPUT(_type="text",_name="precio",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.precio_compra < form.vars.precio).count()==0:
            form.errors.codigo="No hay productos con precios de compra menores al ingresado"
            response.flash = 'No hay productos con precios de compra menores al ingresado'
        else:
            listado =db(db.producto.precio_compra < form.vars.precio).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DESCRIPCION',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE COMPRA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.precio_compra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
           
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
         response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_entre_compra():
    subtitulo=T('Listado de Productos')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Precio inferior:",INPUT(_type="integer",_name="precio1",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("Precio superior:",INPUT(_type="integer",_name="precio2",requires=IS_NOT_EMPTY(error_message= 'Campo obligatorio'))),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db((db.producto.precio_compra >= form.vars.precio1) & (db.producto.precio_compra <= form.vars.precio2)).count()==0:
            form.errors.codigo="No hay productos con precios de compra entre los precios ingresados"
            response.flash = 'No hay productos con precios de compra entre los precios ingresados'
        else:
            listado =db((db.producto.precio_compra >= form.vars.precio1) & (db.producto.precio_compra <= form.vars.precio2)).select(db.producto.ALL, orderby=db.producto.precio_compra)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DESCRIPCION',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE COMPRA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.precio_compra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
           
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
         response.flash = 'Hay un error en el formulario'
    else:
        response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)

#--------------------------------------------------------Proveedores--------------------------------------------------------#

def proveedor_codigo():
    subtitulo=T('Listado de proveedores por ID')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("ID a buscar:",INPUT(_type="text",_name="id",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.proveedor.id==form.vars.id).count()==0:
            form.errors.codigo="El ID ingresado no se encuentra registrado"
            response.flash = 'El ID ingresado no se encuentra registrado'
        else:
            listado =db(db.proveedor.id==form.vars.id).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EMPRESA',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('LOCALIDAD',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('EMAIL',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.nombre_empresa,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def proveedor_nombre():
    subtitulo=T('Listado de proveedores por nombre')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Nombre a buscar:",INPUT(_type="text",_name="nombre",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.proveedor.nombre_empresa==form.vars.nombre).count()==0:
            form.errors.codigo="El nombre ingresado no se encuentra registrado"
            response.flash = 'El nombre ingresado no se encuentra registrado'
        else:
            listado =db(db.proveedor.nombre_empresa==form.vars.nombre).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EMPRESA',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('LOCALIDAD',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('EMAIL',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.nombre_empresa,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def proveedor_ciudad():
    subtitulo=T('Listado de proveedores por Localidad')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Localidad a buscar:",INPUT(_type="text",_name="ciudad",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.proveedor.localidad==form.vars.ciudad).count()==0:
            form.errors.codigo="La localidad ingresada no se encuentra registrada"
            response.flash = 'La localidad ingresada no se encuentra registrada'
        else:
            listado =db(db.proveedor.localidad==form.vars.ciudad).select(db.proveedor.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EMPRESA',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('LOCALIDAD',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('EMAIL',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.nombre_empresa,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.localidad,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.email,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_uno():
    subtitulo=T('Listado de productos por nombre')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("Producto a buscar:",INPUT(_type="text",_name="equipo",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.equipo.lower()==form.vars.equipo).count()==0:
            form.errors.codigo="El celular ingresado no se encuentra registrado"
            response.flash = 'El celular ingresado no se encuentra registrado'
        else:
            listado =db(db.producto.equipo.lower()==form.vars.equipo).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('EQUIPO',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('PRECIO DE VENTA',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('STOCK',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' PRODUCTO',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.precio_venta,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.stock,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'

    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)


def productos_varios():
    subtitulo=T('Busqueda producto')
    tablaFinal=[]
    i=0
    form2=''
    form=FORM(TABLE(TR("producto:",INPUT(_type="text",_name="producto",requires=IS_NOT_EMPTY())),TR("",INPUT(_type="submit",_value="Buscar"))))
    if form.accepts(request.vars,session):
        if db(db.producto.equipo.upper().contains(form.vars.producto)).count()==0:
            form.errors.codigo= "El celular ingresado no se encuentra registrado"
            response.flash = "El celular ingresado no se encuentra registrado"
        else:
            listado =db(db.producto.equipo.upper().contains(form.vars.producto)).select(db.producto.ALL)
            for x in listado:
                i=i+1
            lista=[]
            lista.append(TABLE(TR(TH('NOMBRE',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('APELLIDO',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH('DNI',_style='width:200px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TFOOT(TR(TH('Total: ',_style='width:20px; color:#000; background: #99f; border: 2px solid #cdcdcd'),TH(i,' CLIENTE',_style='width:120px; color:#000; background: #99f; border: 2px solid #cdcdcd'))),
            *[TR(TD(x.equipo,_style='width:20px; color:#000; background: #eef; border: 2px solid #cdcdcd'),
            TD(x.descripcion,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),TD(x.codigo_barra,_style='width:200px; color:#000; background: #eef; border: 2px solid #cdcdcd'),)
            for x in listado]),))
            tablaFinal = DIV(lista)
            form2=FORM(TABLE(TR("",INPUT(_type="submit",_value="Volver"))))

            #refresca
            #redirect(URL('referentesPorCiudad',args=(),vars=dict()))
    elif form.errors:
       response.flash = 'Hay un error en el formulario'
    else:
       response.flash = 'Complete el Formulario'
    
    return dict(subtitulo=subtitulo, form=form, tabla=tablaFinal,cant=i,form2=form2)
