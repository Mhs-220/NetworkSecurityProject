import flask

def set_response_headers(response):
    _set_feature_headers(response.headers)
    _set_frame_options_headers(response.headers)
    _set_content_security_policy_headers(response.headers)
    # _set_hsts_headers(response.headers)
    _set_referrer_policy_headers(response.headers)
    return response

def _set_feature_headers(headers):
    headers['Feature-Policy'] = {}

def _set_frame_options_headers(headers):
    headers['X-Frame-Options'] = 'SAMEORIGIN'

def _set_content_security_policy_headers(headers):
    headers['X-XSS-Protection'] = '1; mode=block'
    headers['X-Content-Type-Options'] = 'nosniff'
    headers['X-Download-Options'] = 'noopen'

def _set_hsts_headers(headers):
    value = 'max-age={}'.format(31556926) \
            + '; includeSubDomains' \
            + '; preload'

    headers['Strict-Transport-Security'] = value

def _set_referrer_policy_headers(headers):
    headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
