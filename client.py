import argparse
import time
import google.auth.crypt
import google.auth.jwt
import requests

def generate_jwt(sa_keyfile,
                 sa_email,
                 audience,
                 expiry_length=3600):

    """Generates a signed JSON Web Token using a Google API Service Account."""

    now = int(time.time())

    # build payload
    payload = {
        'iat': now,
        # expires after 'expiry_length' seconds.
        "exp": now + expiry_length,
        # iss must match 'issuer' in the security configuration in your
        # swagger spec (e.g. service account email). It can be any string.
        'iss': sa_email,
        # aud must be either your Endpoints service name, or match the value
        # specified as the 'x-google-audience' in the OpenAPI document. Campo host del OPEN API (PRIVADO) Nombre publico en el apigateway
        'aud':  audience,
        # sub and email should match the service account's email address
        'sub': sa_email,
        'email': sa_email
    }

    # sign with keyfile
    signer = google.auth.crypt.RSASigner.from_service_account_file(sa_keyfile)
    signed_jwt = google.auth.jwt.encode(signer, payload)

    return signed_jwt



def make_jwt_request(signed_jwt, url):
    """Makes an authorized request to the endpoint"""
    headers = {
        'Authorization': 'Bearer {}'.format(signed_jwt.decode('utf-8')),
        'content-type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    print(response.status_code, response.content)
    response.raise_for_status()

if __name__ == '__main__':

    expiry_length = 3600
    keyfile_jwt = generate_jwt('softlution-1342-7abd00605574.json',
                               'jwt-api-v1@softlution-1342.iam.gserviceaccount.com',
                               'gateway-softlution-v1-275qnmqmijsqk.apigateway.softlution-1342.cloud.goog',
                               expiry_length)

   # print(keyfile_jwt)                           
    make_jwt_request(keyfile_jwt, 'https://api-softlution-v1-eq52hn0.uc.gateway.dev/lista')