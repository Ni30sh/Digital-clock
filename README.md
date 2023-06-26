# Digital Clock

This is a simple digital clock application built using Tkinter library in Python. It displays the current time, date, and day of the week.

## Prerequisites

Make sure you have Python installed on your system. You can download it from the official Python website: [https://www.python.org](https://www.python.org)

## Installation

1. Clone the repository or download the code file.
2. Open the terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command to install the required dependencies:

   ```
   pip install tkinter
   ```

## Usage

1. Open the terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to start the application:

   ```
   python <filename>.py
   ```

## How it works

The application uses the Tkinter library to create the graphical user interface. It retrieves the current time, date, and day of the week using the `datetime` module.

The main components of the application are:

- `clock_hr`: Displays the current hour.
- `clock_min`: Displays the current minutes.
- `clock_sec`: Displays the current seconds.
- `ampm_clock`: Displays whether it's AM or PM.
- `date_lab`: Displays the current date.
- `month_lab`: Displays the current month.
- `year_lab`: Displays the current year.
- `day_lab`: Displays the current day of the week.

The `date_time` function is responsible for updating the clock and date labels every 200 milliseconds. It retrieves the current time and updates the labels accordingly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
