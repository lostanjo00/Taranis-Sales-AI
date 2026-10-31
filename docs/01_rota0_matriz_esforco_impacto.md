# Matriz Esforço × Impacto — Priorização das Iniciativas de IA
**Projeto:** Taranis Sales AI — Challenge Alura (AI for Business)  
**Etapa:** Rota 0 — Base Estratégica (Obrigatória)  
**Documentos de Referência:** [`docs/00_premissas_e_governanca.md`](./00_premissas_e_governanca.md) | [`docs/01_rota0_ai_canvas.md`](./01_rota0_ai_canvas.md)  
**Classificação Metodológica:** Estimativas analíticas baseadas em `[FATO]` e `[HIPÓTESE]`.  

---

## 1. Metodologia e Critérios de Ponderação

A **Matriz Esforço × Impacto** é o instrumento formal de decisão para avaliar e priorizar as três oportunidades de Inteligência Artificial diagnosticadas no AI Canvas da Taranis Black.

Todas as notas atribuídas representam **estimativas analíticas fundamentadas** nos fatos fornecidos pelo Challenge Alura e em hipóteses operacionais explícitas, sem suposição prévia de resultados e sem estimativas financeiras inventadas.

---

### 1.1. Dimensão: Impacto no Negócio (Eixo Vertical — $I$)
Avalia a capacidade potencial de cada solução em mitigar os gargalos documentados e apoiar a eficiência da organização.

| Subcritério | Peso | Foco de Alinhamento Estratégico |
| :--- | :---: | :--- |
| **I1. Redução da Sobrecarga Operacional** | **30% (0,30)** | Potencial de liberar horas da equipe comercial gastas com rotinas burocráticas e repetitivas (`[FATO]` ~40% do tempo semanal perdido). |
| **I2. Apoio à Eficácia e Conversão B2B** | **30% (0,30)** | Potencial de apoiar a superação das objeções críticas de preço e prazo em vendas de alto ticket (`[FATO]`). |
| **I3. Qualidade e Integridade da Informação** | **20% (0,20)** | Potencial de melhoria na completude, padronização e tempestividade dos dados de clientes e pipeline comercial. |
| **I4. Escalabilidade do Modelo de Vendas** | **20% (0,20)** | Suporte esperado à expansão comercial da empresa (`[FATO]` crescimento anual recente de 35% com 280 colaboradores) sem crescimento proporcional da burocracia. |
| **Total Impacto** | **100% (1,00)** | — |

**Fórmula de Impacto:**
$$\text{Impacto Final } (I) = (I1 \times 0{,}30) + (I2 \times 0{,}30) + (I3 \times 0{,}20) + (I4 \times 0{,}20)$$

---

### 1.2. Dimensão: Esforço Global (Eixo Horizontal — $E$)
Avalia os atritos de implementação, complexidade técnica, riscos regulatórios e barreiras organizacionais.

| Subcritério | Peso | Foco de Complexidade de Implementação |
| :--- | :---: | :--- |
| **E1. Complexidade Técnica e Arquitetura** | **35% (0,35)** | Nível de desenvolvimento, engenharia de prompt estruturada, infraestrutura e integração sistêmica (ex: CRM/APIs). |
| **E2. Governança de Dados, Risco e LGPD** | **30% (0,30)** | Complexidade de conformidade jurídica, minimização, tratamento de dados corporativos públicos, prevenção de alucinações e DPA. |
| **E3. Gestão de Mudanças e Curva de Adoção** | **35% (0,35)** | Resistência cultural, esforço de capacitação da equipe comercial, disciplina de revisão humana e mudança de hábitos. |
| **Total Esforço** | **100% (1,00)** | — |

**Fórmula de Esforço:**
$$\text{Esforço Final } (E) = (E1 \times 0{,}35) + (E2 \times 0{,}30) + (E3 \times 0{,}35)$$

---

### 1.3. Escala de Pontuação (1 a 5)

| Nível | Pontuação de Impacto ($I$) | Pontuação de Esforço ($E$) |
| :---: | :--- | :--- |
| **1** | **Muito Baixo:** Impacto marginal; não altera o cenário operacional da empresa. | **Muito Baixo:** Implementação elementar; sem integrações ou barreiras culturais. |
| **2** | **Baixo:** Impacto pontual restrito a uma tarefa secundária. | **Baixo:** Baixa fricção técnica e de processos; rápida assimilação. |
| **3** | **Médio:** Alívio perceptível em uma dor operacional ou comercial relevante. | **Médio:** Demanda parametrização, fluxos definidos e treinamento moderado. |
| **4** | **Alto:** Resolução substancial esperada de um dos gargalos centrais documentados. | **Alto:** Integração sistêmica mandatória, governança estrita ou forte mudança cultural. |
| **5** | **Muito Alto:** Transformação estrutural esperada no faturamento ou produtividade da área. | **Muito Alto:** Risco arquitetural severo, alta sensibilidade de dados ou barreira cultural crítica. |

---

### 1.4. Definição dos Limiares e Quadrantes

O limiar divisor dos eixos é o ponto médio da escala: **3,00**. As regras formais de enquadramento são:

* **Quadrante 1 — Ganhos Rápidos (*Quick Wins*) [$E \le 3{,}00$ e $I > 3{,}00$]:** Alto impacto potencial com esforço moderado ou baixo. Devem ser priorizados como pilotos de retorno ágil.
* **Quadrante 2 — Projetos Estratégicos [$E > 3{,}00$ e $I > 3{,}00$]:** Alto impacto potencial e alto esforço. Exigem planejamento estruturado, recursos dedicados e cronograma em fases.
* **Quadrante 3 — Melhorias Pontuais [$E \le 3{,}00$ e $I \le 3{,}00$]:** Baixo impacto e baixo esforço. Executados oportunisticamente.
* **Quadrante 4 — Despriorizar / Evitar [$E > 3{,}00$ e $I \le 3{,}00$]:** Baixo impacto e alto esforço. Consomem recursos sem contrapartida compatível.

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
*\* Nota: A Oportunidade 1 situa-se no limiar exato do Q1 ($E = 3{,}00$), na fronteira com o Q2.*

---

## 2. Pontuação Comparativa e Cálculos Verificáveis

A tabela abaixo detalha as notas estimadas por subcritério e a aplicação estrita das fórmulas ponderadas:

| Dimensão / Subcritério | Peso | Oportunidade 1: Automação de CRM | Oportunidade 2: Personalização de E-mails & Leads | Oportunidade 3: Copiloto de Vendas Consultivas |
| :--- | :---: | :---: | :---: | :---: |
| **I1. Sobrecarga Operacional** | 0,30 | 4,0 | 4,0 | 2,0 |
| **I2. Eficácia e Conversão B2B** | 0,30 | 2,0 | 3,0 | 5,0 |
| **I3. Qualidade da Informação** | 0,20 | 5,0 | 3,0 | 3,0 |
| **I4. Escalabilidade do Modelo** | 0,20 | 4,0 | 4,0 | 4,0 |
| **IMPACTO CONSOLIDADO ($I$)** | **1,00** | **3,60** | **3,50** | **3,50** |
| | | | | |
| **E1. Complexidade Técnica** | 0,35 | 4,0 | 2,0 | 3,0 |
| **E2. Governança e LGPD** | 0,30 | 3,0 | 3,0 | 2,0 |
| **E3. Gestão de Mudanças** | 0,35 | 2,0 | 3,0 | 4,0 |
| **ESFORÇO CONSOLIDADO ($E$)** | **1,00** | **3,00** | **2,65** | **3,05** |
| | | | | |
| **Coordenadas na Matriz $(E, I)$** | — | **(3,00 ; 3,60)** | **(2,65 ; 3,50)** | **(3,05 ; 3,50)** |
| **Classificação de Quadrante** | — | **Quadrante 1 (Ganhos Rápidos)** | **Quadrante 1 (Ganhos Rápidos)** | **Quadrante 2 (Projeto Estratégico)** |

### Detalhamento das Contas

1. **Oportunidade 1 (Automação de CRM):**
   * $I = (4{,}0 \times 0{,}30) + (2{,}0 \times 0{,}30) + (5{,}0 \times 0{,}20) + (4{,}0 \times 0{,}20) = 1{,}20 + 0{,}60 + 1{,}00 + 0{,}80 = \mathbf{3{,}60}$
   * $E = (4{,}0 \times 0{,}35) + (3{,}0 \times 0{,}30) + (2{,}0 \times 0{,}35) = 1{,}40 + 0{,}90 + 0{,}70 = \mathbf{3{,}00}$

2. **Oportunidade 2 (Personalização de E-mails e Leads):**
   * $I = (4{,}0 \times 0{,}30) + (3{,}0 \times 0{,}30) + (3{,}0 \times 0{,}20) + (4{,}0 \times 0{,}20) = 1{,}20 + 0{,}90 + 0{,}60 + 0{,}80 = \mathbf{3{,}50}$
   * $E = (2{,}0 \times 0{,}35) + (3{,}0 \times 0{,}30) + (3{,}0 \times 0{,}35) = 0{,}70 + 0{,}90 + 1{,}05 = \mathbf{2{,}65}$

3. **Oportunidade 3 (Copiloto de Vendas Consultivas):**
   * $I = (2{,}0 \times 0{,}30) + (5{,}0 \times 0{,}30) + (3{,}0 \times 0{,}20) + (4{,}0 \times 0{,}20) = 0{,}60 + 1{,}50 + 0{,}60 + 0{,}80 = \mathbf{3{,}50}$
   * $E = (3{,}0 \times 0{,}35) + (2{,}0 \times 0{,}30) + (4{,}0 \times 0{,}35) = 1{,}05 + 0{,}60 + 1{,}40 = \mathbf{3{,}05}$

---

## 3. Justificativa Individual das Pontuações

### 3.1. Oportunidade 1: Automação de Registros no CRM
* **I1 = 4,0:** Apresenta potencial para contribuir na redução do tempo de digitação manual de notas de reuniões, auxiliando no alívio de parte dos ~40% do tempo perdido pela equipe comercial (`[FATO]`).
* **I2 = 2,0:** Impacto indireto na conversão de vendas; organizar o CRM melhora a visibilidade do funil, mas não resolve diretamente o momento da negociação de preço e prazo com o comprador.
* **I3 = 5,0:** É a iniciativa com maior potencial para padronizar o preenchimento de campos obrigatórios e mitigar a perda de histórico de interações com clientes corporativos (`[HIPÓTESE]`).
* **I4 = 4,0:** Pode contribuir para que o crescimento acelerado da empresa (`[FATO]` 35% ao ano) seja suportado por uma base de dados comerciais estruturada e auditável.
* **E1 = 4,0:** `[HIPÓTESE]` Exige integrações de API com o sistema de CRM em uso (cujas especificações técnicas não foram confirmadas nos materiais oficiais) e fluxos de extração em formato estruturado (JSON).
* **E2 = 3,0:** Demanda governança para expurgo de transcrições brutas, proteção contratual (DPA) e minimização de dados corporativos conforme a LGPD (`[PROPOSTA]`).
* **E3 = 2,0:** `[HIPÓTESE]` Baixa resistência esperada da equipe comercial, uma vez que a solução visa eliminar um trabalho manual burocrático, dependendo da disciplina de conferência humana antes do salvamento.

---

### 3.2. Oportunidade 2: Personalização de E-mails e Qualificação de Leads B2B
* **I1 = 4,0:** Possui potencial para mitigar a necessidade de redação manual de mensagens genéricas (`[FATO]`), visando reduzir o tempo despendido em abordagens de prospecção e follow-ups.
* **I2 = 3,0:** Mensagens contextualizadas às dores de cada perfil (RH, Facilities e Compras) têm potencial de aumentar as taxas de resposta e agendamento de reuniões (`[HIPÓTESE]`), embora não encerrem a negociação final de preço/prazo.
* **I3 = 3,0:** Pode padronizar o tom da abordagem inicial da marca, mas atua prioritariamente na saída da comunicação, não no repositório central de dados da empresa.
* **I4 = 4,0:** Pode permitir que a equipe de prospecção amplie a capacidade de contato em contas em expansão sem decair na relevância da comunicação.
* **E1 = 2,0:** Baixa dependência de integrações complexas na largada; pode ser operada via templates estruturados, engenharia de prompts e copiloto de redação assistida.
* **E2 = 3,0:** Exige rigor na observância da LGPD quanto ao tratamento de dados corporativos públicos (art. 7º, §§ 3º e 4º), mecanismo claro de *opt-out* e trava obrigatória para impedir disparos autônomos (`[PROPOSTA]`).
* **E3 = 3,0:** `[HIPÓTESE]` Demanda treinamento para que os consultores aprendam a calibrar o tom das mensagens e mantenham a prática de revisão crítica prévia.

---

### 3.3. Oportunidade 3: Copiloto de Vendas Consultivas e Tratamento de Objeções
* **I1 = 2,0:** Não foca prioritariamente na redução de digitação ou preenchimento de ferramentas, atuando essencialmente na capacitação e preparação intelectual do vendedor.
* **I2 = 5,0:** Visa apoiar o enfrentamento das objeções centrais do desafio comercial (`[FATO]`): preço e prazo em vendas de alto ticket, capacitando o vendedor com argumentos ergonômicos e de valor percebido.
* **I3 = 3,0:** Pode contribuir para a uniformidade do discurso comercial da empresa, sem impacto direto na integridade técnica do banco de dados.
* **I4 = 4,0:** Apresenta potencial para contribuir na aceleração da rampa de novos vendedores necessários para sustentar o crescimento de 35% ao ano (`[FATO]`), buscando mitigar a dependência de consultores seniores.
* **E1 = 3,0:** Demanda curadoria detalhada da base de conhecimento (*grounding* estrito), criação de regras anti-alucinação e prompts estruturados de roleplay/simulação de clientes.
* **E2 = 2,0:** Baixo risco à LGPD se operado em ambiente restrito com cenários simulados e dados inteiramente sintéticos, preservando as demais medidas de privacidade e segurança e vedando expressamente a inserção de dados contratuais reais de clientes (`[PROPOSTA]`).
* **E3 = 4,0:** `[HIPÓTESE]` Demanda maior esforço de gestão de mudanças, pois requer adaptação na postura comercial dos vendedores, adoção de argumentos consultivos e incorporação de rotinas de treinamento via IA.

---

## 4. Análise de Sensibilidade

A proximidade de algumas notas em relação ao limiar $3{,}00$ exige uma análise de sensibilidade para avaliar a estabilidade das classificações diante de incertezas operacionais:

1. **Sensibilidade do Copiloto de Vendas ($E = 3{,}05$):**
   * O Copiloto de Vendas situa-se ligeiramente dentro do **Quadrante 2 (Projeto Estratégico)** ($3{,}05 > 3{,}00$).
   * *Cenário de Variação:* Caso a Taranis Black adote uma interface simplificada de consulta (sem necessidade de integração a sistemas legados) ou se a equipe demonstrar rápida receptividade ao treinamento, reduzindo a nota de Gestão de Mudanças ($E3$) de $4{,}0$ para $3{,}0$, o esforço global cai de $3{,}05$ para **$2{,}70$**.
   * *Consequência:* Nesse cenário, o Copiloto migraria para o **Quadrante 1 (Ganho Rápido / Quick Win)**, tornando-se uma solução de implementação ágil.

2. **Sensibilidade da Automação de CRM ($E = 3{,}00$):**
   * A Automação de CRM situa-se exatamente na borda do **Quadrante 1 (Ganho Rápido)** ($E = 3{,}00$).
   * *Cenário de Variação:* Uma vez que os sistemas de CRM da Taranis Black não foram confirmados nos materiais do Challenge (`[HIPÓTESE]`), caso a ferramenta em uso não possua APIs abertas ou exija conectores customizados de alto custo, a complexidade técnica ($E1$) pode subir de $4{,}0$ para $5{,}0$. Isso elevaria o esforço global para **$3{,}35$**.
   * *Consequência:* Nesse caso, a Automação de CRM migraria imediatamente para o **Quadrante 2 (Projeto Estratégico)**, demandando um cronograma de integração mais longo e cauteloso.

3. **Sensibilidade da Personalização de E-mails ($E = 2{,}65$):**
   * A classificação da Personalização de E-mails no **Quadrante 1 (Ganho Rápido)** decorre das premissas operacionais adotadas, especialmente quanto à baixa fricção inicial de infraestrutura.
   * *Cenário de Variação:* Caso as exigências regulatórias, de governança e proteção contratual se tornem mais rigorosas (por exemplo, exigindo auditorias complexas sobre dados corporativos ou restrições severas de compliance), elevando a nota de Governança e LGPD ($E2$) de $3{,}0$ para $5{,}0$ e mantendo $E1 = 2{,}0$ e $E3 = 3{,}0$, o esforço consolidado passará de $2{,}65$ para **$3{,}25$** [$(2{,}0 \times 0{,}35) + (5{,}0 \times 0{,}30) + (3{,}0 \times 0{,}35) = 0{,}70 + 1{,}50 + 1{,}05 = 3{,}25$].
   * *Consequência:* Nesse cenário, a iniciativa migraria para o **Quadrante 2 (Projeto Estratégico)**, exigindo maior estruturação jurídica e de governança antes da operação.

---

## 5. Recomendação de Priorização Fundamentada

Com base nos resultados analíticos e nas diretrizes de governança da Taranis Black, recomenda-se uma estratégia de implementação **faseada e combinada**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ ROTEIRO ESTRATÉGICO DE ADOÇÃO (ROADMAP FASEADO)                       │
├───────────────────────┬───────────────────────┬────────────────────────┤
│ FASE 1: ONDA IMEDIATA │ FASE 2: PILOTO DE     │ FASE 3: ESTRUTURAÇÃO   │
│ (QUICK WIN PURO)      │ PREPARO CONSULTIVO    │ SISTÊMICA              │
│                       │                       │                        │
│ Personalização de     │ Copiloto de Vendas &  │ Automação de CRM       │
│ E-mails e Leads       │ Objeções (Treinamento)│ (Integração Técnica)   │
│                       │                       │                        │
│ • E = 2,65 | I = 3,50 │ • E = 3,05 | I = 3,50 │ • E = 3,00 | I = 3,60  │
│ • Validação ágil      │ • Foco em objeções de │ • Depende de validação │
│ • Baixo atrito        │   preço e prazo       │   das APIs do CRM em   │
│   arquitetural        │ • Potencial formativo │   uso na empresa       │
└───────────────────────┴───────────────────────┴────────────────────────┘
```

### Racional da Recomendação

1. **Início com a Oportunidade 2 (Personalização de E-mails e Qualificação):**
   * Posicionada com segurança no **Quadrante 1 (Quick Win)** ($E = 2{,}65$).
   * Apresenta potencial de entrega de valor operacional ágil para a equipe de prospecção, com expectativa de redução no tempo de elaboração de abordagens e baixo risco arquitetural.
2. **Evolução Imediata para a Oportunidade 3 (Copiloto de Vendas e Objeções):**
   * Embora classificada formalmente no **Quadrante 2 (Estratégico)** ($E = 3{,}05$) pela exigência de aculturamento comercial, possui a maior pontuação de apoio à conversão B2B ($I2 = 5{,}0$).
   * Como indicado na análise de sensibilidade, se iniciado em formato de capacitação e simulação de roleplay (desconectado de integrações de software complexas), o projeto apresenta características operacionais de um ganho rápido (*Quick Win*) educacional, com potencial de impacto na preparação da equipe para o enfrentamento de objeções comerciais, ressalvando-se que tais ganhos constituem expectativas analíticas e ainda não foram empiricamente medidos na Taranis Black.
3. **Mapeamento e Faseamento da Oportunidade 1 (Automação de CRM):**
   * Apesar de classificada no limite do **Quadrante 1** ($E = 3{,}00$) pelo seu alto impacto em integridade de dados ($I3 = 5{,}0$), sua execução prática requer previamente a confirmação técnica do sistema de CRM utilizado pela Taranis Black.
   * Deve ser tratada como a base estrutural de sustentação técnica do roadmap comercial.
