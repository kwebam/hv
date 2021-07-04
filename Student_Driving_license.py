from tkinter import*
root = Tk();
root.title("Driving Licence");
root.geometry("300x400");

root.configure(bg="white");
canvas=Canvas(root,width=400,height=250);
canvas.create_image(0,0,anchor=NW);
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E");


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white");
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :");
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :");
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :");
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :");
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :");
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :");

# Create all the labels required to be displayed

id_input = "19827198349"
name_input = "Amol"
dob_input = "12 December 2012"
pin_input = "596231"
address_input = "Amarpali Platinum, Noida, Tower - D, Floor-5, Flat No.504"
vehicle_type_input = "Four Wheeler"

# Define the function

def show_driving_license():
    label_id_tag['text'] = id_input
    label_name_tag['text'] = name_input
    label_dob_tag['text'] = dob_input
    label_pin_tag['text'] = pin_input
    label_address_tag['text'] = address_input
    label_vehicle_type_tag['text'] = vehicle_type_input

# Created a button
button1 = Button(root, text = "Show Driving License", command = show_driving_license)
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT);
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1);
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id_tag);
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name_tag);
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob_tag);
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin_tag);
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address_tag);
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type_tag);
canvas.pack();


root.mainloop()