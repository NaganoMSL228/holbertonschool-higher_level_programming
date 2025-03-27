def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template with placeholders and a list of objects.

    Args:
        template (str): A string template with placeholders {name}, {event_title}, {event_date}, {event_location}.
        attendees (list): A list of dictionaries containing data for each attendee.
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Create a copy of the template
        personalized_invitation = template

        # Replace placeholders with attendee data or "N/A" if missing
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            if value is None:  # Handle None values
                value = "N/A"
            personalized_invitation = personalized_invitation.replace(f"{{{placeholder}}}", str(value))

        # Create output file
        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(personalized_invitation)
