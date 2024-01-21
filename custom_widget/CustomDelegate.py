from PyQt6 import QtWidgets, QtCore, QtGui

class CustomDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        if option.state & QtWidgets.QStyle.StateFlag.State_MouseOver:
            option.state &= ~QtWidgets.QStyle.StateFlag.State_MouseOver
        if option.state & QtWidgets.QStyle.StateFlag.State_Selected:
            option.state &= ~QtWidgets.QStyle.StateFlag.State_Selected
        rect = QtCore.QRectF(option.rect)
        rect.adjust(5, 5, -5, -5) 

        painter.save()
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing) 
        painter.setBrush(QtGui.QColor("#F8F2EC"))
        painter.setPen(QtCore.Qt.PenStyle.NoPen)

        radius = 10.0 
        painter.drawRoundedRect(rect, radius, radius)

        painter.restore()

        super().paint(painter, option, index)