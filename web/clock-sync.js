// Estimación del desfase entre el reloj local y el del servidor.
// Algoritmo tipo NTP con cuatro marcas de tiempo por intercambio (en ms epoch):
//   t0: cliente envía, t1: servidor recibe, t2: servidor responde, t3: cliente recibe.
// offset = ((t1 - t0) + (t2 - t3)) / 2   (serverTime ≈ localTime + offset)
// delay  = (t3 - t0) - (t2 - t1)          (tiempo de red de ida y vuelta)
// Se conserva la muestra con menor delay: es la más fiable.

export function computeSample(t0, t1, t2, t3) {
  return {
    offset: ((t1 - t0) + (t2 - t3)) / 2,
    delay: (t3 - t0) - (t2 - t1),
  };
}

export function bestSample(samples) {
  if (samples.length === 0) throw new Error("No hay muestras de sincronía");
  return samples.reduce((best, s) => (s.delay < best.delay ? s : best));
}

// Hora local en ms epoch con precisión de sub-milisegundo.
const nowEpoch = () => performance.timeOrigin + performance.now();

// Ejecuta n intercambios contra `url` (GET que devuelve { serverTime } en ms epoch).
// Devuelve la muestra de menor delay: { offset, delay } en ms.
export async function measureOffset(url, n = 8, fetchImpl = fetch) {
  const samples = [];
  for (let i = 0; i < n; i++) {
    const t0 = nowEpoch();
    const res = await fetchImpl(url, { cache: "no-store" });
    const { serverTime } = await res.json();
    const t3 = nowEpoch();
    // El servidor responde en un único instante, así que t1 = t2 = serverTime.
    samples.push(computeSample(t0, serverTime, serverTime, t3));
  }
  return bestSample(samples);
}
