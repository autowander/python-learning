def application(environ, start_response):
	start_response('200 OK', [('Connect-Type', 'text/html')])
	return [b'<h1>Hello World!<h1>']