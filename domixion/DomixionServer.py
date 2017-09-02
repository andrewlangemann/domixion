import BaseHTTPServer
import os
import SocketServer
import traceback


class DomixionRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Request handler that returns HTML with randomized Dominion cards"""

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        try:
            if self.path == '/cards':
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()

                # TODO: Get randomized cards.
                cards = [
                    'adventures/coinoftherealm.jpg',
                    'prosperity/traderoute.jpg',
                    'guilds/masterpiece.jpg',
                    'adventures/magpie.jpg',
                ]

                cardListItems = []
                for card in cards:
                    cardListItems.append(
                        '<div class="card"><img src="http://dominion.diehrstraits.com/scans/%s"/></div>' % card)

                self.wfile.write(
                    """
                        <html>
                            <head>
                                <title>Domixion Cards</title>
                                <link href="resources/style.css" rel="stylesheet">
                            </head>
                            <body>
                                <div class="cardContainer">
                                    {cards}
                                </div>
                            </body>
                        </html>
                        """.format(cards=''.join(cardListItems)))
                self.wfile.close()

            elif self.path.startswith('/resources'):
                # Get the resource out of the Resources directory and write its contents to the response.
                scriptDir = os.path.dirname(os.path.realpath(__file__))
                resourceFileName = scriptDir + self.path.replace('/', '\\')
                with open(resourceFileName, 'r') as resourceFile:
                    contents = resourceFile.read()
                    if self.path.endswith('.css'):
                        self.send_response(200)
                        self.send_header('Content-Type', 'text/css')
                        self.end_headers()

                        self.wfile.write(contents)
                        self.wfile.close()

        except:
            self.send_response(500)
            self.send_header('Content-Type', 'text/html')
            self.wfile.write(
                """
                    <html>
                        <head>
                            <title>Domixion Cards - Error</title>
                        </head>
                        <body>
                            <h2>Exception!</h2>
                            <body>{exceptionText}</body>
                        </body>
                    </html>
                """.format(exceptionText=traceback.format_exc().replace('\n', '<br/>')))
            self.end_headers()


def RunServer():
    port = 8000
    httpd = SocketServer.TCPServer(("", port), DomixionRequestHandler)

    print("serving at port", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        httpd.socket.close()
