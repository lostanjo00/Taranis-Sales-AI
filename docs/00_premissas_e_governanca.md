# Premissas de Trabalho, Governança e Base de Dados — Taranis Black
**Projeto:** Taranis Sales AI — Challenge Alura (AI for Business) | ONE G11  
**Versão:** 2.0 (Harmonizada com o Kit Oficial de Dados Simulados)  
**Status:** Baseline Oficial Consolidada  

---

## 1. Objetivo do Documento

Este documento estabelece as diretrizes fundamentais de governança, integridade de dados e limites metodológicos para o desenvolvimento do projeto **Taranis Sales AI**.

O objetivo é garantir que toda a estratégia de Inteligência Artificial, materiais comerciais e análises posteriores estejam estritamente ancorados nos fatos fornecidos pelo desafio da Alura e no Kit Oficial de Dados Simulados da Taranis Black, eliminando alucinações, dados inverídicos ou suposições tratadas indevidamente como verdades.

---

## 2. Framework Epistemológico de Dados

Para assegurar rigor técnico e consultivo, todas as informações utilizadas no projeto devem ser classificadas em uma das três categorias a seguir:

1. **[FATO]**: Dado explicitamente fornecido nos enunciados, aulas, materiais oficiais e no Kit de Apoio do Challenge Taranis Black (Alura / ONE G11). Não pode ser alterado nem distorcido.
2. **[HIPÓTESE]**: Suposição operacional plausível e necessária para modelagem de processos, claramente identificada como tal. Deve ser testada ou validada e nunca apresentada como verdade consumada.
3. **[PROPOSTA]**: Recomendação estratégica, técnica ou metodológica desenhada pela consultoria de IA para resolver os problemas diagnosticados.

---

## 3. Fatos Conhecidos da Taranis Black (Dados Oficiais)

Os pontos abaixo representam os fatos identificados nos materiais institucionais da Alura analisados até o momento:

* **[FATO] Razão / Atuação:** Empresa brasileira fictícia do setor de ergonomia corporativa.
* **[FATO] Faturamento Anual:** R$ 48 milhões.
* **[FATO] Quadro de Colaboradores:** 280 funcionários.
* **[FATO] Ritmo de Crescimento:** Crescimento anual recente de 35%.
* **[FATO] Portfólio de Produtos:** Focado em três categorias:
  1. Cadeiras de alto desempenho (Linha ErgoPro).
  2. Mesas elétricas reguláveis (Linha SmartDesk).
  3. Cabines acústicas (Linha Silence).
* **[FATO] Desafio Organizacional Geral:** Processos manuais e burocráticos que prejudicam a eficiência operacional.
* **[FATO] Desafio Específico da Área Comercial:**
  * A equipe comercial B2B perde aproximadamente 40% do seu tempo semanal com atividades operacionais e repetitivas (preenchimento manual de CRM, redação de e-mails genéricos e rotinas burocráticas associadas).
  * Objeções frequentes de clientes corporativos focadas em **preço** e **prazo** dificultam e travam o fechamento de propostas comerciais B2B.
* **[FATO] Objetivo de Negócio:** Utilizar Inteligência Artificial para aumentar a produtividade operacional e a eficácia comercial.

---

### 3.1. Dados Parametrizados no Kit Oficial de Simulação (Alura G11)

Com a liberação do Kit Oficial de Apoio (`01_Catalogo_Produtos_e_Precos_Taranis_Black` e `02_Leads_B2B_Comercial.xlsx`), os seguintes parâmetros foram formalmente integrados à base factual da Taranis Black:

#### A. Catálogo Oficial de Produtos, Preços e Especificações Técnicas
* **Linha Taranis ErgoPro (Cadeiras Ergonômicas de Alto Desempenho):**
  * `[FATO]` **ErgoPro Executive:** R$ 3.490,00 | 5 anos de garantia integral | Apoio lombar 3D dinâmico, mecanismo italiano sincronizado, tela mesh alemã respirável | Laudos de conformidade integral à NR-17 (ABERGO) e norma internacional ANSI/BIFMA X5.1.
  * `[FATO]` **ErgoPro Specialist:** R$ 2.490,00 | 5 anos de garantia estrutural e 2 anos para tecido/espuma | Ajustes ergonômicos completos | Laudo NR-17.
  * `[FATO]` **ErgoPro Core:** R$ 1.890,00 | 3 anos de garantia integral | Projetada para postos operacionais em larga escala | Laudo NR-17.
* **Linha Taranis SmartDesk (Mesas Elevatórias Elétricas):**
  * `[FATO]` **SmartDesk Pro Dual 160:** R$ 4.800,00 | Motor duplo alemão com ruído ultrabaixo (<43 dB), velocidade 38 mm/s, sensor anticolisão giroscópico, memória programável para 4 alturas, tampo em madeira com certificação FSC | Garantia de 5 anos para estrutura e 3 anos para componentes elétricos/motores.
  * `[FATO]` **SmartDesk Studio 140:** R$ 3.600,00 | Motor duplo (<46 dB), capacidade de 100 kg, memória digital | Garantia de 5 anos para estrutura e 2 anos para eletrônica.
  * `[FATO]` **SmartDesk Compact 120:** R$ 2.700,00 | Motor simples de alta durabilidade, ideal para modelos de trabalho híbrido e estações compactas.
* **Linha Taranis Silence (Cabines Acústicas Corporativas):**
  * `[FATO]` **Silence Quad (4 Lugares / Sala de Reunião Ágil):** R$ 28.000,00 | Isolamento acústico de 32 dB certificado pela norma ISO 23351-1, sistema ativo de ventilação com sensor de CO2 e renovação total de ar a cada 90 segundos, iluminação LED regulável, tomadas AC e USB-C integradas.
  * `[FATO]` **Silence Duo (2 Lugares / Reuniões 1:1 e Pareamento):** R$ 21.000,00 | Atenuação acústica de 32 dB ISO 23351-1, ventilação inteligente.
  * `[FATO]` **Silence Solo (Individual / Calls e Foco Profundo):** R$ 14.500,00 | Atenuação de 30 dB, mesa retrátil integrada e ergonomia otimizada para trabalho focado.

#### B. Políticas Comerciais, Prazos e Logística Factual
* `[FATO]` **Condições de Pagamento Corporativo:** Faturamento B2B em 30, 60 e 90 dias no boleto bancário para pessoas jurídicas com mais de 2 anos de constituição (sujeito à análise de crédito rápida em até 2 horas).
* `[FATO]` **Prazos de Entrega Logística (Centro de Distribuição em Santa Catarina):**
  * Itens de linha com estoque: **5 a 8 dias úteis** para regiões Sul e Sudeste.
  * Projetos sob medida / customizados: **15 dias úteis** de fabricação e expedição.
  * Regiões Centro-Oeste, Norte e Nordeste: **12 a 20 dias úteis** conforme rota de transporte.
* `[FATO]` **Política de Frete:** Frete CIF gratuito para pedidos corporativos acima de R$ 35.000,00 destinados a capitais e regiões metropolitanas do Sul e Sudeste.
* `[FATO]` **Serviços de Valor Agregado:**
  * Emissão de **Laudo Ergonômico de Posto de Trabalho individualizado** em formato digital (PDF com assinatura digital por Engenheiro de Segurança e Ergonomista credenciado pela ABERGO) sem custo adicional em compras corporativas acima de 10 unidades.
  * Customização gratuita de cores de tela mesh e tampos de madeira FSC para pedidos acima de 30 posições (+5 dias úteis no prazo de fabricação).
  * Disponibilização de biblioteca completa de blocos 3D/BIM (arquivos Revit, SketchUp e AutoCAD) para suporte a arquitetos corporativos e gestores de Facilities.

#### C. Painel de Leads B2B e Mapeamento de Objeções (`02_Leads_B2B_Comercial.xlsx`)
* `[FATO]` **Volume Financeiro do Funil:** O painel oficial cataloga exatamente **20 contas corporativas qualificadas** no CRM, totalizando **R$ 4.693.630,00 em propostas abertas** (ticket médio de R$ 234.681,50).
* `[FATO]` **Personas Decisoras Mapeadas:** Interlocutores distribuídos entre **RH / People**, **Facilities / Infraestrutura / Arquitetura** e **Compras / Procurement / CFO**.
* `[FATO]` **Matriz de Objeções Oficiais (`OBJ-01` a `OBJ-05`):**
  * `OBJ-01` (Preço / Custo de Aquisição Inicial): Comparação direta com cadeiras convencionais de menor preço.
  * `OBJ-02` (Prazo de Entrega e Instalação): Urgência para inauguração de novos escritórios ou expansão de squads.
  * `OBJ-03` (Prioridade de Investimento / Prova de Valor): Dúvida sobre o retorno concreto da ergonomia ativa no absenteísmo corporativo.
  * `OBJ-04` (Conformidade com a NR-17 e Suporte Jurídico): Exigência de laudos e validação para afastar passivos trabalhistas.
  * `OBJ-05` (Durabilidade, Garantia e Manutenção): Receio de custos recorrentes de manutenção e desgaste de peças.

---

## 4. Informações Não Confirmadas e Limites de Dados (O que NÃO inventaremos)

Com a incorporação do Kit de Apoio, as lacunas técnicas e comerciais foram resolvidas documentalmente. Permanecem estritamente como **não confirmadas**, exigindo tratamento como hipóteses prudentes:

| Item Não Confirmado | Risco de Invenção | Como Tratar no Projeto |
| :--- | :--- | :--- |
| **Marca e arquitetura específica do software de CRM legado** | Supor compatibilidade nativa inexistente. | Tratar como `[HIPÓTESE]`; modelar a automação de CRM com conectores padrão de mercado (APIs REST / Webhooks) sem amarrar a uma marca proprietária não citada. |
| **Prontuários e dados de saúde individuais de colaboradores dos clientes** | Violação gravíssima do Art. 11 da LGPD (dados sensíveis de saúde). | `[PROPOSTA]` Bloqueio absoluto de dados nominais de atestados; utilizar exclusivamente dados agregados de absenteísmo corporativo e relatórios de conformidade ergonômica. |
| **Garantia de eliminação total de processos trabalhistas** | Promessa jurídica temerária e infundada. | Tratar a adequação à NR-17 como diligência técnica de conformidade e mitigação de risco regulatório, sem alegar imunidade judicial absoluta. |

---

## 5. Premissas de Trabalho e Diretrizes de Governança

1. **Priorização Neutra e Racional (Rota 0):** A priorização das iniciativas de IA apoia-se nos resultados da Matriz Esforço × Impacto já aprovada:
   * Automação de CRM: $E = 3{,}00$ ; $I = 3{,}60$ (Quadrante 1 — Quick Win / Fronteira Q2)
   * Personalização de E-mails e Leads: $E = 2{,}65$ ; $I = 3{,}50$ (Quadrante 1 — Quick Win)
   * Copiloto de Vendas Consultivas: $E = 3{,}05$ ; $I = 3{,}50$ (Quadrante 2 — Projeto Estratégico / Quick Win Educacional)
2. **Prioridade Estrita do Escopo Obrigatório:** As entregas obrigatórias da Rota 0 e Rota 1 são executadas com fidelidade total aos requisitos do template da Alura.
3. **Abordagem Human-in-the-Loop:** Qualquer fluxo de automação ou uso de IA generativa (e-mails, propostas, interações de CRM) possui ponto de revisão e aprovação humana explícita antes de qualquer envio ao cliente final.
4. **Governança e Proteção de Dados (LGPD):** Bloqueio estrito de dados sensíveis de saúde (Art. 11), base legal legítima para prospecção B2B (Art. 7º, V e IX com opt-out) e uso de contratos empresariais com cláusula DPA (*Data Processing Agreement* — Zero Data Retention).
5. **Isolamento de Ambientes:** Operação restrita ao diretório `Taranis-Sales-AI`, sem contato com outros projetos.
6. **Formato e Rastreabilidade:** Documentação formatada para transposição imediata para o modelo oficial do Google Docs (`template_rota1_vendas.pdf`).
