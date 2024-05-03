import json


class DataParser:

    def __init__(self, file: str) -> None:
        self._file: str = file
        self._extraction_status: bool = False
        self._data: list = []
        self.extract()

    def extract(self):
        try:
            with open(self._file, "r") as f:
                self._data: list = json.load(f)

                if len(self._data) != 0:
                    self._extraction_status: bool = True
        except Exception as e:
            print(e)

    def extract_key(self, key: str) -> list:
        if self._data[0].get(key, None) is not None:
            return [self._data[i].get(key, None) for i in range(len(self._data))]
        else:
            return None

    def extract_type(self, key: str = "all") -> list:
        if key == "all":
            return self.get_data()

        events: list = []
        for event in self._data:
            if event.get("type", 'NA') == key:
                events.append(event)

        return events

    def get_data(self) -> list:
        return self._data