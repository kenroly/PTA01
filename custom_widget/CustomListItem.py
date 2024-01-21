from PyQt6 import QtWidgets

class CustomListItemWidget(QtWidgets.QWidget):
    def __init__(self, id, title, content, updated_at):
        self.id = id
        self.title = title
        self.content = content
        self.updated_at = updated_at
        super().__init__()
        self.setAutoFillBackground(True)
        
        closeButton = QtWidgets.QPushButton('X')
        closeButton.setFixedSize(20, 20)
        # closeButton.clicked.connect(self.onCloseClicked)

        titleLabel = QtWidgets.QLabel(title)
        contentLabel = QtWidgets.QLabel(' '.join(content.split()[:5]) + '...')
        updatedLabel = QtWidgets.QLabel(updated_at)

        titleFont = titleLabel.font()
        titleFont.setPointSize(titleFont.pointSize() + 4)
        titleFont.setBold(True)
        titleLabel.setFont(titleFont)

        updatedFont = updatedLabel.font()
        updatedFont.setPointSize(updatedFont.pointSize() - 2)
        updatedLabel.setFont(updatedFont)
        updatedLabel.setStyleSheet("color: grey")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(titleLabel)
        layout.addWidget(contentLabel)
        layout.addWidget(updatedLabel)
        self.setLayout(layout)
    
    def update(self):
        self.layout().itemAt(0).widget().setText(self.title)
        self.layout().itemAt(1).widget().setText(' '.join(self.content.split()[:5]) + '...')
        self.layout().itemAt(2).widget().setText(self.updated_at)