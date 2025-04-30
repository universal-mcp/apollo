from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class ApolloApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='apollo', integration=integration, **kwargs)
        self.base_url = "{{card_base_url}}"


    def get_cards(self, accountId: Annotated[Any, 'Id da conta do core brancário'] = None, cardId: Annotated[Any, 'Id do cartão'] = None, document: Annotated[Any, 'Documento'] = None, endCancelDate: Annotated[Any, 'Data final do cancelamento do cartão'] = None, endCreateDate: Annotated[Any, 'Data final da criação do cartão'] = None, endEmbossDate: Annotated[Any, 'Data final do emboçamento do cartão'] = None, id: Annotated[Any, 'Id do registro'] = None, limit: Annotated[Any, 'Limite de registros por página'] = None, page: Annotated[Any, 'Página atual'] = None, startCancelDate: Annotated[Any, 'Data inicial do cancelamento do cartão'] = None, startCreateDate: Annotated[Any, 'Data inicial da criação do cartão'] = None, startEmbossDate: Annotated[Any, 'Data inicial do emboçamento do cartão'] = None, status: Annotated[Any, 'Status do cartão (processing/ created/ active/ blocked/ canceled)'] = None) -> dict[str, Any]:
        """
        Get Cards. Objetivo: Buscar cartões dos clientes.  

Basicamente as informações retornadas são:
- "cards": Lista de todos os cartões físicos do cliente.
- "cards"."virtualCard": Cartão virtual atrelado ao cartão físico.
        
        Tags: Apollo Card API
        
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
        Card Request. Objetivo: Solicitar a criação de um novo cartão pré-pago.
A cada chamada deste método um novo cartão físico é solicitado para o cliente, podendo ele ter mais de um cartão.    

A criação do cartão ocorre de forma assíncrona, tendo sua confirmação através de webhook específico. Neste momento o cartão fica com status "processing".    

O uso deste método é obrigatório mesmo que o cliente só vá usar cartão virtual, pois o cartão virtual sempre é atrelado internamente à um físico mesmo sem ser embossado.    

Basicamente devem ser enviadas as seguintes informações:
- “accountId”:  Código da conta do cliente
- “document”: CPF ou CNPJ do cliente
- “address”: Endereço de correspondência para envio do cartão físico.

        
        Tags: Apollo Authorize API
        
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
        Webhook Card Created. Objetivo: Confirmar solicitação de criação de um cartão físico.   

Este método deve ser executado pela empresa emissora do cartão (Orbitall).  

Neste momento o cartão muda seu status de "Processing" para "Created".  

De acordo com a configuração do parceiro, neste momento o cartão físico será embossado automaticamente.  

De acordo com a configuração do parceiro, neste momento o cartão virtual será criado automaticamente.
        
        Tags: Apollo Card API
        
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
        Try Webhook Card Created. Objetivo: Buscar as informações que viriam pelo webhook-card-created.  

Utilizado caso haja alguma falha no webhook que informa quando uma solicitação de cartão foi aprovada.  

As informações de dentro do "data" podem ser utilizados para passar no body do webhook-card-created caso seja necessário.
        
        Tags: Apollo Card API
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_card(self, ) -> dict[str, Any]:
        """
        Get Card. Objetivo: Buscar dados de um cartão.   

Basicamente as informações retornadas são:
- "card": Dados do cartão físico.
- "card"."virtualCard": Dados do cartão virtual atrelado ao cartão físico.      



Route param:
- card_id: Código do cartão físico ("cards.id")
        
        Tags: Apollo Card API
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def emboss(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Emboss. Objetivo: Embossamento do cartão físico.   

Deve ser chamada depois que a solicitação do cartão foi confirmada (status "created").   

Não altera o status do cartão.  

Route param:
- card_id: Código do cartão físico ("cards.id")
        
        Tags: Apollo Card API
        
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
        Activate. Objetivo: Ativar cartão físico.    

Deve ser chamada quando usuário receber o cartão físico. Só é permitido chamar este método após 24 horas do embossamento.  

Status do cartão é alterado para "active".   

Route param:
- card_id: Código do cartão físico ("cards.id")

        
        Tags: Apollo Card API
        
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
        Block. Objetivo: Bloquear temporariamente um cartão físico.  

Status do cartão é alterado para "blocked".      

Route param:
- card_id: Código do cartão físico ("cards.id")

Body:
- isVirtual: Campo flag(bool) que indica se o bloqueio é referente ao cartão físico ou cartão virtual
        
        Tags: Apollo Card API
        
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
        Unblock. Objetivo: Desbloquear temporariamente um cartão físico.

Status do cartão é alterado para "active".      

Route param:
- card_id: Código do cartão físico ("cards.id")

Body:
- isVirtual: Campo flag(bool) que indica se o desbloqueio é referente ao cartão físico ou cartão virtual
        
        Tags: Apollo Card API
        
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
        Cancel. Objetivo: Cancelar um cartão físico.  

Status do cartão é alterado para "canceled".      

Route param:
- card_id: Código do cartão físico ("cards.id")  


Body param:
- description: Campo livre com descrição sobre motivo do cancelamento.   
- reason: Enviar "P" para Perda ou "R" para Roubo.   
        
        Tags: Apollo Card API
        
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
        Virtual Card - Create. Objetivo: Recuperar cartão digital a partir de um físico.   

Para criar um cartão virtual é necessário primeiramente realizar a solicitação de um cartão (*Card Request*).  

Após aprovada a solicitação, o cartão físico fica com status "created" e então é possível solicitar o cartão virtual.  

Uma vez criado, este metodo não cria um novo cartão virtual mas somente retonas os dados do cartão existente com o código de segurança atualizado, sendo este atualizado a cada nova transação do cartão.      

Route param:
- card_id: Código do cartão físico ("cards.id")

        
        Tags: Apollo Card API
        
        """
        
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def virtual_card_security_code(self, request_body: Annotated[Any, ''] = None) -> dict[str, Any]:
        """
        Virtual Card - Security Code. Objetivo: Retornar o código de segurança atual do cartão virtual (CVC).   

Este método deve ser utilizado toda vez que se deseja exibir o código do cartão virtual ao cliente, pois este código é dinâmico, podendo ser alterado a cada nova transação.   

Route param:
- card_id: Código do cartão físico ("cards.id")

        
        Tags: Apollo Card API
        
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
        Card Password Create. Objetivo: Ativar cartão físico.    

Deve ser chamada quando usuário receber o cartão físico. Só é permitido chamar este método após 24 horas do embossamento.  

Status do cartão é alterado para "active".   

Route param:
- card_id: Código do cartão físico ("cards.id")

        
        Tags: Apollo Card API
        
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
        Card Password Change. Objetivo: Ativar cartão físico.    

Deve ser chamada quando usuário receber o cartão físico. Só é permitido chamar este método após 24 horas do embossamento.  

Status do cartão é alterado para "active".   

Route param:
- card_id: Código do cartão físico ("cards.id")

        
        Tags: Apollo Card API
        
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
        Webhook Autorize. Objetivo: Autorizar um débito enviado pelo uso do cartão pré-pago.   

Método disparado pela empresa processadora do cartão (Orbitall), no momento em que cliente utiliza o cartão.   

A autorização será enviada para API do Core, que deve devolver se o cliente tem saldo suficiente para o débito. Além de ser responsável por atualizar o saldo e extrato do cliente.


        
        Tags: Apollo Authorize API
        
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
        Webhook Card Created. Objetivo: Confirmar a solicitação de criação de um cartão pré-pago.   

Este método deve ser desenvolvido na API do Core para receber a confirmação de que o cartão solicitado foi criado, retornando os dados cartão físico.   

Basicamente os dados retornados são:
- "accountId": Código da conta do usuário.
- "card": Dados do cartão físico criado.
- "card"."virtualCard": Dados do cartão virtual criado.

Neste momento o cartão físico fica com status "Created" 
        
        Tags: Core API
        
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
        Webhook Authorize. Objetivo: Processar transações dos cartões pré-pago.   

Este método deve ser desenvolvido na API do Core para gerenciar as transações dos cartões pré-pago, que são disparadas pela bandeira quando um cliente utilizar o cartão.  

Resumidamente a bandeira faz uma chamada à API da empresa emissora do cartão (Orbitall), que faz validações iniciais sobre a transação, e posteriomente chama a API Apollo Authorize para verificar se o cliente tem saldo.   

A Apollo Authorize identifica o cartão e chama a API Core (exmeplo, Lírio API) do parceiro correspondente. Este metodo pode ser chamada em duas situações diferentes:

1. Autorizar Transação ("Status":"approved") 
> A API do Core deve verificar se o cliente tem saldo, e retornar se a transação de débito foi autorizada. Caso o débito seja aprovado, o saldo e extrato do cliente devem ser atualizados. Para compras internacionais o IOF deve ser calculado e considerado no total da transação.

2. Desfazer Transação ("Status": "resufed")
> A API do Core deve desfazer determinada transação, creditando o valor da transação no saldo do cliente, além de atualizar extrato.


*Transações Internacionais*

Compras internacionais retornam informações a mais como:
* CaptureAmount: Valor na moeda real da compra
* CaptureCurrency: Sigla da moeda real da compra
* SettlementeAcount: Valor na moeda utilizada como base para conversão
* SettlementeCurrency: Sigla da moeda utilizada como base para conversão
        
        Tags: Core API
        
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
        Webhook Authorize Information. Objetivo: Informar tentativa de transação não realiza com sucesso.   

Este método deve ser desenvolvido na API do Core para receber as transações dos cartões pré-pago, que não foram concretizadas. Por algum motivo a transação já foi barrada antes de chegar na verificação de saldo do cliente.
        
        Tags: Core API
        
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
        Webhook International Transactions. Objetivo: Retornar informações de transações internacionais para gerar relatório de transações com IOF.

Além das informações que o Authorize envia para o Core no momento de autorizar a transação, o campo "Tax" deve ser retornado contendo o valor do IOF calculado para a transação.
        
        Tags: Core API
        
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