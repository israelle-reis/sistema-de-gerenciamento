# sistema-de-gerenciamento
DESCRIÇÃO DO PROGRAMA
Este programa foi criado em Python com a finalidade de simular o registro e gerenciamento básico de um produto.
O sistema possibilita que o usuário forneça informações sobre o produto e execute ações como visualização, cálculo de estoque, aplicação de desconto e verificação de disponibilidade.

LÓGICA PARA O DESENVOLVIMENTO/ COMO EXECUTAR

Primeiro pensamos que o sistema deve solicitar ao usuário as informações básicas de um produto, como o nome, a quantidade e o preço. Após receber esses dados, o programa deve determinar se o produto está disponivel (Se a quantidade for maior que zero -> produto disponível (True), Caso contrário -> produto indisponivel(False). Em seguida, o sistema deve exibir um menu de opções para um o usuário escolher qual operação deseja realizar. Dependendo da opção escolhida, o programa executa diferentes ações: Exibir informações do produto: O sistema irá apresentar os dados informados(nome, quantidade e preço), calcular o valor total em estoque: O programa realizará uma operação matemática: multiplica a quantidade pelo preço (total = quantidade * preco), Além disso, o menu exibirá a opção Aplicar desconto ao preço: o usuário informa um percentual de desconto. O sistema calcula o valor do desconto e exibe o novo valor (novo_preco = preco - (preco * desconto/100)). O menu também sugerirá a opção de Confirmar se a quantidade cumpre um valor mínimo: O usuário informa uma quantidade mínima ideal para o estoque, o programa compara esse valor com a quantidade atual usando uma condição (quantidade >= minimo).Se a quantidade for maior ou igual ao mínimo, o estoque é considerado suficiente. Na sequência, a opção atualizar a quantidade do produto: o sistema solicita uma nova quantidade ao usuário e substitui o valor antigo, após a atualização, a variável disponivel é recalculada com base na nova quantidade (quantidade > 0).

EXEMPLO DE USO
Entrada do usuário:

Nome: Cimento
Quantidade: 25
Preço: R$ 32.50 

Saída (opção 1)
INFORMAÇÕES
Nome: Cimento
Quantidade: 25
Preço: R$ 32.50
Status: Disponível

Saída (opção 2)
Valor total em estoque: R$ 812.5

Saída (opção 3)
Digite o percentual de desconto: 10
Preço com desconto: R$ 29.25

Saída (opção 4)
Digite a quantidade mínima ideal: 30
Estoque baixo! Repor produto.
Saída (opção 5)
Estoque atual: 25
Digite a nova quantidade:0
Quantidade atualizada!
