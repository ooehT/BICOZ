[requisitos_plataforma_de_servi_os_para_rep_blicas.md](https://github.com/user-attachments/files/34295974/requisitos_plataforma_de_servi_os_para_rep_blicas.md)
# Requisitos — Plataforma de Serviços para Repúblicas

## 1. Visão do Produto
A **Plataforma de Serviços para Repúblicas** é uma aplicação web desenvolvida para conectar rapidamente moradores de repúblicas estudantis a prestadores de serviços de confiança (como eletricistas, encanadores e chaveiros) para a resolução de urgências e necessidades do dia a dia. Seu principal diferencial em relação a plataformas genéricas é o foco na velocidade e no atendimento imediato, destacando visualmente os profissionais disponíveis em tempo real para minimizar o tempo de espera dos estudantes em situações emergenciais.

## 2. Papéis de Usuário

| Papel | Descrição |
|-------|-----------|
| **Morador da República (Cliente)** | Estutante ou morador responsável por solicitar serviços rápidos e emergenciais para a manutenção da república. |
| **Prestador de Serviço** | Profissional autônomo ou técnico que oferece serviços de manutenção, frete ou reparos e gerencia sua disponibilidade na plataforma. |
| **Administrador (Admin)** | Gerenciador do sistema responsável por supervisionar a plataforma, categorias e contas ativas. |

---

## 3. Histórias de Usuário

### H01 — Alternar Status de Disponibilidade (Essencial)
**Como** Prestador de Serviço, **eu quero** alternar meu status entre "Disponível" e "Ocupado" com um único clique na tela inicial **para** informar aos clientes se posso atender a chamados imediatamente.

**Critérios de aceitação:**
- [ ] O sistema permite a alteração do status por meio de um botão simples na página principal do prestador.
- [ ] O status é atualizado imediatamente no banco de dados e refletido visualmente com cores indicativas (Verde para "Disponível" e Vermelho para "Ocupado").

---

### H02 — Cadastro de Perfil Profissional (Essencial)
**Como** Prestador de Serviço, **eu quero** cadastrar meu perfil informando meu nome, telefone e selecionando meu ofício **para** que os moradores de repúblicas possam me identificar e entrar em contato.

**Critérios de aceitação:**
- [ ] O campo de telefone possui validação estrita aceitando apenas formatos com 11 dígitos numéricos (DDD + número).
- [ ] O ofício deve ser selecionado obrigatoriamente a partir de uma lista pré-definida de categorias (ex: Encanador, Eletricista, Chaveiro, Frete).

---

### H03 — Priorização de Profissionais Disponíveis (Essencial)
**Como** Morador de República, **eu quero** visualizar a lista de prestadores ordenada com os profissionais disponíveis no topo **para** encontrar rapidamente quem pode resolver minha urgência.

**Critérios de aceitação:**
- [ ] A ordenação padrão da listagem prioriza prestadores com o status "Disponível".
- [ ] Prestadores com status "Ocupado" são exibidos no final da lista e destacados com visualização diferenciada (fotos/cards acinzentados).

---

### H04 — Filtrar Serviços por Categoria (Essencial)
**Como** Morador de República, **eu quero** filtrar a lista de prestadores por categoria de serviço **para** visualizar apenas os profissionais do setor que preciso no momento.

**Critérios de aceitação:**
- [ ] A interface exibe ícones intuitivos para cada categoria pré-definida (ex: Gás, Elétrica, Encanamento, Frete).
- [ ] Ao clicar em uma categoria, a listagem é filtrada instantaneamente exibindo apenas prestadores associados àquele ofício.

---

### H05 — Visualização de Contato do Prestador (Importante)
**Como** Morador de República, **eu quero** visualizar os detalhes de contato (nome e telefone) do prestador **para** que eu possa acioná-lo via ligação ou aplicativo de mensagem.

**Critérios de aceitação:**
- [ ] Ao selecionar um prestador na lista, os dados de contato completos e atualizados ficam visíveis para o morador.

---

### H06 — Gerenciamento de Categorias pelo Administrador (Importante)
**Como** Administrador, **eu quero** cadastrar e editar as categorias de serviços predefinidas no sistema **para** manter as opções organizadas e atualizadas conforme a demanda das repúblicas.

**Critérios de aceitação:**
- [ ] O Administrador possui uma área restrita para criar, editar ou desativar categorias de serviços.

---

### H07 — Filtro Rápido por Apenas Disponíveis (Desejável)
**Como** Morador de República, **eu quero** aplicar um filtro toggle de "Apenas Disponíveis" **para** ocultar completamente os profissionais que estão ocupados.

**Critérios de aceitação:**
- [ ] Existe uma chave seletora na tela de busca que, quando ativada, remove todos os profissionais "Ocupados" da listagem.

---

### H08 — Avaliação de Confianças / Reviews (Fora do Escopo)
**Como** Morador de República, **eu quero** atribuir uma nota de 1 a 5 estrelas e um comentário ao prestador após o atendimento **para** aumentar a segurança e a recomendação para outros estudantes.

**Critérios de aceitação:**
- [ ] *Esta funcionalidade foi alocada para o backlog futuro e não será desenvolvida no presente semestre.*

---

## 4. Priorização de Requisitos

| Prioridade | Histórias |
|------------|-----------|
| **Essencial** | H01, H02, H03, H04 |
| **Importante** | H05, H06 |
| **Desejável** | H08 |
| **Fora do escopo** | H07 |

---

## 5. Requisitos Não Funcionais

| ID | Requisito |
|----|-----------|
| **RNF01** | **Usabilidade:** A interface deve ser responsiva (mobile-first), garantindo uso fluido em dispositivos móveis utilizados pelos moradores e prestadores. |
| **RNF02** | **Desempenho:** A atualização de status e o carregamento da lista de prestadores filtrada devem ocorrer em menos de 2 segundos sob condições normais de conexão. |
| **RNF03** | **Segurança:** O sistema deve garantir a validação dos dados de entrada (como o formato estrito de 11 dígitos para telefones) no front-end e no back-end para prevenir inconsistências no banco de dados. |
