# 🐍 Python: Jogos e Lógica

Mini jogos de terminal em Python que desenvolvi durante um **curso em vídeo** para praticar lógica de programação. Alguns jogos têm duas versões (a segunda é indicada por `2.0` no nome do arquivo), para mostrar como o código evoluiu de uma versão simples para uma mais completa.

## 🎮 Jogos

### 1. Adivinhe o número
O computador "pensa" em um número e o jogador tenta adivinhar.

| Arquivo | Descrição |
|---|---|
| `Adivinhe_Numero.py` | Versão inicial: uma única tentativa, número de 0 a 5, com suspense usando `sleep` |
| `Adivinhe_Numero2.0.py` | Versão com laço `while`: o jogador tenta até acertar e o jogo conta os palpites |

### 2. Par ou Ímpar
| Arquivo | Descrição |
|---|---|
| `Par_ou_Impar.py` | Informa se um número digitado é par ou ímpar (operador `%`) |
| `Par_ou_Impar2.0.py` | Jogo completo contra o computador, com contador de vitórias. Continua até o jogador perder |

### 3. Jokenpo (Pedra, Papel e Tesoura)
| Arquivo | Descrição |
|---|---|
| `Pedra_Papel_Tesoura.py` | Jogo de pedra, papel e tesoura contra o computador, com `if/elif` para definir o vencedor |

## 📚 Conceitos praticados

- Estruturas de decisão: `if`, `elif`, `else`
- Laços de repetição: `while` e `while True` com `break`
- Entrada de dados com `input()` e conversão com `int()`
- Números aleatórios com `random.randint()`
- Operador de resto da divisão (`%`)
- Formatação de texto com f-strings
- Pausas no programa com `time.sleep()`
- Operadores lógicos (`and`, `or`)

## 🔧 Correções

- **Jokenpo**: corrigi a mensagem de resultado quando o jogador escolhe Pedra e o computador escolhe Papel (o papel cobre a pedra, então quem vence é o computador).

## ▶️ Como rodar

1. Instale o [Python 3](https://www.python.org/downloads/)
2. Clone ou baixe este repositório
3. No terminal, execute o arquivo do jogo que quiser:

```bash
python Adivinhe_Numero2.0.py
```

## 🚀 Próximos passos

- [ ] Tratar entradas inválidas (letras no lugar de números) com `try/except`
- [ ] Mostrar o nome das jogadas no Jokenpo (em vez de só o número)
- [ ] Adicionar placar e várias rodadas no Jokenpo
- [ ] Organizar os jogos em pastas
- [ ] Criar novos jogos

---
Feito por [@gabibarriquello](https://github.com/gabibarriquello)
