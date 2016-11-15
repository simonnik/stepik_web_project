def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text-plain')]
    body = environ['QUERY_STRING'].split('&')
    body = [i+"\r\n" for i in body]
    start_response(status, headers)
    return body