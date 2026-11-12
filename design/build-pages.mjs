// Convierte las pantallas del lienzo (design/canvas/*.dc.html) en páginas web
// normales para publicarlas en GitHub Pages.
// Uso: node design/build-pages.mjs <carpeta-salida> [página-del-lienzo]
// La página del lienzo por defecto es "v2".
import { readFileSync, writeFileSync, mkdirSync, copyFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const canvasDir = join(here, 'canvas');
const out = process.argv[2] || join(here, '..', '_site');
const pageId = process.argv[3] || 'v2';

const canvas = JSON.parse(readFileSync(join(canvasDir, 'canvas.json'), 'utf8'));
const firstPage = (canvas.pages && canvas.pages[0] && canvas.pages[0].id) || null;
const boards = Object.entries(canvas.boards)
  .map(([file, b]) => ({ file, ...b }))
  .filter((b) => (b.page || firstPage) === pageId)
  .sort((a, b) => a.y - b.y || a.x - b.x);

const htmlName = (file) => file.replace(/\.dc\.html$/, '.html');
const fixLinks = (s) => s.replace(/\.dc\.html/g, '.html');
const pick = (src, re, fallback) => {
  const m = src.match(re);
  return m ? m[1] : fallback;
};
const escapeHtml = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function convert(src) {
  const title = pick(src, /<title>([\s\S]*?)<\/title>/, '');
  const lang = pick(src, /<html lang="([^"]+)"/, 'es');
  const helmet = pick(src, /<helmet>([\s\S]*?)<\/helmet>/, '');
  const body = pick(src, /<\/helmet>([\s\S]*?)<\/x-dc>/, '');
  const logic = pick(
    src,
    /<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/,
    'class Component extends DCLogic { renderVals() { return {}; } }'
  );
  return `<!doctype html>
<html lang="${lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title}</title>
${helmet.trim()}
<style>html,body{margin:0}body{display:flex;justify-content:center;background:#E9DFCC;min-height:100vh}#app{flex:none}</style>
</head>
<body>
<div id="app"></div>
<template id="tpl">${fixLinks(body)}</template>
<script src="dc-lite.js"></script>
<script>
${fixLinks(logic).trim()}
DC.mount(Component);
</script>
</body>
</html>
`;
}

mkdirSync(out, { recursive: true });
copyFileSync(join(here, 'pages', 'dc-lite.js'), join(out, 'dc-lite.js'));
writeFileSync(join(out, '.nojekyll'), '');

for (const b of boards) {
  const src = readFileSync(join(canvasDir, b.file), 'utf8');
  writeFileSync(join(out, htmlName(b.file)), convert(src));
}

// Agrupa las pantallas por filas del lienzo; cada fila toma el título más cercano por encima.
const titles = Object.values(canvas.notes || {})
  .filter((n) => n.kind === 'title1' && (n.page || firstPage) === pageId)
  .sort((a, b) => a.y - b.y);
const groups = [];
for (const b of boards) {
  let g = groups.find((x) => x.y === b.y);
  if (!g) {
    const above = titles.filter((t) => t.y < b.y).pop();
    g = { y: b.y, title: above ? above.text : '', items: [] };
    groups.push(g);
  }
  g.items.push(b);
}

const phoneScale = 0.8;
function tile(b) {
  const scale = b.w === 390 ? phoneScale : Math.min(0.6, 1000 / b.w);
  const w = Math.round(b.w * scale);
  const h = Math.round(b.h * scale);
  const name = escapeHtml(b.title || htmlName(b.file));
  const href = htmlName(b.file);
  return `<figure class="tile${b.w === 390 ? '' : ' wide'}">
<a href="${href}" class="frame" style="width:${w}px;height:${h}px" aria-label="Abrir: ${name}">
<iframe src="${href}" title="${name}" loading="lazy" tabindex="-1" style="width:${b.w}px;height:${b.h}px;transform:scale(${scale})"></iframe>
</a>
<figcaption><a href="${href}">${name}</a></figcaption>
</figure>`;
}

const start = boards.find((b) => b.file === 'Encuentros.dc.html') || boards.find((b) => b.w === 390);
const today = new Date().toLocaleDateString("es-ES", { timeZone: "Europe/Madrid", day: "numeric", month: "long", year: "numeric" });
const rosette = `<svg width="56" height="56" viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="98" fill="#2B1E16"/><g stroke="#2B1E16" stroke-width="4"><circle cx="100" cy="30" r="22" fill="#3E8A3A"/><circle cx="135" cy="39.4" r="22" fill="#E2B23C"/><circle cx="160.6" cy="65" r="22" fill="#23509E"/><circle cx="170" cy="100" r="22" fill="#8C1C2B"/><circle cx="160.6" cy="135" r="22" fill="#E07B24"/><circle cx="135" cy="160.6" r="22" fill="#E2B23C"/><circle cx="100" cy="170" r="22" fill="#3E8A3A"/><circle cx="65" cy="160.6" r="22" fill="#8C1C2B"/><circle cx="39.4" cy="135" r="22" fill="#23509E"/><circle cx="30" cy="100" r="22" fill="#E2B23C"/><circle cx="39.4" cy="65" r="22" fill="#E07B24"/><circle cx="65" cy="39.4" r="22" fill="#8C1C2B"/></g><circle cx="100" cy="100" r="52" fill="#2B1E16"/><g stroke="#2B1E16" stroke-width="4"><circle cx="113" cy="68.6" r="15" fill="#23509E"/><circle cx="131.4" cy="87" r="15" fill="#E07B24"/><circle cx="131.4" cy="113" r="15" fill="#3E8A3A"/><circle cx="113" cy="131.4" r="15" fill="#8C1C2B"/><circle cx="87" cy="131.4" r="15" fill="#23509E"/><circle cx="68.6" cy="113" r="15" fill="#E07B24"/><circle cx="68.6" cy="87" r="15" fill="#3E8A3A"/><circle cx="87" cy="68.6" r="15" fill="#8C1C2B"/></g><circle cx="100" cy="100" r="19" fill="#E2B23C" stroke="#2B1E16" stroke-width="4"/><path d="M100 88v24M90 97h20" stroke="#2B1E16" stroke-width="5" stroke-linecap="round"/></svg>`;

const index = `<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Una Voz · diseño</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500..800&amp;family=Nunito:wght@400;600;700;800&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;background:#FBF5EA;color:#2B1E16;font-family:Nunito,system-ui,sans-serif}
main{max-width:1100px;margin:0 auto;padding:28px 20px 64px}
header{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
h1{margin:0;font-family:Fraunces,Georgia,serif;font-size:36px;line-height:42px}
.lead{margin:12px 0 20px;font-size:17px;line-height:25px;color:#5A4A3C;max-width:720px}
.start{display:inline-flex;align-items:center;height:52px;padding:0 22px;border-radius:16px;background:#8C1C2B;color:#FFF8EC;font-weight:800;font-size:17px;text-decoration:none}
h2{margin:44px 0 16px;font-family:Fraunces,Georgia,serif;font-size:26px;line-height:32px}
.row{display:flex;flex-wrap:wrap;gap:20px}
.tile{margin:0;display:flex;flex-direction:column;gap:10px}
.tile.wide{max-width:100%}
.frame{display:block;position:relative;overflow:hidden;border-radius:22px;border:1px solid #E2CFAE;background:#fff;box-shadow:0 6px 18px rgba(43,30,22,.08)}
.tile.wide .frame{border-radius:12px;max-width:100%;overflow:auto}
.frame iframe{position:absolute;left:0;top:0;border:0;transform-origin:0 0;pointer-events:none}
figcaption a{color:#2B1E16;font-weight:800;font-size:15px}
footer{margin-top:48px;font-size:14px;line-height:20px;color:#6B5A4C}
footer a{color:#8C1C2B}
</style>
</head>
<body>
<main>
<header>${rosette}<h1>Una Voz · diseño</h1></header>
<p class="lead">Prototipo navegable de la versión ${escapeHtml(pageId.replace(/^v/, ''))}. Toca una pantalla para abrirla; dentro, los botones llevan a las siguientes. Los textos entre corchetes son datos que aún faltan.</p>
${start ? `<a class="start" href="${htmlName(start.file)}">Empezar el recorrido</a>` : ''}
${groups.map((g) => `<h2>${escapeHtml(g.title)}</h2>\n<div class="row">\n${g.items.map(tile).join('\n')}\n</div>`).join('\n')}
<footer>Actualizado el ${today}. Fuente: <a href="https://github.com/enderHugin/mobile-audio-sync/tree/design/flujo-e-interfaz/design">rama design/flujo-e-interfaz</a>.</footer>
</main>
</body>
</html>
`;
writeFileSync(join(out, 'index.html'), index);
console.log(`${boards.length} pantallas → ${out}`);
