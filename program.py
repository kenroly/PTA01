from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox, QListWidget, QSplitter
from PyQt6 import uic
import sys
import queue
from custom_widget.CustomListItem import CustomListItemWidget
from custom_widget.CustomDelegate import CustomDelegate
from worker.DatabaseInsertNoteWorker import DatabaseInsertNoteWorker
from worker.DatabaseUpdateDateWorker import DatabaseUpdateDateWorker
from datetime import datetime
import os

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('gui/mainwindow.ui', self)
        
        self.insert_queue = queue.Queue()
        self.insertWorker = DatabaseInsertNoteWorker(self.insert_queue) 
        self.insertWorker.start()
        
        self.update_queue = queue.Queue()
        self.updateWorker = DatabaseUpdateDateWorker(self.update_queue)
        self.updateWorker.start()
        
        self.noteList = self.findChild(QListWidget, 'noteList')
        self.loadNotes()
        
        self.mainSplitter = self.findChild(QSplitter, 'mainSplitter')
        QtCore.QTimer.singleShot(100, self.adjustSplitter)
        
        self.noteList.itemClicked.connect(self.onNoteClicked)
        self.noteTitle.textChanged.connect(self.onNoteContentChanged)
        self.noteContent.textChanged.connect(self.onNoteContentChanged)
        self.addNoteButton.clicked.connect(self.onAddNoteButtonClicked)
        
    def onNoteClicked(self, item):
        self.is_changing = True
        self.noteList.setCurrentItem(item)
        self.resetNoteData()
        self.is_changing = False
        
    def resetNoteData(self):
        self.noteTitle.setText(self.noteList.itemWidget(self.noteList.currentItem()).title)
        self.noteContent.setText(self.noteList.itemWidget(self.noteList.currentItem()).content)
    
    def onNoteContentChanged(self):
        if not self.is_changing:
            new_content = self.noteContent.toPlainText()
            new_title = self.noteTitle.text()
            self.noteList.itemWidget(self.noteList.currentItem()).content = new_content
            self.noteList.itemWidget(self.noteList.currentItem()).title = new_title
            self.noteList.itemWidget(self.noteList.currentItem()).updated_at = 'Just now'
            self.noteList.itemWidget(self.noteList.currentItem()).update()
            
            id = self.noteList.itemWidget(self.noteList.currentItem()).id
            updated_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            self.update_queue.put((id, new_title, new_content, updated_at))
        
    def onAddNoteButtonClicked(self):
        item = QtWidgets.QListWidgetItem(self.noteList)
        self.noteList.addItem(item)
        custom_item_widget = CustomListItemWidget('', '', '', 'Just now')
        custom_item_widget.setStyleSheet("""
            background-color: #F8F2EC;
            border-radius: 5px;
        """)
        self.noteList.setItemWidget(item, custom_item_widget)
        item.setSizeHint(custom_item_widget.sizeHint())
        self.noteList.setCurrentItem(item)
        self.noteTitle.setText('')
        self.noteContent.setText('')
        
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.insert_queue.put((now, now))
    
    def adjustSplitter(self):
        totalWidth = self.mainSplitter.width()
        self.mainSplitter.setSizes([totalWidth // 4, 3 * totalWidth // 4])
    
    def loadNotes(self):
        import sqlite3
        conn = sqlite3.connect('data/notes.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM notes")
        data = c.fetchall()
        conn.close()
        self.noteList.setItemDelegate(CustomDelegate())
        for note in data:
            item = QtWidgets.QListWidgetItem(self.noteList)
            self.noteList.addItem(item)
            custom_item_widget = CustomListItemWidget(note[0], note[1], note[2], note[4])
            custom_item_widget.setStyleSheet("""
                background-color: #F8F2EC;
                border-radius: 5px;
            """)
            self.noteList.setItemWidget(item, custom_item_widget)
            item.setSizeHint(custom_item_widget.sizeHint())
    def closeEvent(self, event):
        self.insertWorker.stop()
        self.updateWorker.stop()

        self.insertWorker.wait()
        self.updateWorker.wait()

        super(Main, self).closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    mainPage = Main()
    mainPage.show()
    
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    
    app.exec()