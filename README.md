# API_REST_Hoteis

# 1 Consultar Hotéis

Requisição
Requisição para listar todos os hotéis do sistema, podendo opcionalmente receber filtros personalizados via path, de forma que se o cliente não definir nenhum parâmetro de consulta (nenhum filtro), os parâmetros receberão os valores padrão. 

	Possíveis parâmetros de consulta
	cidade ⇒ Filtrar hotéis pela cidade escolhida. Padrão: Nulo 

	estrelas_min ⇒ Avaliações mínimas de hotéis de 0 a 5. Padrão: 0

	estrelas_max ⇒ Avaliações máximas de hotéis de 0 a 5. Padrão: 5

	diaria_min ⇒ Valor mínimo da diária do hotel de R$ 0 a R$ 10.000,00. Padrão: 0

	diaria_max ⇒ Valor máximo da diária do hotel de R$ 0 a R$ 10.000,00. Padrão: 10000

	limit ⇒ Quantidade máxima de elementos exibidos por página. Padrão: 50

	offset ⇒ Quantidade de elementos pular (geralmente múltiplo de limit). Padrão: 0

# Método : GET

URL = /hoteis?estrelas_min=4.5&limit=10&offset=0&diaria_max=600

Como resposta, obtém-se uma lista de hotéis que se enquadram nos filtros da requisição acima:

s
