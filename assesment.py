#importing the necessary librarys for this code to function
import tkinter
from tkinter import ttk
from tkinter import messagebox, simpledialog

#these lines of codes are the commands
def enter_data():
    #information that was submitted being used for displaying submission
    reservation_name = reservation_name_entry.get()
    title = title_combobox.get()
    num_people = people_spinbox.get()
    time = time_spinbox.get()
    am_pm = AMORPM_combobox.get()

    #if any parts aren't submitted this line checks it and shows a warning
    if not all([reservation_name, title, num_people, time, am_pm]):
        messagebox.showwarning("Incomplete Form", "Please fill in all reservation fields!")
        return

    #grabs all selected items from the listbox
    try:
        selected_indices = menu_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Selection Missing", "Please select a food item from the menu first!")
            return
        selected_items = [menu_listbox.get(i) for i in selected_indices]
    except IndexError:
        messagebox.showwarning("Selection Missing", "Please select a food item from the menu first!")
        return

    # Ask for quantity for each selected item
    order_items = []    

    for item in selected_items:
        quantity = simpledialog.askinteger(
            "Quantity",
            f"How many {item} would you like?",
            minvalue=1,
            parent=window
        )

        if quantity is None:
            return

        order_items.append({
            "item": item,
            "quantity": quantity
        })

    # Format order items with numbering and quantity
    orders_text = "\n".join(
        [f"  {i+1}. {order['item']} x {order['quantity']}" for i, order in enumerate(order_items)]
    )

    #making the code grammatically correct
    food_label = "Foods Ordered" if len(selected_items) > 1 else "Food Ordered"

    #this line of code is it preparing the display of the listed items
    confirmation = (
        f"RESERVATION CONFIRMATION\n"
        f"{'='*39}\n"
        f"Reservation Name: {reservation_name}\n"
        f"Title: {title}\n"
        f"Number of People: {num_people}\n"
        f"Reservation Time: {time} {am_pm}\n"
        f"{'='*39}\n"
        f"{food_label}\n"
        f"{'='*39}\n"
        f"{orders_text}\n"
        f"{'='*39}"
    )
    messagebox.showinfo("Order Confirmation", confirmation)

    # Return data as a dictionary for further processing
    reservation_data = {
        "name": reservation_name,
        "title": title,
        "people": num_people,
        "time": time,
        "am_pm": am_pm,
        "orders": order_items
    }
    return reservation_data





#window for the code
window = tkinter.Tk()
window.title("menu entering website")
frame = tkinter.Frame(window)
frame.pack()

# saving the users info
user_info_frame =tkinter.LabelFrame(frame, text="user information")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

#reservations
reservation_name_label = tkinter.Label(user_info_frame, text="name for reservation")
reservation_name_label.grid(row=0, column=0)
reservation_name_entry = tkinter.Entry(user_info_frame)
reservation_name_entry.grid(row=1, column=0)

#the persons title e.g sir or mr
title_label = tkinter.Label(user_info_frame,text="title")
title_combobox = ttk.Combobox(user_info_frame, values=["Pr","Mr","Ms","Dr"])
title_combobox.grid(row=1, column=1)
title_label.grid(row=0, column=1)

#the amount of people with them
people_label= tkinter.Label(user_info_frame, text= "people")
people_spinbox= tkinter.Spinbox(user_info_frame, from_= 0, to= 60)
people_label.grid(row=2,column=0)
people_spinbox.grid(row=3, column=0)

#time of reservation
time_label = tkinter.Label(user_info_frame, text="Time of Reservation")
time_spinbox = tkinter.Spinbox(user_info_frame, from_=1, to=12, width=5)
amorpm_label = tkinter.Label(user_info_frame, text="AM / PM")
AMORPM_combobox = ttk.Combobox(user_info_frame, values=["AM", "PM"])
AMORPM_combobox.grid(row=2, column=2)
amorpm_label.grid(row=3, column=2)
time_label.grid(row=2,column=1)
time_spinbox.grid(row=3, column=1)


#setting up padding for info above/ user info frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10 ,pady=5)

#start of corse frame
corse_frame = tkinter.LabelFrame(frame) 
corse_frame.grid(row=1,column=0,sticky="nesw", padx=20, pady=20)

# Add a label
label = tkinter.Label(corse_frame, text="Online Ordering Menu", font=("Arial", 14, "bold"), pady=10)
label.grid(row=0,column=0)

# Create the Listbox 
menu_listbox = tkinter.Listbox(corse_frame, font=("Arial", 11), selectmode=tkinter.MULTIPLE, width=50, height=6)
menu_listbox.grid(row=1,column=0)

#these are the list of items 
menu_items = [
"Classic Beef Burger — $18.00",
"Double Cheeseburger — $22.00",
"Bacon Cheeseburger — $21.00",
"BBQ Beef Burger — $20.00",
"Spicy Chicken Burger — $19.00",
"Crispy Chicken Burger — $19.00",
"Margherita Pizza — $18.00",
"Pepperoni Pizza — $21.00",
"Hawaiian Pizza — $21.00",
"BBQ Chicken Pizza — $23.00",
"Meat Lovers Pizza — $24.00",
"Four Cheese Pizza — $23.00",
"Supreme Pizza — $25.00",
"Chicken & Bacon Pizza — $24.00",
"Spicy Beef Pizza — $23.00",
"Grilled Sirloin Steak — $32.00",
"Ribeye Steak — $38.00",
"Scotch Fillet — $36.00",
"Steak & Chips — $34.00",
"Peppercorn Steak — $36.00",
"Garlic Butter Steak — $37.00",
"Grilled Beef Skewers — $25.00",
"BBQ Beef Ribs — $32.00",
"Mixed Grill — $39.00",
"Grilled Lamb Chops — $35.00",
"Spaghetti Bolognese — $21.00",
"Spaghetti Carbonara — $22.00",
"Chicken Alfredo — $23.00",
"Beef Lasagne — $22.00",
"Chicken Pesto Pasta — $23.00",
"Seafood Pasta — $27.00",
"Garlic Prawn Pasta — $26.00",
"Vegetable Pasta — $20.00",
"Beef & Mushroom Pasta — $24.00",
"Spicy Chicken Pasta — $23.00",
"Macaroni & Cheese — $18.00",
"Four Cheese Pasta — $22.00",
"Regular Chips — $7.00",
"Loaded Fries — $12.00",
"Garlic Bread — $8.00",
"Potato Wedges — $9.00",
"Garden Salad — $9.00",
"Caesar Salad — $12.00",
"Steamed Vegetables — $8.00",
"Mac & Cheese — $10.00",
"Big Breakfast — $24.00",
"Bacon & Eggs — $16.00",
"Sausage & Eggs — $17.00",
"Eggs Benedict — $19.00",
"Scrambled Eggs on Toast — $15.00",
"Avocado Toast — $16.00",
"Breakfast Burger — $18.00",
"Pancakes — $15.00",
"French Toast — $16.00",
"Belgian Waffles — $17.00",
"Breakfast Burrito — $18.00",
"Hash Browns — $7.00",
"Chocolate Brownie — $10.00",
"Chocolate Cake — $11.00",
"Cheesecake — $12.00",
"New York Cheesecake — $13.00",
"Apple Crumble — $11.00",
"Sticky Date Pudding — $12.00",
"Chocolate Lava Cake — $13.00",
"Banana Split — $14.00",
"Chocolate Sundae — $12.00",
"Vanilla Ice Cream — $8.00",
"Chocolate Ice Cream — $8.00",
"Strawberry Ice Cream — $8.00",
"Churros — $10.00",
"Brownie & Ice Cream — $14.00",
"Coca-Cola — $5.00",
"Coca-Cola Zero — $5.00",
"Sprite — $5.00",
"Fanta — $5.00",
"Ginger Beer — $6.00",
"Sparkling Water — $5.00",
"Still Water — $4.00",
"Orange Juice — $7.00",
"Apple Juice — $7.00",
"Pineapple Juice — $7.00",
"Fresh Lemonade — $8.00",
"Iced Tea — $7.00",
"Milkshake — $10.00",
"Chocolate Milkshake — $11.00",
"Strawberry Milkshake — $11.00",
"Vanilla Milkshake — $11.00",
]

#the end of menu code
for item in menu_items:
    menu_listbox.insert(tkinter .END, item)

#padding for next group of code above/corse frame
for widget in corse_frame.winfo_children():
    widget.grid_configure(padx=10 ,pady=5)  

#button to enter data
button = tkinter.Button(frame,text= "amounts",command= enter_data)
button.grid(row=3,column=0, sticky="news",padx=20, pady=20)


window.mainloop()