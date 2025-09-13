'''
#  Auth Flow : Register -> Login -> Profile(Protected)

1) Register: 
        - User sends name/email/password to POST /register
        - Server creates a new user and stores it in the database

2) Login: 
        - User submits credentials to POST /login
        - If valid, server returns a JWT token:
'''
from flask_jwt_extended import create_access_token
# After password Check
access_token = create_access_token(identity=user_id) # type: ignore
return jsonify(access_token= access_token)      #type:ignore

'''
        - The token is given to the frontend (stored in localStorage/cookies)

3) Profile (Protected routes):
        - User requests /profile but must send their JWT in the Authorization header.
        - Protected the route: 
'''

from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/profile')
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify(name=user.name, email=user.email)

# If token is missing or invalid, access is denied.