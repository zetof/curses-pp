class Widget():

    def __init__(self, label, line, col):
        self._line = line
        self._col = col
        self._get_key(label)

    def _get_key(self, label):
        self._label = []
        star = label.find('*')
        self._label.append(label[:star])
        self._label.append(label[star + 2:])
        self._key = label[star + 1]

    def get_key(self):
        return self._key
