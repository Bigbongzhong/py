import os

class LibraryItem:
    def __init__(self, item_id, title, author, available=True, borrowed_by=""):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.available = available
        self.borrowed_by = borrowed_by

    def __str__(self):
        status = "✅ In stock" if self.available else f"⛔ Borrowed by {self.borrowed_by}"
        return f"[{self.item_id}] \"{self.title}\" by {self.author} - {status}"

    def to_line(self):
        return f"{self.item_id}|{self.title}|{self.author}|{int(self.available)}|{self.borrowed_by}\n"

    def from_line(line):
        parts = line.strip().split('|')
        return LibraryItem(parts[0], parts[1], parts[2], bool(int(parts[3])), parts[4])


class CatalogManager:
    def __init__(self, storage_file='library_data.txt'):
        self.storage_file = storage_file
        self.inventory = []
        self.load_items()

    def load_items(self):
        if os.path.exists(self.storage_file):
            try:
                f = open(self.storage_file, 'r')
                for line in f:
                    self.inventory.append(LibraryItem.from_line(line))
                f.close()
            except Exception as e:
                print(f"⚠️ Failed to load catalog: {e}")

    def save_items(self):
        try:
            f = open(self.storage_file, 'w')
            for item in self.inventory:
                f.write(item.to_line())
            f.close()
        except Exception as e:
            print(f"⚠️ Could not update storage: {e}")

    def add_item(self, item):
        if any(existing.item_id == item.item_id for existing in self.inventory):
            print("⚠️ Item ID already exists. Choose a unique ID.")
            return
        self.inventory.append(item)
        self.save_items()
        print("📗 New item added to the catalog.")

    def display_all(self):
        if not self.inventory:
            print("📭 Catalog is currently empty.")
            return
        for item in self.inventory:
            print(item)

    def lend_item(self, item_id, user_id):
        for item in self.inventory:
            if item.item_id == item_id:
                if item.available:
                    item.available = False
                    item.borrowed_by = user_id
                    self.save_items()
                    print(f"📤 Issued to: {user_id}")
                else:
                    print(f"⛔ Already borrowed by {item.borrowed_by}")
                return
        print("❌ Item not found.")

    def return_item(self, item_id):
        for item in self.inventory:
            if item.item_id == item_id:
                if not item.available:
                    item.available = True
                    item.borrowed_by = ""
                    self.save_items()
                    print("📥 Item successfully returned.")
                else:
                    print("ℹ️ Item was not on loan.")
                return
        print("❌ Invalid item ID.")

    def list_borrowed(self):
        borrowed = [item for item in self.inventory if not item.available]
        if not borrowed:
            print("📦 All items are currently available.")
        else:
            for item in borrowed:
                print(f"{item} [Borrower ID: {item.borrowed_by}]")

    def remove_item(self, item_id):
        for i, item in enumerate(self.inventory):
            if item.item_id == item_id:
                confirm = input(f"⚠️ Delete '{item.title}'? Type 'confirm': ").lower()
                if confirm == 'confirm':
                    del self.inventory[i]
                    self.save_items()
                    print("🗑️ Item removed.")
                else:
                    print("🚫 Deletion aborted.")
                return
        print("❌ No item matches that ID.")


def launch_menu():
    catalog = CatalogManager()

    print("📘 Welcome to the Simple Library Catalog System")
    while True:
        print("\n🔧 MENU OPTIONS")
        print("1. ➕ Add Item")
        print("2. 📚 View Catalog")
        print("3. 📤 Lend Item")
        print("4. 📥 Return Item")
        print("5. 🔍 View Borrowed Items")
        print("6. 🗑️ Remove Item")
        print("7. ❎ Exit")
        action = input("👉 Select (1–7): ")

        if action == '1':
            item_id = input("🆔 Item ID: ")
            title = input("📖 Title: ")
            author = input("✍️ Author: ")
            catalog.add_item(LibraryItem(item_id, title, author))
        elif action == '2':
            catalog.display_all()
        elif action == '3':
            item_id = input("📤 Enter Item ID to lend: ")
            user_id = input("🪪 Your User ID: ")
            catalog.lend_item(item_id, user_id)
        elif action == '4':
            item_id = input("📥 Enter Item ID to return: ")
            catalog.return_item(item_id)
        elif action == '5':
            catalog.list_borrowed()
        elif action == '6':
            item_id = input("🗑️ Enter Item ID to remove: ")
            catalog.remove_item(item_id)
        elif action == '7':
            catalog.save_items()
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid selection. Try again.")


if __name__ == "__main__":
    launch_menu()
