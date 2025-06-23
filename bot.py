from telethon import TelegramClient
import asyncio
import datetime
from config import api_id, api_hash, canal_origem, canal_destino, horarios_envio, id_inicial

client = TelegramClient("session_bot", api_id, api_hash)

# Variável global para controlar o ID da próxima mensagem a enviar
proximo_id = id_inicial

async def enviar_video():
    global proximo_id
    try:
        # Tenta buscar a mensagem pelo ID
        msg = await client.get_messages(canal_origem, ids=proximo_id)

        if msg and msg.video:
            await client.send_file(canal_destino, msg.media, caption=msg.message or "")
            print(f"[{datetime.datetime.now()}] Vídeo ID {proximo_id} enviado com sucesso.")
        else:
            print(f"[{datetime.datetime.now()}] ID {proximo_id} não contém vídeo. Pulando.")

        proximo_id += 1  # Avança para o próximo ID

    except Exception as e:
        print(f"Erro ao enviar vídeo ID {proximo_id}: {e}")
        proximo_id += 1  # Avança mesmo em erro

async def agendar_envios():
    while True:
        agora = datetime.datetime.now().strftime("%H:%M")
        if agora in horarios_envio:
            await enviar_video()
            await asyncio.sleep(60)  # espera 1 minuto para evitar múltiplos envios no mesmo horário
        await asyncio.sleep(5)  # checa a cada 5 segundos

async def main():
    await client.start()
    print("Bot iniciado. Aguardando horários programados...")
    await agendar_envios()

asyncio.run(main())
