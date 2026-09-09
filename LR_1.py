from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich import print as rprint
from rich.console import Console
from rich.table import Table

# Приймає дані від користувача з терміналу
variant = IntPrompt.ask("Введіть варіант")
first_name = Text(Prompt.ask("Введіть ім'я"), style="bold green")
last_name = Text(Prompt.ask("Введіть прізвище"), style="bold #005fff")
group = Text(Prompt.ask("Введіть групу", choices=["КБ-106", "КБ-107", "КБ-108"],
                        case_sensitive=False), style="bold #d787ff")
variant = Text(f"{variant}", style="bold #d787ff")

# Виводить інформацію в термінал
rprint(first_name)
rprint(last_name)
rprint(group)
rprint(variant)

#Створює заповнену таблицю з даними про студента
console = Console()
text = Text("Інформація про студента", style="bold bright_red")
table = Table(title=text, header_style="bold bright_green")
table.add_column("Ім'я ", style="bold green", justify="right", no_wrap=True)
table.add_column("Прізвище ", style="bold #005fff", justify="right")
table.add_column("Група", justify="right", style="bold #d787ff")
table.add_column("Варіант", justify="right", style="bold #d787ff")
table.add_row(first_name, last_name, group, f"{variant}")
console.print(table)
