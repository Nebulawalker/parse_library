import requests


def check_for_redirect(response):
    if response.history:
        raise requests.exceptions.HTTPError(
            f'Request redirected, skip {response.history[0].url}\n'
        )
