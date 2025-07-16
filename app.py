from flask import Flask, request

app = Flask(__name__)

@app.route('/eventsub', methods=['POST'])
def eventsub():
    data = request.json

    # Responder al challenge de verificación webhook
    if 'challenge' in data:
        return data['challenge'], 200

    event_type = data.get('subscription', {}).get('type')
    event = data.get('event', {})

    if event_type == 'channel.cheer':
        user = event.get('user_name')
        bits = event.get('bits')
        print(f"Bits donados por {user}: {bits}")

    elif event_type == 'channel.subscribe':
        user = event.get('user_name')
        tier = event.get('tier')
        print(f"{user} se suscribió en tier {tier}")

    elif event_type == 'channel.subscription.gift':
        gifter = event.get('user_name')
        recipient = event.get('recipient_user_name')
        print(f"{gifter} regaló una suscripción a {recipient}")

    elif event_type == 'channel.subscription.message':
        user = event.get('user_name')
        message = event.get('message', {}).get('text')
        print(f"Mensaje de suscripción de {user}: {message}")

    elif event_type == 'channel.raid':
        raider = event.get('from_broadcaster_user_name')
        viewers = event.get('viewers')
        print(f"Raid recibido de {raider} con {viewers} viewers")

    else:
        print(f"Evento no manejado: {event_type}")

    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Usa PORT si está, si no 8080 local
    app.run(host='0.0.0.0', port=port)
