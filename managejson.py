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
        except FileNotFoundError:
            self._data = []
        except json.JSONDecodeError:
            self._data = []

    def append(self, commentaire: dict) -> None:
        """Cette methode ajoute un commentaire au fichier json"""
        self.get_data()
        self._data.append(commentaire)

        try:
            with open(self._file, "w") as f:
                json.dump(self._data, f, indent=4)
        except Exception as e:
            print(e)

    def delete_ligne(self, id: int) -> bool:
        """Cette methode supprime une donnée du fichier json"""
        tmp: list[dict] = []
        self.get_data()

        for ligne in self._data:
            if ligne.get("id", "not valid value") != id:
                tmp.append(ligne)

        self.append(data=tmp)
        return tmp != self._data


    def delete_ligne(self, id: int) -> bool:
        """Cette méthode supprime une donnée du fichier JSON avec le numéro de d'identifiant"""
        self.get_data() 
        origin_size = len(self._data)
        tmp: list[dict] = []

        for ligne in self._data:
            if ligne.get("id", "not valid value") != id:
                tmp.append(ligne)

        if len(tmp) < origin_size:  # Vérifie que la taille de tmp est inférieure
            try:
                with open(self._file, "w") as f:
                    json.dump(tmp, f, indent=4)

                self._data = tmp 
                return True
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'écriture du fichier: {e}")
                return False

        return False

