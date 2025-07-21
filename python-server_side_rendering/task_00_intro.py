import os

def genera_invitacion(template, attendees):
    # Verificar tipos de entrada
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Verificar si la plantilla o la lista están vacías
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Procesa cada asistente
    for idx, attendee in enumerate(attendees, start=1):
        # Reemplazar los valores del asistente o "N/A" si faltan
        invitation = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )
        
        # Crea el archivo
        filename = f"output_{idx}.txt"
        
        # Escribir el archivo
        with open(filename, 'w') as file:
            file.write(invitation)

    print(f"Generated {len(attendees)} invitation files.")