# Free Unlimited Bitly Account Generator

This repository provides a Python script to create free unlimited Bitly URL shortener accounts quickly and efficiently via the command line.

## Features

- **Command-Line Based:** Easily create Bitly accounts by passing required arguments.
- **Automated Process:** Handles account creation by sending requests to Bitly's signup endpoint.
- **Customizable Inputs:** Specify username, email, and password for each account.

## File Structure

The repository consists of a single Python file:

- `Bitly-Account-Generator.py`: The main script that contains the logic for creating Bitly accounts.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tamilts124/Bitly-Account-Generator.git
   cd Bitly-Account-Generator
   ```

2. **Install Dependencies:**
   Ensure you have the required Python libraries installed:
   - `requests`

   Install them using pip:
   ```bash
   pip install requests
   ```

3. **Run the Script:**
   Execute the script directly using the required options:
   ```bash
   python Bitly-Account-Generator.py -u <username> -p <password> -e <email>
   ```

## Usage

### Command-Line Options

| Option       | Description                       | Required |
|--------------|-----------------------------------|----------|
| `-u`, `--username` | The desired Bitly account username | Yes      |
| `-p`, `--password` | Password for the Bitly account     | Yes      |
| `-e`, `--email`    | Email ID for the Bitly account     | Yes      |

### Example Usage

```bash
python Bitly-Account-Generator.py -u myusername -p mypassword -e myemail@example.com
```

### Output

- On successful account creation, the script will output:
  ```plaintext
  Account Created, Success!
  ```
- If there are errors during account creation, the errors will be displayed with details:
  ```plaintext
  > email: This email is already in use.
  > username: Username is not available.
  ```

## How It Works

1. The script sends a request to the Bitly signup page to fetch a CSRF token (`_xsrf`).
2. It uses the token along with the provided username, email, and password to send a POST request to Bitly's signup endpoint.
3. The response from the server indicates whether the account creation was successful or if errors occurred.

## Notes

- Ensure an active internet connection while using the script.
- Use unique email IDs and usernames to avoid conflicts with existing accounts.
- This script is intended for educational and ethical purposes only. Do not use it for spamming or malicious activities.

## Example Output

```plaintext
> python Bitly-Account-Generator.py -u testuser -p testpass123 -e testuser@example.com

Account Created, Success!
```

## License

This project is licensed under the [MIT License](LICENSE).

