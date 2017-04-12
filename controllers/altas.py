# -*- coding: utf-8 -*-
# intente algo como
def index(): return dict(message="hello from altas.py")

#alta_cliente
def alta_cliente():
    form = SQLFORM(db.clientes)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_proveedor
def alta_proveedor():
    form = SQLFORM(db.proveedores)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_producto
def alta_producto():
    form = SQLFORM(db.articulos)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_ventas
def alta_ventas():
    form = SQLFORM(db.ventas)
    if form.accepts(request.vars, session):
        response.flash = 'El formulario fue aceptado'
        if form.accepts(request.vars, session):
            redirect(URL('alta_ventas'))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)

#alta_vendedor
def alta_vendedor():
    form = SQLFORM(db.vendedores)
    if form.accepts(request.vars, session):
        response.flash = 'Formulario aceptado'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    else:
        response.flash = 'Complete el formulario'
    return dict(f=form)
