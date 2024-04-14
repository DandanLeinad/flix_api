import csv
from datetime import datetime
from django.core.management.base import BaseCommand, CommandParser
from actors.models import Actor


class Command(BaseCommand):
    """
    Classe de comando do Django para importar atores de um arquivo CSV.
    """

    # Define a descrição do comando que será exibida
    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "file_name",
            type=str,
            help="Nome do arquivo CSV contendo os atores a serem importados",
        )

    # Define a lógica do comando
    def handle(self, *args, **options):
        file_name = options["file_name"]

        with open(file_name, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                birthday = datetime.strptime(
                    row["birthday"], "%Y-%m-%d"
                ).date()
                nationality = row["nationality"]

                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS("Atores importados com sucesso!"))
