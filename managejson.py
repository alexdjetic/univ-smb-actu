import json


class ManageJson:

    def __init__(self, file: str) -> None:
        self._file: str = file
        self._data: list = []

    def get_data(self) -> None:
        try:
            with open(self._file, "r") as f:
                self._data: list = json.load(f)
        except Exception as e:
            print(e)

    def append(self, commentaire: dict) -> None:
        self.get_data()
        self._data.append(commentaire)

        try:
            with open(self._file, "w") as f:
                #f.write(json.dumps(self._data))
                json.dump(self._data, f)
        except Exception as e:
            print(e)
