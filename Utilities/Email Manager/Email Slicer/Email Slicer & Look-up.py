
import re
from tkinter import *
from tkinter import filedialog
import pandas as pd
import requests


class EmailSlicer:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Email Slicer")
        self.__root.geometry("500x500")
        self.__emails = []
        self.__results = []
        self.__create_widgets()

    def __create_widgets(self):
        self.__instructions = Label(self.__root, text="Enter email addresses separated by commas:")
        self.__instructions.pack()
        self.__email_entry = Entry(self.__root, width=50)
        self.__email_entry.pack()
        self.__slice_button = Button(self.__root, text="Slice Emails", command=self.__slice)
        self.__slice_button.pack()
        self.__save_button = Button(self.__root, text="Save Results", command=self.__save_results, state=DISABLED)
        self.__save_button.pack()
        self.__results_text = Text(self.__root, width=50, height=10)
        self.__results_text.pack()

    def __validate_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex, email)

    def __lookup_email(self, email):
        # Replace with your own API key and endpoint   #try norbert/hunter email look-up api
        api_key = "YOUR_API_KEY"
        endpoint = f"https://api.emailfinder.io/v1/email?email={email}&api_key={api_key}"
        response = requests.get(endpoint)
        data = response.json()
        if "error" in data:
            return {"Name": "Not Found", "Location": "Not Found"}
        else:
            name = data["name"]
            location = data["location"]
            return {"Name": name, "Location": location}

    def __slice(self):
        emails = list(set(self.__email_entry.get().split(",")))
        result_str = ""
        for email in emails:
            email = email.strip()
            if not self.__validate_email(email):
                self.__results_text.delete("1.0", END)
                self.__results_text.insert(END, f"Invalid email: {email}")
                return
            username, domain = email.split("@")
            extension = domain.split(".")[-1]
            lookup_result = self.__lookup_email(email)
            result = {"Email": email, "Username": username, "Domain": domain, "Extension": extension,
                      "Name": lookup_result["Name"], "Location": lookup_result["Location"]}
            self.__results.append(result)
            result_str += f"Email: {email}\nUsername: {username}\nDomain: {domain}\nExtension: {extension}\nName: {lookup_result['Name']}\nLocation: {lookup_result['Location']}\n\n"
        self.__results_text.delete("1.0", END)
        self.__results_text.insert(END, result_str)
        self.__save_button.config(state=NORMAL)

    def __save_results(self):
        filename = filedialog.asksaveasfilename(defaultextension=".xlsx")
        if filename:
            try:
                df = pd.read_excel(filename)
                new_df = pd.DataFrame(self.__results)
                df = pd.concat([df, new_df]).drop_duplicates(subset=["Email"])
            except FileNotFoundError:
                df = pd.DataFrame(self.__results)
            df.sort_values(by=["Username", "Domain", "Extension"], inplace=True)
            df.to_excel(filename, index=False)
            self.__results_text.delete("1.0", END)
            self.__results_text.insert(END, f"Results saved to {filename}")

    def run(self):
        self.__root.mainloop()


if __name__ == "__main__":
    email_slicer = EmailSlicer()
    email_slicer.run()
