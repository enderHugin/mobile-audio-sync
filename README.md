# mobile-audio-sync

Reproducción de una misma pista en muchos móviles a la vez, con sincronía de canto.

## Arquitectura

1. **Reloj de referencia.** Servidor con `chrony` sincronizado por NTS o NTP. Expone `GET /time`.
2. **Sincronía del cliente.** `web/clock-sync.js` estima el desfase con intercambios tipo NTP y conserva la muestra de menor retardo.
3. **Arranque programado.** Todos los móviles arrancan la reproducción en un instante absoluto acordado.
4. **Calibración por dispositivo.** Pendiente: test de latencia de salida para auriculares.
5. **Balizas por radio.** Pendiente y opcional: Wi-Fi Aware o BLE en una app nativa.

## Estructura

- `server/`: endpoint de tiempo.
- `web/`: cliente de sincronía (módulo ES, sin dependencias).
- `test/`: pruebas unitarias del cálculo de desfase.
- `bench/`: medición del error entre móviles (pendiente).

## Uso

```sh
npm start          # endpoint de tiempo en :8787 (variable PORT)
npm test           # pruebas
```

## Estado

Fase inicial: cálculo de desfase y endpoint de tiempo. Sin reproductor ni medición real todavía.
