import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

#rumus BMI
    def calculate_bmi(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return bmi

#saran bedasarkan hasil BMI di output
    def get_advice(self, bmi):
        if bmi < 18.5:
            advice = "Berat badan Anda kurang. Disarankan untuk menambah berat badan."
        elif 18.5 <= bmi <= 24.9:
            advice = "Berat badan Anda optimal. Disarankan untuk menjaga kestabilan berat badan."
        elif 25 <= bmi <= 29.9:
            advice = "Berat badan Anda berlebih. Disarankan untuk menurunkan berat badan."
        else:
            advice = "Anda mengalami obesitas. Disarankan untuk berkonsultasi dengan dokter."
        return advice

class BMIApp:
    def __init__(self):
        self.bmi_stack = []
        self.bmi_queue = []
        self.tips_button_shown = False
        self.tips_text = ""

#login
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "faisal" and password == "gg":
            self.login_window.destroy()
            self.open_main_ui()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

#main ui kalkulator
    def open_main_ui(self):
        self.main_window = tk.Tk()
        self.main_window.title("BMI (Body Mass Indeks) Calculator")
        self.main_window.geometry("300x200")

        weight_label = tk.Label(self.main_window, text="Berat Badan (kg):")
        weight_label.pack()
        self.weight_entry = tk.Entry(self.main_window)
        self.weight_entry.pack()

        height_label = tk.Label(self.main_window, text="Tinggi Badan (cm):")
        height_label.pack()
        self.height_entry = tk.Entry(self.main_window)
        self.height_entry.pack()

        age_label = tk.Label(self.main_window, text="Umur (tahun):")
        age_label.pack()
        self.age_entry = tk.Entry(self.main_window)
        self.age_entry.pack()

        calculate_button = tk.Button(self.main_window, text="Hitung BMI", command=self.calculate_bmi)
        calculate_button.pack()
        
        history_button = tk.Button(self.main_window, text="Riwayat", command=self.show_history_stack)
        history_button.pack()

        self.main_window.protocol("WM_DELETE_WINDOW", self.close_app)

        self.main_window.mainloop()

#output kalkulator bmi
    def calculate_bmi(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get())
        age = int(self.age_entry.get())

        bmi_calculator = BMICalculator(weight, height, age)
        bmi = bmi_calculator.calculate_bmi()
        advice = bmi_calculator.get_advice(bmi)

        self.bmi_stack.append((weight, height, age, bmi, advice))
        self.bmi_queue.append((weight, height, age, bmi, advice))

        result_message = f"BMI Anda: {bmi:.2f}\n\n{advice}]"
        messagebox.showinfo("Hasil BMI", result_message)

#buat menu tips
        def show_tips():
            tips_window = tk.Toplevel()
            tips_window.title("Tips")
            tips_window.geometry("700x200")

            if "kurang" in advice:
                tip1_label = tk.Label(tips_window, text="Pilih Jenis Makanan Yang Padat Gizi", font=("Arial", 12, "bold"))
                tip1_label.pack()

                tip1_description = tk.Label(tips_window, text="Anda bisa mengonsumsi makanan seperti roti gandum utuh dengan sayuran, daging rendah lemak, buah-buahan, serta kacang-kacangan.",
                                            font=("Arial", 10))
                tip1_description.pack()

                tip2_label = tk.Label(tips_window, text="Makan Sebelum Tidur", font=("Arial", 12, "bold"))
                tip2_label.pack()

                tip2_description = tk.Label(tips_window, text="Makan sebelum tidur dapat menambah berat badan karena metabolisme tubuh melambat saat tidur. Hal ini memungkinkan kalori yang masuk disimpan oleh tubuh sebagai lemak. Namun, cara ini mungkin tidak cocok bila Anda menderita GERD.",
                                            font=("Arial", 10))
                tip2_description.pack()

            elif "optimal" in advice:
                tip_label = tk.Label(tips_window, text="Jaga Pola Makan dan Aktivitas Fisik", font=("Arial", 12, "bold"))
                tip_label.pack()

                tip_description = tk.Label(tips_window, text="Pola makan seimbang dan rutin berolahraga dapat membantu menjaga kestabilan berat badan.",
                                    font=("Arial", 10))
                tip_description.pack()

            elif "berlebih" in advice:
                tip1_label = tk.Label(tips_window, text="Kurangi Asupan Makanan Tinggi Lemak dan Gula", font=("Arial", 12, "bold"))
                tip1_label.pack()

                tip1_description = tk.Label(tips_window, text="Hindari makanan yang tinggi lemak dan gula seperti makanan cepat saji, minuman bersoda, dan makanan manis.",
                                            font=("Arial", 10))
                tip1_description.pack()

                tip2_label = tk.Label(tips_window, text="Rutin Berolahraga", font=("Arial", 12, "bold"))
                tip2_label.pack()

                tip2_description = tk.Label(tips_window, text="Olahraga teratur dapat membantu membakar kalori berlebih dan menurunkan berat badan.",
                                            font=("Arial", 10))
                tip2_description.pack()

            elif "obesitas" in advice:
                tip_label = tk.Label(tips_window, text="Konsultasikan dengan Dokter", font=("Arial", 12, "bold"))
                tip_label.pack()

                tip_description = tk.Label(tips_window, text="Segera konsultasikan dengan dokter untuk tindakan lebih lanjut dalam mengelola berat badan Anda.",
                                    font=("Arial", 10))
                tip_description.pack()

# Menampilkan messagebox dengan pilihan "Iya" dan "Tidak"
        user_choice = messagebox.askquestion("Butuh Tips?", "Apakah Anda butuh tips?")
        if user_choice == "yes" and not self.tips_button_shown:
            self.tips_button_shown = True
            tips_button = tk.Button(self.main_window, text="Butuh Tips?", command=show_tips)
            tips_button.pack()
        elif user_choice == "no":
            self.close_app
            self. n

    def close_app(self):
        self.main_window.destroy()

#riwayat penggunaan kalkulator bmi
    def show_history_stack(self):
        history_window = tk.Toplevel()
        history_window.title("History")
        history_window.geometry("900x200")

        history_label = tk.Label(history_window, text="Riwayat")
        history_label.pack()

        for data in reversed(self.bmi_stack):
            weight, height, age, bmi, advice = data
            history_entry = tk.Label(history_window, text=f"Berat Badan: {weight} kg | Tinggi Badan: {height} cm | Umur: {age} tahun | BMI: {bmi:.2f} | Saran: {advice}")
            history_entry.pack()

# gui login page
login_app = BMIApp()

login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("300x150")

username_label = tk.Label(login_window, text="Username:")
username_label.pack()
login_app.username_entry = tk.Entry(login_window)
login_app.username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
login_app.password_entry = tk.Entry(login_window, show="*")
login_app.password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login_app.login)
login_button.pack()

login_app.login_window = login_window  

login_window.mainloop()
