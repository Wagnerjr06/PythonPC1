# Diccionario
mime_types= {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}


nom_archivo= input("Ingrese el nombre del archivo: ").strip()
nom_archivo_lower= nom_archivo.lower()
tipo_mime='application/octect-stream'
for sufijo in mime_types.keys():
    if nom_archivo_lower.endswith(sufijo):
        tipo_mime=mime_types[sufijo]
print(f"El tipo MIME para [nom_archivo] es {tipo_mime}")