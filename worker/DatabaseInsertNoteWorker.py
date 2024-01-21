from PyQt6 import QtCore
import sqlite3
import logging

class DatabaseInsertNoteWorker(QtCore.QThread):
    def __init__(self, insert_queue):
        super().__init__()
        self.insert_queue = insert_queue
        self.running = True
    
    def run(self):
        conn = sqlite3.connect('data/notes.sqlite')
        try:
            while self.running:
                try:
                    created_at, updated_at = self.insert_queue.get()
                    c = conn.cursor()
                    c.execute("""
                            INSERT INTO notes (title, content, created_at, updated_at)
                            VALUES (?, ?, ?, ?)
                            """, ("", "", created_at, updated_at))
                    conn.commit()
                    self.insert_queue.task_done()
                except Exception as e:
                    logging.error("Error in database operation: " + str(e))
        finally:
            conn.close()
    
    def stop(self):
        self.running = False
        self.insert_queue.put((None, None))
