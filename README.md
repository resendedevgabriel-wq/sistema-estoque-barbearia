# 💈 Sistema de Alerta e Previsão de Estoque - Barbearia

Automação em Python desenvolvida para análise de estoque crítico e cálculo preditivo do custo de reposição mínima para estabelecimentos comerciais.

---

## 📌 Funcionalidades

* **Varredura Automática:** Analisa a quantidade disponível de cada produto cadastrado.
* **Alertas de Nível Crítico:** Identifica itens que estão abaixo do limite seguro de estoque (menos de 5 unidades).
* **Cálculo de Reposição Inteligente:** Estima o custo exato necessário para repor apenas as unidades faltantes até atingir o nível de segurança.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Estruturas de Dados:** Listas e Dicionários
* **Controle de Fluxo:** Laços de repetição (`for`) e Estruturas condicionais (`if`)

---

## 💻 Exemplo de Saída no Terminal

ALERTA: Pomada precisa de +3 un. para atingir o minimo seguro! Atualmente (2 un.)
ALERTA: Oleo para Penteado precisa de +1 un. para atingir o minimo seguro! Atualmente (4 un.)
Custo total estimado para reposiçao minima!: R$ 110.0
