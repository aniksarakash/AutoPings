# Ping Dashboard

A web-based dashboard that pings added web addresses or hostnames in real-time and is viewable via a browser. It fetches and displays the user's IPv4 and IPv6 addresses, country, browser information, and operating system details.

## Features

- Fetch and display user's IPv4 and IPv6 addresses.
- Fetch and display user's country, browser, and operating system details.
- Real-time ping monitoring for added hosts with status, RTT (Round Trip Time), and packet loss percentage.
- Add and remove hosts for monitoring.

![Ping Dashboard Screenshot](https://raw.githubusercontent.com/aniksarakash/Autopings/main/preview.png)

## Technologies Used

- Flask (Python)
- Flask-SocketIO
- HTML/CSS (Bootstrap)
- JavaScript (jQuery)
- Pythonping

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ping-dashboard.git
   cd ping-dashboard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Replace `YOUR_TOKEN_HERE` with your actual token from `ipinfo.io` in `app.py`.

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and go to `http://localhost:5000`.

## Usage

1. **Viewing User Information**:
   - The dashboard will automatically display the user's IPv4 and IPv6 addresses, country, browser, and operating system details.

2. **Adding a Host**:
   - Enter a hostname or IP address in the "Enter host address" field and click "Add Host".
   - The host will be added to the list and will be monitored in real-time.

3. **Removing a Host**:
   - Click the "Remove" button next to the host you want to remove from the list.

## Project Structure

```
ping-dashboard/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── requirements.txt
└── README.md
```

- **app.py**: The main Flask application file.
- **templates/**: Directory containing HTML templates.
- **static/**: Directory containing static files (CSS, JavaScript).
- **requirements.txt**: File containing the list of Python dependencies.
- **README.md**: Project documentation.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Additional Notes

- Ensure you have `ipinfo.io` token for fetching the IP and location information.
- The `requirements.txt` should include all necessary dependencies for the project:
  ```plaintext
  Flask
  Flask-SocketIO
  requests
  pythonping
  ```
