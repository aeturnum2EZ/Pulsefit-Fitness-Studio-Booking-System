#main.py - Pulsefit Studio Class Booking System
#Author: Chris Boong Zu Xi, Goh Shao Hang, Chia Zheng Hong


#=========================================== File I/O Functions ============================================
def read_file(filepath):
    try:
        file = open(filepath, "r")
        lines = []
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)
        file.close()
        return lines

    except FileNotFoundError:
        print("File not found.")
        return []

def write_file(filepath, lines, mode = 'w'):
    try:
        with open(filepath, 'w') as f:
            for line in lines:
                f.write(str(line).rstrip('\n') + '\n')
        return True
    except Exception as e:
        print(f"Error writing to {filepath}: {e}")
        return False

def append_file(filepath, line):
    try:
        with open(filepath, 'a') as f:
            f.write(line + '\n')
        return True
    except Exception as e:
        print(f"Error appending to {filepath}: {e}")
        return False

def clear_screen():
    print("\n" * 50)

def display_logo():
    print("=" * 100)
    print("       🏢 PULSEFIT STUDIO - CLASS BOOKING SYSTEM")
    print("=" * 100)
    print()

def display_separator():
    print("-" * 100)

def generate_next_id(filepath, prefix):
    lines = read_file(filepath)

    if not lines:
        return f"{prefix}001"

    max_id = 0
    for line in lines:
        parts = line.split(',')
        if parts:
            id_val = parts[0].strip()
            if id_val.startswith(prefix):
                num_part = id_val[len(prefix):]
                if num_part.isdigit():
                    num_id = int(num_part)
                    if num_id > max_id:
                        max_id = num_id

    return f"{prefix}{str(max_id + 1).zfill(3)}"

#=================================================== LOGIN PAGE ===================================================

def main_page():
    while True:
        clear_screen()
        display_logo()
        print()
        print("1. Login")
        print("2. Register New Member Account")
        print("3. Administration")
        print("4. Exit\n")

        option = input("Select option (1-4): ")

        if option == '1':
            member_login_page()
        elif option == '2':
            register_member()
            main_page()
        elif option == '3':
            admin_login_page()
        elif option == '4':
            logout()
            return
        else:
            print("Please select 1-4!.")
            input("Press Enter to continue...")

def logout():
    clear_screen()
    print("====================================================================")
    print("      THANK YOU FOR USING PULSEFIT STUDIO CLASS BOOKING SYSTEM!")
    print("           We hope you enjoyed your experience with us.")
    print("====================================================================")

def member_login_page():
    clear_screen()
    display_separator()
    print("      WELCOME TO MEMBER LOGIN PAGE")
    display_separator()
    print()

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not username or not password:
        print("Username and password cannot be empty!")
        input("Press Enter to continue...")
        return
    else:
        lines = read_file('data/members.txt')

        username_found = False
        user_password_found = False
        for line in lines:
            if not line.strip():
                continue
            parts = line.split(",")
            if len(parts) >= 6:
                user_username = parts[1]
                user_password = parts[5]
                if user_username == username:
                    username_found = True
                    if user_password == password:
                        member_id = parts[0]
                        user_fullname = parts[2]
                        print(f"Login successful! Welcome back, {user_fullname}.")
                        input(f"Press Enter to continue...")
                        member_menu(member_id)
                        return

    if not username_found:
        print("Username doesn't existed!")
        input(f"Press Enter to continue...")
    elif not user_password_found:
        print(f"Password input doesn't match the username!")
        input(f"Press Enter to continue...")
        print()
        while True:
            loss_password = input("Do you forget password? (y/n): ").lower()
            if loss_password == 'y':
                forget_password()
                break
            elif loss_password == 'n':
                return
            else:
                print("Please input correctly!")
                print()


def admin_login_page():
    clear_screen()
    display_separator()
    print("      WELCOME TO ADMINISTRATION LOGIN PAGE")
    display_separator()
    print()

    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if not username or not password:
            print("Username or password cannot be empty!")
            input("Press Enter to continue...")
            return
        else:
            lines = read_file('data/admins.txt')
            user_found = False
            password_correct = False
            staff_role = ''

            for line in lines:
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) >= 6:
                    staff_username = parts[1]
                    staff_password = parts[5]

                    if staff_username == username:
                        user_found = True
                        if staff_password == password:
                            password_correct = True
                            staff_role = parts[6]
                        break

            if not user_found:
                print("Username doesn't existed!")
                input("Press Enter to continue...")
                return
            elif not password_correct:
                print("Password input doesn't match the username!")
                input("Press Enter to continue...")
                return
            else:
                print(f"Login successful! Welcome back, {staff_role}.")
                input("Press Enter to continue...")

                if staff_role == "Booking Officer":
                    booking_officer_menu()
                    break
                elif staff_role == "Member Officer":
                    print()
                    print("The menu page is for members only, so this page does not exist for your account. Thank you for your cooperation.")
                    input("Press Enter to continue...")
                    break
                elif staff_role == "Admin":
                    admin_menu()
                    break

def forget_password():
    clear_screen()
    display_separator()
    print("      RESET PASSWORD")
    display_separator()

    username = input("Re-enter your username: ").strip()
    if not username:
        print("Username cannot be empty!\n")
        input("Press Enter to continue...")
        return

    while True:
        email = input("Enter your email address: ").strip()
        if email.find("@") > 0:
            domain_part = email.split("@")[1]
            if not domain_part.find(".") > 0:
                print(f"Invalid format. Domain must contain a valid extension (.com / .edu)\n")
            else:
                break
        else:
            print("Invalid format. Email must contain an '@' symbol after username. Try it again!\n")

    lines = read_file('data/members.txt')
    update_lines = []
    username_found = False
    email_found = False
    for line in lines:
        if line.startswith("#"):
            update_lines.append(line)
            continue
        if not line:
            continue
        parts = line.split(",")
        if len(parts) >= 6:
            user_username = parts[1]
            user_email = parts[3]
            if username == user_username:
                username_found = True
                if user_email == email:
                    email_found = True
                    print(f"User {user_username} verified success\n")
                    while True:
                        new_password = input("Enter a new password: ").strip()
                        if len(new_password) < 8:
                            print("Password must be at least 8 characters long!\n")
                        elif not any(c.isdigit() for c in new_password):
                            print("Password must include at least 1 number!\n")
                        elif not any(c.isalpha() for c in new_password):
                            print("Password must include at least 1 alphabet!\n")
                        else:
                            confirm_password = input("Enter new password again: ").strip()
                            if confirm_password != new_password:
                                print("Password does not match!\n")
                            else:
                                break
                    parts[5] = new_password
            update_lines.append(",".join(parts))
        else:
            update_lines.append(line)

    if not username_found:
        print("Username does not match!\n")
        input("Press Enter to continue...")
    elif not email_found:
        print("Email address does not match!\n")
        input("Press Enter to continue...")
    else:
        write_file("data/members.txt", update_lines)
        print("Password updated successfully!")
        input("Press Enter to continue...")

#=================================================== ADMIN MENU ===================================================

def manage_classes():
    while True:
        clear_screen()
        display_separator()
        print("\n--- Manage Classes ---")
        display_separator()
        print()
        print("1. Add Class")
        print("2. Update Class")
        print("3. Remove Class")
        print("4. Back")
        choice = input("Enter choice: ")
        if choice == "1":
            add_class()
        elif choice == "2":
            update_class()
        elif choice == "3":
            remove_class()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")

def view_classes():
    clear_screen()
    display_separator()
    print("         View All Classes")
    display_separator()
    print()
    print(f"{'Class ID':<10} | {'Class Name':<12} | {'Date':<12} | {'Time':<10} | {'Capacity':<8} | {'Member Filled':<12}")
    display_separator()

    classes = read_file('data/classes.txt')
    if len(classes) == 0:
        print("No classes at the moment.")
        input("Press Enter to continue...")
        return

    valid_count = 0
    for line in classes:
        if not classes:
            continue
        parts = line.split(',')
        if len(parts) >= 5:
            print(f"{parts[0].strip():<10} | {parts[1].strip():<12} | {parts[2].strip():<12} | {parts[3].strip():<10} | {parts[4].strip():<8} | {parts[5].strip():<12}")
            valid_count += 1

    print("-" * 75)
    print(f"\nTotal Valid Classes: {valid_count}")
    input("Press Enter to continue...")
    return

def view_members():
    clear_screen()
    display_separator()
    print("      VIEW ALL MEMBER INFORMATION")
    display_separator()
    print()
    print(f"{'Member ID':<12} | {'Username':<12} | {'Full Name':<25} | {'Email':<30} | {'Phone Number':<12} | {'Password':<20}")
    display_separator()

    total_members = 0
    members = read_file('data/members.txt')
    for member in members:
        if not member:
            continue
        parts = member.split(',')
        if len(parts) >= 6:
            print(f"{parts[0]:<12} | {parts[1]:<12} | {parts[2]:<25} | {parts[3]:<30} | {parts[4]:<12} | {parts[5]:<20}")
            total_members += 1
    print()
    print(f"Total members: {total_members}")
    input("Press enter to continue...")

def view_bookings():
    clear_screen()
    display_separator()
    print("      VIEW MEMBER BOOKING")
    display_separator()
    print()
    print(f"{'Booking ID':<12} | {'Member ID':<12} | {'Class ID':<12} | {'Date':<12} | {'Time':<8} | {'Status':<12}")
    display_separator()

    total_booking = 0
    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if booking.startswith("#"):
            continue
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) >= 6:
            print(f"{parts[0]:<12} | {parts[1]:<12} | {parts[2]:<12} | {parts[3]:<12} | {parts[4]:<8} | {parts[5]:<12}")
            total_booking += 1
    print()
    print(f"Total bookings: {total_booking}")
    input("Press enter to continue...")

def view_payments():
    clear_screen()
    display_separator()
    print("         View All Payments")
    display_separator()
    print()
    print(f"{'Payment ID':<10} | {'Member ID':<10} | {'Class ID':<10} | {'Payment Amount':<8} | {'Date':<15} | {'Payment Status':<12}")
    display_separator()

    payments = read_file('data/payments.txt')
    if len(payments) == 0:
        print("No payments at the moment.")
        input("Press Enter to continue...")
        return

    valid_count = 0
    for line in payments:
        if not payments:
            continue
        parts = line.split(',')
        if len(parts) >= 5:
            print(f"{parts[0].strip():<10} | {parts[1].strip():<10} | {parts[2].strip():<10} | {parts[3].strip():<8} | {parts[4].strip():<15} | {parts[5].strip():<12}")
            valid_count += 1

    print("-" * 75)
    print(f"\nTotal Valid Payments: {valid_count}")
    input("Press Enter to continue...")

def generate_report():
    clear_screen()
    display_separator()
    print("         PULSEFIT STUDIO - OVERALL REPORT")
    display_separator()

    bookings = read_file('data/bookings.txt')
    total_bookings = 0
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(",")
        if len(parts) >= 6:
            total_bookings += 1

    classes = read_file('data/classes.txt')
    total_classes = 0
    max_filled = -1
    min_filled = 9999
    popular_class_id = ""
    most_popular_class = ""
    least_popular_class = ""
    total_capacity = 0
    total_filled = 0
    for cls in classes:
        if not cls:
            continue
        parts = cls.split(",")
        if len(parts) >= 6:
            total_classes += 1
            total_capacity += int(parts[4])
            total_filled += int(parts[5])
            if int(parts[5]) > max_filled:
                max_filled = int(parts[5])
                most_popular_class = parts[1]
                popular_class_id = parts[0]
            if int(parts[5]) <= min_filled:
                min_filled = int(parts[5])
                least_popular_class = parts[1]

    fill_rate = (total_filled / total_capacity) * 100

    payments = read_file('data/payments.txt')
    total_revenue = 0
    highest_revenue = 0
    for payment in payments:
        if not payment:
            continue
        parts = payment.split(",")
        if len(parts) >= 6:
            total_revenue += int(parts[3])
            if parts[2] == popular_class_id:
                highest_revenue += int(parts[3])

    members = read_file('data/members.txt')
    total_member = 0
    most_active_member = ""
    highest_count = -1
    most_inactive_member = ""
    lowest_count = 9999
    for member in members:
        if not member:
            continue
        parts = member.split(",")
        if len(parts) >= 6:
            total_member += 1
            member_count = int(parts[6])
            member_name = parts[2]
            if member_count > highest_count:
                highest_count = member_count
                most_active_member = member_name
            if member_count <= lowest_count:
                lowest_count = member_count
                most_inactive_member = member_name

    print(f'''
    Total Bookings:                     {total_bookings}
    Total Members:                      {total_member}
    Total Revenue:                      {total_revenue}
    Total Classes:                      {total_classes}
    
    Most popular class:                 {most_popular_class}
    Most unpopular class:               {least_popular_class}
    Highest revenue per class session:  {highest_revenue}
    Fill Rate (%):                      {fill_rate:.2f}
    
    Most active member:                 {most_active_member}
    Most bookings per member:           {highest_count}
    Most inactive member:               {most_inactive_member}
    Least bookings per member:          {lowest_count}
    ''')
    print()
    input("Press Enter to continue...")
    return

def add_class():
    clear_screen()
    display_separator()
    print("         Add Class")
    display_separator()
    print()

    class_name = input("Enter a class name: ")

    while True:
        year = int(input("Enter a year (>=2026): "))
        if year < 2026:
            print("Invalid year.")
            input("Press enter to continue...")
            return
        else:
            break

    while True:
        months_31 = ['01', '03', '05', '07', '08', '10', '12']
        months_30 = ['04', '06', '09', '11']
        date_28 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
        date_30 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
        date_31 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

        month = input("Enter a month (01-12): ")
        date =  input("Enter a date (01-31): ")
        if month in months_31:
            if date not in date_31:
                print("Invalid date! This month has 31 days.")
                input("Press enter to continue...")
                return
            else:
                break
        elif month in months_30:
            if date not in date_30:
                print("Invalid date! This month only has 30 days.")
                input("Press enter to continue...")
                return
            else:
                break
        elif month == '02':
            if date not in date_28:
                print("Invalid date! February only has 28 days.")
                input("Press enter to continue...")
                return
            else:
                break
        else:
            break

    while True:
        hour = int(input("Enter a class time in hour(0-24): "))
        if hour < 0 or hour > 24:
            print("Invalid time.")
            input("Press enter to continue...")
            return
        else:
            break

    while True:
        minute = input("Enter a class time in minutes(00, 15, 30, 45): ")
        if minute == '00' or minute == '15' or minute == '30' or minute == '45':
            break
        else:
            print("Invalid time.")
            input("Press enter to continue...")
            return

    while True:
        capacity = int(input("Member capacity: "))
        if capacity <= 2:
            print("Invalid capacity.")
            input("Press enter to continue...")
            return
        else:
            break

    class_id = generate_next_id('data/classes.txt', 'C')
    new_class = f"\n{class_id},{class_name},{year}-{month}-{date},{hour}:{minute},{capacity},0"

    if append_file('data/classes.txt', new_class):
        print(f"Class {class_name} added successfully.")
        input("\nPress Enter to continue...")
    else:
        print("Failed to add a class!")
        input("\nPress Enter to continue...")
        return

def update_class():
    clear_screen()
    display_separator()
    print("         UPDATE CLASS DETAILS")
    display_separator()
    view_classes()
    print()

    class_id = input("Enter a class ID to update: ")
    if not class_id:
        print("Class ID cannot be empty.")
        input("\nPress Enter to continue...")
        return

    classes = read_file('data/classes.txt')
    updated_classes = []
    class_found = False

    for cls in classes:
        if cls.startswith("#"):
            updated_classes.append(cls.strip())
            continue
        if not cls:
            continue
        parts = cls.split(",")
        if len(parts) >= 6 and parts[0] == class_id:
            class_found = True
            print("Press Enter without typing anything to keep the current value.")
            print()
            current_name = parts[1].strip()
            new_name = input(f"Class Name [{current_name}]: ").strip()
            parts[1] = new_name if new_name else current_name

            current_date = parts[2].strip()
            new_date = input(f"Date (YYYY-MM-DD) [{current_date}]: ").strip()

            parts[2] = new_date if new_date else current_date

            current_time = parts[3].strip()
            new_time = input(f"Time (HH:MM) [{current_time}]: ").strip()
            parts[3] = new_time if new_time else current_time

            current_cap = parts[4].strip()
            new_cap = input(f"Capacity [{current_cap}]: ").strip()
            parts[4] = new_cap if new_cap else current_cap

            while True:
                confirm = input(f"\nAre you sure you want to update ({class_id})? (y/n): ").strip().lower()
                if confirm == 'n':
                    print("Removal cancelled.")
                    input("Press Enter to continue...")
                    return
                elif confirm == 'y':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            updated_classes.append(",".join(parts))
        else:
            updated_classes.append(cls)

    if class_found:
        write_file('data/classes.txt', updated_classes)
        print(f"\nClass {class_id} updated successfully.")
    else:
        print(f"Class ID not found")

    input("\nPress Enter to continue...")
    return

def remove_class():
    clear_screen()
    display_separator()
    print("          REMOVE A CLASS")
    display_separator()

    view_classes()
    print()

    class_id = input("Enter a class ID to remove: ")
    if not class_id:
        print("Class ID cannot be empty")
        input("\nPress Enter to continue...")
        return

    classes = read_file('data/classes.txt')
    removed_classes = []
    class_found = False
    removed_class_name = ""

    for cls in classes:
        if cls.startswith("#"):
            removed_classes.append(cls)
            continue
        if not cls:
            continue
        parts = cls.split(",")
        if len(parts) >= 6 and parts[0] == class_id:
            class_found = True
            removed_class_name = parts[1].strip()
        else:
            removed_classes.append(cls)

    if not class_found:
        print("Class ID not found")
        input("\nPress Enter to continue...")
        return

    while True:
        confirm = input(f"\nAre you sure you want to remove ({class_id})? (y/n): ").strip().lower()
        if confirm == 'n':
            print("Removal cancelled.")
            input("Press Enter to continue...")
            return
        elif confirm == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    write_file('data/classes.txt', removed_classes)
    print(f"\nClass '{removed_class_name}' ({class_id}) successfully removed!")
    input("Press Enter to continue...")

def admin_menu():
    while True:
        clear_screen()
        display_separator()
        print("     ADMIN MENU")
        display_separator()
        print()
        print("1. Manage Classes")
        print("2. View All Classes")
        print("3. View All Members")
        print("4. View All Bookings")
        print("5. View All Payments")
        print("6. Generate Overall Report")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            manage_classes()
        elif choice == "2":
            view_classes()
        elif choice == "3":
            view_members()
        elif choice == "4":
            view_bookings()
        elif choice == "5":
            view_payments()
        elif choice == "6":
            generate_report()
        elif choice == "7":
            break
        else:
            print("Invalid choice, please enter a number between 1 to 6.")
            input("Press Enter to continue...")

#=================================================== BOOKING MENU ===================================================

def register_member():
    clear_screen()
    display_separator()
    print("         REGISTER NEW MEMBER")
    display_separator()


    print("\n**** Please provide member details ****")

    while True:
        username = input("Enter username: ").strip()
        if len(username) < 8:
            print("Username must be at least 8 characters long!\n")
        else:
            break

    while True:
        full_name = input("Enter your full name: ").upper().strip()
        if not full_name:
            print("Full name cannot be empty!")
        if any(c.isdigit() for c in full_name):
            print("Full Name have no any digits!\n")
        else:
            break

    while True:
        email = input("Enter your email address: ").strip()
        if email.find("@") > 0:
            domain_part = email.split("@")[1]
            if not domain_part.find(".") > 0:
                print(f"Invalid format. Domain must contain a valid extension (.com / .edu)\n")
            else:
                break
        else:
            print("Invalid format. Email must contain an '@' symbol after username. Try it again!\n")

    valid_num = ('010','011','012','013','014','016','017','018','019')
    while True:
        phone_num = input("Enter your phone number: ").strip()
        if not phone_num.startswith(valid_num):
            print("Please use a Malaysia number!\n")
        if not 10 <= len(phone_num) <= 11:
            print("Please insert a proper phone number!\n")
        elif not phone_num.isdigit():
            print("Phone number contain digits only!\n")
        else:
            break

    while True:
        password = input("Enter a new password: ").strip()
        if len(password) < 8:
            print("Password must be at least 8 characters long!\n")
        elif not any(c.isdigit() for c in password):
            print("Password must include at least 1 number!\n")
        elif not any(c.isalpha() for c in password):
            print("Password must include at least 1 alphabet!\n")
        else:
            confirm_password = input("Enter new password again: ").strip()
            if confirm_password != password:
                print("Password does not match!\n")
            else:
                break

    member_id = generate_next_id('data/members.txt', 'M')
    new_member = f"\n{member_id},{username},{full_name},{email},{phone_num},{password},0"

    if append_file('data/members.txt', new_member):
        print(f"Member registered successfully! Your New ID: {member_id}")
        print(f"Username: {username}, Full Name: {full_name}, Email: {email}, Phone: {phone_num}, Password: {password}")
        print()
        input("Press Enter to continue...")
        return
    else:
        print("Failed to register new member!\n")
        return

def process_booking():
    clear_screen()
    display_separator()
    print("    PROCESS NEW BOOKING")
    display_separator()

    member_id = input("Enter Member ID (e.g., M001): ").strip()
    if not member_id:
        print("Member ID cannot be empty!")
        input("Press Enter to continue...")
        return

    members = read_file('data/members.txt')
    member_found = False
    member_name = ""
    for member in members:
        if not member:
            continue
        parts = member.split(",")
        if len(parts) > 0 and parts[0] == member_id:
            member_found = True
            member_name = parts[1]
            break
    if not member_found:
        print("Member not existed!")
        input("Press Enter to continue...")
        return

    print(f"\nMember: {member_name} (ID: {member_id}) verified success\n")
    input("Press Enter to continue...")

    view_available_classes()

    print()

    class_id = input("Enter Class ID (e.g., C001): ").strip()
    if not class_id:
        print("Class ID cannot be empty!")
        input("Press Enter to continue...")
        return

    classes = read_file('data/classes.txt')
    class_found = False
    class_name = ""
    class_date = ""
    class_time = ""
    class_capacity = 0
    class_booked = 0

    for cls in classes:
        parts = cls.split(",")
        if len(parts) >= 6 and parts[0] == class_id:
            class_found = True
            class_name = parts[1]
            class_date = parts[2]
            class_time = parts[3]
            class_capacity = int(parts[4])
            class_booked = int(parts[5])
            break

    if not class_found:
        print("Class not found!")
        input("Press Enter to continue...")
        return

    print(f"Class ID: {class_id}")
    print(f"Class Name: {class_name}")
    print(f"Class Date: {class_date}")
    print(f"Class Time: {class_time}")
    print(f"Class Capacity: {class_capacity}")
    print(f"Class Booked: {class_booked}\n")

    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(",")
        if len(parts) >= 6 and parts[1] == member_id:
            existed_class_id = parts[2]
            existed_status = parts[5]
            if existed_class_id == class_id and existed_status == "Confirmed":
                print("This member already has a booking for this class!")
                input("Press Enter to continue...")
                return

    if class_booked >= class_capacity:
        while True:
            choice = input("Class is full! Would you like to add to waitlist? (y/n): ").lower()
            if choice == 'y':
                booking_id = generate_next_id('data/bookings.txt', 'B')
                new_booking = f"{booking_id},{member_id},{class_id},{class_date},{class_time},Waitlisted,None"
                append_file('data/bookings.txt', new_booking)
                print("You have successfully added to waitlist!")
                input("Press Enter to continue...")
                return
            elif choice == 'n':
                print("Booking cancelled!")
                input("Press Enter to continue...")
                return
            else:
                print("Please enter yes(y) or no(n): ")

    while True:
        confirm_booking = input("Confirm booking? (y/n): ").lower()
        if confirm_booking == 'y':
            break
        elif confirm_booking == 'n':
            print("Booking cancelled!")
            return
        else:
            print("Please enter yes(y) or no(n): ")

    booking_id = generate_next_id('data/bookings.txt','B')
    new_booking = f"{booking_id},{member_id},{class_id},{class_date},{class_time},Confirmed,Incoming"
    append_file('data/bookings.txt', new_booking)

    new_classes = []
    for cls in classes:
        if cls.startswith("#"):
            new_classes.append(cls)
            continue
        if not cls:
            continue
        parts = cls.split(',')
        if len(parts) >= 6 and parts[0] == class_id:
            parts[5] = str(int(class_booked + 1))
            new_classes.append(",".join(parts))
        else:
            new_classes.append(cls)

    write_file('data/classes.txt', new_classes)

    print(f"Booking confirmed! Booking ID: {booking_id}")
    print(f"Member: {member_name} | Class: {class_name} | Date: {class_date} | Time: {class_time}")

    input("Press Enter to continue...")

def cancel_booking():
    clear_screen()
    display_separator()
    print("    CANCEL EXISTED BOOKING")
    display_separator()

    view_member_bookings_history()

    print()
    booking_id = input("Enter a booking ID (e.g., B001): ")

    bookings = read_file('data/bookings.txt')
    booking_found = False
    class_id = ""
    member_id = ""
    class_date = ""
    class_time = ""
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) > 0 and parts[0] == booking_id:
            booking_found = True
            member_id = parts[1]
            class_id = parts[2]
            class_date = parts[3]
            class_time = parts[4]
            break

    if not booking_found:
        print("Booking not found!")
        input("Press Enter to continue...")
        return

    members = read_file('data/members.txt')
    member_found = False
    member_name = ""
    for member in members:
        if not member:
            continue
        parts = member.split(",")
        if len(parts) > 0 and parts[0] == member_id:
            member_found = True
            member_name = parts[1]
            break

    if not member_found:
        print("Member not found!")
        input("Press Enter to continue...")
        return

    class_found = False
    classes = read_file('data/classes.txt')
    class_name = ""
    class_booked = ""
    for cls in classes:
        if not cls:
            continue
        parts = cls.split(',')
        if len(parts) > 0 and parts[0] == class_id:
            class_found = True
            class_name = parts[1]
            class_booked = int(parts[5])
            break

    if not class_found:
        print("Class not found!")
        input("Press Enter to continue...")
        return

    print(f"\nBooking Details:")
    print(f"  ID: {booking_id}")
    print(f"  Member: {member_name} (ID: {member_id})")
    print(f"  Class: {class_name} ({class_id}) on {class_date} at {class_time}")

    confirm = input("Are you sure you want to cancel this booking? (y/n): ").strip().lower()
    if confirm == 'n':
        print("Cancellation cancelled.")
        input("Press Enter to continue...")
        return
    elif confirm == 'y':
        lines = read_file('data/bookings.txt')
        new_status = "Cancelled"

        cancel_booking = []
        for line in lines:
            if line.startswith("#"):
                cancel_booking.append(line)
                continue
            if not line:
                continue
            parts = line.split(",")
            if len(parts) >= 5 and parts[0] == booking_id:
                parts[5] = new_status
                parts[6] = "None"
                cancel_booking.append(",".join(parts))
            else:
                cancel_booking.append(line)
        write_file('data/bookings.txt', cancel_booking)

        minus_classes = []
        for cls in classes:
            if cls.startswith("#"):
                minus_classes.append(cls)
                continue
            if not cls:
                continue
            parts = cls.split(',')
            if len(parts) >= 6 and parts[0] == class_id:
                parts[5] = str(int(class_booked - 1))
                minus_classes.append(",".join(parts))
            else:
                 minus_classes.append(cls)
        write_file('data/classes.txt', minus_classes)

        print("Booking cancelled successfully!")
        input("Press Enter to return to the Booking Officer Menu... ")
        return
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        return

def reschedule_booking():
    clear_screen()
    display_separator()
    print("       RESCHEDULE BOOKING")
    display_separator()

    view_member_bookings_history()
    print()

    booking_id = input("Enter a Booking ID to reschedule: ").strip()
    if not booking_id:
        print("Booking ID cannot be empty!")
        input("Press Enter to continue...")
        return

    booking_found = False
    original_class_id = ""
    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) >= 6 and parts[0] == booking_id:
            booking_found = True
            original_class_id = parts[2]
            print()
            print(f"{parts[0]:<8} {parts[1]:<8} {parts[2]:<8} {parts[3]:<15} {parts[4]:<8} {parts[5]:<12}")
            input("Press Enter to continue...")
            break

    if not booking_found:
        print(f"Booking ID {booking_id} not found!")
        input("Press Enter to continue...")
        return

    clear_screen()
    display_separator()
    print("         Available Classes for Rescheduling")
    display_separator()

    view_available_classes()
    print()

    adjust_class_id = input("Enter a class ID to reschedule: ").strip()
    if not adjust_class_id:
        print("Class ID cannot be empty!")
        input("Press Enter to continue...")
        return

    classes = read_file('data/classes.txt')
    adjust_class_name = ""
    adjust_class_date = ""
    adjust_class_time = ""

    for cls in classes:
        if not cls:
            continue
        parts = cls.split(',')
        if len(parts) >= 6 and parts[0] == adjust_class_id:
            adjust_class_name = parts[1]
            adjust_class_date = parts[2]
            adjust_class_time = parts[3]

    while True:
        confirm = input("Are you sure you want to reschedule this booking? (y/n): ").strip().lower()
        if confirm == 'n':
            print("Reschedule cancelled.")
            input("Press Enter to continue...")
            return
        elif confirm == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


    lines = read_file('data/bookings.txt')
    reschedule_booking = []
    for line in lines:
        if line.startswith("#"):
            reschedule_booking.append(line)
            continue
        if not line:
            continue
        parts = line.split(",")
        if len(parts) >= 5 and parts[0] == booking_id:
            parts[2] = adjust_class_id
            parts[3] = adjust_class_date
            parts[4] = adjust_class_time
            parts[5] = "Confirmed"
            parts[6] = "Incoming"
            reschedule_booking.append(",".join(parts))
        else:
            reschedule_booking.append(line)
    write_file('data/bookings.txt', reschedule_booking)

    rows = read_file('data/classes.txt')
    update_classes = []
    for row in rows:
        if row.startswith("#"):
            update_classes.append(row)
            continue
        if not row:
            continue
        parts = row.split(",")
        if len(parts) >= 5:
            current_id = parts[0]
            if current_id == original_class_id:
                current_filled = parts[5]
                parts[5] = str(int(current_filled) - 1)
                update_classes.append(",".join(parts))
            elif current_id == adjust_class_id:
                current_filled = parts[5]
                parts[5] = str(int(current_filled) + 1)
                update_classes.append(",".join(parts))
            else:
                update_classes.append(row)
        else:
            update_classes.append(row)

    write_file('data/classes.txt', update_classes)
    print(f"Booking '{booking_id}' successfully moved to {adjust_class_name}!")
    input("Press Enter to continue...")

def view_member_bookings_history():
    clear_screen()
    display_separator()
    print("      VIEW MEMBER BOOKING HISTORY")
    display_separator()
    print()
    print(f"{'Booking ID':<12} | {'Member ID':<12} | {'Class ID':<12} | {'Date':<12} | {'Time':<8} | {'Status':<12}")
    display_separator()

    total_booking = 0
    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) >= 6:
            print(f"{parts[0]:<12} | {parts[1]:<12} | {parts[2]:<12} | {parts[3]:<12} | {parts[4]:<8} | {parts[5]:<12}")
            total_booking += 1
    print()
    print(f"Total bookings: {total_booking}")
    input("Press enter to continue...")

def view_member_attendance_history():
    clear_screen()
    display_separator()
    print("         MEMBER ATTENDANCE HISTORY")
    display_separator()
    print()

    member_id = input("Enter member ID (eg. M001): ")
    if not member_id:
        print("Member ID cannot be empty!")
        input("Press Enter to continue...")
        return

    members = read_file('data/members.txt')
    member_name = ""
    member_found = False

    for member in members:
        if not member:
            continue
        parts = member.split(',')
        if len(parts) > 0 and parts[0] == member_id:
            member_found = True
            member_name = parts[2]
            continue

    if not member_found:
        print("Member not found!")
        input("Press Enter to continue...")
        return

    classes = read_file('data/classes.txt')
    classname = {}
    for cls in classes:
        if not cls:
            continue
        parts = cls.split(',')
        if len(parts) >= 4:
            classname[parts[0]] = parts[1]

    print(f"{'Booking ID':<12} | {'Class ID':<10} | {'Class Name':<15} | {'Date':<12} | {'Time':<8} | {'Status':<10}")
    print(f"{'-' * 10:<12} {'-' * 8:<10} {'-' * 10:<15} {'-' * 10:<12} {'-' * 4:<8} {'-' * 9:<10}")


    total_booked = 0
    total_attend = 0
    total_absent = 0
    total_upcoming = 0
    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) >= 6 and parts[1] == member_id:
            booking_id = parts[0]
            class_id = parts[2]
            booking_date = parts[3]
            booking_time = parts[4]
            booking_status = parts[5]
            booking_attendance = parts[6]

            class_name = classname.get(class_id,"Unknown")
            print(f"{booking_id:<12} | {class_id:<10} | {class_name:<15} | {booking_date:<12} | {booking_time:<8} | {booking_status:<10}")
            total_booked += 1
            if booking_attendance == "Attended":
                total_attend += 1
            elif booking_attendance == "Absent":
                total_absent += 1
            elif booking_attendance == "Upcoming":
                total_upcoming += 1
            else:
                break

    print()
    display_separator()
    print(f"Attendance Summary for {member_id}: {member_name}")
    print(f"Total Booked Classes: {total_booked}")
    print(f"Total Attended Classes: {total_attend}")
    print(f"Total Absent Classes: {total_absent}")
    print(f"Total Upcoming Classes: {total_upcoming}")
    display_separator()
    input("Press Enter to return to the Booking Officer Menu... ")

def booking_officer_menu():
    while True:
        clear_screen()
        display_separator()
        print("         BOOKING OFFICER MENU")
        display_separator()
        print()

        print("1. Register New Member")
        print("2. Process Booking")
        print("3. Cancel Booking")
        print("4. Reschedule Booking")
        print("5. View Member Booking History")
        print("6. View Member Attendance History")
        print("7. Back To Main Page\n")
        option = input("Select an option (1-7): ")

        if option == '1':
            register_member()
        elif option == '2':
            process_booking()
        elif option == '3':
            cancel_booking()
        elif option == '4':
            reschedule_booking()
        elif option == '5':
            view_member_bookings_history()
        elif option == '6':
            view_member_attendance_history()
        elif option == '7':
            break
        else:
            print("Invalid selection. Please enter (1-7).")
            input("Press Enter to continue...")

#=================================================== MEMBER MENU ===================================================
def view_time_slots():
    print("\n--- View Time Slots ---")
    time_slots = read_file('data/classes.txt')
    if len(time_slots) == 0:
        print("No time slots available.")
        return

    display_separator()
    print(f"{'Class ID':<10} | {'Class Name':<15} | {'Time Slot'}")
    print("-" * 50)
    for line in time_slots:
        parts = line.split(',')
        if len(parts) >= 4:
            print(f"{parts[0].strip():<10} | {parts[1].strip():<15} | {parts[3].strip()}")
    display_separator()
    input("Press Enter to continue...")
    return

def view_available_classes():
    display_separator()
    print("\n--- View Available Classes ---")
    display_separator()
    print()
    available_class = read_file('data/classes.txt')
    if len(available_class) == 0:
        print("No classes available at the moment.")
        input("Press Enter to continue...")
        return

    print("-" * 75)
    print(f"{'Class ID':<10} | {'Class Name':<12} | {'Date':<12} | {'Time':<10} | {'Capacity':<8} | {'Member Filled':<12}")
    print("-" * 75)

    valid_count = 0
    for line in available_class:
        if not available_class:
            continue
        parts = line.split(',')
        if len(parts) >= 5:
            print(f"{parts[0].strip():<10} | {parts[1].strip():<12} | {parts[2].strip():<12} | {parts[3].strip():<10} | {parts[4].strip():<8} | {parts[5].strip():<12}")
            valid_count += 1

    print("-" * 75)
    print(f"\nTotal Valid Classes: {valid_count}")
    input("Press Enter to continue...")

def request_booking(member_id):
    view_available_classes()

    print()

    class_id = input("Enter Class ID (e.g., C001): ").strip()
    if not class_id:
        print("Class ID cannot be empty!")
        input("Press Enter to continue...")
        return

    classes = read_file('data/classes.txt')
    class_found = False
    class_name = ""
    class_date = ""
    class_time = ""
    class_capacity = 0
    class_booked = 0

    for cls in classes:
        parts = cls.split(",")
        if len(parts) >= 6 and parts[0] == class_id:
            class_found = True
            class_name = parts[1]
            class_date = parts[2]
            class_time = parts[3]
            class_capacity = int(parts[4])
            class_booked = int(parts[5])
            break

    if not class_found:
        print("Class not found!")
        input("Press Enter to continue...")
        return

    print(f"Class ID: {class_id}")
    print(f"Class Name: {class_name}")
    print(f"Class Date: {class_date}")
    print(f"Class Time: {class_time}")
    print(f"Class Capacity: {class_capacity}")
    print(f"Class Booked: {class_booked}\n")

    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(",")
        if len(parts) >= 6 and parts[1] == member_id:
            existed_class_id = parts[2]
            existed_status = parts[5]
            if existed_class_id == class_id and existed_status == "Confirmed":
                print("This member already has a booking for this class!")
                input("Press Enter to continue...")
                return

    if class_booked >= class_capacity:
        while True:
            choice = input("Class is full! Would you like to add to waitlist? (y/n): ").lower()
            if choice == 'y':
                booking_id = generate_next_id('data/bookings.txt', 'B')
                new_booking = f"{booking_id},{member_id},{class_id},{class_date},{class_time},Waitlisted,None"
                append_file('data/bookings.txt', new_booking)
                print("You have successfully added to waitlist!")
                input("Press Enter to continue...")
                return
            elif choice == 'n':
                print("Booking cancelled!")
                input("Press Enter to continue...")
                return
            else:
                print("Please enter yes(y) or no(n): ")

    while True:
        confirm_booking = input("Confirm booking? (y/n): ").lower()
        if confirm_booking == 'y':
            break
        elif confirm_booking == 'n':
            print("Booking cancelled!")
            return
        else:
            print("Please enter yes(y) or no(n): ")

    booking_id = generate_next_id('data/bookings.txt','B')
    new_booking = f"{booking_id},{member_id},{class_id},{class_date},{class_time},Confirmed,Incoming"
    append_file('data/bookings.txt', new_booking)

    new_classes = []
    for cls in classes:
        if cls.startswith("#"):
            new_classes.append(cls)
            continue
        if not cls:
            continue
        parts = cls.split(',')
        if len(parts) >= 6 and parts[0] == class_id:
            parts[5] = str(int(class_booked + 1))
            new_classes.append(",".join(parts))
        else:
            new_classes.append(cls)

    write_file('data/classes.txt', new_classes)

    print(f"Booking confirmed! Booking ID: {booking_id}")
    print(f"Member ID: {member_id} | Class: {class_name} | Date: {class_date} | Time: {class_time}")

    input("Press Enter to continue...")

def member_cancel_booking(member_id):
    clear_screen()
    display_separator()
    print("         CANCEL BOOKING")
    display_separator()

    view_booking_history(member_id)

    print()
    booking_id = input("Enter a booking ID (e.g., B001): ")

    bookings = read_file('data/bookings.txt')
    booking_found = False
    class_id = ""
    class_date = ""
    class_time = ""
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) > 0 and parts[0] == booking_id:
            if parts[1] == member_id:
                booking_found = True
                class_id = parts[2]
                class_date = parts[3]
                class_time = parts[4]
                break

    if not booking_found:
        print("Booking not found!")
        input("Press Enter to continue...")
        return

    members = read_file('data/members.txt')
    member_found = False
    member_name = ""
    for member in members:
        if not member:
            continue
        parts = member.split(",")
        if len(parts) > 0 and parts[0] == member_id:
            member_found = True
            member_name = parts[1]
            break

    if not member_found:
        print("Member not found!")
        input("Press Enter to continue...")
        return

    class_found = False
    classes = read_file('data/classes.txt')
    class_name = ""
    class_booked = ""
    for cls in classes:
        if not cls:
            continue
        parts = cls.split(',')
        if len(parts) > 0 and parts[0] == class_id:
            class_found = True
            class_name = parts[1]
            class_booked = int(parts[5])
            break

    if not class_found:
        print("Class not found!")
        input("Press Enter to continue...")
        return

    print(f"\nBooking Details:")
    print(f"  ID: {booking_id}")
    print(f"  Member: {member_name} (ID: {member_id})")
    print(f"  Class: {class_name} ({class_id}) on {class_date} at {class_time}")

    confirm = input("Are you sure you want to cancel this booking? (y/n): ").strip().lower()
    if confirm == 'n':
        print("Cancellation cancelled.")
        input("Press Enter to continue...")
        return
    elif confirm == 'y':
        lines = read_file('data/bookings.txt')
        new_status = "Cancelled"
        cancel_booking = []
        for line in lines:
            if line.startswith("#"):
                cancel_booking.append(line)
                continue
            if not line:
                continue
            parts = line.split(",")
            if len(parts) >= 5 and parts[0] == booking_id:
                parts[5] = new_status
                parts[6] = "None"
                cancel_booking.append(",".join(parts))
            else:
                cancel_booking.append(line)
        write_file('data/bookings.txt', cancel_booking)

        minus_classes = []
        for cls in classes:
            if cls.startswith("#"):
                minus_classes.append(cls)
                continue
            if not cls:
                continue
            parts = cls.split(',')
            if len(parts) >= 6 and parts[0] == class_id:
                parts[5] = str(int(class_booked - 1))
                minus_classes.append(",".join(parts))
            else:
                 minus_classes.append(cls)

        write_file('data/classes.txt', minus_classes)
        print("Booking cancelled successfully!")
        input("Press Enter to return to the Booking Officer Menu... ")
        return
    else:
        print("Invalid input!")
        input("Press Enter to continue...")
        return

def view_booking_history(member_id):
    display_separator()
    print("      VIEW BOOKING HISTORY")
    display_separator()
    print()
    print(f"{'Booking ID':<12} {'Member ID':<12} {'Class ID':<12} {'Date':<12} {'Time':<8} {'Status':<12}")
    display_separator()

    total_booking = 0
    booking_found = False
    bookings = read_file('data/bookings.txt')
    for booking in bookings:
        if not booking:
            continue
        parts = booking.split(',')
        if len(parts) >= 6 and parts[1] == member_id:
            booking_found = True
            print(f"{parts[0]:<12} {parts[1]:<12} {parts[2]:<12} {parts[3]:<12} {parts[4]:<8}{parts[5]:<12}")
            total_booking += 1

    if not booking_found:
        print(f"Booking user {member_id} not found.")
        input("Press enter to continue...")
        return

    print()
    print(f"Total bookings: {total_booking}")
    input("Press enter to continue...")

def view_payment_history(member_id):
    clear_screen()
    display_separator()
    print("      VIEW PAYMENT HISTORY")
    display_separator()
    print()
    print(f"{'Payment ID':<10} | {'Member ID':<10} | {'Class ID':<10} | {'Payment Amount':<15} | {'Date':<15} | {'Payment Status':<15}")
    display_separator()

    total_payment = 0
    payment_found = False
    payments = read_file('data/payments.txt')
    for payment in payments:
        if not payment:
            continue
        parts = payment.split(',')
        if len(parts) >= 6 and parts[1] == member_id:
            payment_found = True
            print(f"{parts[0].strip():<10} | {parts[1].strip():<10} | {parts[2].strip():<10} | {parts[3].strip():<15} | {parts[4].strip():<15} | {parts[5].strip():<15}")
            total_payment += 1

    if not payment_found:
        print(f"Payments for user {member_id} not found.")
        input("Press enter to continue...")
        return

    print()
    print(f"Total payments: {total_payment}")
    input("Press enter to continue...")

def member_menu(member_id):
    while True:
        clear_screen()
        display_separator()
        print("     Member Menu")
        display_separator()
        print('''
    1. View Time Slots
    2. View Available Classes
    3. Request Booking
    4. Cancel Booking
    5. View Booking History
    6. View Payment History
    7. Back to Main Page
    ''')

        choice = input('Please enter your choice (1-6): ').strip()

        if choice == '1':
            view_time_slots()
        elif choice == '2':
            view_available_classes()
        elif choice == '3':
            request_booking(member_id)
        elif choice == '4':
            member_cancel_booking(member_id)
        elif choice == '5':
            view_booking_history(member_id)
        elif choice == '6':
            view_payment_history(member_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please enter a number between 1 to 6.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_page()