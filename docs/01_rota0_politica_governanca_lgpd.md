# Política de Governança, Ética e Conformidade com a LGPD — Taranis Black
**Projeto:** Taranis Sales AI — Challenge Alura (AI for Business) | ONE G11  
**Etapa:** Rota 0 — Base Estratégica (Obrigatória) — Etapa 3 do Template Oficial  
**Documentos de Referência:** [`docs/00_premissas_e_governanca.md`](./00_premissas_e_governanca.md) | [`docs/01_rota0_ai_canvas.md`](./01_rota0_ai_canvas.md)  
**Classificação Metodológica:** Diretrizes corporativas mandatórias baseadas em `[FATO]` e `[PROPOSTA]`  

---

## 1. Contexto e Escopo de Governança

Este documento estabelece a **Política Corporativa de Inteligência Artificial Responsável, Ética e Proteção de Dados** da Taranis Black, correspondente à **Etapa 3 da Rota 0** do template oficial da Alura.

O propósito desta política é instituir salvaguardas regulatórias, técnicas e comportamentais para o uso de ferramentas de IA no departamento comercial, assegurando conformidade estrita com a **Lei Geral de Proteção de Dados (Lei nº 13.709/2018 — LGPD)**, mitigando riscos de viés algorítmico e alucinações comerciais, e preservando a integridade jurídica da empresa em negociações B2B de alto valor.

---

## 2. Política Corporativa de IA Responsável (Matriz Pode vs. Não Pode)

A tabela abaixo define as regras operacionais mandatórias de conduta para todos os consultores comerciais, operadores e desenvolvedores do Taranis Sales AI:

| Dimensão Operacional | O QUE PODE (Práticas Autorizadas e Incentivadas) ✅ | O QUE NÃO PODE (Condutas Expressamente Proibidas) ❌ |
| :--- | :--- | :--- |
| **Uso de Ferramentas de IA** | • Utilizar ferramentas corporativas autenticadas com acordo de processamento de dados seguro (*Enterprise DPA*).<br>• Gerar rascunhos de e-mails, resumos de reuniões e planos de negociação. | • Utilizar ferramentas públicas ou gratuitas de IA sem garantia contratual de privacidade.<br>• Inserir senhas, chaves de API ou segredos industriais nos prompts. |
| **Dados de Clientes e Prospects** | • Inserir dados contextuais corporativos estritamente comerciais (nome profissional, cargo institucional, razão social e histórico da conta).<br>• Trabalhar com dados cadastrais sintetizados e dados de público corporativo. | • Inserir dados pessoais sensíveis, documentos de identificação pessoal (CPF, RG) ou contatos privados de tomadores de decisão.<br>• Inserir minutas contratuais com valores não públicos sem anonimização prévia. |
| **Saúde e Ergonomia (NR-17)** | • Empregar conceitos técnicos normativos de ergonomia (NR-17 / ABERGO) e princípios de prevenção postural e conforto.<br>• Citar laudos técnicos oficiais disponíveis no Catálogo da Taranis Black. | • **Proibição Absoluta:** Inserir atestados médicos nominais, CID, laudos clínicos ou prontuários de saúde de colaboradores de clientes.<br>• Afirmar cura de patologias (LER/DORT) ou prometer "eliminação total de passivos trabalhistas". |
| **Condições Comerciais e Prazos** | • Utilizar os preços e prazos oficiais do Catálogo (`01_Catalogo...`): linhas *ErgoPro*, *SmartDesk* e *Silence* e regras do CD de Santa Catarina.<br>• Explorar parcelamento em 30/60/90 dias e frete CIF acima de R$ 35 mil. | • Prometer descontos, prazos especiais ou condições customizadas fora da política comercial oficial da empresa.<br>• Comprometer a Taranis Black com cronogramas logísticos não homologados pelo time de Operações. |
| **Envio de Mensagens e Automação** | • Utilizar a IA como coautora e revisora de mensagens comerciais.<br>• Aplicar rigorosamente a aprovação humana (*Human-in-the-Loop*) antes de qualquer disparo. | • Realizar disparos autônomos ou automatizados sem a leitura, validação e autorização ativa de um consultor de vendas humano.<br>• Enviar mensagens em massa não personalizadas com características de spam. |

---

## 3. Identificação de Riscos de Viés e Conformidade com a LGPD

### 3.1. Mitigação de Riscos de Viés Algorítmico no Processo Comercial

No desenho de algoritmos de qualificação e priorização de oportunidades B2B (*Lead Scoring*), identificou-se um risco crítico de **viés de porte empresarial (*Size Bias*)**:

* **Descrição do Risco:** Algoritmos comerciais convencionais tendem a priorizar automaticamente empresas com grande número de colaboradores (ex: corporações com +1.000 funcionários), descartando ou atribuindo pontuação baixa a empresas de pequeno porte ou estúdios especializados.
* **Evidência Factual da Base da Taranis Black (`02_Leads_B2B_Comercial.xlsx`):**
  * O caso real da conta **Studio Alfa Arquitetura (#1044)**: possui apenas **45 colaboradores**, mas tem o **2º maior pedido de todo o pipeline da empresa (R$ 635.500,00)**, contemplando 4 Cabines Silence Quad e 45 Mesas SmartDesk Pro para um projeto de retrofit corporativo.
  * Se o algoritmo operasse com viés simples de porte, essa conta de altíssimo valor seria despriorizada.
* **Mecanismo de Mitigação Implementado:**
  * Modelagem multidimensional do *Lead Scoring*, combinando número de posições com **Ticket Estimado da Oportunidade**, **Urgência da Demanda** e **Orçamento Reservado**.
  * Trava algorítmica impedindo o descarte automático de qualquer conta com proposta superior a R$ 100.000,00, independentemente do número de colaboradores.

---

### 3.2. Conformidade Rigorosa com a LGPD (Lei nº 13.709/2018)

| Requisito Legal da LGPD | Impacto no Projeto Taranis Sales AI | Medida Prática de Conformidade Implementada |
| :--- | :--- | :--- |
| **Proteção Especial a Dados Sensíveis (Art. 11)** | Riscos relacionados a laudos ergonômicos e atestados médicos de colaboradores de empresas-alvo. | **Bloqueio Absoluto:** A Taranis Black não processa dados de saúde identificados ou identificáveis em seus sistemas comerciais. Argumentos de vendas utilizam exclusivamente dados estatísticos agregados e parâmetros gerais de conformidade com a NR-17. |
| **Base Legal para Abordagens B2B (Art. 7º, V e IX)** | Prospecção de decisores corporativos em novos clientes potenciais. | **Enquadramento em Legítimo Interesse (Art. 7º, IX) e Procedimentos Pré-Contratuais (Art. 7º, V):** Elaboração formal do Teste de Balanceamento e Proporcionalidade (*LIA — Legitimate Interests Assessment*), limitando contatos estritamente ao ambiente e interesses profissionais do titular. |
| **Direito de Oposição e Opt-Out (Art. 8º e Art. 18)** | Direito do contato profissional de não receber abordagens comerciais. | **Mecanismo de Descadastramento Imediato:** Inclusão de rodapé padronizado em 100% dos e-mails gerados, permitindo ao destinatário solicitar a interrupção imediata dos contatos, com exclusão definitiva de listas de prospecção em até 24 horas. |
| **Minimização de Dados (Art. 6º, III)** | Coleta excessiva de dados durante pesquisas comerciais. | **Princípio da Necessidade Estrita:** Os modelos e formulários coletam exclusivamente: Nome Profissional, E-mail Corporativo, Cargo e Empresa. É proibido o armazenamento de dados biográficos ou de vida pessoal. |
| **Segurança e Contratos com Fornecedores (Art. 46)** | Tráfego de dados empresariais por provedores de IA em nuvem. | **Cláusulas de DPA (*Zero Data Retention*):** Contratação exclusiva de planos empresariais de IA que assegurem que nenhum dado trafegado é retido para treinamento de modelos de terceiros, com criptografia ponta a ponta (TLS 1.3 / AES-256). |

---

## 4. Comitê de Ética em IA e Rituais de Auditoria

Para assegurar que as diretrizes desta política sejam vivenciadas na rotina da organização e que a conformidade evolua com as novas versões dos modelos, institui-se o **Comitê Corporativo de Ética e Governança de IA da Taranis Black**.

### 4.1. Composição Multidisciplinar do Comitê

O comitê é composto por 5 membros permanentes com competências complementares:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ COMPOSIÇÃO DO COMITÊ DE ÉTICA EM IA — TARANIS BLACK                   │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Encarregado de Dados (DPO) / Consultor Jurídico LGPD [Liderança]   │
│ 2. Coordenador Comercial / Head de Operações de Vendas (Sales Ops)     │
│ 3. Especialista em Segurança da Informação & Infraestrutura de TI      │
│ 4. Ergonomista Chefe / Engenheiro de Segurança do Trabalho (NR-17)    │
│ 5. Gestor de Recursos Humanos & People Analytics                       │
└────────────────────────────────────────────────────────────────────────┘
```

1. **DPO / Jurídico (Presidente do Comitê):** Guardião da conformidade com a LGPD, avaliação de bases legais e monitoramento de riscos regulatórios.
2. **Coordenador Comercial / Sales Ops:** Responsável por garantir que as diretrizes éticas não engessem o processo de vendas e que a equipe mantenha a disciplina de uso.
3. **Especialista em TI e Segurança:** Responsável pelo controle de acessos (RBAC), chaves de API, monitoramento de conexões seguras e avaliação técnica de fornecedores de IA.
4. **Ergonomista Chefe (Certificação ABERGO):** Validador técnico das informações de conformidade biomecânica e adequação normativa à NR-17 incluídas nas bases de conhecimento da IA.
5. **Gestor de RH / People:** Responsável pelo monitoramento do clima organizacional, acompanhamento de eventuais resistências culturais e capacitação ética contínua dos colaboradores.

---

### 4.2. Cadência dos Rituais de Auditoria e Controle

O comitê opera sob três rituais formais com objetivos e periodicidades distintas:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ RITUAIS DE AUDITORIA E MONITORAMENTO CONTÍNUO                          │
├───────────────────────┬───────────────────────┬────────────────────────┤
│ RITUAL SEMANAL        │ RITUAL MENSAL         │ RITUAL TRIMESTRAL      │
│ (AMOSTRAGEM OPERAC.)  │ (QUALIDADE & VIÉS)    │ (GOVERNANÇA & LGPD)    │
│                       │                       │                        │
│ • Amostragem de 10%   │ • Auditoria de aluci- │ • Auditoria de acessos │
│   dos rascunhos de    │   nações de catálogo  │   e revogação RBAC     │
│   e-mails e CRM       │ • Avaliação de viés no│ • Validação de DPA com │
│ • Foco em checagem de │   Lead Scoring        │   provedores de IA     │
│   Human-in-the-Loop   │ • Ajuste fino de      │ • Relatório Executivo  │
│ • Responsável: Sales  │   System Prompts      │   para a Diretoria     │
│   Ops & Ergonomista   │ • Responsável: Comitê │ • Responsável: DPO &   │
│                       │   Técnico             │   Segurança da Inform. │
└───────────────────────┴───────────────────────┴────────────────────────┘
```

1. **Ritual Semanal — Auditoria Operacional por Amostragem (10%):**
   * *Escopo:* Análise de uma amostra aleatória de 10% dos e-mails enviados e registros gerados no CRM.
   * *Objetivo:* Verificar se os consultores estão mantendo a revisão humana obrigatória (*Human-in-the-Loop*) e se não houve inserção indevida de dados proibidos.
2. **Ritual Mensal — Revisão Tática de Prompts e Alucinações:**
   * *Escopo:* Revisão das saídas geradas pelo Copiloto de Vendas e pelo gerador de e-mails.
   * *Objetivo:* Identificar desvios de tom de voz, verificar se houve alguma tentativa do modelo de inventar condições fora do Catálogo Oficial e atualizar a base RAG caso novos produtos sejam homologados.
3. **Ritual Trimestral — Auditoria Executiva de Governança e LGPD:**
   * *Escopo:* Avaliação formal de segurança da informação, auditoria de logs de acesso e revisão dos relatórios de impacto à proteção de dados (RIPD).
   * *Objetivo:* Apresentar à Diretoria Executiva da Taranis Black o parecer de conformidade ética, incidentes prevenidos e recomendações de evolução tecnológica.
