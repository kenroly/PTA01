from PyQt6 import QtCore
import sqlite3
import logging
from queue import Empty

class DatabaseUpdateDateWorker(QtCore.QThread):
    def __init__(self, update_queue):
        super().__init__()
        self.update_queue = update_queue
        self.running = True

    def run(self):
        conn = sqlite3.connect('data/notes.sqlite')
        try:
            while self.running:
                try:
                    # Block until an item is available
                    note_id, new_title, new_content, updated_at = self.update_queue.get()
                    c = conn.cursor()
                    c.execute("""
                            UPDATE notes 
                            SET
                                title = ?,
                                content = ?,
                                updated_at = ?
                            WHERE id = ?
                            """, (new_title, new_content, updated_at, note_id))
                    conn.commit()
                    self.update_queue.task_done()
                except Empty:
                    continue
                except Exception as e:
                    logging.error("Error in database operation: " + str(e))
        finally:
            conn.close()

    def stop(self):
        self.running = False
        self.update_queue.put((None, None, None))
