'''
#  What is JWT and Why used in APIs:

- JWT (JSON Web Token):

- A JWT is a compact, digitally signed token that securely transmits user information (like user ID) 
  between the server and client, usually for authentication

- Structure: Consists of three parts—Header (algorithm + type), Payload (user claims), Signature (security key).


# Why use JWT: 

    - Stateless: No need to store user session on the server, making it scalable.

    - Secure: Client includes JWT in every request; server can instantly verify without extra lookups.

    - API Standard: Used in modern APIs for login, session management, and authorization.
'''
# Example JWT(Shortened):

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...     #type: ignore

# Sent via HTTP header: Authorization: Bearer <JWT-TOKEN>