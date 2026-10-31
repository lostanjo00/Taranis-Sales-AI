# Priorização Baseada em Dados & Gestão de Mudança — Taranis Black
**Projeto:** Taranis Sales AI — Challenge Alura (AI for Business) | ONE G11  
**Etapa:** Rota 0 — Base Estratégica (Obrigatória) — Etapa 2 do Template Oficial  
**Documentos de Referência:** [`docs/00_premissas_e_governanca.md`](./00_premissas_e_governanca.md) | [`docs/01_rota0_ai_canvas.md`](./01_rota0_ai_canvas.md) | [`docs/01_rota0_matriz_esforco_impacto.md`](./01_rota0_matriz_esforco_impacto.md)  
**Classificação Metodológica:** Estimativas analíticas baseadas em `[FATO]`, `[HIPÓTESE]` e `[PROPOSTA]`  

---

## 1. Contexto e Objetivos

Este documento formaliza a **Etapa 2 da Rota 0** do template oficial da Alura, estabelecendo o plano quantitativo de métricas de sucesso, estimativas de horas liberadas, retorno sobre investimento (ROI) projetado e a estratégia estruturada de gestão de mudança cultural para a Taranis Black.

O plano ancora-se diretamente nos resultados auditados da **Matriz Esforço × Impacto**, nos fatos operacionais documentados (`[FATO]` ~40% do tempo comercial consumido em burocracia e 20 contas somando R$ 4,69 milhões paradas no funil) e no compromisso de governança de não apresentar projeções futuras como fatos consumados, mas como metas gerenciais rigorosamente calculadas.

---

## 2. Ordem de Implantação das Iniciativas (Roteiro da Matriz Esforço × Impacto)

A priorização estratégica obedece às coordenadas analíticas validadas na Matriz Esforço × Impacto, organizando a transformação em **três ondas evolutivas**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ CRONOGRAMA INTEGRADO DE IMPLANTAÇÃO (ROADMAP ESTRATÉGICO)                              │
├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
│ ONDA 1: MÊS 1 A MÊS 2    │ ONDA 2: MÊS 2 A MÊS 4    │ ONDA 3: MÊS 4 A MÊS 6            │
│ (QUICK WIN IMEDIATO)     │ (CAPACITAÇÃO DE VALOR)   │ (SUSTENTAÇÃO SISTÊMICA)          │
│                          │                          │                                  │
│ Personalização de E-mails│ Copiloto de Vendas &     │ Automação de Registros no CRM    │
│ e Qualificação de Leads  │ Tratamento de Objeções   │                                  │
│                          │                          │                                  │
│ • Coord: (2,65 ; 3,50)   │ • Coord: (3,05 ; 3,50)   │ • Coord: (3,00 ; 3,60)           │
│ • Quadrante 1 (Quick Win)│ • Quadrante 2 / Q1 Educ. │ • Quadrante 1 / Borda Q2         │
│ • Baixo atrito técnico   │ • Destrava as 5 objeções │ • Depende de integração com APIs │
│ • Impacto imediato no funil│ • Foco em valor (TCO)  │ • Padroniza dados corporativos   │
└──────────────────────────┴──────────────────────────┴──────────────────────────────────┘
```

### Racional de Sequenciamento
1. **Onda 1 — Personalização de E-mails & Leads ($E = 2{,}65$ | $I = 3{,}50$):** Início imediato pela iniciativa de menor complexidade de infraestrutura. Entrega valor tangível na primeira quinzena para o time de prospecção, estabelecendo o primeiro contato positivo da equipe comercial com a IA.
2. **Onda 2 — Copiloto de Vendas Consultivas ($E = 3{,}05$ | $I = 3{,}50$):** Entra em operação como ferramenta de capacitação e simulação de *roleplay*. Ataca a principal dor comercial (`[FATO]` objeções de preço e prazo), preparando os consultores para converter o pipeline represado antes da automação sistêmica.
3. **Onda 3 — Automação de Registros no CRM ($E = 3{,}00$ | $I = 3{,}60$):** Enquanto as duas primeiras iniciativas geram tração e engajamento, a equipe de TI homologa as APIs e conectores do CRM, permitindo uma implantação madura e com baixo atrito operacional.

---

## 3. Métricas de Sucesso, Horas Economizadas e ROI Estimado

### 3.1. Diagnóstico da Carga Horária e Horas Economizadas

* `[FATO]` A equipe comercial perde aproximadamente 40% do seu tempo semanal com atividades operacionais e repetitivas.
* `[HIPÓTESE]` Considerando uma jornada padrão de 40 horas semanais por consultor de vendas, o tempo consumido por tarefas burocráticas equivale a **16 horas semanais por vendedor**.
* `[PROPOSTA]` O Taranis Sales AI visa recuperar **14 horas semanais por vendedor**, atacando as três frentes do problema:

| Frente de Atuação da IA | Horas Dedicadas (Baseline Atual) | Horas Recuperadas (Meta Proposta) | Tempo Restante com IA | Ganho de Eficiência |
| :--- | :---: | :---: | :---: | :---: |
| **Personalização de E-mails e Triagem de Leads** | 6,0 h / semana | **5,0 h / semana** | 1,0 h / semana (revisão) | **83,3%** de redução no tempo de redação |
| **Pesquisa e Preparação para Objeções de Vendas** | 3,5 h / semana | **3,0 h / semana** | 0,5 h / semana (consulta ágil) | **85,7%** de redução no tempo de pesquisa |
| **Preenchimento Manual e Atualização de CRM** | 6,5 h / semana | **6,0 h / semana** | 0,5 h / semana (validação humana) | **92,3%** de redução no tempo de digitação |
| **Total de Sobrecarga Burocrática** | **16,0 h / semana (40%)** | **14,0 h / semana (35%)** | **2,0 h / semana (5%)** | **Redução de 87,5% da carga burocrática** |

$$\text{Impacto na Capacidade Comercial: } \frac{14\text{ horas liberadas}}{40\text{ horas totais}} = +35\% \text{ de tempo útil real redirecionado para relacionamento com clientes.}$$

---

### 3.2. Projeção de Recuperação de Receita e ROI Estimado

A modelagem de retorno econômico fundamenta-se nos dados reais do painel comercial da Taranis Black (`[FATO]` `02_Leads_B2B_Comercial.xlsx`):

* `[FATO]` **Pipeline Atual em Negociação:** 20 contas corporativas abertas somando **R$ 4.693.630,00**.
* `[FATO]` Todas as 20 contas enfrentam atualmente travas formais categorizadas nas 5 objeções oficiais (`OBJ-01` a `OBJ-05`).
* `[HIPÓTESE]` Com o suporte do Copiloto de Vendas e argumentos consultivos de valor/TCO, estabelece-se como meta destravar uma taxa de conversão adicional entre **25% e 35%** desse volume represado:

$$\text{Receita Recuperada (Cenário Conservador - 25%): } R\$\,4.693.630,00 \times 0{,}25 = \mathbf{R\$\,1.173.407,50}$$

$$\text{Receita Recuperada (Cenário Alvo - 35%): } R\$\,4.693.630,00 \times 0{,}35 = \mathbf{R\$\,1.642.770,50}$$

#### Estimativa de Custo de Implementação e ROI do Projeto:
* `[HIPÓTESE]` Investimento total estimado em desenvolvimento, licenças corporativas de IA com DPA, infraestrutura segura de APIs e programa de treinamento da equipe: **R$ 120.000,00**.
* `[PROPOSTA]` **Cálculo de Retorno sobre o Investimento (ROI):**

$$\text{ROI Conservador} = \frac{\text{Receita Recuperada } - \text{Custo}}{\text{Custo}} = \frac{R\$\,1.173.407,50 - R\$\,120.000,00}{R\$\,120.000,00} = \mathbf{877{,}8\% \text{ (ou 9,7x o investimento)}}$$

$$\text{ROI Alvo} = \frac{R\$\,1.642.770,50 - R\$\,120.000,00}{R\$\,120.000,00} = \mathbf{1.268{,}9\% \text{ (ou 13,6x o investimento)}}$$

*Ressalva Metodológica de Governança:* Esses números representam o potencial analítico projetado com base na conversão das contas existentes, devendo ser acompanhados mensalmente por indicadores de desempenho reais.

---

### 3.3. Painel de Metas de Adoção e KPIs por Iniciativa

| Iniciativa | Métrica Operacional Primária | Meta em 60 Dias | Meta em 120 Dias | Meta em 180 Dias (Maturidade) |
| :--- | :--- | :---: | :---: | :---: |
| **1. E-mails e Leads** | Taxa de utilização ativa dos rascunhos de e-mail pela equipe. | 60% dos e-mails | 85% dos e-mails | **≥ 95%** dos e-mails comerciais |
| | Redução no tempo médio de personalização por mensagem. | -40% do tempo | -65% do tempo | **-80%** (de 25 min para 5 min) |
| **2. Copiloto de Vendas** | Realização de simulações de roleplay antes de reuniões críticas. | 1 simulação/semana | 3 simulações/semana | **≥ 5 simulações/semana por vendedor** |
| | Taxa de conversão de propostas que apresentaram objeções. | Linha de base | +15% de avanço | **+25% a +35% de propostas ganhas** |
| **3. Automação de CRM** | Taxa de completude de campos obrigatórios no CRM em até 24h. | 50% dos campos | 80% dos campos | **≥ 95% dos registros atualizados** |
| | Horas semanais liberadas de digitação por vendedor. | 2,0 h / semana | 4,5 h / semana | **6,0 h / semana por consultor** |

---

## 4. Plano de Gestão de Mudança Cultural

A introdução de Inteligência Artificial em equipes comerciais B2B de alta performance frequentemente esbarra em barreiras humanas e comportamentais. Para mitigar esses riscos, adota-se um framework estruturado de mudança cultural:

### 4.1. Mapeamento das Resistências Culturais e Planos de Ação

| Barreira Cultural Mapeada | Causa Raiz Psicológica | Plano de Ação Prático de Mitigação |
| :--- | :--- | :--- |
| **Síndrome do "Sempre vendi assim"** | Vendedores seniores acreditam que seu método empírico é superior e desconfiam de orientações geradas por IA. | **Apresentação Orientada a Resultados:** Envolver os vendedores seniores no refinamento dos prompts; demonstrar que a IA atua como assistente pessoal de pesquisa para poupá-los de tarefas chatas, e não como um fiscal de conduta. |
| **Medo da Substituição Profissional** | Receio de que a automação torne o consultor dispensável pela diretoria. | **Posicionamento Institucional Transparente:** Comunicação clara da liderança afirmando que a venda ergonômica consultiva de alto ticket é essencialmente humana e insubstituível; a IA existe para eliminar o trabalho braçal e permitir que o vendedor atue como consultor estratégico. |
| **Falta de Confiança nas Respostas (Alucinação)** | Medo de passar informações erradas de garantia ou preço para o comprador. | **Arquitetura Fechada (*Grounding*):** Treinamento demonstrando que o copiloto utiliza estritamente o Catálogo Oficial da Taranis Black; exigência obrigatória de validação humana antes de qualquer envio. |
| **Sobrecarga de Novas Ferramentas** | Cansaço com múltiplos logins, sistemas legados e interfaces pouco amigáveis. | **Integração no Fluxo de Trabalho Habitual:** Disponibilização da IA nos canais que o vendedor já utiliza no dia a dia (extensão de e-mail e atalhos rápidos), sem exigir preenchimentos redundantes. |

---

### 4.2. Estratégia de Implementação e Adoção em 4 Pilares

```text
┌────────────────────────────────────────────────────────────────────────┐
│ OS 4 PILARES DA GESTÃO DE MUDANÇA NA TARANIS BLACK                    │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. SQUAD DE       │ 2. SEGURANÇA      │ 3. CAPACITAÇÃO                 │
│ EMBAIXADORES      │ PSICOLÓGICA       │ PRÁTICA                        │
│                   │                   │                                │
│ Seleção de 3 con- │ Erros em simu-    │ Workshops mão na               │
│ sultores referên- │ lações de role-   │ massa focados nas 20           │
│ cia para co-criar │ play não impactam │ contas reais do                │
│ e validar os      │ avaliação indivi- │ pipeline da empresa            │
│ primeiros prompts │ dual do vendedor  │                                │
├───────────────────┴───────────────────┴────────────────────────────────┤
│ 4. RECONHECIMENTO & GAMIFICAÇÃO: Celebração de vitórias rápidas        │
│    (ex: primeiro contrato destravado via contorno de objeção da IA).   │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Squad de Embaixadores Comerciais (*Early Adopters*):**
   * Seleção prévia de 2 a 3 consultores de vendas respeitados pelos pares (um perfil júnior e dois seniores).
   * Esses colaboradores participam da calibração inicial dos prompts de e-mail e objeções, tornando-se porta-vozes legítimos dos benefícios para o restante da equipe.
2. **Ambiente Seguro de Aprendizado (*Roleplay* com Segurança Psicológica):**
   * As simulações do Copiloto de Vendas são tratadas como ambiente de treino e desenvolvimento individual, sem compartilhamento de notas de desempenho punitivas com a gerência.
   * O foco é permitir que o vendedor teste abordagens ousadas e aprenda com o feedback da IA antes de interagir com o cliente real.
3. **Capacitação Prática em Casos Reais:**
   * Treinamentos conduzidos diretamente sobre a base oficial de 20 contas abertas (`02_Leads_B2B_Comercial.xlsx`), ensinando os consultores a gerar abordagens sob medida para os casos reais de clientes que estão travados por preço ou prazo.
4. **Ciclos Semanais de Feedback e Refinamento:**
   * Ritos semanais de 30 minutos ("Voz do Vendedor") para coletar críticas, apontar alucinações ou termos artificiais e ajustar os prompts continuamente com a equipe técnica.
