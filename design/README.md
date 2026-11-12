# Diseño: flujo e interfaz de participación

Diseño del flujo del participante y de las pantallas de móvil. La **versión 2 (cálida)** es la vigente; la versión 1 se conserva para comparar.

- **Lienzo editable:** https://claude.ai/artifact/Hkk4yG9unjmRy2ZoYzJ37e (abre en la página «Versión 2 · cálida»; privado de su propietario hasta que lo comparta).
- **Fuente del lienzo:** [`canvas/`](canvas/). Son archivos `.dc.html` del editor de diseño: necesitan su entorno (`support.js`) para verse, así que GitHub no los muestra como página. Sirven como referencia de estructura, textos, colores y medidas para implementar la web en `web/`.

## Tono

Hogar, quedada, encuentro, valentía, tradición y contemplación. No es para gente que sepa música: es para gente que quiere cantar y quedar en un lugar concreto.

## Flujo (versión 2)

1. **Encuentros.** Lista de fechas fijadas por la organización, cada una con su cuenta atrás.
2. **Lugar.** Mapa con plazas y caminos. Si no hay uno cerca, se propone tocando el mapa.
3. **¿Cómo vienes?** Cantar, orar o aportar; una o varias.
4. **Canciones.** Las del encuentro, en orden; se marcan las que se van a cantar.
5. **Voz.** Sin lenguaje musical: «la melodía», «aguda de mujer», «grave de hombre»…
6. **Tus datos.** Nombre y correo o móvil.
7. **Mi encuentro.** Entrada con cuenta atrás, ensayar e invitar.
8. **El día.** En el lugar, ante el Santísimo, todos a la vez en el mundo.

### Cómo se habilita un lugar

Alguien lo propone (plaza o camino) → se apuntan **25 personas** → un **sacerdote confirma que expondrá el Santísimo** → lugar habilitado. El mínimo y la exigencia del sacerdote se ajustan por encuentro en la pantalla de organización.

### Organización

La organización crea cada encuentro y solo puede publicarlo cuando la composición, las voces separadas, la base y la voz de guía están listas. Las traducciones de la letra son opcionales.

## Identidad

- **Símbolo:** un rosetón de catedral. Cada persona es un cristal: su rosetón personal tiene seis pétalos con los colores de cómo viene.
- **Símbolos:** custodia (orar), nota (cantar), corazón (aportar), vieira (camino), pin con cruz (plaza), palma (valentía), cruz, estrella (encuentro), vela (orar desde casa), banderines (quedada).
- **Tipografías:** Fraunces (títulos) y Nunito (texto).

| Color | Uso | Valor |
|---|---|---|
| Granate | Entrega; botones principales | `#8C1C2B` |
| Oro | Lo eterno, el Santísimo | `#E2B23C` (texto `#8A6416`) |
| Marfil | Fondo, hogar | `#FBF5EA` |
| Tinta | Texto | `#2B1E16` |
| Verde | Cantar | `#3E8A3A` (texto `#2F6B2C`) |
| Azul | Orar | `#23509E` |
| Naranja | Aportar | `#E07B24` (texto `#A44E0E`) |

El color de cada forma de apoyo va siempre con su icono y su nombre.

## Pantallas (versión 2)

| Archivo | Pantalla |
|---|---|
| `Flujo2.dc.html` | Diagrama del flujo |
| `Identidad.dc.html` | Rosetón, símbolos, colores y tipografías |
| `Encuentros.dc.html` | Lista de encuentros con cuenta atrás |
| `Lugares.dc.html` | Mapa y lista de lugares |
| `ProponerLugar.dc.html` | Proponer plaza o camino (interactiva) |
| `Lugar.dc.html` | Ficha del lugar y requisitos |
| `Participar.dc.html` | ¿Cómo vienes? (interactiva) |
| `Cancion.dc.html` | Canciones del encuentro (interactiva) |
| `TuVoz.dc.html` | Elegir voz (interactiva) |
| `TusDatos.dc.html` | Último paso |
| `MiEncuentro.dc.html` | Entrada con cuenta atrás |
| `Ensayar.dc.html` | Ensayo con letra (interactiva) |
| `DiaDelEncuentro.dc.html` | El día, ante el Santísimo |
| `Organizador.dc.html` | Crear un encuentro (interactiva) |

Versión 1: `Main`, `Colores`, `Inicio`, `Unete`, `Registro`, `MiEspacio`, `Canciones`, `Voz`, `Ensayo`, `Convocatorias`, `Oracion`, `Aportar`, `ModoEvento`, `EnDirecto`, `Despues`.

## Marcadores

Los datos que aún no existen van entre corchetes: `[FECHA 1]`, `[N]`, `[Título de la canción]`, `[PARROQUIA]`, `[EDAD MÍNIMA]`. «Una Voz» es un nombre provisional. Las líneas de letra son de relleno. Los nombres de lugares del mapa son de ejemplo.

## Decisiones pendientes

- **Nombre** del evento.
- **Canciones por encuentro:** una sola o un programa de varias (el diseño supone varias, en orden).
- **Sacerdote obligatorio o no.** Exponer el Santísimo en la calle o hacer una procesión con él suele requerir el visto bueno de la parroquia y del obispado, además del permiso municipal para ocupar la plaza o la calle. Conviene que la ficha del lugar recoja también ese permiso.
- **Datos personales:** apuntarse revela la participación en un acto religioso, dato de categoría especial del RGPD (art. 9). Hace falta consentimiento explícito.
- **Aportaciones:** requieren una entidad legal y un proveedor de pagos.
- **Edad mínima** de registro según el país.
- **Qué oye cada participante el día:** solo la música, o la música con su voz de guía.
