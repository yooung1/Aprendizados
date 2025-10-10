# ⚙️ CONDICIONAIS

> Uma **condicional** é uma forma de criar condições de "estado".  
> Por exemplo: *se usuário tiver mais do que 18 anos → executar determinada ação.*  
> Em outras palavras, criamos condições para alterar o comportamento do código conforme o contexto.

---

## 🧭 O QUE DEVE SER FEITO

A abordagem ideal é a seguinte:

1. **Verificar as condições de falha logo no início:**  
   - verificar se o objeto é inválido;  
   - verificar se está faltando algum dado;  
   - verificar se o usuário tem permissão.  

   Se alguma dessas condições falhar, deve-se interromper a execução imediatamente.

2. **Executar a lógica principal apenas após todas as validações:**  
   Isso garante que todas as pré-condições foram satisfeitas, permitindo executar a lógica principal da função em um único nível de indentação.

---

## 🧩 FONTES

- 🔗 **Fonte principal:**  
  [Refactoring Guru — Replace Nested Conditional with Guard Clauses](https://refactoring.guru/pt-br/replace-nested-conditional-with-guard-clauses)

- 🔗 **Fonte 1:**  
  [Reddit — Best Practices for Nested Conditionals](https://www.reddit.com/r/learnprogramming/comments/a6hpcb/whats_the_best_practices_way_to_write_a_stupidly)

- 🔗 **Fonte 1.1:**  
  [Comentário 1 no Reddit](https://www.reddit.com/r/learnprogramming/comments/a6hpcb/comment/ebx54vj/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

- 🔗 **Fonte 1.2:**  
  [Comentário 2 no Reddit](https://www.reddit.com/r/learnprogramming/comments/a6hpcb/comment/ebuwubd/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

---

## 🚫 NÃO USE CONDICIONAIS ANINHADAS

Condicionais aninhadas tornam o código confuso e difícil de ler, pois exigem que você **mantenha em mente as condições anteriores** enquanto interpreta as seguintes.

### Exemplo ruim — condicional aninhada:

```python
# Exemplo de condicional aninhada
def getPayAmount(self):
    if self.isDead:
        result = deadAmount()
    else:
        if self.isSeparated:
            result = separatedAmount()
        else:
            if self.isRetired:
                result = retiredAmount()
            else:
                result = normalPayAmount()
    return result
```

Na forma acima, o código se torna difícil de ler e entender.  
Enquanto você o analisa, precisa manter várias condições em mente, o que **complica o raciocínio** e prejudica a manutenção.  
A seguir, veremos uma forma **mais clara, otimizada e performática** de estruturar essas condições.

---

## 🧩 CONTEXTO

Condicionais aninhadas criam um código “sujo”, de difícil leitura — tanto para outros desenvolvedores quanto para o “você do futuro”.  
Separar as condições em blocos independentes melhora a **clareza e previsibilidade do fluxo lógico**.

---

## 💡 SOLUÇÃO — CONDICIONAIS OTIMIZADAS

A ideia é **barrar cedo** as condições de erro (falhas) e executar a lógica principal somente se todas forem satisfeitas.

```python
def getPayAmount(self):
    if self.isDead:
        return deadAmount()
    if self.isSeparated:
        return separatedAmount()
    if self.isRetired:
        return retiredAmount()
    return normalPayAmount()
```

Neste formato, fica claro que:
- Cada condição de erro encerra a função imediatamente;  
- O código principal permanece limpo e direto;  
- A leitura é mais simples e a manutenção mais fácil.

---

## 🔧 OUTRAS SOLUÇÕES

Quando a condicional for muito extensa, é possível criar **funções específicas** para tratá-la.  
Isso melhora a organização e a reutilização do código.

```python
def is_valid_user(user):
    return (
        user.age >= 18 and 
        user.has_driving_license and 
        user.type != "banned"
    )

if not is_valid_user(user):
    return "REJECTED"

# Fluxo principal
return "ACCEPTED -- EXECUTE PROCESS"
```

Essa abordagem deixa o código mais **modular**, **legível** e **testável**.

---

## ✅ RESUMO

- Evite condicionais aninhadas.  
- Use **guard clauses** (cláusulas de proteção) para validar e sair cedo.  
- Mantenha a lógica principal em **um único nível de indentação**.  
- Extraia funções específicas quando a condição for complexa.  
- Escreva sempre pensando no “você do futuro”.

---
