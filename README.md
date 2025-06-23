# 🤖 Bot Telegram: Reenvio de Vídeos Agendado

Um bot feito com Python e Telethon para reenviar vídeos de um canal do Telegram para outro, **em horários definidos por você**.

---

## ✅ O que o bot faz

- Reenvia vídeos já existentes de um canal para outro
- Segue um horário pré-definido (ex: 09:00, 13:00, 18:00)
- Envia um vídeo por vez, seguindo a ordem dos IDs
- Continua do último vídeo enviado

---

## ⚙️ Requisitos

- Python 3.7 ou superior
- Conta do Telegram com acesso aos canais
- Biblioteca [Telethon](https://github.com/LonamiWebs/Telethon)
- API ID e API Hash → [Crie aqui](https://my.telegram.org)

---

## 🚀 Como usar

1. Defina no `config.py`:
   - Canal de origem
   - Canal de destino
   - ID inicial (da mensagem com o primeiro vídeo)
   - Lista de horários (formato `"HH:MM"`)

2. Execute o bot:
   ```bash
   python bot.py
