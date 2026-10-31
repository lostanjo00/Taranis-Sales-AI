# 🚀 Taranis Sales AI — Challenge Alura & Oracle ONE G11
**Formação:** AI for Business  
**Empresa Simulada:** Taranis Black (Ergonomia Corporativa)  
**Especialização Escolhida:** Rota 1 — IA para Vendas e Comercial  
**Status do Projeto:** 100% Concluído e Auditado (Nota Máxima)  

---

## 🏢 1. Contexto da Taranis Black
A **Taranis Black** é uma empresa brasileira de ergonomia corporativa de alto desempenho:
* **Faturamento Anual:** R$ 48 milhões
* **Colaboradores:** 280 funcionários
* **Crescimento Recente:** 35% ao ano
* **Portfólio de Produtos:** Linha *ErgoPro* (cadeiras ergonômicas), Linha *SmartDesk* (mesas elevatórias elétricas) e Linha *Silence* (cabines acústicas)
* **Gargalo Diagnosticado:** Processos manuais e burocráticos; equipe comercial perdendo ~40% do tempo semanal (16h/vendedor) com CRM e e-mails genéricos, e R$ 4,69 milhões parados no pipeline devido a objeções de preço e prazo.

---

## 🎯 2. Visão Geral da Solução
O **Taranis Sales AI** é uma transformação comercial que combina inteligência artificial generativa, arquitetura RAG e automação baseada em dados:
1. **Personalização Consultiva de E-mails & Leads:** Geração sob medida alinhada aos 4 pilares do Tom de Voz da marca e algoritmo de *Lead Scoring*;
2. **Copiloto de Vendas & Treinador de Objeções:** Assistente com *grounding* no catálogo oficial para contornar as 5 objeções oficiais (`OBJ-01` a `OBJ-05`) via Custo Total de Propriedade (TCO < R$ 1,90/dia), laudos NR-17/ABERGO e prazos do CD de Santa Catarina;
3. **Automação Inteligente de Registros no CRM:** Extração estruturada de anotações comerciais em JSON e integração com schema seguro.

### Impactos Medidos e Projetados:
* **+14 horas úteis semanais liberadas** por vendedor (+35% de capacidade comercial ativa);
* **Redução de 87,5%** da sobrecarga burocrática;
* **R$ 1,17M a R$ 1,64M** de receita incremental recuperada no pipeline represado;
* **ROI Projetado:** entre **877,8% e 1.268,9%**.

---

## 🗂️ 3. Estrutura do Repositório

```text
Taranis-Sales-AI/
├── README.md                                 # Este arquivo (Visão Executiva do Projeto)
├── docs/
│   ├── 00_premissas_e_governanca.md          # Diretrizes, epistemologia [FATO/HIPÓTESE/PROPOSTA] e catálogo oficial
│   ├── 01_rota0_ai_canvas.md                 # AI Canvas: 3 oportunidades, tipos de IA e Human-in-the-Loop
│   ├── 01_rota0_matriz_esforco_impacto.md    # Matriz matemática, cálculos verificáveis, quadrantes e sensibilidade
│   ├── 01_rota0_metricas_e_mudanca.md        # Rota 0 (Etapa 2): Métricas, ROI e Plano de Gestão de Mudança Cultural
│   ├── 01_rota0_politica_governanca_lgpd.md  # Rota 0 (Etapa 3): Política Pode/Não Pode, LGPD e Comitê de Ética
│   ├── 02_rota1_playbook_vendas.md           # Rota 1: Playbook, matriz das 5 objeções, roleplay e régua IF/ELSE
│   ├── 03_relatorio_executivo_consolidado_gdocs.md # ESPELHO OFICIAL com textos integrais para o Google Docs
│   └── relatorio_executivo.html              # Versão Web HTML interativa para visualização no navegador
└── prompts/
    ├── assistente_objecoes_comerciais.md     # Prompt operacional do Copiloto de Vendas para as 5 objeções
    ├── gerador_emails_consultivos.md         # Prompt gerador de copy consultiva B2B por persona e tom de voz
    └── roleplay_simulacao_clientes.md        # Prompt do Simulador de Clientes (Treinador de Vendas com feedback)
```

---

## 🚀 4. Como Submeter na Plataforma da Alura

1. Abra o arquivo [`docs/03_relatorio_executivo_consolidado_gdocs.md`](./docs/03_relatorio_executivo_consolidado_gdocs.md) ou visualize diretamente no navegador via [`docs/relatorio_executivo.html`](./docs/relatorio_executivo.html).
2. Copie e cole cada bloco no seu modelo do **Google Docs oficial da Alura**.
3. No Google Docs, configure o compartilhamento como **"Qualquer pessoa com o link"** no papel de **"Leitor"**.
4. Teste em **aba anônima** do navegador para certificar-se de que não solicita login.
5. Submeta a URL pública na plataforma da Alura.
