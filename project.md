# Sistema Simplificado de Gestão de Funcionários por Empresa

Este documento descreve a estrutura, funcionalidades e fluxo de um sistema simples para gerenciar funcionários e empresas, com níveis de acesso diferenciados.

---

## 1. Entidades Principais

### Empresa

* Nome
* CNPJ (ou identificador único)
* Setor opcional

### Usuário/Funcionário

* Nome de usuário
* E-mail
* Senha
* Cargo
* Nível (Admin, Gerente, Funcionário)
* Empresa vinculada

---

## 2. Papéis e Permissões

### Admin

* Pode criar, editar e deletar qualquer funcionário.
* Pode transferir funcionários entre empresas.
* Pode criar novas empresas.

### Gerente

* Pode criar e editar funcionários da própria empresa.
* Não pode deletar funcionários.
* Pode mover funcionários apenas dentro da própria empresa.

### Funcionário comum

* Apenas visualiza o próprio perfil.
* Sem permissão para criar, transferir ou deletar outros funcionários.

---

## 3. Funcionalidades Principais

1. CRUD de empresas (Admin).
2. CRUD de funcionários (Admin e Gerente com restrições de empresa).
3. Transferência de funcionários entre empresas (Admin total, Gerente limitado).
4. Listagem de funcionários por empresa.
5. Autenticação segura para acesso à API (JWT ou outro método).
6. Perfil do usuário com visualização e edição limitada (para funcionários).

---

## 4. Fluxo da API

* **Admin:**

  * Gerencia todas as empresas e funcionários.
  * Pode criar novas empresas e transferir funcionários entre elas.

* **Gerente:**

  * Gerencia apenas funcionários da própria empresa.
  * Pode criar, editar e mover funcionários dentro da empresa.

* **Funcionário:**

  * Visualiza e edita apenas o próprio perfil.

---

## Observações

* Estrutura simples e direta, fácil de evoluir.
* Possibilidade de adicionar histórico de transferências, logs e outras funcionalidades no futuro.
* Permite gerenciar múltiplas empresas e funcionários com controle de acesso baseado em papéis.
