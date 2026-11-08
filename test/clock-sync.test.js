import { test } from "node:test";
import assert from "node:assert/strict";
import { computeSample, bestSample } from "../web/clock-sync.js";

test("reloj cliente adelantado 100 ms, red simétrica de 20 ms", () => {
  // Servidor en t=1000 (real). Cliente va 100 ms adelantado: su hora = real + 100.
  // Ida 10 ms, vuelta 10 ms, procesado 0 ms.
  const t0 = 1100 - 0; // cliente envía (real 1000 + 100 de adelanto)
  const t1 = 1010;     // servidor recibe (real)
  const t2 = 1010;     // servidor responde
  const t3 = 1120;     // cliente recibe (real 1020 + 100)
  const s = computeSample(t0, t1, t2, t3);
  assert.equal(s.offset, -100); // el cliente debe restar 100 ms
  assert.equal(s.delay, 20);
});

test("bestSample elige la muestra con menor delay", () => {
  const samples = [
    { offset: 5, delay: 40 },
    { offset: 2, delay: 8 },
    { offset: 3, delay: 15 },
  ];
  assert.deepEqual(bestSample(samples), { offset: 2, delay: 8 });
});

test("bestSample lanza error sin muestras", () => {
  assert.throws(() => bestSample([]));
});
