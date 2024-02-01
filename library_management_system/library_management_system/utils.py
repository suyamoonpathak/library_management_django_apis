"""
utils.py

This module contains a utility function for customizing the response payload of the JWT authentication.

jwt_response_payload_handler:
    - Function to customize the response payload when a user authenticates and receives a JWT token.
    - Parameters:
        - token (str): JWT token generated for the user.
        - user (User): The authenticated user.
        - request (HttpRequest): The incoming HTTP request.
    - Returns:
        - dict: Customized response payload containing the token, username, and user ID.

Usage:
    - Integrate this function into your Django project's settings to customize the JWT response payload.
    - Typically used with the 'JWT_RESPONSE_PAYLOAD_HANDLER' setting in Django settings.

Author: Suyamoon Pathak
Date: 01-02-2024
"""

def jwt_response_payload_handler(token, user=None, request=None):
    """
    Customize the response payload for JWT authentication.
    """
    return {
        'token': token,
        'user': str(user),
        'user_id': user.id
    }
