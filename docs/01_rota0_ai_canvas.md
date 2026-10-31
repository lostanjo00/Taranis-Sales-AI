# AI Canvas — Oportunidades de Inteligência Artificial para a Taranis Black
**Projeto:** Taranis Sales AI — Challenge Alura (AI for Business) | ONE G11  
**Etapa:** Rota 0 — Base Estratégica (Obrigatória) — Etapa 1 do Template Oficial  
**Documento de Referência:** [`docs/00_premissas_e_governanca.md`](./00_premissas_e_governanca.md)  
**Classificação Metodológica:** `[FATO]` | `[HIPÓTESE]` | `[PROPOSTA]`  

---

## 1. Contexto e Metodologia

Este documento estabelece o **AI Canvas** da Taranis Black, mapeando formalmente três oportunidades de aplicação de Inteligência Artificial para endereçar os desafios de eficiência operacional e vendas consultivas da empresa, em estrita aderência aos requisitos da **Etapa 1 da Rota 0** do template oficial da Alura.

Em conformidade estrita com as diretrizes de governança estabelecidas para o projeto:
* **`[FATO]`**: Informações confirmadas nos materiais institucionais e no Kit Oficial de Dados Simulados do Challenge Alura.
* **`[HIPÓTESE]`**: Premissas de trabalho e modelagens operacionais plausíveis, não confirmadas documentalmente.
* **`[PROPOSTA]`**: Recomendações técnicas, funcionais e estratégicas desenhadas pela consultoria.
* **Neutralidade Decisória:** Nenhuma oportunidade é declarada prioritária nesta etapa; a priorização formal é fundamentada na Matriz Esforço × Impacto.

---

## 2. Análise Estruturada das Oportunidades de IA

---

### 2.1. Oportunidade 1: Automação de Registros no CRM

#### 2.1.1. Problema de Negócio
* `[FATO]` A empresa enfrenta processos manuais e burocráticos que prejudicam a eficiência operacional.
* `[FATO]` A equipe comercial B2B perde aproximadamente 40% do tempo semanal com o conjunto de atividades operacionais e repetitivas, composto por preenchimento de CRM, redação de e-mails genéricos e rotinas burocráticas associadas.
* `[HIPÓTESE]` A parcela de tempo consumida pela digitação manual no CRM desvia os consultores de interações diretas e consultivas com prospects e clientes.
* `[HIPÓTESE]` Registros manuais feitos horas após as reuniões podem conter omissões de requisitos técnicos de projetos, atrasos de atualização de etapas e perda de histórico de negociação.

#### 2.1.2. Usuários e Beneficiários
* **Usuários Primários:** `[HIPÓTESE]` Vendedores corporativos (SDRs, Account Executives/Closers) responsáveis pela interface diária com clientes e atualização de negócios.
* **Beneficiários Secundários:** `[HIPÓTESE]` Gerentes Comerciais e Diretoria Executiva, que demandam visibilidade tempestiva e fidedigna das 20 contas abertas no pipeline (`[FATO]` totalizando R$ 4,69 milhões).

#### 2.1.3. Classificação por Tipo de IA e Justificativa (Requisito Oficial Alura)
* **Classificação:** `[PROPOSTA]` **IA Generativa + IA Tradicional (Híbrida)**.
* **Justificativa Técnica:**
  * **IA Generativa (LLM):** Necessária para interpretar anotações comerciais não estruturadas, atas de reuniões e áudios transcritos de vendedores, compreendendo nuances contextuais e extraindo entidades de negócio estruturadas (ex: decisores identificados, volumes pretendidos de *ErgoPro* ou *SmartDesk*, objeções registradas e próximos passos acordados) em formato padronizado JSON.
  * **IA Tradicional (Automação Baseada em Regras / APIs REST):** Responsável pela validação sintática do schema JSON retornado pelo modelo, aplicação de regras de integridade relacional e envio seguro dos dados aos endpoints da API do sistema legado de CRM da empresa.

#### 2.1.4. Supervisão Humana (*Human-in-the-Loop* — Requisito Oficial Alura)
* **Protocolo de Supervisão:** `[PROPOSTA]` **Revisão e Confirmação Humana Obrigatória Pré-Salvamento**.
* **Mecanismo Operacional:** A IA não possui permissão de gravação direta e autônoma na base de dados de produção do CRM. O sistema gera uma visualização em formato de rascunho (*staging card*), na qual os campos extraídos são destacados na tela do vendedor. O profissional revisa, edita eventuais imprecisões e clica expressamente no botão de confirmação para efetivar o registro no sistema.

#### 2.1.5. Dados Necessários, Fontes e Governança LGPD
* **Dados Necessários:** Anotações brutas de reuniões, pontos de ação, resumos de conversas comerciais e campos estruturados de negócio (etapa do funil, decisores envolvidos, produtos de interesse e data do próximo contato).
* **Fontes:** Anotações digitais comerciais, históricos de mensagens corporativas com clientes e formulários internos.
* **Diretrizes de LGPD e Privacidade:**
  * `[PROPOSTA]` **Minimização de Dados:** Processar estritamente dados de contexto corporativo B2B, eliminando qualquer menção a dados sensíveis de saúde individual ou vida privada.
  * `[PROPOSTA]` **Base Legal Adequada:** Procedimentos preliminares relacionados a contrato a pedido do titular (art. 7º, V da LGPD) e legítimo interesse (art. 7º, IX).
  * `[PROPOSTA]` **Proteção Contratual:** Uso exclusivo de provedores corporativos de IA que assegurem via contrato (*Data Processing Agreement* — DPA) a não utilização dos dados empresariais da Taranis Black para retreinamento de modelos públicos (*Zero Data Retention*).
  * `[PROPOSTA]` **Retenção Limitada:** Descarte programado de anotações brutas intermediárias após a validação e consolidação dos registros no CRM.
  * `[PROPOSTA]` **Segurança:** Criptografia em trânsito (TLS 1.3) e em repouso (AES-256), com controle de acesso granular baseado em função (RBAC).

#### 2.1.6. Benefícios Esperados
* `[PROPOSTA]` Redução substancial do tempo dedicado à digitação manual de relatórios de reuniões, liberando horas para atividades de alto valor agregado.
* `[PROPOSTA]` Padronização da qualidade e completude dos registros de oportunidades no pipeline comercial.
* `[PROPOSTA]` Eliminação da defasagem temporal entre a realização de uma reunião comercial e seu registro oficial.

#### 2.1.7. Riscos e Mitigações
* **Risco de Alucinação / Inconsistência:** O modelo inventar prazos, valores de propostas ou demandas que não foram discutidos.
  * *Mitigação:* `[PROPOSTA]` *Human-in-the-Loop* mandatória com schema de validação rígido e alertas visuais de confiança.
* **Risco de Vazamento de Informações:** Tráfego de dados comerciais confidenciais por serviços de terceiros sem termos de segurança.
  * *Mitigação:* `[PROPOSTA]` Arquitetura fechada com chaves de API empresariais e auditoria de tráfego.

#### 2.1.8. Métricas de Sucesso
* Variação do tempo médio semanal dedicado por colaborador ao preenchimento de registros comerciais.
* Índice de completude dos campos-chave de oportunidades no CRM dentro de 24 horas pós-interação.
* Taxa de aceitação e edição das sugestões geradas pela IA por parte dos consultores comerciais.

#### 2.1.9. Estimativa de Esforço
* **Complexidade Técnica:** Média (desenvolvimento de prompts estruturados para extração em JSON, validação de schema e conectores com o sistema de CRM).
* **Esforço de Gestão de Mudança:** `[HIPÓTESE]` Baixo a Médio (alta receptividade da equipe comercial por eliminar esforço burocrático, exigindo treinamento na disciplina de conferência prévia).

---

### 2.2. Oportunidade 2: Personalização de E-mails e Qualificação de Leads B2B

#### 2.2.1. Problema de Negócio
* `[FATO]` A equipe comercial perde tempo significativo com redação de e-mails genéricos, dentro do volume total de ~40% de tempo semanal consumido por tarefas repetitivas.
* `[HIPÓTESE]` Abordagens padronizadas e sem aderência às prioridades dos diferentes interlocutores corporativos (`[FATO]` personas de **RH / People**, **Facilities / Arquitetura** e **Compras / Procurement / CFO**) resultam em baixas taxas de resposta inicial.
* `[HIPÓTESE]` A triagem manual de contas corporativas carece de critérios uniformes de priorização de leads.

#### 2.2.2. Usuários e Beneficiários
* **Usuários Primários:** `[HIPÓTESE]` Pré-vendedores (SDRs/BDRs) e Executivos de Contas focados na prospecção ativa e qualificação de novas oportunidades B2B.
* **Beneficiários Secundários:** `[HIPÓTESE]` Tomadores de decisão nas empresas-alvo corporativas (gestores de RH, Facilities e Compras), que recebem comunicações contextualizadas às suas atribuições e dores técnicas reais.

#### 2.2.3. Classificação por Tipo de IA e Justificativa (Requisito Oficial Alura)
* **Classificação:** `[PROPOSTA]` **IA Generativa + IA Preditiva / Tradicional (Híbrida)**.
* **Justificativa Técnica:**
  * **IA Generativa (LLM):** Utilizada para a redação contextualizada e persuasiva de assuntos e corpos de e-mail consultivos, adaptando rigorosamente a mensagem aos 4 pilares de Tom de Voz da Taranis Black (*Científico, Empático, Sofisticado, Descomplicado* documentados no Kit de Apoio `03_Marketing...`), correlacionando os produtos (*ErgoPro, SmartDesk, Silence*) com as dores da persona.
  * **IA Preditiva / Tradicional (Algoritmo de Lead Scoring):** Algoritmo de pontuação e priorização de leads que analisa variáveis firmográficas e comportamentais (porte da empresa, setor, regime de trabalho presencial/híbrido e orçamento estimado) para classificar o lead em graus de maturidade comercial (ex: Lead Quente, Morno, Frio), direcionando o esforço dos consultores.

#### 2.2.4. Supervisão Humana (*Human-in-the-Loop* — Requisito Oficial Alura)
* **Protocolo de Supervisão:** `[PROPOSTA]` **Trava Técnica Contra Disparo Autônomo e Validação Humana Mandatória**.
* **Mecanismo Operacional:** É terminantemente proibido qualquer envio automático autônomo de mensagens para clientes. O assistente de IA opera exclusivamente como gerador de rascunhos (*drafts*). O consultor comercial humano deve ler o e-mail gerado, verificar se a menção a produtos (*ErgoPro*, *SmartDesk* ou *Silence*) e condições de frete/pagamento está correta, ajustar o tom de voz conforme seu relacionamento com a conta e efetuar o disparo manualmente.

#### 2.2.5. Dados Necessários, Fontes e Governança LGPD
* **Dados Necessários:** Informações corporativas da empresa-alvo (setor, porte, regime de trabalho), cargo/área do decisor (`RH`, `Facilities` ou `Compras`), histórico de interação no pipeline e catálogo oficial de produtos da Taranis Black (`[FATO]` fichas técnicas e preços das linhas *ErgoPro*, *SmartDesk* e *Silence*).
* **Fontes:** Canais institucionais corporativos, formulários de entrada de leads e catálogo oficial da empresa.
* **Diretrizes de LGPD e Privacidade:**
  * `[PROPOSTA]` **Enquadramento de Dados Públicos:** Reconhecer expressamente que dados profissionais publicizados (ex: LinkedIn institucional ou sites empresariais) estão plenamente sujeitos à LGPD (art. 7º, §§ 3º e 4º), exigindo tratamento pautado pela boa-fé, legítimo interesse comercial fundamentado, finalidade compatível e respeito aos direitos do titular.
  * `[PROPOSTA]` **Minimização:** Utilizar unicamente dados de contato estritamente comerciais (nome profissional, cargo, empresa e e-mail corporativo), vedada qualquer coleta de dados sensíveis ou vida privada.
  * `[PROPOSTA]` **Mecanismo de Opt-Out:** Garantir link/instrução clara e imediata no rodapé de todas as mensagens para que o contato corporativo solicite a interrupção das abordagens comerciais.
  * `[PROPOSTA]` **Revisão Humana:** Trava técnica obrigatória de envio manual.

#### 2.2.6. Benefícios Esperados
* `[PROPOSTA]` Redução substancial do tempo gasto na redação de mensagens de primeiro contato e follow-ups comerciais.
* `[PROPOSTA]` Maior relevância na comunicação consultiva, direcionando argumentos específicos para cada interlocutor (bem-estar/NR-17 para RH; layout/acústica ISO 23351-1 para Facilities; TCO e faturamento 30/60/90 para Compras).
* `[PROPOSTA]` Aceleração na identificação de contas com alto potencial de compra.

#### 2.2.7. Riscos e Mitigações
* **Risco de Promessas Comerciais Fictícias:** A IA gerar mensagens prometendo prazos de fabricação irreais ou preços fora do catálogo oficial.
  * *Mitigação:* `[PROPOSTA]` Engenharia de prompts com *grounding* estrito nos dados do Catálogo Oficial da Taranis Black e conferência humana antes do envio.
* **Risco de Spam e Rejeição:** Comunicações repetitivas com estilo artificial.
  * *Mitigação:* `[PROPOSTA]` Adoção estrita da matriz de tom de voz oficial da marca (*Como falamos vs. Como NÃO falamos*).

#### 2.2.8. Métricas de Sucesso
* Tempo médio despendido na elaboração e customização de mensagens de abordagem comercial.
* Taxa de resposta de abordagens iniciais e taxa de conversão de leads qualificados em reuniões agendadas.
* Índice de conformidade das mensagens com a política de tom de voz da Taranis Black.

#### 2.2.9. Estimativa de Esforço
* **Complexidade Técnica:** Baixa a Média (templates de prompts parametrizados por persona, heurística de Lead Scoring e interface de rascunhos).
* **Esforço de Gestão de Mudança:** `[HIPÓTESE]` Médio (demanda treinamento da equipe de prospecção para operar o assistente e manter o senso crítico na validação dos textos).

---

### 2.3. Oportunidade 3: Copiloto de Vendas Consultivas e Tratamento de Objeções

#### 2.3.1. Problema de Negócio
* `[FATO]` Objeções recorrentes de clientes corporativos focadas em **preço** e **prazo** dificultam e travam o fechamento de propostas comerciais B2B (`[FATO]` R$ 4,69 milhões travados em 20 contas do CRM).
* `[HIPÓTESE]` Diante de comparações com mobiliário corporativo comum de baixo custo, os consultores comerciais encontram desafios para articular os diferenciais de Custo Total de Propriedade (TCO), garantia de 5 anos e conformidade com laudos da NR-17.
* `[HIPÓTESE]` Há variabilidade de preparo argumentativo entre consultores comerciais novos e seniores, resultando em concessão desnecessária de descontos de margem.

#### 2.3.2. Usuários e Beneficiários
* **Usuários Primários:** `[HIPÓTESE]` Executivos de Contas (Closers/Account Executives) que conduzem negociações consultivas de alto ticket e novos consultores comerciais em programa de capacitação/onboarding.
* **Beneficiários Secundários:** `[HIPÓTESE]` Compradores corporativos nos clientes, que recebem subsídios técnicos detalhados para defender a aquisição perante comitês de investimento e diretorias financeiras.

#### 2.3.3. Classificação por Tipo de IA e Justificativa (Requisito Oficial Alura)
* **Classificação:** `[PROPOSTA]` **IA Generativa com Arquitetura RAG (Retrieval-Augmented Generation)**.
* **Justificativa Técnica:**
  * **IA Generativa com Grounding em RAG:** A solução requer a combinação de modelos avançados de linguagem para geração de diálogo interativo e argumentação persuasiva com uma camada estrita de recuperação documental (RAG). O modelo busca respostas exclusivamente dentro da base de conhecimento fechada da empresa (Catálogo Oficial com linhas *ErgoPro*, *SmartDesk* e *Silence*, laudos NR-17/ABERGO, prazos do CD de Santa Catarina e matriz oficial das 5 objeções `OBJ-01` a `OBJ-05`), impedindo alucinações técnicas ou comerciais.
  * **Módulo de Simulação (Roleplay Conversacional):** Capacidade generativa de assumir personas hiper-realistas de compradores (ex: comprador intransigente de Procurement ou diretora de RH cética) para treinar vendedores em simulações interativas antes de reuniões críticas.

#### 2.3.4. Supervisão Humana (*Human-in-the-Loop* — Requisito Oficial Alura)
* **Protocolo de Supervisão:** `[PROPOSTA]` **Copiloto Consultivo de Apoio Intelectual e Treinamento (Sem Ação Direta no Cliente)**.
* **Mecanismo Operacional:** O copiloto atua estritamente em ambiente interno de capacitação e preparação pré-reunião. Ele não possui qualquer canal de comunicação externa com o prospect. A condução da negociação, a escolha dos argumentos e a decisão final sobre condições comerciais competem 100% ao consultor de vendas humano, mantendo a autenticidade e o julgamento humano no centro do relacionamento B2B.

#### 2.3.5. Dados Necessários, Fontes e Governança LGPD
* **Dados Necessários:** Catálogo oficial com dados técnicos das linhas *ErgoPro*, *SmartDesk* e *Silence*, matriz oficial das 5 objeções B2B (`OBJ-01` a `OBJ-05`), prazos de entrega do CD de Santa Catarina, políticas de garantia de 3 a 5 anos e diretrizes da NR-17.
* **Fontes:** Documentos oficiais do Kit de Apoio da Taranis Black (`01_Catalogo...` e `02_Leads...`).
* **Diretrizes de LGPD e Privacidade:**
  * `[PROPOSTA]` **Ambiente Fechado e Dados Sintéticos:** Operação do copiloto restrita a dados conceituais e cenários simulados baseados no Kit de Apoio Oficial. É expressamente proibido o upload de minutas contratuais reais de clientes, dados financeiros confidenciais ou nomes reais de compradores em ferramentas públicas de IA.
  * `[PROPOSTA]` **Bloqueio de Dados Sensíveis de Saúde (Art. 11 da LGPD):** Proibição absoluta de alimentar o modelo com atestados médicos ou históricos de saúde individual de colaboradores; a argumentação ergonômica apoia-se em conceitos normativos da NR-17 e ergonomia preventiva agregada.
  * `[PROPOSTA]` **Controle de Acesso (RBAC) e Auditoria:** Acesso autenticado para a equipe comercial com registro de logs de prompts para auditoria periódica.

#### 2.3.6. Benefícios Esperados
* `[PROPOSTA]` Apoio consultivo à equipe de vendas com argumentos estruturados focados em valor (TCO, durabilidade, laudo ergonômico NR-17 e garantia de até 5 anos), sem erosão desnecessária de margens comerciais.
* `[PROPOSTA]` Padronização da postura consultiva diante de objeções de cronograma e prazo fabril, orientando o diálogo para planejamento conjunto e entregas parciais a partir do CD em Santa Catarina.
* `[PROPOSTA]` Aceleração na rampa de aprendizado de novos consultores comerciais por meio de simulações realistas e seguras de negociação.

#### 2.3.7. Riscos e Mitigações
* **Risco de Promessas Médicas ou Jurídicas Indevidas:** A IA prometer cura de patologias posturais ou imunidade a processos trabalhistas.
  * *Mitigação:* `[PROPOSTA]` *System Prompts* defensivos com regras imperativas de bloqueio de afirmações clínicas ou percentuais não documentados, tratando a ergonomia como prevenção e conformidade.
* **Risco de Robotização Comercial:** O consultor ler roteiros rígidos durante a negociação.
  * *Mitigação:* `[PROPOSTA]` Uso do copiloto prioritariamente como ferramenta de preparação e simulação pré-reunião.

#### 2.3.8. Métricas de Sucesso
* Taxa de avanço e conversão de propostas que apresentaram objeções formais de preço e prazo no CRM (`[FATO]` R$ 4,69 milhões em pipeline aberto).
* Redução no ciclo médio de negociação em contas que demandam fundamentação técnica e ergonômica.
* Desempenho e segurança argumentativa dos consultores em simulações periódicas de roleplay com a IA.

#### 2.3.9. Estimativa de Esforço
* **Complexidade Técnica:** Média (estruturação de base de conhecimento com RAG fechado, engenharia de prompts de simulação e interface de consulta).
* **Esforço de Gestão de Mudança:** `[HIPÓTESE]` Médio a Alto (demanda mudança na cultura de vendas, incentivando o estudo de conceitos consultivos e o uso ativo de simulações pela equipe comercial).

---

## 3. Tabela Comparativa Consolidada (AI Canvas Unificado)

A tabela abaixo consolida a análise das três iniciativas sob critérios uniformes, contemplando todas as exigências formais da **Etapa 1 da Rota 0** do template da Alura:

| Dimensão de Análise | 2.1. Automação de Registros no CRM | 2.2. Personalização de E-mails & Leads | 2.3. Copiloto de Vendas Consultivas |
| :--- | :--- | :--- | :--- |
| **Problema Principal** | `[FATO]` ~40% do tempo semanal perdido em rotinas operacionais (inclui CRM e e-mails). | `[FATO]` Redação manual de e-mails genéricos; `[HIPÓTESE]` baixa taxa de retorno inicial. | `[FATO]` Objeções de preço e prazo que travam o fechamento de propostas no CRM. |
| **Classificação por Tipo de IA (Alura)** | `[PROPOSTA]` **IA Generativa + IA Tradicional** (LLM para extração de entidades em JSON + validação de schema e APIs REST). | `[PROPOSTA]` **IA Generativa + IA Preditiva/Tradicional** (LLM para redação com Tom de Voz + algoritmo de Lead Scoring). | `[PROPOSTA]` **IA Generativa com Arquitetura RAG** (Grounding no catálogo oficial + prompts de roleplay interativo). |
| **Supervisão Humana (*Human-in-the-Loop*)** | `[PROPOSTA]` **Aprovação prévia obrigatória:** Vendedor valida o rascunho de dados antes da gravação no CRM. | `[PROPOSTA]` **Trava contra envio autônomo:** Todo e-mail é revisado, ajustado e disparado manualmente pelo consultor. | `[PROPOSTA]` **Apoio interno formativo:** Uso restrito à preparação intelectual e simulações; vendedor conduz a negociação. |
| **Usuários Principais** | `[HIPÓTESE]` Vendedores corporativos (SDRs/Closers) e Lideranças Comerciais. | `[HIPÓTESE]` Profissionais de prospecção comercial corporativa e qualificação. | `[HIPÓTESE]` Executivos de Contas (Closers) e consultores em capacitação comercial. |
| **Personas Impactadas no Cliente** | Gestão Comercial interna e governança operacional. | **RH / People**, **Facilities / Arquitetura** e **Compras / Procurement / CFO**. | Tomadores de decisão e comitês de compras corporativas (RH, Facilities e Compras). |
| **Produtos da Taranis Utilizados** | Portfólio completo estruturado em campos do CRM. | Linhas **ErgoPro, SmartDesk e Silence** correlacionadas às dores da persona. | Linhas **ErgoPro, SmartDesk e Silence**, matriz `OBJ-01` a `OBJ-05` e laudos NR-17. |
| **Benefício Principal** | `[PROPOSTA]` Redução da sobrecarga burocrática e pipeline atualizado em tempo real. | `[PROPOSTA]` Comunicação consultiva relevante e triagem qualificada de contas. | `[PROPOSTA]` Argumentação de valor (TCO e garantia) e superação de objeções de preço/prazo. |
| **Risco Crítico** | Alucinação em valores, datas ou etapas contratuais. | Geração de promessas comerciais não homologadas ou tom impessoal. | Promessas infundadas de benefícios médicos ou garantias contratuais inexistentes. |
| **Mitigação Mandatória** | `[PROPOSTA]` Revisão humana ativa prévia (*Human-in-the-Loop*). | `[PROPOSTA]` Envio estritamente manual após revisão do consultor. | `[PROPOSTA]` Validação de respostas com base documental e revisão humana. |
| **Requisitos LGPD** | Minimização, retenção limitada de notas e base legal definida (procedimentos contratuais/legítimo interesse). | Enquadramento criterioso de dados corporativos públicos, canal de opt-out e minimização de dados. | Ambiente fechado, proibição de dados reais confidenciais de clientes e auditoria de prompts. |
| **Métrica Primária** | Variação no tempo dedicado a registros comerciais operacionais. | Tempo de customização de contatos e taxa de engajamento de leads. | Taxa de avanço e conversão de propostas com objeção de preço/prazo. |
| **Complexidade Técnica Estimada** | Média (extração estruturada e integração com sistema de CRM). | Baixa a Média (engenharia de prompts e geração assistida de rascunhos). | Média (base de conhecimento controlada e simulações de diálogo). |
| **Gestão de Mudança Estimada** | `[HIPÓTESE]` Baixa a Média (rotina de validação e conferência humana). | `[HIPÓTESE]` Média (adaptação ao uso do assistente como coautor de abordagens). | `[HIPÓTESE]` Média a Alta (aculturamento em vendas consultivas e simulações). |

---

## 4. Próximos Passos no Projeto

Com as três oportunidades estruturadas, classificadas por tipo de IA e com seus protocolos de supervisão humana devidamente estabelecidos, o projeto cumpre integralmente os requisitos da **Etapa 1 da Rota 0**.

Os próximos documentos da Rota 0 detalharão formalmente a **Etapa 2 (Métricas de Sucesso & Plano de Mudança Cultural)** e a **Etapa 3 (Política de Governança, Riscos/LGPD, Comitê e Auditoria)**, conectando-se diretamente às decisões estabelecidas na Matriz Esforço × Impacto.
