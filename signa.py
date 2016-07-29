'''
php server:

 $hmac_sha1_str = base64_encode(hash_hmac("sha1", $string_to_sign, $secret_access_key));
 $signature = urlencode($hmac_sha1_str);



'''
# python client

import urllib,base64,hmac,hashlib
secret_access_key='tNEA6EfI3aqd2Ko'
string_to_sign='aaa'


signature = urllib.quote(
    base64.b64encode(
        hmac.new(secret_access_key, string_to_sign, digestmod=hashlib.sha1)
        .hexdigest()
    ))


print signature
