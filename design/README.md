# Diseño: flujo e interfaz de participación

Diseño del flujo del participante y de las pantallas de móvil. La **versión 2** (oscura, con la vidriera) es la vigente; la versión 1 se conserva para comparar.

- **Lienzo editable:** https://claude.ai/artifact/Hkk4yG9unjmRy2ZoYzJ37e (abre en la página «Versión 2»; privado de su propietario hasta que lo comparta).
- **Ver en la web (cualquier navegador):** https://enderhugin.github.io/mobile-audio-sync/ — se genera con `node design/build-pages.mjs <carpeta>` y se publica en la rama `gh-pages`.
- **Fuente del lienzo:** [`canvas/`](canvas/). Son archivos `.dc.html` del editor de diseño: necesitan su entorno (`support.js`) para verse, así que GitHub no los muestra como página. Sirven como referencia de estructura, textos, colores y medidas para implementar la web en `web/`.

## Tono

Poco texto, claro y práctico. Quien llega ya sabe a qué viene, porque lo ha visto en un vídeo: la web es el medio de convocatoria. La emoción (pertenencia, hogar, estabilidad, altar, aventura, encuentro) la ponen la imagen y los símbolos, no las palabras.

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

### Sacerdotes

Cada sacerdote puede ofrecerse en un lugar para exponer el Santísimo y para confesar antes de empezar, con su horario. La organización confirma cada ofrecimiento con la parroquia antes de mostrarlo. La ficha del lugar, tu encuentro y la pantalla del día indican dónde y cuándo se confiesa.

### Organización

La organización crea cada encuentro y solo puede publicarlo cuando la composición, las voces separadas, la base y la voz de guía están listas. Las traducciones de la letra son opcionales.

## Identidad

- **Símbolo:** un rosetón real en su muro de piedra, con la luz atravesándolo: la foto del rosetón de la catedral de Sigüenza (ver créditos), recortada y retocada.
- **Rosetón personal:** seis pétalos con los colores de cómo viene cada persona, enmarcados en oro.
- **Símbolos:** custodia (el altar), casa (el hogar), estandarte (la convocatoria), palma (el martirio), cruz (la fe), vieira (el camino), pin con cruz (la plaza), nota (cantar), vela (orar desde casa), corazón (aportar), estola (la confesión).
- **Tipografías:** Fraunces (títulos) y Nunito (texto).

| Color | Uso | Valor |
|---|---|---|
| Noche | Fondo | `#0F0B08` |
| Piedra | Superficies y bordes | `#1A130F`, `#3A2C21` |
| Marfil | Texto | `#F4EADB` (secundario `#BFAE97`) |
| Oro | Lo eterno; botones principales | `#E2B23C` |
| Granate | Entrega; la convocatoria | `#8C1C2B` (fondo `#3D0C14`) |
| Verde | Cantar | `#3E8A3A` (texto `#7CC47A`) |
| Azul | Orar | `#2D5FB8` (texto `#8EAEF0`) |
| Naranja | Aportar | `#E07B24` (texto `#F2A65E`) |

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
| `MiEncuentro.dc.html` | Tu encuentro con cuenta atrás |
| `Ensayar.dc.html` | Ensayo con letra (interactiva) |
| `DiaDelEncuentro.dc.html` | El día, ante el Santísimo |
| `Organizador.dc.html` | Crear un encuentro (interactiva) |
| `Sacerdote.dc.html` | Sacerdotes: ofrecerse para exponer y confesar (interactiva) |

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

## Créditos

Ver [`pages/CREDITOS.md`](pages/CREDITOS.md). La foto del rosetón es de EventusBonus (Wikimedia Commons), CC BY-SA 4.0.
