import requests


def requests_get(protocal, host, port, url, headers={}, params={}):
    reqeusts_result = {}
    if port:
        requests_url = '{0}://{1}:{2}{3}'.format(protocal, host, port, url)
    else:
        requests_url = '{0}://{1}{2}'.format(protocal, host, url)

    try:
        r = requests.get(requests_url, headers=headers, params=params)
        r.raise_for_status()
        json_result = r.json()
        reqeusts_result['data'] = json_result
        reqeusts_result['errors'] = ''
    except requests.exceptions.RequestException as e:
        json_result = r.json()
        if json_result['errors']:
            reqeusts_result['errors'] = json_result['errors']
        else:
            reqeusts_result['errors'] = e

    return reqeusts_result


def requests_post(protocal, host, port, url, headers={}, json={}):
    reqeusts_result = {}
    if port:
        requests_url = '{0}://{1}:{2}{3}'.format(protocal, host, port, url)
    else:
        requests_url = '{0}://{1}{2}'.format(protocal, host, url)

    try:
        r = requests.post(requests_url, headers=headers, json=json)
        r.raise_for_status()
        json_result = r.json()
        reqeusts_result['data'] = json_result
        reqeusts_result['errors'] = ''
    except requests.exceptions.RequestException as e:
        json_result = r.json()
        if json_result['errors']:
            reqeusts_result['errors'] = json_result['errors']
        else:
            reqeusts_result['errors'] = e

    return reqeusts_result
