import customtkinter as ctk
import requests

API_KEY = "54ecf86d"
OMDB_URL = "http://www.omdbapi.com/" 

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("OMDb Finder")
app.geometry("500x350")

def search():
    name = entry.get()
    url = f"{OMDB_URL}?t={name}&apikey={API_KEY}"
    
    try:
        data = requests.get(url, timeout=5).json()

        if data.get('Response') == 'True':
            result.configure(text=f"Filmul: {data['Title']}", text_color="green")
            title.configure(text=f"Titlu: {data.get('Title', '-')}")
            year.configure(text=f"Anul: {data.get('Year', '-')}")
            actors.configure(text=f"Actori: {data.get('Actors', '-')}")
            plot.configure(text=f"Sinopsis: {data.get('Plot', '-')}")
        else:
            result.configure(text=f"Eroare: Filmul nu a fost găsit!", text_color="red")
            for lbl in [title, year, actors, plot]: lbl.configure(text="-")

    except requests.exceptions.RequestException as e:
        result.configure(text=f"Eroare conexiune: {e}", text_color="red")
        
ctk.CTkLabel(app, text="Nume film:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=(15, 5), sticky="w")
entry = ctk.CTkEntry(app, width=250, placeholder_text="Ex: The Matrix")
entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")
ctk.CTkButton(app, text="Căutare", command=search).grid(row=1, column=1, padx=10, pady=5, sticky="w")

result = ctk.CTkLabel(app, text="Așteptare...", font=("Arial", 16, "bold"), text_color="white")
result.grid(row=2, column=0, columnspan=2, padx=10, pady=(15, 10), sticky="w")

title = ctk.CTkLabel(app, text="Titlu: -", wraplength=450, justify="left")
title.grid(row=3, column=0, columnspan=2, padx=10, pady=3, sticky="w")

year = ctk.CTkLabel(app, text="Anul: -")
year.grid(row=4, column=0, columnspan=2, padx=10, pady=3, sticky="w")

actors = ctk.CTkLabel(app, text="Actori: -", wraplength=450, justify="left")
actors.grid(row=5, column=0, columnspan=2, padx=10, pady=3, sticky="w")

plot = ctk.CTkLabel(app, text="Sinopsis: -", wraplength=450, justify="left")
plot.grid(row=6, column=0, columnspan=2, padx=10, pady=3, sticky="w")


app.mainloop()
