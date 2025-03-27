import tpm2_pytss

with tpm2_pytss.ESAPI() as esapi:
    sealed_data = esapi.seal(
        parent_auth=None,
        sensitive_data=private_key,
        auth_policy=None
    )
