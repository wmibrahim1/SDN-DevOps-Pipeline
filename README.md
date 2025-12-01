# DevOps SDN Project

This project is a simple DevOps-style integration that automates "software-defined" network
policy updates using a CI/CD pipeline.

When you update the `policy.yaml` file and push changes to GitHub:
- A CI/CD pipeline runs unit tests on the SDN simulator.
- If tests pass, the controller applies the new policy.
- A Webex bot sends a notification to a Webex space.

## Technologies Used

- **Python** – SDN simulator, controller, and Webex notification script
- **YAML** – For defining network policy (`policy.yaml`)
- **Pytest** – For unit testing the SDN logic
- **GitHub Actions** – CI/CD pipeline (or Jenkins if you add it)
- **Webex Bot** – For sending pipeline notifications
- **SDN-style Simulator** – Simple Python class that simulates SDN behavior

## Project Structure

```text
DevOps/
├── policy.yaml
├── requirements.txt
├── README.md
├── controller/
│   ├── __init__.py
│   ├── controller.py
│   ├── sdn_simulator.py
│   └── tests/
│       ├── __init__.py
│       └── test_policy.py
├── notifications/
│   ├── __init__.py
│   └── webex_notify.py
└── .github/
    └── workflows/
        └── ci-cd.yml
```

## Local Setup (MacBook)

1. **Open Terminal** and change into the directory where you want the project to live.

   ```bash
   cd ~/Documents
   ```

2. **Create a folder (DevOps) and open the project**.

   - Move newly created files into this folder.
   - Then open it (or use Finder).

   If you're already in the project folder after opening, you should see something like:

   ```bash
   ls
   DevOps
   ```

3. **Change into the project directory:**

   ```bash
   cd DevOps
   ```

4. **(Optional but recommended) Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   When it's activated, your prompt will start with `(venv)`.

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running Locally

### 1. Run the tests

From inside `DevOps`:

```bash
pytest controller/tests
```

This runs the unit tests in `controller/tests/test_policy.py` to verify the SDN simulator logic.

### 2. Apply the policy

```bash
python controller/controller.py
```

This loads `policy.yaml`, applies the rules to the SDN simulator, and prints the applied rules.

You should see output similar to:

```text
Applied rules:
ALLOW: host1 -> host2
BLOCK: host1 -> host3
```

## Webex Notification Script

The `notifications/webex_notify.py` script sends a message to a Webex space.

1. Export your Webex bot token and room ID in the terminal:

   ```bash
   export WEBEX_TOKEN="your_webex_bot_token_here"
   export WEBEX_ROOM_ID="your_webex_room_id_here"
   ```

2. Run the script:

   ```bash
   python notifications/webex_notify.py
   ```

If everything is set correctly, you should receive a message in your Webex space.

## GitHub Actions CI/CD

The CI/CD workflow is defined in:

```text
.github/workflows/ci-cd.yml
```

It does the following when you push to the `main` branch:

1. Checks out the code.
2. Sets up Python.
3. Installs dependencies (`pytest`, `pyyaml`, `requests`).
4. Runs the tests with `pytest controller/tests`.
5. Runs the controller to apply the SDN policy.
6. Calls the Webex notification script.

Make sure you set these repository secrets in GitHub:

- `WEBEX_TOKEN`
- `WEBEX_ROOM_ID`

under **Settings → Secrets and variables → Actions → New repository secret**.

## Notes

- This project uses a **simulated SDN environment**, not real network devices.
- You can extend it later using real SDN tools like Mininet + a controller framework (e.g., Ryu or ONOS),
  but for your course project, this level of integration demonstrates DevOps + SDN concepts clearly.
