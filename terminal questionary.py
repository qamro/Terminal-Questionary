import questionary


name = questionary.text("Who are you? ").ask()

password = questionary.password("Enter your password :").ask()

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
    
    
# NOTE: "separator".join(iterable) combines the elements of an iterable into one string, using the separator between each element.
# this print(', '.join(topics)) prints for example: Deployment, Database, REST APIs  