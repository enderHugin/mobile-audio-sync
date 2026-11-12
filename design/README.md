# Diseño: flujo e interfaz de participación

Primera versión del flujo del participante y de las pantallas de móvil.

- **Lienzo editable:** https://claude.ai/artifact/Hkk4yG9unjmRy2ZoYzJ37e (privado de su propietario hasta que lo comparta).
- **Fuente del lienzo:** [`canvas/`](canvas/). Son archivos `.dc.html` del editor de diseño: necesitan su entorno (`support.js`) para verse, así que GitHub no los muestra como página. Sirven como referencia de estructura, textos, colores y medidas para implementar la web en `web/`.

## Flujo

1. **Descubrir.** Inicio con la identidad, la próxima convocatoria y la cuenta atrás.
2. **Unirse.** Elegir cómo apoyar: cantar, orar o aportar (una o varias). Cada elección da color.
3. **Comprometerse.** Registro sin contraseña (enlace por correo), compromiso de asistencia y permisos.
4. **Prepararse**, según lo elegido:
   - **Cantar:** elegir canción y voz por tesitura (con prueba de micrófono opcional) y ensayar la pista.
   - **Orar:** a la hora del evento o en un turno del relevo de 24 h.
   - **Aportar:** una vez o cada mes, viendo a qué se destina.
5. **Convocatoria.** Recordatorios y ensayo general en línea, que también es la prueba técnica.
6. **Día del evento.** Modo evento: comprobaciones, reloj sincronizado, cuenta atrás y letra en directo.
7. **Después.** Agradecimiento, mapa de participación, pregunta sobre la sincronía y siguiente convocatoria.

## Colores de apoyo

| Apoyo | Icono | Relleno | Texto sobre claro |
|---|---|---|---|
| Canto | nota musical | `#16A34A` | `#15803D` |
| Oración | llama | `#1D4ED8` | `#1D4ED8` |
| Aportación | corazón | `#FB923C` | `#C2410C` |

- Quien apoya de varias formas lleva un anillo repartido a partes iguales entre sus colores.
- El anillo con los tres colores es el símbolo del evento.
- El color nunca va solo: siempre con icono y nombre. Los tres tonos difieren también en luminosidad, para distinguirse con daltonismo.

Base neutra: fondo `#F5F6F8`, superficie `#FFFFFF`, texto `#111827`, texto secundario `#4B5563`. Modo evento en oscuro: fondo `#0B0F17`. Tipografías: Bricolage Grotesque (títulos) e Inter (texto).

## Pantallas

| Archivo | Pantalla |
|---|---|
| `Main.dc.html` | Diagrama del flujo |
| `Colores.dc.html` | Sistema de colores |
| `Inicio.dc.html` | Inicio para visitantes |
| `Unete.dc.html` | Elegir cómo apoyar (interactiva) |
| `Registro.dc.html` | Registro y compromiso |
| `MiEspacio.dc.html` | Inicio de la persona registrada |
| `Canciones.dc.html` | Lista de canciones |
| `Voz.dc.html` | Elegir voz por tesitura (interactiva) |
| `Ensayo.dc.html` | Reproductor de ensayo con letra y mezcla |
| `Convocatorias.dc.html` | Fechas y recordatorios |
| `Oracion.dc.html` | Oración y relevo |
| `Aportar.dc.html` | Aportación puntual o mensual (interactiva) |
| `ModoEvento.dc.html` | Preparación del día del evento |
| `EnDirecto.dc.html` | Letra durante la canción |
| `Despues.dc.html` | Después del evento |

## Marcadores

Los datos que aún no existen van entre corchetes: `[FECHA DEL EVENTO]`, `[LUGAR]`, `[N]`, `[Título de la canción]`, `[EDAD MÍNIMA]`, `[PROVEEDOR DE PAGO]`. «Una Voz» es un nombre provisional. Las líneas de letra son de relleno. Los rangos de voz son los habituales de coro; cada canción tendrá los suyos.

## Decisiones pendientes

- Nombre del evento y si tiene un marco religioso explícito (afecta al tono de la pantalla de oración).
- **Datos de oración:** revelan creencias, categoría especial del RGPD (art. 9). Hace falta consentimiento explícito; por eso mostrarse en el mapa es una casilla aparte y opcional. Las intenciones compartidas necesitan moderación.
- **Aportaciones:** requieren una entidad legal (asociación o fundación) y un proveedor de pagos para cobros mensuales y certificados de donación.
- **Edad mínima de registro:** depende del país.
- Qué oye cada participante el día del evento: solo la base, o la base más una guía de su voz.
