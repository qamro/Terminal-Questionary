import questionary


name = questionary.text("Who are you? ").ask()

framework = questionary.select(
    "Which framework do you want a tutorial on? ",
    choices = ["Django", "Flask", "Ruby on Rails", "Fast API"]
).ask()

topics = questionary.checkbox(
    "What should we cover? ",
    choices = ["Deployment", "Authentication", "Database", "REST APIs"]
).ask()

confirmed = questionary.confirm("Submit?").ask()


if confirmed:   # that returns True if you type Yes and False if you type No
    
    print(f"Thanks {name}! You want a {framework} video covering {', '.join(topics)} !")