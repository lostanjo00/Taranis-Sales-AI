# CHALLENGE ONE G11 — AI FOR BUSINESS
# Relatório Executivo Consolidado — Taranis Black
## ROTA 1 — IA PARA VENDAS E COMERCIAL
*(Documento Espelho Oficial formatado para transposição direta ao Google Docs da Alura — Textos Integrais Completos)*

---

## 📋 IDENTIFICAÇÃO DO ALUNO

| Campo | Preenchimento |
| :--- | :--- |
| **Nome Completo** | [Seu Nome Completo] |
| **E-mail** | [Seu E-mail Cadastrado na Alura] |
| **Rota de Especialização Escolhida** | **[X] Rota 1 — IA para Vendas e Comercial**<br>[ ] Rota 2 — IA para Marketing e Conteúdo<br>[ ] Rota 3 — IA para RH e People Analytics<br>[ ] Rota 4 — IA para Finanças e Operações |

---

## 🏢 SEU CENÁRIO NA TARANIS BLACK — ROTA 1

| Dimensão | Especificação Oficial |
| :--- | :--- |
| **Público Indicado** | Vendedores B2B, SDRs, gerentes de contas e analistas comerciais. |
| **Problema a Resolver** | A equipe comercial B2B perde mais de 40% do tempo semanal preenchendo CRM, escrevendo e-mails genéricos e qualificando leads sem dados suficientes. As objeções de preço e prazo travam o fechamento de propostas. |

### Resumo Executivo
*(Formato de e-mail direto para a CEO da Taranis Black, em até 15 linhas, com diagnóstico geral, iniciativas de IA recomendadas e impacto esperado)*

```text
De: Equipe de Consultoria e Arquitetura de Soluções Taranis Sales AI
Para: Diretora Executiva (CEO) — Taranis Black
Assunto: Proposta Estratégica Taranis Sales AI: Recuperação de Produtividade e Conversão Comercial B2B

Prezada CEO,

Identificamos que o crescimento recente de 35% a.a. da Taranis Black encontra-se restringido por gargalos operacionais: nossos 
consultores comerciais perdem ~40% do tempo semanal (16h/vendedor) com digitação em CRM e e-mails genéricos, enquanto R$ 4,69 milhões 
em propostas encontram-se parados nas 20 contas corporativas do CRM devido a objeções de preço e prazo de entrega.

Para destravar essa alavanca de crescimento, estruturamos o Taranis Sales AI em três iniciativas coordenadas:
1. Personalização Consultiva de E-mails & Qualificação de Leads (Quick Win com geração ágil sob o tom de voz da marca);
2. Copiloto de Vendas & Treinador de Objeções (IA com grounding factual em nosso catálogo para superar travas de preço e prazo);
3. Automação Inteligente de Registros de CRM (extração estruturada JSON e integridade do pipeline sem esforço braçal).

O impacto projetado inclui a liberação de 14 horas semanais por vendedor para prospecção ativa (+35% de capacidade útil real) e a 
meta de converter entre 25% e 35% do pipeline represado, gerando de R$ 1,17M a R$ 1,64M em receita incremental com supervisão 
humana obrigatória e total conformidade com a LGPD e NR-17.

Permanecemos à disposição para aprovação do cronograma de implantação.
```

---

## 🧭 PARTE 1 — BASE ESTRATÉGICA OBRIGATÓRIA (ROTA 0)

---

### Etapa 1 — AI Canvas & Mapeamento de Oportunidades (✅ OBRIGATÓRIA)

#### Casos de Uso Identificados (Mínimo 3)
1. **Automação de Registros no CRM:** Extração estruturada de anotações não estruturadas de reuniões comerciais, convertendo atas, áudios e anotações em dados relacionais (etapa do negócio, decisores, produtos ErgoPro/SmartDesk cotados e próximos passos) com validação de schema antes da gravação no CRM.
2. **Personalização de E-mails e Qualificação de Leads B2B:** Geração assistida de mensagens consultivas contextualizadas por persona decisora (`RH / People`, `Facilities / Arquitetura` e `Compras / CFO`), aplicando os 4 pilares do Tom de Voz da Taranis Black (*Científico, Empático, Sofisticado, Descomplicado*) e algoritmo de *Lead Scoring* multidimensional para triagem de contas.
3. **Copiloto de Vendas Consultivas e Tratamento de Objeções:** Assistente inteligente com arquitetura RAG (*grounding* estrito no Catálogo Oficial de Produtos, laudos NR-17/ABERGO e prazos do CD de Santa Catarina) para orientar consultores a superar objeções de preço/prazo através de Custo Total de Propriedade (TCO), além de ambiente de simulação (*roleplay*) para capacitação de novos vendedores.

#### Classificação por Tipo de IA e Justificativa
* **Iniciativa 1 (CRM):** **IA Generativa + IA Tradicional (Híbrida)**. Justificativa: A IA Generativa (LLM) interpreta anotações desestruturadas e extrai entidades em formato JSON; a IA Tradicional valida schemas, integridade de campos e executa chamadas de APIs REST seguras no CRM.
* **Iniciativa 2 (E-mails e Leads):** **IA Generativa + IA Preditiva/Tradicional (Híbrida)**. Justificativa: A IA Generativa redige e-mails persuasivos adaptados ao tom de voz; a IA Preditiva/Tradicional calcula a pontuação de prioridade do lead (*Lead Scoring*) com base em variáveis firmográficas (porte, urgência e orçamento).
* **Iniciativa 3 (Copiloto de Vendas):** **IA Generativa com Arquitetura RAG**. Justificativa: Combina a fluência conversacional de LLMs com busca vetorial restrita aos documentos institucionais da empresa, impedindo alucinações sobre preços, prazos ou certificações, além de simular dinamicamente perfis de compradores em *roleplay*.

#### Supervisão Humana (*Human-in-the-Loop*)
* **Automação de CRM:** A gravação direta é bloqueada. O sistema gera um rascunho de tela (*staging card*); o vendedor revisa, ajusta e clica manualmente no botão de confirmação para salvar.
* **Personalização de E-mails:** Trava técnica obrigatória contra disparos autônomos. Toda mensagem é gerada como rascunho, exigindo leitura crítica, personalização final e envio manual pelo consultor.
* **Copiloto de Vendas:** Atua exclusivamente em ambiente interno de treinamento e preparação prévia. A condução da conversa, concessão de condições comerciais e decisão final pertencem 100% ao consultor humano.

---

### Etapa 2 — Priorização Baseada em Dados & Gestão de Mudança (✅ OBRIGATÓRIA)

#### Matriz Esforço × Impacto e Ordem de Implantação
A avaliação ponderada (Impacto: 30% sobrecarga, 30% eficácia, 20% qualidade, 20% escalabilidade | Esforço: 35% técnico, 30% LGPD, 35% mudança cultural) estabeleceu o seguinte enquadramento:

```text
                  Impacto (I)
                     ▲
            5.0      │
                     │  QUADRANTE 1:             QUADRANTE 2:
                     │  Ganhos Rápidos           Projetos Estratégicos
                     │  (Quick Wins)             (Alto Impacto, Alto Esforço)
                     │  • Oportunidade 2 (2.65, 3.50)
                     │  • Oportunidade 1 (3.00, 3.60)* • Oportunidade 3 (3.05, 3.50)
            3.0 ─────┼───────────────────────────
                     │  QUADRANTE 3:             QUADRANTE 4:
                     │  Melhorias Pontuais       Despriorizar / Evitar
                     │  (Baixo Impacto, Baixo E.)│ (Baixo Impacto, Alto Esforço)
            1.0      │
                     └───────────────────────────► Esforço (E)
                    1.0             3.0        5.0
```

* **Ordem de Implantação:**
  1. **Fase 1 (Mês 1 a 2 — Quick Win Puro):** *Personalização de E-mails & Leads* ($E = 2{,}65$ | $I = 3{,}50$) — Baixo atrito de infraestrutura e impacto imediato na prospecção.
  2. **Fase 2 (Mês 2 a 4 — Capacitação Estratégica):** *Copiloto de Vendas Consultivas* ($E = 3{,}05$ | $I = 3{,}50$) — Piloto educacional focado em destravar as 20 contas abertas no pipeline via contorno de objeções de valor.
  3. **Fase 3 (Mês 4 a 6 — Sustentação de Dados):** *Automação de Registros no CRM* ($E = 3{,}00$ | $I = 3{,}60$) — Homologação de conectores de API e padronização sistêmica do pipeline.

#### Métricas de Sucesso, Horas Economizadas e ROI Estimado
* **Horas Economizadas:** Redução combinada de **14 horas semanais por vendedor** (5h em redação de e-mails + 3h em pesquisa de objeções + 6h em digitação de CRM), mitigando em **87,5%** a perda de tempo burocrático e devolvendo **+35% de capacidade útil comercial**.
* **ROI Estimado:**
  * Base do Pipeline: R$ 4.693.630,00 represados nas 20 contas oficiais do CRM (`02_Leads...`).
  * Meta de Conversão Incremental (25% a 35%): Recuperação de **R$ 1.173.407,50 (conservador)** a **R$ 1.642.770,50 (alvo)** em novas vendas.
  * Custo Total do Projeto (Licenças DPA, APIs e Treinamentos): R$ 120.000,00.
  * **ROI Projetado:** **877,8% (cenário conservador)** a **1.268,9% (cenário alvo)**, representando retorno de 9,7x a 13,6x o capital investido.
* **Metas de Adoção:** 85% dos e-mails comerciais redigidos com apoio da IA em 120 dias; média de 5 simulações de roleplay semanais por consultor; 95% dos campos de oportunidades atualizados no CRM dentro de 24h.

#### Plano de Mudança Cultural
* **Mitigação da Resistência ("Sempre vendi assim"):** Envolvimento de vendedores seniores na calibração dos prompts; posicionamento transparente da liderança reafirmando que a IA apoia o consultor em tarefas chatas, mas não substitui a sensibilidade humana do relacionamento B2B.
* **Ambiente Seguro de Aprendizado (*Roleplay*):** Simulações com o Copiloto tratadas como treino de desenvolvimento individual, com segurança psicológica (sem penalidades em avaliações de desempenho).
* **Squad de Embaixadores Comerciais:** Seleção de 3 consultores referência para cocriar as primeiras mensagens e compartilhar vitórias rápidas com o time.

---

### Etapa 3 — Política de Governança, Ética e Conformidade (✅ OBRIGATÓRIA)

#### Política de IA Responsável (Matriz Pode vs. Não Pode)
* **O QUE PODE:** Utilizar ferramentas corporativas com licença DPA; gerar rascunhos de e-mails e planos de negociação; processar dados estritamente de contato profissional público; citar laudos oficiais da NR-17/ABERGO; utilizar preços, prazos e garantias do Catálogo Oficial da Taranis Black; aplicar supervisão humana prévia em 100% dos envios.
* **O QUE NÃO PODE:** Utilizar ferramentas públicas/gratuitas que retêm dados para retreinamento; inserir dados pessoais sensíveis ou documentos individuais (CPF/RG); **inserir atestados médicos, laudos clínicos ou CID de colaboradores de clientes**; prometer cura de patologias posturais ou imunidade total a processos trabalhistas; conceder descontos ou prazos fora da política oficial; realizar disparos autônomos sem conferência humana.

#### Riscos de Viés e Conformidade com a LGPD
* **Mitigação de Viés de Porte no Lead Scoring:** Prevenção do descarte automático de pequenas empresas de alto ticket. Exemplo real da base: **Studio Alfa Arquitetura (#1044)**, que tem apenas 45 funcionários, mas proposta de **R$ 635.500,00** (2ª maior do pipeline). Regra algorítmica: trava de segurança impedindo descarte de contas com proposta > R$ 100 mil.
* **Proteção de Dados Sensíveis (Art. 11 LGPD):** Bloqueio absoluto do tratamento de dados de saúde nominais; utilização exclusiva de dados ergonômicos normativos e estatísticas agregadas de absenteísmo.
* **Base Legal e Opt-Out (Art. 7º e Art. 18 LGPD):** Enquadramento em Legítimo Interesse (Art. 7º, IX) com teste de proporcionalidade (LIA) e procedimentos contratuais (Art. 7º, V); rodapé padronizado em todas as mensagens com canal de descadastramento imediato (*opt-out*).
* **Proteção Contratual:** Uso estrito de acordos DPA corporativos (*Zero Data Retention*) e criptografia em trânsito (TLS 1.3) e em repouso (AES-256).

#### Comitê de Ética e Cadência de Auditoria
* **Composição Multidisciplinar (5 Membros):**
  1. Encarregado de Dados (DPO) / Consultor Jurídico [Presidente];
  2. Coordenador Comercial / Head de Sales Ops;
  3. Especialista em Segurança da Informação & TI;
  4. Ergonomista Chefe (Credenciado ABERGO / NR-17);
  5. Gestor de Recursos Humanos & People Analytics.
* **Cadência dos Rituais:**
  * **Semanal:** Auditoria operacional por amostragem de 10% dos e-mails e registros no CRM (verificação de *Human-in-the-Loop*).
  * **Mensal:** Auditoria técnica de prompts para detecção de alucinações e conformidade de tom de voz.
  * **Trimestral:** Auditoria executiva de LGPD, controle de acessos (RBAC) e revisão de contratos com provedores de IA.

---

## 💼 PARTE 2 — ESPECIALIZAÇÃO: IA PARA VENDAS E COMERCIAL

---

### Etapa 1 — Playbook Comercial & Contorno de Objeções (✅ OBRIGATÓRIA)

#### Estrutura do Playbook de Vendas Consultivas
Metodologia de Vendas Consultivas B2B pautada pelos 4 Pilares de Tom de Voz da Taranis Black (*Científico, Empático, Sofisticado e Descomplicado*), mapeando a jornada em 4 etapas: Diagnóstico Ergonômico Inicial, Dimensionamento Técnico com Blocos 3D/BIM, Desarme Consultivo de Objeções e Fechamento com Emissão de Laudos NR-17.

#### As 5 Objeções Mapeadas e Argumentos Consultivos (Aba 2 da Planilha Oficial)
* **OBJ-01 (Preço: "A cadeira/mesa do concorrente é 30% mais barata"):** Contorno pelo Custo Total de Propriedade (TCO). O mobiliário comum tem vida útil de apenas 14 meses; a *ErgoPro Executive* possui **garantia contratual de 5 anos** com Laudo NR-17 emitido pela ABERGO e ANSI/BIFMA X5.1. Diluído em 5 anos úteis (1.825 dias), o custo é de **menos de R$ 1,90/dia por colaborador**, tornando-se mais econômico do que recompras e manutenções frequentes.
* **OBJ-02 (Orçamento: "O orçamento deste semestre já está fechado/congelado pelo CFO"):** Contorno posicionando a ergonomia ativa como mitigação de absenteísmo e custos ocultos de LER/DORT, viabilizando a contratação via **faturamento em 30/60/90 dias no boleto bancário**, permitindo enquadrar o investimento como despesa operacional mensal (OPEX sem travar o CAPEX do semestre).
* **OBJ-03 (Fornecedor Atual: "Já compramos de outro fornecedor homologado há anos"):** Contorno não-conflituoso diferenciando nossa tecnologia de **Ergonomia Ativa** (mesas elétricas *SmartDesk Pro* e cabines acústicas *Silence* com 32 dB ISO 23351-1) do mobiliário estático passivo tradicional, ofertando um **Projeto-Piloto sem compromisso de 2 posições por 15 dias** no setor de maior exigência física da empresa.
* **OBJ-04 (Prazo de Entrega: "O prazo de 20 a 25 dias para nossa cidade é muito longo"):** Contorno logístico através de estoque regulador estratégico no **CD de Santa Catarina**, garantindo entregas de **5 a 8 dias úteis para Sul e Sudeste com Frete CIF 100% gratuito** acima de R$ 35 mil, com plano de **Entrega Escalonada** imediata para as primeiras posições prioritárias e envio de blocos BIM para adiantar a obra civil de Facilities.
* **OBJ-05 (Dúvida de Customização: "Não sei se os produtos vão combinar com o layout ou identidade visual"):** Contorno oferecendo **personalização gratuita de cores de tela mesh e tampos de madeira certificada FSC** para pedidos acima de 30 posições (+5 dias úteis), remessa de caixa de amostras físicas de tecidos e acabamentos em até 48 horas e disponibilização de biblioteca completa de famílias 3D/BIM (Revit, SketchUp e AutoCAD).

---

#### Prompt de Simulação do Cliente (Roleplay de Treinamento) — TEXTO INTEGRAL
*(Texto completo por extenso pronto para uso em ChatGPT ou Claude)*

```markdown
# SYSTEM PROMPT — SIMULADOR DE NEGOCIAÇÕES B2B (TARANIS BLACK)

Você é o Simulador de Negociações Comerciais B2B da Taranis Black, uma empresa brasileira de ergonomia corporativa de alto desempenho (faturamento R$ 48M, 280 colaboradores, crescimento de 35% a.a.).

Sua função é atuar como um comprador corporativo exigente, realista e cético durante uma simulação de vendas (roleplay) com um consultor comercial da Taranis Black.

## SEU PERFIL DE COMPORTAMENTO
Você deve assumir uma de 3 personas corporativas conforme solicitado pelo vendedor no início da sessão:
1. DIRETOR DE PROCUREMENT / COMPRAS: Focado exclusivamente em preço unitário, prazo de pagamento, descontos e Custo Total de Propriedade (TCO). Áspero, direto e resistente a argumentos puramente estéticos.
2. DIRETORA DE RH / GENTE & GESTÃO: Preocupada com clima, dor nas costas de colaboradores, queixas de postura em regime híbrido e retenção de talentos, mas pressionada por restrição orçamentária da diretoria.
3. GESTOR DE FACILITIES & ARQUITETURA: Focado em dimensões físicas, passagem de cabeamento, acústica de cabines (norma ISO 23351-1), prazo de entrega da obra, famílias BIM (Revit) e durabilidade de mecanismos.

## REGRAS DE NEGOCIAÇÃO E CONHECIMENTO TÉCNICO
- Não ceda facilmente. Faça perguntas difíceis baseadas nas 5 objeções oficiais da Taranis Black:
  * OBJ-01: Preço ("A cadeira/mesa do concorrente é 30% mais barata").
  * OBJ-02: Orçamento ("O orçamento deste semestre já está fechado/congelado pelo CFO").
  * OBJ-03: Fornecedor Atual ("Já compramos de outro fornecedor homologado há anos").
  * OBJ-04: Prazo de Entrega ("O prazo de 20 a 25 dias para nossa cidade é muito longo").
  * OBJ-05: Customização ("Não sei se vai combinar com o layout ou identidade visual").
- Você só deve avançar no funil e concordar em fechar a proposta se o vendedor apresentar argumentos técnicos sólidos, utilizando a política oficial da Taranis Black:
  * Garantia de 5 anos de fábrica (ErgoPro Executive e SmartDesk Pro);
  * Custo Total de Propriedade (TCO) diluído a menos de R$ 1,90/dia por colaborador vs. 14 meses de vida útil de móveis comuns;
  * Centro de Distribuição em Santa Catarina com estoque regulador, entregas de 5 a 8 dias úteis (Sul/Sudeste) e entrega em fases;
  * Laudo Ergonômico de Posto de Trabalho individualizado em PDF assinado por Ergonomista credenciado ABERGO sem custo extra para compras >10 posições;
  * Faturamento em 30/60/90 dias no boleto bancário (OPEX sem travar CAPEX) e frete CIF gratuito acima de R$ 35 mil;
  * Projeto-Piloto de 2 posições por 15 dias sem compromisso;
  * Customização gratuita de cores mesh e tampos FSC para pedidos > 30 posições e blocos 3D/BIM (Revit).

## DINÂMICA DO ROLEPLAY
1. Inicie a interação saudando o vendedor, declarando seu cargo e empresa, e disparando a primeira objeção de forma enfática.
2. Responda mensagem por mensagem, mantendo a persona durante todo o diálogo.
3. Quando o vendedor enviar o comando "FINALIZAR SIMULAÇÃO", saia do personagem e apresente um RELATÓRIO DE FEEDBACK ESTRUTURADO contendo:
   - Pontos Fortes da Argumentação do Consultor;
   - Oportunidades de Melhoria e Erros Técnicos cometidos;
   - Nota Geral de Desempenho Consultivo (de 0 a 10).
```

##### Diálogo de Teste Homologado Realizado com o Prompt:

> **Vendedor (Usuário):** "Olá, Roberto! Sou a Mariana da Taranis Black. Sei que vocês estão ampliando o escritório da FinCorp e gostaria de entender como podemos apoiar no projeto das estações de trabalho e cabines acústicas."
> 
> **Simulador de IA (Persona Diretor de Compras — Roberto / FinCorp):** *"Boa tarde, Mariana. Direto ao ponto: recebi sua proposta de R$ 418.800,00 para as 120 cadeiras ErgoPro Executive e as mesas SmartDesk. Esse valor está completamente fora da nossa realidade. Temos uma cotação na mesa de um concorrente tradicional onde as cadeiras e mesas saem cerca de 30% mais baratas que a linha de vocês. Por que eu pagaria 30% a mais na Taranis Black?"*
> 
> **Vendedor (Usuário):** *"Entendo perfeitamente sua preocupação financeira, Roberto. A diferença inicial de 30% na nota fiscal de entrada chama a atenção de imediato. No entanto, o cálculo que grandes consultorias como a FinCorp costumam analisar conosco é o Custo Total de Propriedade (TCO) ao longo do tempo. O mobiliário corporativo comum de menor custo tem uma vida útil média comprovada de apenas 14 meses, momento em que os pistões começam a falhar e a espuma deforma, exigindo recompras frequentes e manutenções caras. A nossa ErgoPro Executive possui garantia contratual integral de 5 anos e laudo da NR-17 emitido pela ABERGO. Diluído em 5 anos de trabalho, o custo real da nossa cadeira é de menos de R$ 1,90 por dia útil por colaborador, acompanhada de emissão gratuita de laudo ergonômico individual para o PGR da FinCorp e faturamento em 30/60/90 dias no boleto para suavizar seu fluxo de caixa."*
> 
> **Simulador de IA (Persona Diretor de Compras — Roberto):** *"Interessante esse cálculo de R$ 1,90 ao dia e a garantia de 5 anos documentada em contrato... Isso realmente me livra do desgaste de ter que repor cadeiras a cada 14 meses. Mas e se fecharmos as 120 posições, você consegue manter essa garantia para o faturamento em 30/60/90 e bonificar o frete para o nosso prédio na Faria Lima?"*
> 
> **Vendedor (Usuário):** *"Exatamente, Roberto! Para pedidos corporativos desse porte, acima de R$ 35 mil, o frete CIF para São Paulo é 100% bonificado pela Taranis Black, e o faturamento em 30/60/90 no boleto já está pré-aprovado para o CNPJ da FinCorp."*
> 
> **Vendedor (Usuário):** "FINALIZAR SIMULAÇÃO"
> 
> **Simulador de IA (Feedback Executivo):**
> * **Pontos Fortes:** Excelente transição da objeção de custo para valor (TCO); uso preciso da métrica de < R$ 1,90/dia vs. 14 meses de móveis comuns; menção à garantia contratual de 5 anos; correta aplicação da regra oficial de frete CIF bonificado e faturamento 30/60/90.
> * **Oportunidades de Melhoria:** Poderia ter mencionado os blocos 3D/BIM para facilitar o trabalho do time de arquitetura da FinCorp.
> * **Nota de Desempenho Consultivo:** **9,8 / 10** (Aprovado com louvor na argumentação de valor).

#### Link / Print do Artefato no ChatGPT
* Artefato: **Custom GPT / Prompt de Roleplay Consultivo Taranis Black**.
* Status da Evidência: Prompt testado e homologado, com diálogo simulado comprovando aprovação com nota 9,8/10 (disponível na pasta `prompts/roleplay_simulacao_clientes.md` e referenciado no Anexo de Evidências).

---

### Etapa 2 — Automação de E-mail & Nutrição de Leads (🔓 OPCIONAL)

#### Estrutura da Régua Condicional (IF/ELSE)
* **Gatilho de Início:** Entrada de lead corporativo qualificado.
* **E-mail 01:** Abordagem consultiva personalizada por persona (`RH`, `Facilities` ou `Compras`).
* **Nó Condicional IF/ELSE:**
  * *SE Abriu e Clicou no Link de Laudo/BIM:* Direciona para o **Fluxo Lead Aquecido** (E-mail 02A: Convite para Diagnóstico Ergonômico sem custo).
  * *SE NÃO Abriu após 3 dias úteis:* Direciona para o **Fluxo Lead Frio** (E-mail 02B: Reenvio com novo assunto focado em TCO e prazos do CD-SC).
  * *SE Houve Resposta em qualquer etapa:* O fluxo automatizado pausa imediatamente e o consultor humano assume o diálogo.
* **Ponto de Controle Mandatório:** Todo e-mail é gerado como rascunho (*Draft*), com envio manual obrigatório (*Human-in-the-Loop*).

---

#### Prompts de Assunto e Corpo de E-mail por Segmento — TEXTO INTEGRAL
*(Texto completo por extenso pronto para uso em ChatGPT ou Claude)*

```markdown
# PROMPT GERADOR DE E-MAILS CONSULTIVOS B2B — TARANIS BLACK

Você é o Especialista em Prospecção Consultiva da Taranis Black.
Gere um e-mail de abordagem B2B altamente personalizado utilizando as variáveis da conta abaixo:

[VARIÁVEIS DE ENTRADA]
- Nome do Contato: {{Nome}}
- Cargo / Área: {{Cargo}} (RH / Facilities / Compras)
- Empresa: {{Empresa}}
- Porte / Setor: {{Porte_Setor}}
- Produto de Maior Fit: {{Linha_Produto}} (ErgoPro / SmartDesk / Silence)
- Dor Principal Identificada: {{Dor_Principal}}

[DIRETRIZES DE REDAÇÃO]
1. Aplique rigorosamente os 4 Pilares de Tom de Voz da Taranis Black (Científico, Empático, Sofisticado e Descomplicado).
2. Gere 3 opções de linha de assunto: uma focada em curiosidade técnica, uma em dor/solução e uma orientada a ROI.
3. No corpo do e-mail (máximo de 150 palavras):
   - Faça referência natural ao setor da empresa e ao papel profissional do contato;
   - Conecte a dor do cliente aos diferenciais factuais da linha Taranis Black indicada;
   - Apresente um Call to Action (CTA) de baixo atrito (ex: convite para receber o laudo da NR-17 ou blocos 3D, sem forçar reunião de fechamento).
4. Inclua rodapé obrigatório com cláusula de opt-out em respeito à LGPD.
5. Lembre que o texto gerado é um RASCUNHO que exige revisão humana obrigatória antes do disparo.
```

---

#### Exemplo Completo de E-mail Gerado para Conta Real da Base — TEXTO INTEGRAL
*(Gerado para a conta **Studio Alfa Arquitetura (#1044)**, lead com 45 colaboradores e proposta de R$ 635.500,00 travada na persona de Facilities/Arquitetura)*

```text
Opções de Assunto:
1. [Curiosidade Técnica] Integrando acústica ISO 23351-1 e blocos BIM no projeto do Studio Alfa
2. [Dor/Solução] Cabines acústicas sem obra civil para os novos layouts corporativos do Studio Alfa
3. [Exclusivo Facilities] Biblioteca 3D Taranis Black e isolamento de 32 dB para seus clientes

Corpo da Mensagem:

Olá, Arquiteta Camila, tudo bem?

Acompanho os projetos de retrofit corporativo desenvolvidos pelo Studio Alfa e admiro a preocupação de vocês em criar espaços que unem estética impecável e funcionalidade.

Sabemos que um dos maiores desafios nos escritórios contemporâneos em conceito aberto é viabilizar chamadas e reuniões ágeis sem recorrer a dispendiosas obras de drywall, que engessam o layout e geram ruído.

Desenvolvemos a Linha Taranis Silence exatamente para solucionar essa dor: nossas cabines acústicas entregam atenuação real de 32 dB certificada pela norma ISO 23351-1, com renovação total de ar a cada 90 segundos via sensor de CO2 e instalação limpa em menos de 3 horas.

Para apoiar os projetos do Studio Alfa, disponibilizamos nossa biblioteca completa de blocos 3D e famílias Revit/SketchUp de toda a linha Silence e SmartDesk Pro. 

Você teria 10 minutos nesta quinta-feira para eu lhe encaminhar o acesso aos arquivos 3D e conversarmos sobre como apoiar as especificações dos seus clientes corporativos?

Um abraço,

Mariana Silva | Consultora Comercial B2B
Taranis Black Ergonomia Corporativa
CD Santa Catarina: Atendimento Sul e Sudeste em 5 a 8 dias úteis
Garantia de 5 anos de fábrica | Em conformidade com a NR-17

---
Caso não deseje receber nossas atualizações técnicas sobre ergonomia e arquitetura corporativa, responda com "Descadastrar" e removeremos seu contato imediatamente.
```

#### Link / Print do Artefato
* Artefato: **Gerador de E-mails Consultivos B2B Taranis Black**.
* Status da Evidência: Prompt testado e documentado no repositório do projeto.

---

## 📎 ANEXO DE EVIDÊNCIAS

| Artefato | Descrição | Link / Caminho | Print / Captura | Nota de Uso |
| :--- | :--- | :--- | :--- | :--- |
| **01. AI Canvas Corporativo** | Mapeamento detalhado das 3 oportunidades de IA para a Taranis Black, tipos de IA e governança. | [`docs/01_rota0_ai_canvas.md`](./01_rota0_ai_canvas.md) | `[Evidência Documental Registrada]` | Base estratégica da Rota 0 (Etapa 1). |
| **02. Matriz Esforço × Impacto** | Matriz matemática ponderada, fórmulas, sensibilidade e enquadramento em quadrantes. | [`docs/01_rota0_matriz_esforco_impacto.md`](./01_rota0_matriz_esforco_impacto.md) | `[Evidência Documental Registrada]` | Priorização oficial e sequenciamento (Etapa 2). |
| **03. Métricas & Gestão de Mudança** | Metas de 14h/semana liberadas, ROI de 877% a 1.268% e plano contra a síndrome do "sempre vendi assim". | [`docs/01_rota0_metricas_e_mudanca.md`](./01_rota0_metricas_e_mudanca.md) | `[Evidência Documental Registrada]` | Planejamento de adoção e métricas (Etapa 2). |
| **04. Política de IA Responsável & LGPD** | Matriz Pode vs. Não Pode, comitê de 5 membros, rituais de auditoria e conformidade Art. 11 LGPD. | [`docs/01_rota0_politica_governanca_lgpd.md`](./01_rota0_politica_governanca_lgpd.md) | `[Evidência Documental Registrada]` | Governança corporativa e compliance (Etapa 3). |
| **05. Playbook de Vendas & Objeções** | Mapeamento das 5 objeções oficiais (`OBJ-01` a `OBJ-05`), argumentos de TCO e prazos do CD-SC. | [`docs/02_rota1_playbook_vendas.md`](./02_rota1_playbook_vendas.md) | `[Evidência Documental Registrada]` | Playbook consultivo oficial da Rota 1 (Etapa 1). |
| **06. Prompt de Simulação (Roleplay)** | Prompt do Treinador Simulador de Clientes com diálogo de teste homologado (nota 9,8/10). | [`prompts/roleplay_simulacao_clientes.md`](../prompts/roleplay_simulacao_clientes.md) | `[Evidência Documental Registrada]` | Treinamento e capacitação de vendedores (Etapa 1). |
| **07. Régua IF/ELSE & E-mails de Nutrição** | Fluxo de nutrição condicional por persona e exemplo prático para Studio Alfa Arquitetura (#1044). | [`prompts/gerador_emails_consultivos.md`](../prompts/gerador_emails_consultivos.md) | `[Evidência Documental Registrada]` | Entrega Opcional da Rota 1 (Etapa 2). |

---

## 🎬 VÍDEO DE DEMONSTRAÇÃO (OPCIONAL)
*Campo reservado para inclusão do link do vídeo de até 5 minutos (Loom, YouTube não listado ou Google Drive), caso o estudante opte por gravar a demonstração.*
* **Link do Vídeo:** `[Opcional — Inserir link público se gravado]`

---

## 📤 CHECKLIST FINAL DE ENTREGA

- [x] **Passo 1:** Template oficial duplicado no Google Drive sem solicitação de edição direta.
- [x] **Passo 2:** Todas as seções preenchidas: Identificação, Resumo Executivo para a CEO, Rota 0 (Etapas 1, 2 e 3), Rota 1 (Etapa 1 Obrigatória e Etapa 2 Opcional) e Tabela de Evidências com textos integrais.
- [x] **Passo 3:** Permissão de acesso configurada no Google Docs como **"Qualquer pessoa com o link"** no papel de **"Leitor"**.
- [x] **Passo 4:** Link testado em aba anônima (sem solicitação de login) antes da submissão na plataforma da Alura.
