# Apollo MCP Server

An MCP Server for the Apollo API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Apollo API.


| Tool | Description |
|------|-------------|
| `get_cards` | Retrieve card details from the banking core system, optionally filtered by various parameters including dates, status, and identifiers. Returns both physical and linked virtual cards. |
| `card_request` | Requests the creation of a new prepaid card. This method initiates an asynchronous card creation process and always requires a physical card, even for virtual cards. |
| `webhook_card_created` | Handles webhook notifications for card creation, transitioning the card status from 'Processing' to 'Created' and triggering automated embossing/virtual card generation based on partner configuration. |
| `try_webhook_card_created` | Attempts to retrieve card creation data when the webhook fails, providing equivalent information that would normally be delivered via webhook-card-created. |
| `get_card` | Retrieves detailed card information including physical card data and associated virtual card. |
| `emboss` | Embosses a physical card by sending a PATCH request to the specified URL with the provided request body. |
| `activate` | Activates a physical card by sending a PATCH request to update its status to 'active'. This should be called after the user receives the card and not before 24 hours have passed since the embossing. |
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
