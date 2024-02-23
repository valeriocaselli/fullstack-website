from itsdangerous import URLSafeTimedSerializer

def generation_confirmation_token(email):
    # Function to generate a different token for each email
    serializer = URLSafeTimedSerializer('supersafekey')
    return serializer.dumps(email, salt='49500638755478474074859624111180149435')

def confirm_token(token, expiration=3600):
    # 3600 = available time to confirm token (3600s is an hour)
    serializer = URLSafeTimedSerializer('supersafekey')
    try:
        email = serializer.loads(
            token,
            salt='49500638755478474074859624111180149435',
            max_age=expiration
        )
    except:
        return False
    return email

