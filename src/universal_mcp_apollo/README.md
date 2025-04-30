# Universal Mcp Apollo MCP Server

An MCP Server for the Universal Mcp Apollo API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_apollo/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Trello API.

| Tool | Description |
|------|-------------|
| `get_cards` | Retrieve card details from the banking core system, optionally filtered by various parameters including dates, status, and identifiers. |
| `card_request` | Requests the creation of a new prepaid card. |
| `webhook_card_created` | Handles webhook notifications for card creation, transitioning the card status from 'Processing' to 'Created' and triggering automated embossing/virtual card generation based on partner configuration. |
| `try_webhook_card_created` | Attempts to retrieve card creation data when the webhook fails, providing equivalent information that would normally be delivered via webhook-card-created. |
| `get_card` | Retrieves detailed card information including physical card data and associated virtual card. |
| `emboss` | Embosses a physical card by sending a PATCH request to the specified URL with the provided request body. |
| `activate` | Activates a physical card by sending a PATCH request to update its status to 'active'. |
| `block` | Temporarily blocks a physical/virtual card by updating its status to 'blocked'. |
| `unblock` | Unblocks a physical or virtual card by changing its status to 'active'. |
| `cancel` | Cancel a physical card by updating its status to 'canceled' via API. |
| `virtual_card_create` | Creates or retrieves a virtual card linked to a physical card that was previously requested and approved, updating the security code with each transaction. |
| `virtual_card_security_code` | Fetches the current security code (CVC) of a virtual card. |
| `card_password_create` | Creates a password for a physical card to activate it. |
| `card_password_change` | Activates a physical card by updating its password and changing its status to 'active'. |
| `webhook_autorize` | Runs a webhook to authorize a debit transaction using a prepaid card, triggered by the card's processing company (Orbitall), which updates the customer's balance and statement. |
| `webhook_card_created1` | Handles the creation of a prepaid card by confirming the request and returning physical card details. |
| `webhook_authorize` | Processes prepaid card transactions by verifying client balance and handling transaction approval or reversal. |
| `webhook_authorize_information` | Handles and reports failed transactions directly to the Core API. |
| `webhook_international_transactions` | Retrieves international transaction information to generate a transaction report with IOF. |
## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_apollo/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Trello app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 