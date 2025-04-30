from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class ApolloApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='apollo', integration=integration, **kwargs)
        self.base_url = "{{card_base_url}}"


    def get_cards(self, accountId: Annotated[Any, 'Id da conta do core brancário'] = None, cardId: Annotated[Any, 'Id do cartão'] = None, document: Annotated[Any, 'Documento'] = None, endCancelDate: Annotated[Any, 'Data final do cancelamento do cartão'] = None, endCreateDate: Annotated[Any, 'Data final da criação do cartão'] = None, endEmbossDate: Annotated[Any, 'Data final do emboçamento do cartão'] = None, id: Annotated[Any, 'Id do registro'] = None, limit: Annotated[Any, 'Limite de registros por página'] = None, page: Annotated[Any, 'Página atual'] = None, startCancelDate: Annotated[Any, 'Data inicial do cancelamento do cartão'] = None, startCreateDate: Annotated[Any, 'Data inicial da criação do cartão'] = None, startEmbossDate: Annotated[Any, 'Data inicial do emboçamento do cartão'] = None, status: Annotated[Any, 'Status do cartão (processing/ created/ active/ blocked/ canceled)'] = None) -> dict[str, Any]:
        """
        Retrieve card details from the banking core system, optionally filtered by various parameters including dates, status, and identifiers. Returns both physical and linked virtual cards.
        
        Args:
            accountId: Id da conta do core brancário
            cardId: Id do cartão
            document: Documento
            endCancelDate: Data final do cancelamento do cartão
            endCreateDate: Data final da criação do cartão
            endEmbossDate: Data final do emboçamento do cartão
            id: Id do registro
            limit: Limite de registros por página
            page: Página atual
            startCancelDate: Data inicial do cancelamento do cartão
            startCreateDate: Data inicial da criação do cartão
            startEmbossDate: Data inicial do emboçamento do cartão
            status: Status do cartão (processing/created/active/blocked/canceled)
        
        Returns:
            Dictionary containing a 'cards' list with physical cards and their linked virtual cards
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to HTTP errors (e.g., 4xx/5xx responses)
        
        Tags:
            retrieve, list, card-api, async_job, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page": page,
                "limit": limit,
                "id": id,
                "accountId": accountId,
                "cardId": cardId,
                "document": document,
                "status": status,
                "startCreateDate": startCreateDate,
                "endCreateDate": endCreateDate,
                "startCancelDate": startCancelDate,
                "endCancelDate": endCancelDate,
                "startEmbossDate": startEmbossDate,
                "endEmbossDate": endEmbossDate,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def card_request(self, accountId: Annotated[Any, ''] = None, cardId: Annotated[Any, ''] = None, externalPrivateLabelAccountId: Annotated[Any, ''] = None, partner: Annotated[dict[str, Any], ''] = None) -> dict[str, Any]:
        """
        Requests the creation of a new prepaid card. This method initiates an asynchronous card creation process and always requires a physical card, even for virtual cards.
        
        Args:
            accountId: Account ID of the client.
            cardId: ID of the card.
            externalPrivateLabelAccountId: External private label account ID.
            partner: Partner details in dictionary format.
        
        Returns:
            A dictionary containing the response data.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            create, card, prepaid, important
        """
        request_body = {
            "accountId": accountId,
            "cardId": cardId,
            "externalPrivateLabelAccountId": externalPrivateLabelAccountId,
            "partner": partner,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_card_created(self, bin: Annotated[Any, ''] = None, cardId: Annotated[Any, ''] = None, id: Annotated[Any, ''] = None, last4Digits: Annotated[Any, ''] = None, privateLabelAccount: Annotated[dict[str, Any], ''] = None, token: Annotated[Any, ''] = None, validThru: Annotated[Any, ''] = None) -> Any:
        """
        Handles webhook notifications for card creation, transitioning the card status from 'Processing' to 'Created' and triggering automated embossing/virtual card generation based on partner configuration.
        
        Args:
            bin: Bank Identification Number (BIN) associated with the card
            cardId: Unique identifier for the card being processed
            id: System-generated identifier for the card creation request
            last4Digits: Last four digits of the card number
            privateLabelAccount: Dictionary containing private label account details (merchant-specific card configuration)
            token: Security token associated with the card
            validThru: Card expiration date in MM/YY format
        
        Returns:
            Parsed JSON response from the card processing API containing creation confirmation details
        
        Raises:
            requests.HTTPError: Raised for 4XX/5XX responses from the API endpoint
        
        Tags:
            card-api, webhook-handler, async-processing, status-update, orbitall-integration, physical-card, virtual-card, important
        """
        request_body = {
            "bin": bin,
            "id": id,
            "last4Digits": last4Digits,
            "privateLabelAccount": privateLabelAccount,
            "token": token,
            "validThru": validThru,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "cardId": cardId,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def try_webhook_card_created(self, ) -> Any:
        """
        Attempts to retrieve card creation data when the webhook fails, providing equivalent information that would normally be delivered via webhook-card-created.
        
        Args:
            None: This method has no parameters.
        
        Returns:
            A JSON-parsed response containing card creation details equivalent to webhook payload data.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request fails (status code >= 400).
        
        Tags:
            webhook, card-created, api, fallback, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_card(self, ) -> dict[str, Any]:
        """
        Retrieves detailed card information including physical card data and associated virtual card.
        
        Returns:
            Dictionary containing card details with keys 'card' (physical card data) and 'card.virtualCard' (associated virtual card data)
        
        Raises:
            requests.HTTPError: Raised for invalid API requests (4XX client errors or 5XX server errors)
        
        Tags:
            retrieve, card, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def emboss(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Embosses a physical card by sending a PATCH request to the specified URL with the provided request body.
        
        Args:
            request_body: Optional dictionary containing data for embossing request. Defaults to None.
        
        Returns:
            The JSON response from the server.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            emboss, card-management, physical-card, update, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def activate(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Activates a physical card by sending a PATCH request to update its status to 'active'. This should be called after the user receives the card and not before 24 hours have passed since the embossing.
        
        Args:
            request_body: Optional request body (any type) for the activation request.
        
        Returns:
            Response data from the successful activation in JSON format.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            activate, card, management, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def block(self, isVirtual: Annotated[bool, ''] = None) -> Any:
        """
        Temporarily blocks a physical/virtual card by updating its status to 'blocked'.
        
        Args:
            isVirtual: Boolean flag indicating whether to block the virtual card (True) or physical card (False)
        
        Returns:
            JSON response containing the updated card status and details
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid requests, authentication failures, or server errors when the API request fails
        
        Tags:
            block, card-management, api, important
        """
        request_body = {
            "isVirtual": isVirtual,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def unblock(self, isVirtual: Annotated[bool, ''] = None) -> Any:
        """
        Unblocks a physical or virtual card by changing its status to 'active'.
        
        Args:
            isVirtual: Boolean flag indicating whether to unblock the virtual card (True) or physical card (False) associated with this account
        
        Returns:
            Deserialized JSON response containing updated card status information
        
        Raises:
            requests.HTTPError: Raised if the PATCH request fails, typically due to invalid card_id or authorization issues
        
        Tags:
            unblock, card-management, api-integration, important
        """
        request_body = {
            "isVirtual": isVirtual,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def cancel(self, description: Annotated[Any, ''] = None, reason: Annotated[Any, ''] = None) -> Any:
        """
        Cancel a physical card by updating its status to 'canceled' via API.
        
        Args:
            description: Free-text field describing cancellation reason.
            reason: Cancellation reason code: 'P' for Loss, 'R' for Theft.
        
        Returns:
            Parsed JSON response containing cancellation confirmation.
        
        Raises:
            requests.HTTPError: Raised for failed API requests (non-2xx status codes).
        
        Tags:
            cancel, card, async-job, api, important
        """
        request_body = {
            "description": description,
            "reason": reason,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def virtual_card_create(self, ) -> dict[str, Any]:
        """
        Creates or retrieves a virtual card linked to a physical card that was previously requested and approved, updating the security code with each transaction.
        
        Returns:
            Dictionary containing the virtual card details including updated security code from the API response
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (non-2xx status codes)
            RequestException: Raised for network connectivity issues or request failures
        
        Tags:
            virtual-card, card-api, security-update, financial-services, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def virtual_card_security_code(self, request_body: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Fetches the current security code (CVC) of a virtual card.
        
        Args:
            request_body: Optional request body; if provided, it should be annotated with any data type (default: None).
        
        Returns:
            A dictionary containing the security code details of the virtual card.
        
        Raises:
            HTTPError: Raised if the HTTP request to fetch the security code fails, typically due to network issues or invalid responses.
        
        Tags:
            fetch, security-code, virtual-card, management, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def card_password_create(self, password: Annotated[Any, ''] = None, passwordConfirm: Annotated[Any, ''] = None) -> Any:
        """
        Creates a password for a physical card to activate it.
        
        Args:
            password: The password to set for the card; can be of any type.
            passwordConfirm: Confirmation of the password set; must match the password.
        
        Returns:
            JSON response from the server after creating the password.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
        
        Tags:
            create, activate, card-management, important
        """
        request_body = {
            "password": password,
            "passwordConfirm": passwordConfirm,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def card_password_change(self, password: Annotated[Any, ''] = None, passwordConfirm: Annotated[Any, ''] = None, passwordOld: Annotated[Any, ''] = None) -> Any:
        """
        Activates a physical card by updating its password and changing its status to 'active'.
        
        Args:
            password: New password for card activation (must match passwordConfirm)
            passwordConfirm: Confirmation of new password
            passwordOld: Current/previous password of the card
        
        Returns:
            Parsed JSON response containing updated card status from API
        
        Raises:
            requests.HTTPError: Raised for 4XX/5XX responses from API endpoints
        
        Tags:
            card-activation, password-update, api-operation, physical-card, status-change, important
        """
        request_body = {
            "password": password,
            "passwordConfirm": passwordConfirm,
            "passwordOld": passwordOld,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_autorize(self, acquirer_code: Annotated[Any, ''] = None, additional_data: Annotated[Any, ''] = None, authorization_code_reason: Annotated[Any, ''] = None, capture: Annotated[dict[str, Any], ''] = None, card_acceptor: Annotated[dict[str, Any], ''] = None, card_id: Annotated[Any, ''] = None, cardholder_billing: Annotated[dict[str, Any], ''] = None, mti: Annotated[Any, ''] = None, pan: Annotated[Any, ''] = None, pinblock: Annotated[Any, ''] = None, pos_data: Annotated[Any, ''] = None, processing_code: Annotated[Any, ''] = None, settlement_date: Annotated[Any, ''] = None, settlement_value: Annotated[dict[str, Any], ''] = None, stan: Annotated[Any, ''] = None) -> Any:
        """
        Runs a webhook to authorize a debit transaction using a prepaid card, triggered by the card's processing company (Orbitall), which updates the customer's balance and statement.
        
        Args:
            acquirer_code: Acquirer code associated with the transaction.
            additional_data: Any additional data provided for the transaction.
            authorization_code_reason: The reason for the authorization code.
            capture: Information related to capturing the transaction.
            card_acceptor: Details about the card acceptor.
            card_id: The ID of the card used.
            cardholder_billing: Billing information for the cardholder.
            mti: Merchant type indicator.
            pan: Primary account number of the card.
            pinblock: PIN block if applicable.
            pos_data: Point of sale data.
            processing_code: Code for transaction processing.
            settlement_date: Date for settlement.
            settlement_value: Value associated with the settlement.
            stan: System trace audit number.
        
        Returns:
            JSON response from the transaction authorization API.
        
        Raises:
            requests.RequestException: Raised if there is a network problem or the API endpoint returns an unsuccessful status code.
        
        Tags:
            authorize, debit, webhook, prepaid-card, important, api-call, balance-update
        """
        request_body = {
            "acquirer_code": acquirer_code,
            "additional_data": additional_data,
            "authorization_code_reason": authorization_code_reason,
            "capture": capture,
            "card_acceptor": card_acceptor,
            "card_id": card_id,
            "cardholder_billing": cardholder_billing,
            "mti": mti,
            "pan": pan,
            "pinblock": pinblock,
            "pos_data": pos_data,
            "processing_code": processing_code,
            "settlement_date": settlement_date,
            "settlement_value": settlement_value,
            "stan": stan,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_card_created1(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Handles the creation of a prepaid card by confirming the request and returning physical card details.
        
        Args:
            request_body: Optional request body data (defaults to None)
        
        Returns:
            A JSON response containing the account ID and details of the physical and virtual cards created.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            card-creation, core-api, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_authorize(self, account_id: Annotated[Any, ''] = None, amount: Annotated[float, ''] = None, card_acceptor: Annotated[dict[str, Any], ''] = None, currency: Annotated[Any, ''] = None, date: Annotated[Any, ''] = None, last_4_digits: Annotated[Any, ''] = None, stan: Annotated[Any, ''] = None, status: Annotated[Any, ''] = None) -> Any:
        """
        Processes prepaid card transactions by verifying client balance and handling transaction approval or reversal.
        
        Args:
            account_id: ID of the client's account (optional)
            amount: Transaction amount (optional)
            card_acceptor: Details of the card acceptor (optional)
            currency: Currency of the transaction (optional)
            date: Date of the transaction (optional)
            last_4_digits: Last four digits of the card (optional)
            stan: Stan number for the transaction (optional)
            status: Status of the transaction (e.g., approved, reversed) (optional)
        
        Returns:
            JSON response from the API request
        
        Raises:
            requests.exceptions.HTTPError: Raised if there is a problem with the HTTP request
        
        Tags:
            authorize, transaction, prepaid-card, core-api, important
        """
        request_body = {
            "account_id": account_id,
            "amount": amount,
            "card_acceptor": card_acceptor,
            "currency": currency,
            "date": date,
            "last_4_digits": last_4_digits,
            "stan": stan,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_authorize_information(self, account_id: Annotated[Any, ''] = None, amount: Annotated[float, ''] = None, card_acceptor: Annotated[dict[str, Any], ''] = None, currency: Annotated[Any, ''] = None, date: Annotated[Any, ''] = None, international: Annotated[dict[str, Any], ''] = None, last_4_digits: Annotated[Any, ''] = None, stan: Annotated[Any, ''] = None) -> Any:
        """
        Handles and reports failed transactions directly to the Core API.
        
        Args:
            account_id: The ID of the account associated with the transaction.
            amount: The amount of the failed transaction.
            card_acceptor: Details about the card acceptor.
            currency: The currency used in the transaction.
            date: The date of the failed transaction.
            international: International transaction details.
            last_4_digits: The last four digits of the card number.
            stan: The System Trace Audit Number (STAN) of the transaction.
        
        Returns:
            A JSON response from the Core API after reporting the transaction.
        
        Raises:
            HTTPError: Raised if the POST request to the Core API fails.
        
        Tags:
            core-api, transaction-reporting, important
        """
        request_body = {
            "account_id": account_id,
            "amount": amount,
            "card_acceptor": card_acceptor,
            "currency": currency,
            "date": date,
            "international": international,
            "last_4_digits": last_4_digits,
            "stan": stan,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def webhook_international_transactions(self, Date: Annotated[Any, 'Data da transação'] = None, request_body: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Retrieves international transaction information to generate a transaction report with IOF.
        
        Args:
            Date: The date of the transaction. Default is None.
            request_body: Request body for additional data. Default is None.
        
        Returns:
            A dictionary containing transaction details, including calculated IOF for each transaction.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            report, transaction, iof, international, important, core-api
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "Date": Date,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()


    def list_tools(self):
        return [
            
            self.get_cards,
            self.card_request,
            self.webhook_card_created,
            self.try_webhook_card_created,
            self.get_card,
            self.emboss,
            self.activate,
            self.block,
            self.unblock,
            self.cancel,
            self.virtual_card_create,
            self.virtual_card_security_code,
            self.card_password_create,
            self.card_password_change,
            self.webhook_autorize,
            self.webhook_card_created1,
            self.webhook_authorize,
            self.webhook_authorize_information,
            self.webhook_international_transactions
        ] 