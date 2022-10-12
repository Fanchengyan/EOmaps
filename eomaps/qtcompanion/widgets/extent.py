from datetime import datetime
from PyQt5 import QtWidgets


class SetExtentToLocation(QtWidgets.QWidget):
    def __init__(self, *args, m=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.m = m

        label = QtWidgets.QLabel("Set map-extent to location:")
        self.inp = QtWidgets.QLineEdit()
        self.inp.returnPressed.connect(self.set_extent)
        self.inp.setToolTip("Query based on 'OpenStreetMap Nominatim' service.")
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.inp)

        self.setLayout(layout)

        self._lastquery = None

    def set_extent(self):
        # make sure that queries have a couple of seconds delay
        # to comply to OpenStreetMap Nominatim Usage Policy
        # (e.g. no more than 1 query per second)
        now = datetime.now()
        if self._lastquery is None:
            self._lastquery = now
        else:
            if (now - self._lastquery).seconds <= 2:
                self.window().statusBar().showMessage("... no fast queries allowed!")
                return

        txt = self.inp.text()
        self.m.set_extent_to_location(txt)
        self.m.redraw()
