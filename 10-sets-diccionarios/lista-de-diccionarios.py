contactos=[
    {
        "nombre":"Federico",
        "email":"federico@federico.com"
    },
    {
        "nombre":"Luis",
        "email":"wixho@luis.com"
    },
    {
        "nombre":"Antonio",
        "email":"toño@antonio.com"
    }
]
    
print(contactos)
contactos[0]["nombre"] = "Federica"
print(contactos[0]["nombre"])

print('\n----------------------------------------')
for contacto in contactos:
    print(f"Nombre del contacto {contacto['nombre']}")
    print(f"Email del contacto {contacto['email']}")
    print('----------------------------------------')
