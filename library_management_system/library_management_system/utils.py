def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': str(user),
        'user_id': user.id
    }
