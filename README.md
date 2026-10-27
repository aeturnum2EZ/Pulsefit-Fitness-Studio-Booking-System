# Fitness Booking System

## 1. Project Overview

The Fitness Booking System is a command-line application developed using Python to manage fitness-related bookings. The system allows users to log in, check booking availability, make reservations, view existing bookings, update booking details, and cancel bookings.

The application also includes administrative management functions to support the management of the booking system.

Booking records are stored in text files, allowing the system to save and retrieve booking information between program executions, provided the application writes and reads the records correctly.

This project was developed as part of a Python programming assignment to demonstrate programming concepts, user interaction, file handling, and booking management.

## 2. Features

### User Features

- **User Login** – Allows users to access the system through a login function.
- **Check Availability** – Allows users to check the availability of fitness booking slots or services.
- **Make Bookings** – Allows users to create new bookings by providing the required information.
- **View Bookings** – Allows users to view existing booking records.
- **Update Bookings** – Allows users to modify details of existing bookings.
- **Cancel Bookings** – Allows users to cancel existing reservations.

### Administrative Features

- **Manage Classes** – Provides administrative functions for managing the booking system.
- **Re-arrange Existed Classes** – Allow administrative to make changes for sudden situation.
- **Overall Summary Report** - Auto generate a summary to analyze the user preferences.

The exact permissions and administrative operations depend on the functions implemented in the program.

## 3. Technologies Used

- **Programming Language:** Python
- **Interface:** Command-line interface (CLI), Terminal
- **Data Storage:** Text files
- **Development Environment:** [Visual Studio Code / IDLE / PyCharm / Other]

## 4. Project Structure

The following is an example project structure. Update the filenames to match the actual files in your repository.

```text
fitness-booking-system/
├── main.py
├── README.md
└── bookings.txt
└── admins.txt
└── members.txt
└── classes.txt
└── payments.txt
```

### File Descriptions

| File | Description |
|---|---|
| `main.py` | Main entry point of the application, if applicable. |
| `README.md` | Project documentation and usage instructions. |
| Python modules | Contain the system's booking, user, and administrative functions. |
| Text files | Store booking records and other data used by the application. |

Replace the example filenames with the actual filenames used in your project.

## 5. Requirements

- Python 3 installed on the computer.
- A terminal or command prompt.
- A code editor, such as Visual Studio Code, if source-code editing is required.

Additional dependencies may be required depending on the libraries used by the application.

## 6. Installation and Setup

### Step 1: Download the Project

Download the project ZIP file from GitHub and extract it into a folder.

Alternatively, clone the repository using Git:

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the actual URL of the GitHub repository.

### Step 2: Open the Project Folder

Open the extracted folder in a terminal or command prompt.

Ensure that the terminal is located in the project directory containing the main Python script.

### Step 3: Verify Python Installation

Run the following command:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

If Python is not installed, download it from the official website:

https://www.python.org/downloads/

### Step 4: Prepare the Data Files

Ensure that the required text files are available in the locations expected by the application.

If the application creates these files automatically, follow the program's normal startup procedure. If initial data or account credentials are required, obtain them from the project configuration or the assignment instructions.

### Step 5: Install Dependencies

If the project uses third-party Python libraries, install them according to the project's dependency list.

For example, if a `bookings.txt` file is provided:

```bash
pip install -r bookings.txt
```

Skip this step if the project uses only the Python standard library and has no external dependencies.

## 7. How to Run the Application

Navigate to the project directory and execute the main Python script.

For example, if the entry point is `main.py`:

```bash
python main.py
```

Alternatively, on Windows:

```bash
py main.py
```

If the main script has a different filename, replace `main.py` with the correct filename.

After the application starts, follow the instructions displayed in the command-line interface.

## 8. How to Use the System

### 8.1 User
Member of Pulsefit Fitness

### 8.1.1 User Login

1. Run the code in cmd, terminal or pycharm.
2. Select the login option.
3. Enter the required login credentials.
4. Follow the system's instructions after authentication.

The exact login procedure depends on the implementation.

### 8.1.2 Check available slots

1. Select the view slots option.
2. Review the availability information displayed by the system.

### 8.1.3 Make a Booking

1. Select the request booking option.
2. Enter the required information.
3. Follow the prompts to submit the booking.
4. Check the system's response to confirm whether the booking was recorded successfully.

### 8.1.4 View Bookings

1. Select the option of view bookings.
2. Provide any required search information, if applicable.
3. Review the displayed booking records.

### 8.1.5 Update a Booking

1. Select the update-booking option.
2. Identify the booking to be modified.
3. Enter the updated information.
4. Follow the system's confirmation or validation messages.

### 8.1.6 Cancel a Booking

1. Select the cancellation option.
2. Identify the booking to be cancelled.
3. Follow the prompts to confirm the cancellation, if required.
4. Check the resulting status or booking list.

### 8.2 Admin
Staff of Pulsefit Fitness

### 8.2.1 Admin Login

1. Access the administrative function using the procedure implemented in the application.
2. Select the login option.
3. Enter the required login credentials.
4. Follow the system's instructions after authentication.

### 8.2.2 Admin Manage Classes
1. Select manage class option.
2. Select 1 of the options like create, delete, re-arrange class.
3. Follow the systems and input required information to finish process.

### 8.2.2 Generate Summary Report
1. Select generate report option.
2. System will generate report and show the user preferences automatically.\

### 8.2.3 View Members, Bookings, Payments and Classes Data
1. Select view any data option
2. Display all required data

### 8.3 Booking Officer
Staff of Pulsefit Fitness

### 8.3.1 Booking Officer Login

1. Access the administrative function using the procedure implemented in the application.
2. Select the login option.
3. Enter the required login credentials.
4. Follow the system's instructions after authentication.

### 8.3.2 Manage Bookings
1. Select manage bookings option such as process, cancel and reschedule booking.
2. Follow the systems and input required information to finish process.

### 8.3.3 View Member Attendance
1. Select view attendance option.
2. The system will display all the member information and officer required to input the member id.
3. Displays all the member related bookings and their attendance status like attended or absent.

Administrative permissions and available operations depend on the implemented system.

## 9. Data Storage

The system uses text files to store booking information.

Text-file storage can allow records to persist after the application closes, provided the application saves the records to disk and reloads them correctly when it starts again.

The actual file format, record structure, file locations, and storage rules depend on the implementation.

**Important:** Back up the relevant data files before making manual changes. Editing a data file incorrectly may affect the application's ability to read its records.

## 10. Limitations

The system's limitations depend on its implementation. Potential limitations of a command-line booking application using text-file storage include:

- No graphical user interface.
- Data integrity may depend on the file-handling and input-validation logic.
- Simultaneous access by multiple users may not be handled safely.
- Authentication security depends on how credentials are stored and verified.
- Automated backup and recovery may not be available.

These are potential limitations, not confirmed deficiencies of the current implementation.

## 11. Author Information

- **Author:** CHRIS
- **Student ID:** 091460
- **Course:** Bachelor in CS with specialism DA
- **Institution:** APU
- **Assignment:** Pulsefit Fitness Booking System

## 12. Academic Purpose

This project was developed for educational purposes as part of a Python programming assignment. It demonstrates the application of Python programming techniques to a fitness booking and management scenario.

