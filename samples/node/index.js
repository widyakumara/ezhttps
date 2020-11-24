const http = require('http');

const HOST = '127.0.0.1';
const PORT = 8888;

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end(`Hello world, from NodeJS ${process.version}`);
}

const server = http.createServer(requestListener);
server.listen(PORT, HOST);

console.log(`Server running on http://${HOST}:${PORT}`);
