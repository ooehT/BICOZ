# TP-engenharia-2
Plataforma de Servicos para Republicas

Este projeto e uma aplicacao desenvolvida para conectar rapidamente Moradores de Republica a Prestadores de Servico de confianca para resolver necessidades diarias e urgencias (como problemas eletricos, gas, fretes, etc.).

Tipos de Usuarios

O sistema possui tres tipos principais de usuarios:

Moradores da Republica (Clientes): Usuarios que buscam servicos rapidos e confiaveis.

Prestadores de Servico: Profissionais que oferecem servicos de manutencao, frete, etc.

Admin: Gerenciadores da plataforma.

Funcionalidades Principais

Para o Prestador de Servico

Status de Disponibilidade em Tempo Real

Descricao: Botao simples na tela inicial para alternar o status de trabalho entre "Disponivel" e "Ocupado".

Regras de Negocio: O status e atualizado em tempo real no banco de dados.

UI/UX: Cores indicativas claras (Verde para Disponivel, Vermelho para Ocupado).

Cadastro de Perfil Profissional

Descricao: Criacao de perfil contendo Nome, Oficio (ex: encanador, eletricista) e Telefone.

Regras de Negocio: Validacao rigorosa de telefone (exigencia de 11 digitos) e selecao de oficios baseada em uma lista pre-definida.

Para o Morador de Republica (Cliente)

Busca e Filtro de Servicos

Descricao: Navegacao por categorias de servicos (ex: Gas, Eletrica, Frete).

UI/UX: Interface intuitiva utilizando icones para representar cada categoria. Ao clicar, a lista exibe apenas os profissionais da area selecionada.

Visualizacao Baseada em Disponibilidade

Descricao: Otimizacao para urgencias, garantindo que o cliente encontre quem pode atende-lo imediatamente.

Regras de Negocio: A ordenacao padrao da lista prioriza profissionais com status "Disponivel".

UI/UX: Profissionais "Ocupados" aparecem no final da lista, destacados com fotos acinzentadas.

Proximos Passos (Backlog Futuro)

Avaliacao de Confianca (Sistema de Reviews): Permitir que os moradores avaliem os prestadores com uma nota de 1 a 5 estrelas. O objetivo e aumentar a seguranca dos estudantes ao permitir a entrada de prestadores nas republicas.
