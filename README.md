# CK0048 - Métodos Numéricos II 🧮

Este repositório reúne o ecossistema de algoritmos e modelagens computacionais desenvolvidos para a disciplina de **Métodos Numéricos II (Cálculo Numérico Avançado)** do Departamento de Computação da Universidade Federal do Ceará (UFC). O foco principal do projeto é a implementação e análise de métodos numéricos para problemas de Álgebra Linear Numérica (Cálculo de Autovalores/Autovetores), Quadratura Gaussiana Avançada, Diferenciação Numérica e Solução de Equações Diferenciais Ordinárias (PVI e PVC).

---

## 🚀 Domínios Matemáticos & Algoritmos Implementados

O repositório está subdividido em módulos que cobrem as ferramentas mais robustas da computação científica:

### 1. Cálculo de Autovalores e Autovetores (Análise Matricial)
* **Método das Potências:** Implementações para isolar componentes espectrais específicos de matrizes lineares:
  * `Potencia Regular`: Localização do autovalor dominante.
  * `Potencia Inversa`: Localização do menor autovalor em magnitude.
  * `Potencia Deslocamento`: Abordagem com *shifts* para acelerar a convergência para autovalores específicos.
* **Método de Jacobi (`Jacobi/`):** Algoritmo iterativo para diagonalização de matrizes simétricas através de rotações ortogonais sucessivas, determinando o espectro completo de autovalores e autovetores.
* **Transformações de Householder (`Householder/`):** Algoritmos de reflexão ortogonal utilizados para tridiagonalizar matrizes estáveis, servindo como etapa de pré-condicionamento.
* **Algoritmo QR (`QR/`):** Decomposição iterativa estável baseada em matrizes de Householder para extração simultânea de todos os autovalores de uma matriz.

### 2. Integração e Diferenciação Numérica Avançada
* **Diferenças Finitas (`Derivada/`):** Implementação de operadores de aproximação de derivadas por três frentes de aproximação:
  * Diferença Progressiva (`forward.py`)
  * Diferença Regressiva (`backward.py`)
  * Diferença Central (`central.py`)
* **Fórmulas de Newton-Cotes (`Newton Codes/`):** Integração numérica baseada em polinômios interpoladores de graus variados.
* **Quadratura Gaussiana (`Quadratura/`):** Integração de alta performance utilizando polinômios ortogonais adaptados para diferentes intervalos e funções peso:
  * Gauss-Legendre (`legendre.py`)
  * Gauss-Chebyshev (`chebyshev.py`)
  * Gauss-Laguerre (`laguerre.py`)
  * Gauss-Hermite (`hermite.py`)
* **Tratamento de Singularidades (`Singularidade/`):** Técnicas adaptativas para contornar descontinuidades e singularidades assintóticas em integrais definidas.

### 3. Solução de Equações Diferenciais Ordinárias (EDOs)
* **Problemas de Valor Inicial (`PVI/`):** Métodos de passo único e passo múltiplo para a evolução temporal de sistemas dinâmicos:
  * `Euler_Explicito.py` e `Euler_Implicito.py`: Abordagens clássicas de primeira ordem estável e instável.
  * `Runge_Kutta.py`: Implementação do método RK4 clássico de quarta ordem de alta precisão.
  * `Preditor_Corretor.py`: Esquema iterativo de passo múltiplo para refinar aproximações locais.
* **Problemas de Valor de Contorno (`PVC/`):** Resolução de equações diferenciais com restrições de fronteira espacial via Método das Diferenças Finitas (MDF), transformando a EDO em um sistema linear esparsamente acoplado.

### 4. Aplicações Práticas e Erros
* **`#Filtros de Imagem/`:** Aplicação prática de transformações matriciais e convoluções numéricas discretas para manipulação e filtragem de imagens digitais.
* **`Area Superficie - Error/`:** Algoritmos para aproximação de áreas geométricas complexas com análise e propagação de erros de truncamento computacional.

---

## 📂 Arquitetura do Repositório

```text
├── #Filtros de Imagem/          # Processamento de imagem via transformações matriciais
├── Area Superficie - Error/     # Cálculo de áreas superficiais e análise de erro
├── Derivada/                    # Diferenças finitas (Forward, Backward, Central)
├── Householder/                 # Tridiagonalização e reflexões de Householder
├── Jacobi/                      # Método de rotação de Jacobi para autovalores
├── Newton Codes/                # Integração por fórmulas de Newton-Cotes
├── Potencia Deslocamento/       # Método das potências modificado com shift
├── Potencia Inversa/            # Método das potências inversas para menor autovalor
├── Potencia Regular/            # Método das potências para autovalor dominante
├── PVC/                         # Problemas de Valor de Contorno (MDF)
├── PVI/                         # Problemas de Valor Inicial (Euler, RK4, Preditor-Corretor)
├── QR/                          # Algoritmo QR para decomposição espectral
├── Quadratura/                  # Quadratura Gaussiana (Legendre, Chebyshev, Laguerre, Hermite)
└── Singularidade/               # Integração numérica de funções singulares
```

## 🛠️ Tecnologias Utilizadas
* Linguagem Principal: Python 3.x
* Bibliotecas Científicas: Numpy (manipulação de matrizes e vetores) e Matplotlib (geração de gráficos de convergência, curvas de erro e saída dos filtros de imagem).

## 🔧 Como Executar os Scripts
### Pré-requisitos
Certifique-se de possuir as bibliotecas matemáticas básicas instaladas em seu ambiente Python:
```bash
pip install numpy matplotlib openpyxl Pillow
```

### Executando uma rotina
Para rodar qualquer família de métodos, basta navegar até o diretório correspondente e executar o script de orquestração (main.py ou correspondente):

```bash
# Exemplo: Executar os testes de Problemas de Valor Inicial (PVI)
cd PVI
python main1.py
```
