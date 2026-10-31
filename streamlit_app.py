import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ---------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Taranis Sales AI — Copiloto Comercial B2B",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# ESTILOS VISUAIS PERSONALIZADOS (CSS)
# ---------------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #0284c7 100%);
        color: white;
        padding: 1.2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .metric-card h3 {
        margin: 0;
        font-size: 0.95rem;
        color: #e0f2fe;
    }
    .metric-card p {
        margin: 0.3rem 0 0 0;
        font-size: 1.8rem;
        font-weight: 700;
    }
    .card-box {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        font-size: 0.8rem;
        font-weight: 600;
        border-radius: 9999px;
        background-color: #dbeafe;
        color: #1e40af;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# DADOS OFICIAIS TARANIS BLACK (GROUNDING)
# ---------------------------------------------------------
PORTFOLIO = {
    "ErgoPro Executive (Cadeira)": {"preco": 3490.00, "garantia_anos": 5, "norma": "NR-17 ABERGO e ANSI/BIFMA X5.1"},
    "ErgoPro Specialist (Cadeira)": {"preco": 2490.00, "garantia_anos": 5, "norma": "NR-17 ABERGO (5 anos estrutural / 2 anos tecido)"},
    "ErgoPro Core (Cadeira)": {"preco": 1890.00, "garantia_anos": 3, "norma": "NR-17 ABERGO"},
    "SmartDesk Pro Dual 160 (Mesa)": {"preco": 4800.00, "garantia_anos": 5, "norma": "Motor duplo alemão <43 dB, tampo FSC"},
    "SmartDesk Studio 140 (Mesa)": {"preco": 3600.00, "garantia_anos": 3, "norma": "Ajuste elétrico com memória"},
    "Silence Quad 4 Lugares (Cabine)": {"preco": 28000.00, "garantia_anos": 5, "norma": "Atenuação 32 dB ISO 23351-1, sensor CO2"},
    "Silence Duo 2 Lugares (Cabine)": {"preco": 21000.00, "garantia_anos": 5, "norma": "Atenuação 32 dB ISO 23351-1"},
    "Silence Solo 1 Lugar (Cabine)": {"preco": 14500.00, "garantia_anos": 3, "norma": "Atenuação 30 dB ISO 23351-1"}
}

OBJECOES = {
    "OBJ-01 (Preço)": {
        "titulo": "Preço: Concorrente é 30% mais barato",
        "dor": "Foco míope no custo inicial de aquisição (CAPEX) sem considerar reposição precoce e passivos trabalhistas.",
        "pilar": "Científico e Sofisticado (TCO < R$ 1,91/dia)",
        "estrategia": "Demonstrar que móveis comuns duram em média 14 meses no uso corporativo severo. Com 5 anos de garantia, o custo da ErgoPro é de R$ 1,91/dia por colaborador, eliminando recompra e incluindo laudo ergonômico individualizado."
    },
    "OBJ-02 (Orçamento)": {
        "titulo": "Orçamento: Congelado/Fechado pelo CFO neste semestre",
        "dor": "Restrição orçamentária para despesas de capital imediatas.",
        "pilar": "Descomplicado e Flexível (Faturamento 30/60/90)",
        "estrategia": "Posicionar ergonomia ativa como mitigação imediata de absenteísmo por LER/DORT (reduz dias parados) e viabilizar via faturamento faturado em 30/60/90 dias no boleto (OPEX diluído)."
    },
    "OBJ-03 (Fornecedor Atual)": {
        "titulo": "Fornecedor Atual: Compramos do mesmo parceiro homologado há anos",
        "dor": "Zona de conforto e aversão ao risco de troca de homologação.",
        "pilar": "Empático e Sem Atrito (Projeto-Piloto)",
        "estrategia": "Não confrontar o fornecedor tradicional. Posicionar a Taranis Black em uma nova categoria (Ergonomia Ativa) e propor Projeto-Piloto de 2 posições por 15 dias sem compromisso em setor com alta taxa de queixas posturais."
    },
    "OBJ-04 (Prazo de Entrega)": {
        "titulo": "Prazo: 20 a 25 dias para nossa cidade é muito longo",
        "dor": "Urgência de inauguração de filial ou admissão de novos colaboradores.",
        "pilar": "Transparente e Operacional (CD Santa Catarina)",
        "estrategia": "Ativar o estoque regulador do CD em Santa Catarina com entrega escalonada imediata de 5 a 8 dias úteis para Sul/Sudeste (Frete CIF bonificado acima de R$ 35 mil)."
    },
    "OBJ-05 (Customização/Layout)": {
        "titulo": "Customização: Dúvida se combina com a identidade visual ou layout",
        "dor": "Insegurança estética de arquitetos e facilities sobre harmonia visual.",
        "pilar": "Visual e Técnico (Famílias BIM/Revit + Amostras 48h)",
        "estrategia": "Disponibilizar biblioteca completa de blocos 3D/BIM (Revit/SketchUp), envio de maleta de amostras físicas de mesh/madeiras em 48h e customização gratuita de cores para pedidos acima de 30 posições (+5 dias úteis)."
    }
}

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=64)
    st.title("Taranis Sales AI")
    st.caption("Challenge Alura & Oracle ONE G11 — AI for Business")
    st.markdown("---")
    
    st.markdown("### 👤 Autor do Projeto")
    st.write("**Mauricio Ribeiro de Souza Junior**")
    st.write("E-mail: `mauriciojr918@gmail.com`")
    st.write("Especialização: **Rota 1 — Vendas B2B**")
    st.markdown("---")
    
    st.markdown("### 🔗 Links Oficiais")
    st.markdown("[🐙 Repositório GitHub](https://github.com/lostanjo00/Taranis-Sales-AI)")
    st.markdown("[📄 Documento Google Docs](https://docs.google.com/document/d/1ThyiyNUsoiy5e4B3MlNzqMmAQR-fZFW2MvcZATGpFuA/edit?usp=sharing)")
    st.markdown("[🌐 Publicação no LinkedIn](https://www.linkedin.com/feed/)")
    st.markdown("---")
    
    st.info("💡 **Status:** 100% Auditado com Grounding Oficial da Taranis Black.")

# ---------------------------------------------------------
# CABEÇALHO PRINCIPAL
# ---------------------------------------------------------
st.markdown('<div class="main-header">🚀 Taranis Sales AI — Copiloto Comercial B2B</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Plataforma Inteligente de Vendas Consultivas, Mitigação de Objeções e Engenharia de TCO para Ergonomia Corporativa</div>', unsafe_allow_html=True)

# CARDS DE IMPACTO NO TOPO
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><h3>HORAS LIBERADAS</h3><p>+14h/sem</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h3>REDUÇÃO BUROCRACIA</h3><p>-87,5%</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h3>RECEITA RECUPERADA</h3><p>R$ 1,17M - 1,64M</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><h3>ROI PROJETADO</h3><p>877% - 1.268%</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# ABAS DA APLICAÇÃO
# ---------------------------------------------------------
tab_copiloto, tab_emails, tab_tco, tab_roleplay, tab_governanca = st.tabs([
    "🎯 Copiloto de Objeções",
    "✉️ Gerador de E-mails Consultivos",
    "📈 Calculadora TCO & ROI",
    "🤖 Treinador Roleplay",
    "🏛️ AI Canvas & Governança"
])

# =========================================================
# ABA 1: COPILOTO DE OBJEÇÕES
# =========================================================
with tab_copiloto:
    st.subheader("🎯 Copiloto de Contorno das 5 Objeções Oficiais")
    st.write("Selecione os parâmetros da oportunidade comercial para gerar a estratégia de abordagem fundamentada em TCO, laudos e normas técnicas:")
    
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        obj_selecionada = st.selectbox("Objeção Apresentada pelo Cliente:", list(OBJECOES.keys()))
    with col_input2:
        produto_selecionado = st.selectbox("Produto Principal da Proposta:", list(PORTFOLIO.keys()))
    with col_input3:
        qtd_posicoes = st.number_input("Quantidade de Posições (unidades):", min_value=1, max_value=500, value=25)
        
    cliente_nome = st.text_input("Nome da Empresa Cliente:", value="TechCorp Inovações S.A.")
    contato_nome = st.text_input("Nome do Decisor:", value="Dr. Roberto Neves (Diretor de Procurement)")
    
    if st.button("Gerar Argumentação Consultiva Estruturada ⚡", type="primary"):
        obj_info = OBJECOES[obj_selecionada]
        prod_info = PORTFOLIO[produto_selecionado]
        valor_total = prod_info["preco"] * qtd_posicoes
        dias_uteis_5anos = 5 * 252 # ~1.260 dias
        tco_diario = prod_info["preco"] / dias_uteis_5anos if prod_info["garantia_anos"] == 5 else prod_info["preco"] / (3 * 252)
        
        st.success("✅ Argumentação estruturada com base nas diretrizes oficiais da Taranis Black:")
        
        c1, c2 = st.columns([1, 1])
        with c1:
            st.markdown("### 🩺 1. Diagnóstico da Objeção")
            st.info(f"**Dor Real:** {obj_info['dor']}")
            st.markdown(f"**Pilar de Tom de Voz:** `{obj_info['pilar']}`")
            st.markdown(f"**Estratégia Recomendada:** {obj_info['estrategia']}")
            
            st.markdown("### 📊 2. Métricas Fatuais de Apoio")
            st.write(f"- **Valor Total do Lote:** R$ {valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            st.write(f"- **TCO Real por Posto:** R$ {tco_diario:.2f}/dia por colaborador ao longo da garantia.")
            st.write(f"- **Garantia de Fábrica:** {prod_info['garantia_anos']} anos com cobertura total ({prod_info['norma']}).")
            if qtd_posicoes >= 10:
                st.write("- **Bônus Ativado:** Laudo Ergonômico de Posto de Trabalho individualizado em PDF assinado por Ergonomista ABERGO sem custo extra.")
            if valor_total >= 35000:
                st.write("- **Condição Logística:** Frete CIF Bonificado (Gratuito) para capitais Sul/Sudeste com entrega de 5 a 8 dias úteis.")
            if qtd_posicoes >= 30:
                st.write("- **Customização VIP:** Cores corporativas da tela mesh e acabamento FSC dos tampos sem acréscimo.")
                
        with c2:
            st.markdown("### 💬 3. Rascunho Consultivo Pronto (Revisão Humana Obrigatória)")
            
            mensagem_rascunho = f"""Olá, {contato_nome}, tudo bem?

Compreendo perfeitamente sua consideração sobre {obj_info['titulo'].lower()}. É um ponto fundamental na gestão responsável de recursos da {cliente_nome}.

Ao analisarmos a implantação das {qtd_posicoes} posições da {produto_selecionado}, nosso foco é o Custo Total de Propriedade (TCO): enquanto móveis convencionais demandam manutenção e reposição após 14 meses, a Taranis Black oferece {prod_info['garantia_anos']} anos de garantia integral de fábrica, resultando em um investimento diluído de apenas R$ {tco_diario:.2f} por dia por colaborador.

Além disso, para este volume de {qtd_posicoes} posições:
• Incluímos gratuitamente o Laudo Ergonômico Individualizado (NR-17 / ABERGO) para o PGR da sua empresa;
• Viabilizamos faturamento faturado em 30/60/90 dias no boleto para adequar ao fluxo financeiro;
• Garantimos atendimento ágil via nosso Centro de Distribuição em Santa Catarina (5 a 8 dias úteis).

Teria 10 minutos nesta semana para avaliarmos uma demonstração técnica sem compromisso de 2 posições-piloto na sua sede?

Atenciosamente,
Consultoria Comercial B2B | Taranis Black"""
            
            st.text_area("Copiar Mensagem:", value=mensagem_rascunho, height=360)
            st.caption("🔒 *Governança Human-in-the-Loop:* Revise o texto antes de disparar.")

# =========================================================
# ABA 2: GERADOR DE E-MAILS CONSULTIVOS
# =========================================================
with tab_emails:
    st.subheader("✉️ Gerador de E-mails Consultivos B2B por Persona")
    st.write("Gere abordagens de alta conversão alinhadas às dores específicas de cada decisor corporativo:")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        persona = st.selectbox("Selecione a Persona de Destino:", [
            "RH / Gente & Gestão (Foco: Bem-estar, Absenteísmo e NR-17)",
            "Facilities & Arquitetura (Foco: Acústica, BIM/Revit e Layout)",
            "Compras / CFO / Procurement (Foco: TCO, ROI e Faturamento 30/60/90)"
        ])
        nome_empresa_email = st.text_input("Empresa Prospectada:", value="Studio Alfa Arquitetura & Design")
    with col_p2:
        dor_especifica = st.selectbox("Principal Ponto de Contato:", [
            "Cabines Acústicas Silence (Retrofit sem obras ou drywall)",
            "Cadeiras ErgoPro (Redução de queixas posturais no regime híbrido)",
            "SmartDesk Pro (Mesas com ajuste elétrico para ergonomia ativa)"
        ])
        nome_contato_email = st.text_input("Nome do Destinatário:", value="Beatriz Siqueira (Gerente de Projetos)")

    if st.button("Gerar E-mail Consultivo Personalizado 🚀", type="primary"):
        st.markdown("### 📋 Sugestões de Assunto (Alta Taxa de Abertura):")
        if "RH" in persona:
            st.write("1. *[Curiosidade]* Nova NR-17: Como empresas de tecnologia estão blindando a saúde postural de times híbridos")
            st.write("2. *[Solução]* Redução de queixas lombares na equipe da {nome_empresa_email}")
            st.write("3. *[Valor]* Laudos ergonômicos ABERGO individualizados para o PGR da {nome_empresa_email}")
            corpo = f"""Olá, {nome_contato_email}, tudo bem?

Acompanho o crescimento da {nome_empresa_email} e sei como é desafiador manter a energia e a retenção de talentos quando queixas de dores nas costas e fadiga postural começam a impactar o dia a dia da equipe.

Na Taranis Black, desenvolvemos a Linha ErgoPro justamente para transformar a ergonomia em produtividade ativa: nossas cadeiras possuem regulagens micrométricas biomecânicas e 5 anos de garantia de fábrica, em conformidade integral com a NR-17 e normas ABERGO.

Para cada posto implantado, fornecemos sem custo o Laudo Ergonômico de Posto de Trabalho individualizado assinado por Ergonomista credenciado, simplificando a conformidade do seu PGR.

Você teria 10 minutos nesta quinta-feira para conversarmos sobre como podemos disponibilizar 2 posições para teste prático na sua equipe?

Um abraço,
Consultoria de Ergonomia Corporativa | Taranis Black

---
Caso não deseje receber nossos conteúdos técnicos sobre saúde ocupacional, responda com "Descadastrar" e removeremos seu contato imediatamente."""
        elif "Facilities" in persona:
            st.write("1. *[Técnico]* Famílias Revit/BIM e conforto acústico de 32 dB para os projetos da {nome_empresa_email}")
            st.write("2. *[Dor]* Privacidade acústica e pods corporativos sem obras ou sujeira")
            st.write("3. *[Agilidade]* Catálogo 3D e pronta-entrega em 5 a 8 dias do CD Santa Catarina")
            corpo = f"""Olá, {nome_contato_email}, tudo bem?

Acompanho os projetos corporativos desenvolvidos pela {nome_empresa_email} e admiro o cuidado com ambientes que integram estética e alta funcionalidade.

Sabemos que um dos maiores desafios nos escritórios contemporâneos é viabilizar chamadas e reuniões ágeis sem recorrer a dispendiosas obras de drywall, que engessam o layout e geram poeira.

Desenvolvemos a Linha Taranis Silence exatamente para solucionar essa dor: nossas cabines acústicas entregam atenuação real de 32 dB certificada pela norma ISO 23351-1, com renovação total de ar a cada 90 segundos via sensor de CO2 e montagem limpa em menos de 3 horas.

Disponibilizamos nossa biblioteca completa de blocos 3D e famílias Revit/SketchUp de toda a linha. Você teria 10 minutos para eu lhe encaminhar o acesso aos arquivos 3D e avaliarmos uma parceria técnica para seus projetos?

Um abraço,
Consultoria Técnica B2B | Taranis Black

---
Caso não deseje receber materiais técnicos sobre arquitetura corporativa, responda com "Descadastrar" e removeremos seu contato imediatamente."""
        else:
            st.write("1. *[Financeiro]* TCO de R$ 1,91/dia e garantia de 5 anos em mobiliário corporativo")
            st.write("2. *[ROI]* Otimização de CAPEX: Faturamento em 30/60/90 para a {nome_empresa_email}")
            st.write("3. *[Eficiência]* Redução do custo de recompra de mobiliário na {nome_empresa_email}")
            corpo = f"""Olá, {nome_contato_email}, tudo bem?

Ao analisar aquisições corporativas de mobiliário, o maior desafio dos times de Procurement é evitar o custo invisível da reposição precoce: pesquisas de mercado mostram que cadeiras de entrada quebram em média após 14 meses, gerando recompra contínua e passivos trabalhistas.

Na Taranis Black, trabalhamos sob a ótica do Custo Total de Propriedade (TCO): com 5 anos de garantia de fábrica integral, o custo de uma cadeira ErgoPro Executive dilui-se a menos de R$ 1,91 por dia de uso por colaborador.

Para apoiar o planejamento financeiro da {nome_empresa_email}, oferecemos faturamento em 30/60/90 dias no boleto bancário (preservando o caixa) e frete CIF bonificado acima de R$ 35 mil com entrega do CD Santa Catarina em 5 a 8 dias úteis.

Você teria 10 minutos nesta semana para avaliarmos uma planilha comparativa de TCO específica para o volume da {nome_empresa_email}?

Atenciosamente,
Consultoria Comercial B2B | Taranis Black

---
Caso não deseje receber nossas análises financeiras de TCO corporativo, responda com "Descadastrar" e removeremos seu contato imediatamente."""

        st.text_area("Corpo do E-mail (Formatado em menos de 150 palavras + Opt-out LGPD):", value=corpo, height=330)

# =========================================================
# ABA 3: CALCULADORA INTERATIVA DE TCO & ROI
# =========================================================
with tab_tco:
    st.subheader("📈 Calculadora Interativa de TCO: Cadeira Comum vs. Taranis ErgoPro")
    st.write("Compare o custo real acumulado em 5 anos (60 meses) de operação corporativa:")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        num_postos = st.slider("Número de Colaboradores / Postos:", 5, 200, 30, step=5)
        custo_comum = st.number_input("Preço de Cadeira Genérica de Mercado (R$):", value=1200.0, step=50.0)
        vida_util_comum_meses = st.slider("Vida Útil Média de Cadeira Genérica (Meses):", 10, 24, 14)
    with col_c2:
        modelo_taranis = st.selectbox("Modelo Taranis ErgoPro:", ["ErgoPro Executive (R$ 3.490)", "ErgoPro Specialist (R$ 2.490)"])
        preco_taranis = 3490.0 if "Executive" in modelo_taranis else 2490.0
        st.write(f"**Garantia Integral Taranis:** 60 Meses (5 Anos)")
        st.write(f"**Laudo NR-17 Incluso:** Sim (R$ 0,00)")
        st.write(f"**Recompra Necessária no Período:** Nenhuma (0)")
        
    # CÁLCULOS
    recompras_necessarias = int(60 / vida_util_comum_meses)
    custo_total_comum_unidade = custo_comum * (1 + recompras_necessarias) + 350.0 # +350 laudo avulso e manutenção
    custo_total_taranis_unidade = preco_taranis
    
    total_gasto_comum = custo_total_comum_unidade * num_postos
    total_gasto_taranis = custo_total_taranis_unidade * num_postos
    economia_gerada = total_gasto_comum - total_gasto_taranis
    
    col_res1, col_res2, col_res3 = st.columns(3)
    with col_res1:
        st.metric("Gasto Total com Cadeiras Comuns (5 Anos)", f"R$ {total_gasto_comum:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col_res2:
        st.metric("Investimento Único Taranis Black (5 Anos)", f"R$ {total_gasto_taranis:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    with col_res3:
        st.metric("Economia Real Direta (TCO)", f"R$ {economia_gerada:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), delta=f"{((economia_gerada/total_gasto_comum)*100):.1f}% de economia")
        
    # GRÁFICO PLOTLY DE EVOLUÇÃO TEMPORAL
    meses = [0, 14, 28, 42, 56, 60]
    evolucao_taranis = [total_gasto_taranis] * len(meses)
    evolucao_comum = [
        custo_comum * num_postos,
        custo_comum * 2 * num_postos,
        custo_comum * 3 * num_postos,
        custo_comum * 4 * num_postos,
        custo_comum * 5 * num_postos,
        total_gasto_comum
    ]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=meses, y=evolucao_comum, mode='lines+markers', name='Cadeira Comum (Recompra a cada 14m)', line=dict(color='#ef4444', width=3)))
    fig.add_trace(go.Scatter(x=meses, y=evolucao_taranis, mode='lines', name='Taranis ErgoPro (Investimento Único 5 Anos)', line=dict(color='#10b981', width=3, dash='dash')))
    
    fig.update_layout(
        title="Curva Cumulativa de Custo ao Longo de 60 Meses (TCO)",
        xaxis_title="Meses de Uso Corporativo",
        yaxis_title="Investimento Acumulado (R$)",
        hovermode="x unified",
        template="plotly_white",
        height=380
    )
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# ABA 4: TREINADOR ROLEPLAY
# =========================================================
with tab_roleplay:
    st.subheader("🤖 Simulador de Treinamento e Capacitação (Roleplay)")
    st.write("Pratique a argumentação de vendas contra nosso Comprador Corporativo Simulado:")
    
    col_sim1, col_sim2 = st.columns([1, 2])
    with col_sim1:
        persona_sim = st.selectbox("Escolha seu Interlocutor:", [
            "Roberto Neves (Diretor de Compras — Foco em Preço e TCO)",
            "Patrícia Lima (Diretora de RH — Foco em Bem-Estar e NR-17)",
            "Carlos Eduardo (Gestor de Facilities — Foco em Prazos e Layout)"
        ])
        if st.button("Iniciar Novo Diálogo de Treino"):
            st.session_state["historico_roleplay"] = [
                {"autor": "bot", "texto": f"Olá. Sou {persona_sim}. Recebi sua proposta para as cadeiras ErgoPro, mas sinceramente achei o preço muito salgado. Nosso fornecedor habitual cobra quase 35% a menos no mesmo lote. Por que eu deveria pagar essa diferença?"}
            ]
            
    with col_sim2:
        if "historico_roleplay" not in st.session_state:
            st.session_state["historico_roleplay"] = [
                {"autor": "bot", "texto": "Olá. Sou Roberto Neves, Diretor de Procurement. Recebi sua proposta comercial da Taranis Black, mas o preço por cadeira está 30% acima dos nossos fornecedores homologados. Por que eu deveria aprovar esse investimento?"}
            ]
            
        for msg in st.session_state["historico_roleplay"]:
            if msg["autor"] == "bot":
                st.chat_message("assistant").write(msg["texto"])
            else:
                st.chat_message("user").write(msg["texto"])
                
        resposta_usuario = st.chat_input("Digite sua resposta consultiva para o comprador...")
        if resposta_usuario:
            st.session_state["historico_roleplay"].append({"autor": "user", "texto": resposta_usuario})
            
            # Avaliação inteligente das palavras-chave
            resp_lower = resposta_usuario.lower()
            mencionou_tco = "tco" in resp_lower or "dia" in resp_lower or "diário" in resp_lower or "1,9" in resp_lower or "custo total" in resp_lower
            mencionou_garantia = "5 anos" in resp_lower or "garantia" in resp_lower or "durabilidade" in resp_lower
            mencionou_laudo = "laudo" in resp_lower or "nr-17" in resp_lower or "abergo" in resp_lower or "pgr" in resp_lower
            mencionou_piloto = "piloto" in resp_lower or "teste" in resp_lower or "demonstração" in resp_lower or "15 dias" in resp_lower
            
            if mencionou_tco and mencionou_garantia and (mencionou_laudo or mencionou_piloto):
                feedback = "Entendi o seu ponto. Esse cálculo do custo diluído ao longo dos 5 anos e o laudo NR-17 realmente fazem sentido para a diretoria não ter dor de cabeça com reposição rápida. Se você me formalizar essa proposta com o faturamento em 30/60/90 e o piloto de 15 dias sem compromisso, eu levo para a reunião da diretoria amanhã!"
                nota = "🏆 **Avaliação do Copiloto:** Nota 10/10! Argumentação perfeita com TCO, garantia de 5 anos e mitigação de risco."
            else:
                feedback = "Entendo que a qualidade seja boa, mas ainda acho o investimento elevado para o nosso orçamento atual. Você tem alguma condição de parcelamento ou demonstração prática para justificar essa diferença antes de eu bater o martelo?"
                nota = "💡 **Dica do Treinador:** Lembre-se de citar o TCO diário (< R$ 1,91/dia), a garantia de 5 anos de fábrica e o Laudo NR-17 gratuito!"
                
            st.session_state["historico_roleplay"].append({"autor": "bot", "texto": feedback})
            st.rerun()

# =========================================================
# ABA 5: GOVERNANÇA & AI CANVAS
# =========================================================
with tab_governanca:
    st.subheader("🏛️ AI Canvas, Matriz de Decisão e Governança Ética (LGPD)")
    
    st.markdown("### 📋 Política de IA Responsável: Matriz Pode vs. Não Pode")
    df_gov = pd.DataFrame({
        "Operação": [
            "Mineração de dados públicos e LinkedIn para personalização B2B",
            "Treinamento de modelos com dados confidenciais ou laudos de clientes",
            "Disparo 100% autônomo de e-mails em massa sem revisão",
            "Envio de e-mails consultivos B2B com opt-out LGPD claro",
            "Copiloto de sugestão de argumentos com Human-in-the-Loop",
            "Armazenamento de dados biomédicos ou fotos de colaboradores"
        ],
        "Classificação": ["✅ PODE", "🚫 NÃO PODE", "🚫 NÃO PODE", "✅ PODE", "✅ PODE", "🚫 NÃO PODE"],
        "Justificativa e Diretriz": [
            "Permitido para qualificação legítima de leads corporativos B2B.",
            "Vedado para proteção de segredo industrial e privacidade dos parceiros.",
            "Obrigatória a revisão humana em 100% das comunicações disparadas.",
            "Conforme Artigo 7º e 9º da LGPD com link imediato de descadastramento.",
            "O vendedor detém a decisão final da estratégia e do tom comercial.",
            "Violação grave do Art. 11 da LGPD (Dados Pessoais Sensíveis de Saúde)."
        ]
    })
    st.dataframe(df_gov, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 🏢 Arquitetura do AI Canvas (3 Oportunidades Priorizadas)")
    c_can1, c_can2, c_can3 = st.columns(3)
    with c_can1:
        st.markdown("""
        **1. E-mails Consultivos & Leads**
        - *Tipo:* IA Generativa + Heurística
        - *Classificação:* Quick Win (Prioridade 1)
        - *Impacto:* Libera 6h/semana por vendedor
        - *Governança:* Human-in-the-Loop 100%
        """)
    with c_can2:
        st.markdown("""
        **2. Copiloto de Objeções (TCO)**
        - *Tipo:* IA Generativa + RAG
        - *Classificação:* Estratégico (Prioridade 2)
        - *Impacto:* Recupera R$ 1,17M a R$ 1,64M
        - *Grounding:* Catálogo oficial e NR-17
        """)
    with c_can3:
        st.markdown("""
        **3. Automação de CRM**
        - *Tipo:* IA Tradicional + LLM Parser
        - *Classificação:* Estratégico (Prioridade 3)
        - *Impacto:* Reduz 87,5% da digitação
        - *Integração:* Validação de schema JSON
        """)

st.markdown("---")
st.caption("Desenvolvido por Mauricio Ribeiro de Souza Junior | Programa Oracle Next Education (ONE G11) & Alura")
