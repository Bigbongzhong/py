import pandas as pd
import os

class Book:
    def __init__(self, id, name, writer, is_available=True, holder=""):
        self.id = id
        self.name = name
        self.writer = writer
        self.is_available = is_available
        self.holder = holder

    def __str__(self):
        status = "Available ✅" if self.is_available else f"Taken by {self.holder}"
        return f"[{self.id}] '{self.name}' by {self.writer} - {status}"

class LibrarySystem:
    def __init__(self, data_file='library_data.xlsx'):
        self.data_file = data_file
        self.collection = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                df = pd.read_excel(self.data_file, engine='openpyxl').fillna("")
                expected_cols = {'BookID', 'Title', 'Author', 'Status', 'HolderID'}
                if not expected_cols.issubset(df.columns):
                    print("❌ File format incorrect. Starting fresh.")
                    return

                for _, row in df.iterrows():
                    self.collection.append(Book(
                        str(row['BookID']),
                        row['Title'],
                        row['Author'],
                        bool(row['Status']),
                        str(row['HolderID'])
                    ))
            except Exception as error:
                print(f"⚠️ Couldn't load data: {error}")

    def save_data(self):
        records = {
            'BookID': [book.id for book in self.collection],
            'Title': [book.name for book in self.collection],
            'Author': [book.writer for book in self.collection],
            'Status': [book.is_available for book in self.collection],
            'HolderID': [book.holder for book in self.collection]
        }
        df = pd.DataFrame(records)
        try:
            df.to_excel(self.data_file, index=False, engine='openpyxl')
        except Exception as error:
            print(f"⚠️ Couldn't save data: {error}")

    def add_new_book(self, book):
        self.collection.append(book)
        self.save_data()
        print("📚 Book has been added to the collection!")

    def list_all_books(self):
        if not self.collection:
            print("📭 No books found.")
            return
        for book in self.collection:
            print(book)

    def issue_book(self, book_id, sap_id):
        for book in self.collection:
            if book.id == book_id:
                if book.is_available:
                    book.is_available = False
                    book.holder = sap_id
                    self.save_data()
                    print(f"✅ Book issued to SAP ID: {sap_id}")
                else:
                    print("⛔ Book is already checked out.")
                return
        print("❌ Book ID not found.")

    def return_book(self, book_id):
        for book in self.collection:
            if book.id == book_id:
                if not book.is_available:
                    book.is_available = True
                    book.holder = ""
                    self.save_data()
                    print("✅ Book returned successfully.")
                else:
                    print("ℹ️ This book wasn't borrowed.")
                return
        print("❌ Book ID not found.")

    def borrowed_books(self):
        found = False
        for book in self.collection:
            if not book.is_available:
                print(f"{book} [Holder: {book.holder}]")
                found = True
        if not found:
            print("📦 All books are currently available.")
            
    def delete_book(self, book_id):
        for i, book in enumerate(self.collection):
            if book.id == book_id:
                confirm = input(f"⚠️ Are you sure you want to delete '{book.name}'? (yes/no): ").lower()
                if confirm == 'yes':
                    del self.collection[i]
                    self.save_data()
                    print("🗑️ Book successfully deleted.")
                else:
                    print("❎ Deletion cancelled.")
                return
        print("❌ Book ID not found.")


def run():
    system = LibrarySystem("library_data.xlsx")


    print("📘 Welcome to the Smart Library Management System")
    while True:
        print("\n🛠️ OPTIONS MENU")
        print("1. ➕ Add Book")
        print("2. 📚 Show All Books")
        print("3. 📤 Issue Book")
        print("4. 📥 Return Book")
        print("5. 🔎 Show Borrowed Books")
        print("6. 🗑️ Delete a Book")
        print("7. ❎ Exit")
        task = input("👉 Choose (1-6): ")

        if task == '1':
            bid = input("🔢 Book ID: ")
            
            title = input("📖 Title: ")
            
            author = input("✍️ Author: ")
            
            system.add_new_book(Book(bid, title, author))
        elif task == '2':
            
            system.list_all_books()
        elif task == '3':
            
            bid = input("📤 Enter Book ID to issue: ")
            sid = input("🪪 Enter your SAP ID: ")
            system.issue_book(bid, sid)
        elif task == '4':
            
            bid = input("📥 Enter Book ID to return: ")
            system.return_book(bid)
        elif task == '5':
            
            system.borrowed_books()
        elif task == '6':
            bid = input("🔎 Enter Book ID to delete: ")
            system.delete_book(bid)
        elif task == '7':
            
            print("👋 Exiting system. Catch you later!")
            break
        else:
            print("⚠️ Invalid input. Please try again.")

if __name__ == "__main__":
    
    run()
