from tkinter import *
from tkinter import ttk
import sqlite3

admin_username = "admin123"
admin_password = "admin123"

root = Tk()
root.geometry("750x400")
root.title("Employee Management")

# con = sqlite3.connect("Management.db")
# c = con.cursor()
# c.execute("""CREATE TABLE employees (
#         first_name text,
#         last_name text,
#         cnic integer,
#         age integer,
#         salary integer,
#         post text
#
# )""")
# con.commit()
# con.close()

frame_admin = LabelFrame(root, text="Admin login", font=("Arial", 28), padx=10, pady=10, border=1, relief="sunken")
frame_admin.pack(padx=10, pady=10)

label_login_u = Label(frame_admin, text="Username", font=("Arial", 28))
label_login_u.grid(row=1, column=0)
label_login_p = Label(frame_admin, text="Password", font=("Arial", 28))
label_login_p.grid(row=2, column=0)

entry_login_u = Entry(frame_admin, borderwidth=5, width=35, font=("Arial", 16))
entry_login_u.grid(row=1, column=1, padx=20, pady=20, ipady=4)
entry_login_p = Entry(frame_admin, borderwidth=5, width=35, font=("Arial", 16))
entry_login_p.grid(row=2, column=1, padx=20, pady=20, ipady=4)

u_e_f_name = Entry()
u_e_l_name = Entry()
u_e_cnic = Entry()
u_e_age = Entry()
u_e_salary = Entry()
u_e_post = Entry()
e_update = Entry()


def submit():
    root_admin_choice = Tk()
    root_admin_choice.geometry("400x500")
    root_admin_choice.title("Employee Management")

    def add_emp():
        root_admin_choice.destroy()
        root_add_emp = Tk()
        root_add_emp.geometry("540x580")
        root_add_emp.title("Employee Management")

        add_f_name = Label(root_add_emp, text="First Name", font=("Arial", 16))
        add_f_name.grid(row=0, column=0, sticky=W)
        add_l_name = Label(root_add_emp, text="Last Name", font=("Arial", 16))
        add_l_name.grid(row=1, column=0, sticky=W)
        add_cnic = Label(root_add_emp, text="CNIC no", font=("Arial", 16))
        add_cnic.grid(row=2, column=0, sticky=W)
        add_age = Label(root_add_emp, text="Age", font=("Arial", 16))
        add_age.grid(row=3, column=0, sticky=W)
        add_salary = Label(root_add_emp, text="Salary", font=("Arial", 16))
        add_salary.grid(row=4, column=0, sticky=W)
        add_post = Label(root_add_emp, text="Post", font=("Arial", 16))
        add_post.grid(row=5, column=0, sticky=W)

        entry_f_name = Entry(root_add_emp, borderwidth=5, width=35, font=("Arial", 12))
        entry_f_name.grid(row=0, column=1, padx=20, pady=20, ipady=4)
        entry_l_name = Entry(root_add_emp, borderwidth=5, width=35, font=("Arial", 12))
        entry_l_name.grid(row=1, column=1, padx=20, pady=20, ipady=4)
        entry_cnic = Entry(root_add_emp, borderwidth=5, width=35, font=("Arial", 12))
        entry_cnic.grid(row=2, column=1, padx=20, pady=20, ipady=4)
        entry_age = Entry(root_add_emp, borderwidth=5, width=35, font=("Arial", 12))
        entry_age.grid(row=3, column=1, padx=20, pady=20, ipady=4)
        entry_salary = Entry(root_add_emp, borderwidth=5, width=35, font=("Arial", 12))
        entry_salary.grid(row=4, column=1, padx=20, pady=20, ipady=4)
        entry_post = Entry(root_add_emp, borderwidth=5, width=35, font=("Arial", 12))
        entry_post.grid(row=5, column=1, padx=20, pady=20, ipady=4)

        def submit_s():
            conn = sqlite3.connect("Management.db")
            c = conn.cursor()
            c.execute("INSERT INTO employees VALUES (:f_name, :l_name, :cnic, :age, :salary, :post)",
            {
                'f_name': entry_f_name.get(),
                'l_name': entry_l_name.get(),
                'cnic': entry_cnic.get(),
                'age': entry_age.get(),
                'salary': entry_salary.get(),
                'post': entry_post.get()
            })

            conn.commit()
            conn.close()

            submit()
            root_add_emp.destroy()

        add_submit = Button(root_add_emp, text="Submit", padx=35, pady=10, font=("Arial", 20), bg="#62b3a9",
                            command=submit_s)
        add_submit.grid(row=6, column=1, padx=75, pady=10)

    def remove_emp():
        root_admin_choice.destroy()
        root_remove_emp = Tk()
        root_remove_emp.geometry("400x400")
        root_remove_emp.title("Employee Management")

        main_frame = Frame(root_remove_emp)
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM employees")
        records = c.fetchall()

        print_record = ""
        num = len(records)
        for i in range(num):
            for j in range(len(records[i])):
                if (j + 1) % 7 == 0:
                    print_record += "ID:   " + str(records[i][j]) + "\n\n"
                elif j == 0:
                    print_record += "First name:   " + str(records[i][j]) + "\n"
                elif j == 1:
                    print_record += "Last name:   " + str(records[i][j]) + "\n"
                elif j == 2:
                    print_record += "CNIC no:   " + str(records[i][j]) + "\n"
                elif j == 3:
                    print_record += "Age:   " + str(records[i][j]) + "\n"
                elif j == 4:
                    print_record += "Salary:   " + str(records[i][j]) + " Rs" + "\n"
                elif j == 5:
                    print_record += "Post:   " + str(records[i][j]) + "\n"

        label_record = Label(second_frame, text=print_record, font=("Arial", 12))
        label_record.grid(row=2, columnspan=2)

        def rem_button():
            id_rem = id_e_rem.get()
            connr = sqlite3.connect("Management.db")
            cr = connr.cursor()
            cr.execute(f"DELETE from employees WHERE rowid ={id_rem}")
            connr.commit()
            connr.close()
            id_e_rem.delete(0, END)
            root_remove_emp.destroy()

        label_rem = Label(second_frame, text="ID", font=("Arial", 16))
        label_rem.grid(row=0, column=0, sticky=W)
        id_e_rem = Entry(second_frame, borderwidth=5, width=35, font=("Arial", 12))
        id_e_rem.grid(row=0, column=1, padx=20, pady=20, ipady=4)
        button_rem = Button(second_frame, text="Remove", padx=35, pady=10, font=("Arial", 20), bg="#ad4b39",
                            command=rem_button)
        button_rem.grid(row=1, column=1, padx=75, pady=10)

        conn.commit()
        conn.close()

    def update():
        root_admin_choice.destroy()
        root_update = Tk()
        root_update.geometry("540x640")
        root_update.title("Employee Management")

        def edit():
            root_update_real = Tk()
            root_update_real.geometry("540x640")
            root_update_real.title("Employee Management")

            def update_rec():
                connu = sqlite3.connect("Management.db")
                cu = connu.cursor()
                record_id = e_update.get()

                cu.execute("""UPDATE employees SET 
                            first_name = :first,
                            last_name = :last,
                            cnic = :cnic,
                            age = :age,
                            salary = :salary,
                            post = :post

                            WHERE oid = :oid""",
                           {
                            'first': u_e_f_name.get(),
                            'last': u_e_l_name.get(),
                            'cnic': u_e_cnic.get(),
                            'age': u_e_age.get(),
                            'salary': u_e_salary.get(),
                            'post': u_e_post.get(),
                            'oid': record_id
                           })

                connu.commit()
                connu.close()

                u_e_f_name.delete(0, END)
                u_e_l_name.delete(0, END)
                u_e_cnic.delete(0, END)
                u_e_age.delete(0, END)
                u_e_salary.delete(0, END)
                u_e_post.delete(0, END)
                root_update.destroy()
                root_update_real.destroy()
                submit()

            update_f_name = Label(root_update_real, text="First Name", font=("Arial", 16))
            update_f_name.grid(row=0, column=0, sticky=W)
            update_l_name = Label(root_update_real, text="Last Name", font=("Arial", 16))
            update_l_name.grid(row=1, column=0, sticky=W)
            update_cnic = Label(root_update_real, text="CNIC no", font=("Arial", 16))
            update_cnic.grid(row=2, column=0, sticky=W)
            update_age = Label(root_update_real, text="Age", font=("Arial", 16))
            update_age.grid(row=3, column=0, sticky=W)
            update_salary = Label(root_update_real, text="Salary", font=("Arial", 16))
            update_salary.grid(row=4, column=0, sticky=W)
            update_post = Label(root_update_real, text="Post", font=("Arial", 16))
            update_post.grid(row=5, column=0, sticky=W)

            global u_e_f_name
            global u_e_l_name
            global u_e_cnic
            global u_e_age
            global u_e_salary
            global u_e_post

            u_e_f_name = Entry(root_update_real, borderwidth=5, width=35, font=("Arial", 12))
            u_e_f_name.grid(row=0, column=1, padx=20, pady=20, ipady=4)
            u_e_l_name = Entry(root_update_real, borderwidth=5, width=35, font=("Arial", 12))
            u_e_l_name.grid(row=1, column=1, padx=20, pady=20, ipady=4)
            u_e_cnic = Entry(root_update_real, borderwidth=5, width=35, font=("Arial", 12))
            u_e_cnic.grid(row=2, column=1, padx=20, pady=20, ipady=4)
            u_e_age = Entry(root_update_real, borderwidth=5, width=35, font=("Arial", 12))
            u_e_age.grid(row=3, column=1, padx=20, pady=20, ipady=4)
            u_e_salary = Entry(root_update_real, borderwidth=5, width=35, font=("Arial", 12))
            u_e_salary.grid(row=4, column=1, padx=20, pady=20, ipady=4)
            u_e_post = Entry(root_update_real, borderwidth=5, width=35, font=("Arial", 12))
            u_e_post.grid(row=5, column=1, padx=20, pady=20, ipady=4)

            conne = sqlite3.connect("Management.db")
            ce = conne.cursor()
            e_id = e_update.get()
            ce.execute("SELECT * FROM employees WHERE oid=" + e_id)
            recordss = ce.fetchall()
            for record in recordss:
                u_e_f_name.insert(0, record[0])
                u_e_l_name.insert(0, record[1])
                u_e_cnic.insert(0, record[2])
                u_e_age.insert(0, record[3])
                u_e_salary.insert(0, record[4])
                u_e_post.insert(0, record[5])

            conne.commit()
            conne.close()

            add_update_b = Button(root_update_real, text="Submit", padx=35, pady=10, font=("Arial", 20), bg="#62b3a9",
                                  command=update_rec)
            add_update_b.grid(row=6, column=1, padx=75, pady=10)
            # root_update.destroy()

        main_frame = Frame(root_update)
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM employees")
        records = c.fetchall()

        print_record = ""
        num = len(records)
        for i in range(num):
            for j in range(len(records[i])):
                if (j + 1) % 7 == 0:
                    print_record += "ID:   " + str(records[i][j]) + "\n\n"
                elif j == 0:
                    print_record += "First name:   " + str(records[i][j]) + "\n"
                elif j == 1:
                    print_record += "Last name:   " + str(records[i][j]) + "\n"
                elif j == 2:
                    print_record += "CNIC no:   " + str(records[i][j]) + "\n"
                elif j == 3:
                    print_record += "Age:   " + str(records[i][j]) + "\n"
                elif j == 4:
                    print_record += "Salary:   " + str(records[i][j]) + " Rs" + "\n"
                elif j == 5:
                    print_record += "Post:   " + str(records[i][j]) + "\n"

        label_record = Label(second_frame, text=print_record, font=("Arial", 12))
        label_record.grid(row=2, columnspan=2, sticky=W)

        global e_update
        label_update = Label(second_frame, text="ID", font=("Arial", 20))
        label_update.grid(row=0, column=0, sticky=W)
        e_update = Entry(second_frame, borderwidth=5, width=35, font=("Arial", 12))
        e_update.grid(row=0, column=1, padx=20, pady=20, ipady=4)

        add_update = Button(second_frame, text="Submit", padx=35, pady=10, font=("Arial", 20), bg="#62b3a9",
                            command=edit)
        add_update.grid(row=1, column=1, padx=75, pady=10)

    def salary_fun():
        root_admin_choice.destroy()
        root_salaries = Tk()
        root_salaries.geometry("540x400")
        root_salaries.title("Employee Management")

        main_frame = Frame(root_salaries)
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM employees")
        records = c.fetchall()

        print_record = ""
        num = len(records)
        for i in range(num):
            for j in range(len(records[i])):
                if (j + 1) % 7 == 0:
                    print_record += "ID:   " + str(records[i][j]) + "\n\n"
                elif j == 0:
                    print_record += "First name:   " + str(records[i][j]) + "\n"
                elif j == 1:
                    print_record += "Last name:   " + str(records[i][j]) + "\n"
                elif j == 2:
                    print_record += "CNIC no:   " + str(records[i][j]) + "\n"
                elif j == 3:
                    print_record += "Age:   " + str(records[i][j]) + "\n"
                elif j == 4:
                    print_record += "Salary:   " + str(records[i][j]) + " Rs" + "\n"
                elif j == 5:
                    print_record += "Post:   " + str(records[i][j]) + "\n"

        label_record = Label(second_frame, text=print_record, font=("Arial", 12))
        label_record.grid(row=5, columnspan=2, sticky=W)

        def salary_show():
            id_s = s_e_id.get()
            abs_s = s_e_abs.get()
            s_e_id.delete(0, END)
            s_e_abs.delete(0, END)

            id_ori = 0
            salary_ori = 0
            num1 = len(records)
            for ii in range(num1):
                for jj in range(len(records[ii])):
                    if (jj + 1) % 7 == 0:
                        id_ori = records[ii][jj]
                    elif jj == 4:
                        salary_ori = records[ii][jj]
                if int(id_ori) >= int(id_s):
                    break
            salary_pres = int(salary_ori) - (int(abs_s) * 1000)
            salary_label = Label(second_frame, text="Salary:   " + str(salary_pres) + " Rs", font=("Arial", 22),
                                 foreground="red")
            salary_label.grid(row=4, columnspan=2, sticky=W)

        salary_but = Button(second_frame, text="Show", padx=35, pady=10, font=("Arial", 20), bg="#62b3a9",
                            command=salary_show)
        salary_but.grid(row=3, column=1, padx=75, pady=10)
        salary_id = Label(second_frame, text="ID", font=("Arial", 16))
        salary_id.grid(row=1, column=0, sticky=W)
        s_e_id = Entry(second_frame, borderwidth=5, width=35, font=("Arial", 12))
        s_e_id.grid(row=1, column=1, padx=20, pady=20, ipady=4)
        salary_abs = Label(second_frame, text="No of Absents", font=("Arial", 16))
        salary_abs.grid(row=2, column=0, sticky=W)
        s_e_abs = Entry(second_frame, borderwidth=5, width=35, font=("Arial", 12))
        s_e_abs.grid(row=2, column=1, padx=20, pady=20, ipady=4)

        conn.commit()
        conn.close()

        def back_s():
            submit()
            root_salaries.destroy()

        back_b_s = Button(second_frame, text="Back", padx=35, pady=10, font=("Arial", 20), bg="#c4523b",
                          command=back_s)
        back_b_s.grid(row=0, column=1, padx=75, pady=10)

    def record_fun():
        root_admin_choice.destroy()
        root_record = Tk()
        root_record.geometry("400x400")
        root_record.title("Employee Management")

        main_frame = Frame(root_record)
        main_frame.pack(fill=BOTH, expand=1)
        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        second_frame = Frame(my_canvas)
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        conn = sqlite3.connect("Management.db")
        c = conn.cursor()
        c.execute("SELECT *, oid FROM employees")
        records = c.fetchall()

        print_record = ""
        num = len(records)
        for i in range(num):
            for j in range(len(records[i])):
                if (j + 1) % 7 == 0:
                    print_record += "ID:   " + str(records[i][j]) + "\n\n"
                elif j == 0:
                    print_record += "First name:   " + str(records[i][j]) + "\n"
                elif j == 1:
                    print_record += "Last name:   " + str(records[i][j]) + "\n"
                elif j == 2:
                    print_record += "CNIC no:   " + str(records[i][j]) + "\n"
                elif j == 3:
                    print_record += "Age:   " + str(records[i][j]) + "\n"
                elif j == 4:
                    print_record += "Salary:   " + str(records[i][j]) + " Rs" + "\n"
                elif j == 5:
                    print_record += "Post:   " + str(records[i][j]) + "\n"

        label_record = Label(second_frame, text=print_record, font=("Arial", 12))
        label_record.grid(row=1, columnspan=2, sticky=W)

        conn.commit()
        conn.close()

        def back_r():
            submit()
            root_record.destroy()

        back_b_r = Button(second_frame, text="Back", padx=35, pady=10, font=("Arial", 20), bg="#c4523b",
                          command=back_r)
        back_b_r.grid(row=0, column=1, padx=75, pady=10)

    add_emp_b = Button(root_admin_choice, text="Add Employee", padx=35, pady=10, font=("Arial", 20), bg="#62b3a9",
                       command=add_emp)
    add_emp_b.grid(row=0, column=0, padx=75, pady=10)
    add_emp_b = Button(root_admin_choice, text="Remove Employee", padx=10, pady=10, font=("Arial", 20), bg="#62b3a9",
                       command=remove_emp)
    add_emp_b.grid(row=1, column=0, padx=75, pady=10)
    add_emp_b = Button(root_admin_choice, text="Update Record", padx=33, pady=10, font=("Arial", 20), bg="#62b3a9",
                       command=update)
    add_emp_b.grid(row=2, column=0, padx=75, pady=10)
    add_emp_b = Button(root_admin_choice, text="Salaries", padx=75, pady=10, font=("Arial", 20), bg="#62b3a9",
                       command=salary_fun)
    add_emp_b.grid(row=3, column=0, padx=75, pady=10)
    add_emp_b = Button(root_admin_choice, text="Record", padx=80, pady=10, font=("Arial", 20), bg="#62b3a9",
                       command=record_fun)
    add_emp_b.grid(row=4, column=0, padx=75, pady=10)


def login():
    u = entry_login_u.get()
    p = entry_login_p.get()
    if u == admin_username and p == admin_password:
        root.destroy()
        submit()
    else:
        label_again = Label(frame_admin, text="Try Again", foreground="red")
        label_again.grid(row=4, column=1)


login_submit = Button(frame_admin, text="Login", width=20, font=("Arial", 20),  bg="cadetblue2", command=login)
login_submit.grid(row=3, column=1, ipady=4)


root.mainloop()
