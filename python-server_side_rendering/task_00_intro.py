import os

def generate_invitations(template, attendees):
    try:
        # Check Input Types
        if not isinstance(template, str):
            print("Error: template should be a string.")
            return

        if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
            print("Error: attendees should be a list of dictionaries.")
            return

        # Handle Empty Inputs
        if not template.strip():
            print("Template is empty, no output files generated.")
            return

        if not attendees:
            print("No data provided, no output files generated.")
            return

        # Process Each Attendee
        for index, attendee in enumerate(attendees, start=1):
            content = template
            for key in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(key)
                if value is None:
                    value = "N/A"
                content = content.replace("{" + key + "}", str(value))
            
            output_filename = f"output_{index}.txt"
            
            # Check if file exists before writing
            if not os.path.exists(output_filename):
                with open(output_filename, 'w') as file:
                    file.write(content)
            else:
                pass

    except Exception as e:
        print(f"An error occurred: {e}")
