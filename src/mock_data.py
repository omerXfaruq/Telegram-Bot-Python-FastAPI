from .validations import MessageBodyModel, ReplyMessage

mock_reply_message = ReplyMessage(**{
    "date": 1441645000,
    "chat": {
        "last_name": "Reply Lastname",
        "type": "private",
        "id": 1111112,
        "first_name": "Reply Firstname",
        "username": "Testusername"
    },
    "message_id": 1334,
    "text": "Original"
})

mock_incoming_message = MessageBodyModel(**{
    'update_id': 642790864,
    'message': {
        'message_id': 94,
        'from': {'id': 8611263057, 'is_bot': False, 'first_name': 'user', 'username': 'username', 'language_code': 'en'},
        'chat': {'id': 8611263057, 'first_name': 'user', 'username': 'username', 'type': 'private'},
        'date': 1632414430, 'text': '.'
    }
}
                                         )
