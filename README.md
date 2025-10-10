# 🧠 APRENDIZADOS DE PROGRAMAÇÃO

> **Repositório pessoal de conhecimento.**  
> Aqui registro tudo que aprendo ao longo dos anos sobre programação — desde lógicas simples até boas práticas e soluções complexas.  
> Este documento funciona como um **cérebro técnico**, um guia vivo que evolui junto com meu aprendizado.

---

## 📘 SOBRE O REPOSITÓRIO

Este projeto serve como um **banco de lógica e referência rápida**.  
Sempre que encontro um problema:

1. Verifico se já documentei algo semelhante.  
2. Se encontrar, aplico e melhoro a solução.  
3. Se não encontrar, estudo, resolvo e documento aqui.

> O objetivo é usar tanto esta documentação que as soluções se tornem automáticas, decoradas e entendidas profundamente.

---

## 📂 CONTEÚDO

### 🔧 Fundamentos
- Boas práticas de programação  
- Estruturas lógicas e condicionais  
- Código limpo (Clean Code)  
- Otimização e legibilidade  

### 🧰 Tratativas
- Tratativas de erros  
- Tratativas de exceções  
- Soluções para problemas recorrentes  
- Estratégias de debug e logs  

### 🧩 Padrões e Arquitetura
- Padrões de projeto (Design Patterns)  
- Estrutura de projetos Django / DRF  
- Boas práticas de API REST  
- Padrões de versionamento e documentação  

### 🐍 Linguagens e Tecnologias
- **Python:** boas práticas, funções úteis, snippets e estruturas  
- **Django:** models, views, serializers, signals, middlewares  
- **Django REST Framework:** endpoints, autenticação, permissões e testes  
- **Banco de Dados:** modelagem, queries otimizadas, relacionamentos e migrações  

---

## 🧱 COMO USAR ESTA DOCUMENTAÇÃO

1. **Preciso resolver um problema:**  
   Consulto o repositório e procuro se já existe algo documentado.

2. **Não encontrei solução:**  
   Estudo o problema, entendo o conceito e desenvolvo uma solução.

3. **Entendi e otimizei:**  
   Documento aqui com explicação e exemplo funcional.

4. **Revisito com frequência:**  
   As soluções mais usadas acabam ficando decoradas e compreendidas de forma natural.

---

## 🏷️ PADRÃO DE TÓPICOS (.MD)

Cada aprendizado deve seguir este modelo:

```markdown
# [TÍTULO DO CONTEÚDO]
> Breve descrição do que o tópico resolve ou ensina.

## 🧩 Contexto
Explique o problema ou situação onde essa lógica é útil.

## 💡 Solução
Descreva a lógica de forma simples e objetiva.

```python
# Exemplo de código funcional
def exemplo():
    print("Olá, mundo!")
```

## 🧠 Entendimento
Explique o porquê da lógica funcionar e quando aplicá-la.

## ⚙️ Boas práticas
- [ ] Use exemplos simples e comentados  
- [ ] Evite duplicar soluções  
- [ ] Mantenha nomes claros e padronizados  
- [ ] Documente melhorias quando otimizar o código
```

---

## 🧭 EXEMPLO REAL

```markdown
# CONDICIONAIS ANINHADAS EM PYTHON (DRF)
> Exemplo simples de uso de condicionais aninhadas para validações em uma view.

## 🧩 Contexto
Usadas quando há verificações que dependem de outras, como permissões ou autenticações.

## 💡 Solução
```python
if user.is_authenticated:
    if user.is_superuser:
        return Response("Acesso total")
    else:
        return Response("Acesso restrito")
else:
    return Response("Usuário não autenticado")
```

## 🧠 Entendimento
Condicionais aninhadas são úteis para validações hierárquicas.  
Mas quando há muitos níveis, o ideal é extrair a lógica para funções auxiliares.

## ⚙️ Boas práticas
- Evite blocos aninhados profundos.  
- Prefira retornos antecipados (`return`) para simplificar a leitura.  
- Separe as regras em funções pequenas e reutilizáveis.
```

---

## 🧩 LICENÇA

Este repositório é de uso **pessoal e educativo**.  
Você pode se inspirar e adaptar o conteúdo, mas sempre valorize o aprendizado contínuo e a prática diária.

---

## 💬 NOTA FINAL

> Este repositório não é apenas uma coleção de códigos,  
> é um **registro do meu crescimento como desenvolvedor**.  
> Cada linha aqui representa um erro resolvido, um conceito entendido e uma evolução prática no caminho da programação.
