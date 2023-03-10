from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os


def _load_credential_from_file(filepath):
    real_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(real_path, 'rb') as f:
        return f.read()

SERVER_CERTIFICATE = _load_credential_from_file('/root/.smartEyes/grpc/cert.crt')
SERVER_CERTIFICATE_KEY = _load_credential_from_file('/root/.smartEyes/grpc/key.key')
