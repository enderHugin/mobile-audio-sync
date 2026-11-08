// Endpoint de tiempo: devuelve la hora del servidor en ms epoch.
// El reloj del servidor debe estar sincronizado con NTS/NTP (chrony) en producción.
import { createServer } from "node:http";
import { pathToFileURL } from "node:url";

export function createTimeServer() {
  return createServer((req, res) => {
    if (req.method === "GET" && req.url === "/time") {
      res.writeHead(200, {
        "Content-Type": "application/json",
        "Cache-Control": "no-store",
        "Access-Control-Allow-Origin": "*",
      });
      res.end(JSON.stringify({ serverTime: Date.now() }));
      return;
    }
    res.writeHead(404).end();
  });
}

// Arranque directo: node server/time-server.js
if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const port = Number(process.env.PORT ?? 8787);
  createTimeServer().listen(port, () => {
    console.log(`time-server escuchando en :${port}`);
  });
}
