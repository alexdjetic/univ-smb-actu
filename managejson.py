import json


class ManageJson:
    """Cette class permet d'obtenir des données à partir d'une fichier json mais aussi d'y ajouter dans le fichier json"""
    
    def __init__(self, file: str) -> None:
        self._file: str = file
        self._data: list = []

    def get_data(self) -> None:
        """Cette methode obtient les données du fichier json"""
        try:
            with open(self._file, "r") as f:
                self._data: list = json.load(f)
        except Exception as e:
            print(e)

    def append(self, commentaire: dict) -> None:
        """Cette methode ajoute un commentaire au fichier json"""
        self.get_data()
        self._data.append(commentaire)

        try:
            with open(self._file, "w") as f:
                #f.write(json.dumps(self._data))
                json.dump(self._data, f)
        except Exception as e:
            print(e)
