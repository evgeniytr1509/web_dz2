from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk
from Bot import Bot


class GUIInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Contact Assistant")

        self.contacts_label = Label(self.window, text="Contacts:")
        self.contacts_label.pack()

        self.contacts_treeview = ttk.Treeview(self.window, columns=("name", "phone", "email", "birthday", "note"))
        self.contacts_treeview.heading("name", text="Name")
        self.contacts_treeview.heading("phone", text="Phone")
        self.contacts_treeview.heading("email", text="Email")
        self.contacts_treeview.heading("birthday", text="Birthday")
        self.contacts_treeview.heading("note", text="Note")
        self.contacts_treeview.pack()

        self.add_button = Button(self.window, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.view_button = Button(self.window, text="View Contact", command=self.view_contact)
        self.view_button.pack()

        self.search_button = Button(self.window, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

    def show_commands(self, commands):
        self.commands_label = Label(self.window, text="Commands:")
        self.commands_label.pack()

        for command in commands:
            button = Button(self.window, text=command, command=lambda cmd=command: self.handle_command(cmd))
            button.pack()

    def start(self):
        self.window.mainloop()

    def add_contact(self):
        contact = simpledialog.askstring("Add Contact", "Enter the contact's name:")
        phone = simpledialog.askstring("Add Contact", "Enter the contact's phone number:")
        email = simpledialog.askstring("Add Contact", "Enter the contact's email address:")
        birthday = simpledialog.askstring("Add Contact", "Enter the contact's birthday:")
        note = simpledialog.askstring("Add Contact", "Enter a note for the contact:")

        if contact and phone and email and birthday and note:
            contact_info = (contact, phone, email, birthday, note)
            self.contacts_treeview.insert("", END, values=contact_info)

    def view_contact(self):
        selected_item = self.contacts_treeview.focus()
        if selected_item:
            contact_info = self.contacts_treeview.item(selected_item)["values"]
            contact_details = f"Name: {contact_info[0]}\nPhone: {contact_info[1]}\nEmail: {contact_info[2]}\n" \
                            f"Birthday: {contact_info[3]}\nNote: {contact_info[4]}"
            messagebox.showinfo("Contact Details", contact_details)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter the name to search:")
        if search_term:
            found_items = self.contacts_treeview.get_children()
            for item in found_items:
                item_values = self.contacts_treeview.item(item)["values"]
                if search_term.lower() in item_values[0].lower():
                    self.contacts_treeview.selection_set(item)
                    self.contacts_treeview.focus(item)
                    self.contacts_treeview.see(item)
                    messagebox.showinfo("Search Result", f"Contact '{item_values[0]}' found.")
                    return
            messagebox.showinfo("Search Result", f"No contact found with the name '{search_term}'.")

    def handle_command(self, command):
        # Обработка остальных команд
        pass

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Contact Assistant")

        self.lbl_name = Label(self.window, text="Name:")
        self.lbl_name.pack()
        self.entry_name = Entry(self.window)
        self.entry_name.pack()

        self.lbl_phone = Label(self.window, text="Phone:")
        self.lbl_phone.pack()
        self.entry_phone = Entry(self.window)
        self.entry_phone.pack()

        self.lbl_email = Label(self.window, text="Email:")
        self.lbl_email.pack()
        self.entry_email = Entry(self.window)
        self.entry_email.pack()

        self.lbl_birthday = Label(self.window, text="Birthday:")
        self.lbl_birthday.pack()
        self.entry_birthday = Entry(self.window)
        self.entry_birthday.pack()

        self.lbl_notes = Label(self.window, text="Notes:")
        self.lbl_notes.pack()
        self.entry_notes = Entry(self.window)
        self.entry_notes.pack()

        self.btn_add = Button(self.window, text="Add Contact", command=self.add_contact)
        self.btn_add.pack()

        self.btn_search = Button(self.window, text="Search Contact", command=self.search_contact)
        self.btn_search.pack()

        self.btn_edit = Button(self.window, text="Edit Contact", command=self.edit_contact)
        self.btn_edit.pack()

        self.contact_list = Listbox(self.window)
        self.contact_list.pack()

        self.window.mainloop()

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        birthday = self.entry_birthday.get()
        notes = self.entry_notes.get()

        # Добавить логику для добавления контакта в базу данных или хранилище данных

        self.contact_list.insert(END, name)  # Добавляем имя контакта в список контактов

        # Очищаем поля ввода
        self.entry_name.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_email.delete(0, END)
        self.entry_birthday.delete(0, END)
        self.entry_notes.delete(0, END)

    def search_contact(self):
        search_name = self.entry_name.get()

        # Добавить логику для поиска контакта в базе данных или хранилище данных

        # Очищаем список контактов
        self.contact_list.delete(0, END)

        # Добавляем найденные контакты в список контактов
        # Здесь предполагается, что найденные контакты хранятся в списке contacts
        contacts = []
        for contact in contacts:
            self.contact_list.insert(END, contact)

        # Очищаем поле ввода
        self.entry_name.delete(0, END)

    def edit_contact(self):
        selected_index = self.contact_list.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No contact selected.")
            return

        # Получаем индекс выбранного контакта из списка контактов
        index = selected_index[0]

        # Получаем данные выбранного контакта из базы данных или хранилища данных

        # Обновляем поля в




if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    #bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']

    interface = GUIInterface()
    interface.show_commands(commands)
    interface.start()