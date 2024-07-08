from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
# window.minsize(width=300, height=150)
window.config(padx=20,pady=20)

#input
miles_input = Entry(width=10)
miles_input.grid(column = 1,row= 0)

# miles to km function
def calculate():
    mile = float(miles_input.get())
    km = round(mile * 1.609)
    kilometer_result_label.config(text=f"{km}")

#label
miles = Label(text = "Miles")
miles.grid(column =2 ,row=0)
miles.config(pady=10,padx=10)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column= 0,row=1)

#label
kilometer_result_label = Label(text='0')
kilometer_result_label.grid(column = 1,row=1)
kilometer = Label(text = "Km")
kilometer.grid(column =2 ,row=1)
kilometer.config(padx=10,pady=10)

# button
calculate_button = Button(text="Calculate",command=calculate)
calculate_button.grid(column = 1,row= 2)



window.mainloop()