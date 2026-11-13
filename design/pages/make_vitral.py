# Genera la vidriera: rosetón de vidrio emplomado en un muro de piedra, con la luz atravesándolo.
import math, random
import numpy as np
from scipy.spatial import Voronoi

PAL = {
    "ruby": (200, 16, 46), "blue": (28, 58, 156), "azure": (47, 125, 224), "emerald": (36, 150, 72),
    "gold": (233, 169, 35), "amber": (224, 106, 24), "violet": (123, 59, 192), "pale": (246, 232, 196),
}

def jitter(rgb, rnd, amt=0.22):
    f = 1 + rnd.uniform(-amt, amt)
    c = [min(255, max(0, int(v * f))) for v in rgb]
    if rnd.random() < 0.08:
        c = [min(255, int(v + (255 - v) * 0.22)) for v in c]
    return "#%02X%02X%02X" % tuple(c)

def vitral(w=390, h=340, cx=195, cy=150, R=96, p="v", rays=True, header_fade=True, bottom_fade=True, seed=11, label="Rosetón de vidriera en un muro de piedra, con la luz entrando"):
    rnd = random.Random(seed)
    o = []
    add = o.append
    add(f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}" style="display:block">')
    add('<defs>')
    add(f'<radialGradient id="{p}halo" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{R*2.6:.0f}"><stop offset="0" stop-color="#FFC66B" stop-opacity="0.55"/><stop offset="0.28" stop-color="#D98A3A" stop-opacity="0.38"/><stop offset="0.6" stop-color="#8A4F22" stop-opacity="0.12"/><stop offset="1" stop-color="#8A4F22" stop-opacity="0"/></radialGradient>')
    add(f'<radialGradient id="{p}sky" gradientUnits="userSpaceOnUse" cx="{cx-R*0.15:.0f}" cy="{cy-R*0.25:.0f}" r="{R*1.1:.0f}"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.34"/><stop offset="0.5" stop-color="#FFF0D0" stop-opacity="0.08"/><stop offset="1" stop-color="#FFF0D0" stop-opacity="0"/></radialGradient>')
    add(f'<radialGradient id="{p}rim" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{R}"><stop offset="0.72" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></radialGradient>')
    add(f'<radialGradient id="{p}splay" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{R+12}"><stop offset="{R/(R+12):.3f}" stop-color="#5E4428"/><stop offset="1" stop-color="#0E0906"/></radialGradient>')
    add(f'<radialGradient id="{p}frame" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{R+34}"><stop offset="{(R+10)/(R+34):.3f}" stop-color="#FFD08A" stop-opacity="0.2"/><stop offset="1" stop-color="#FFD08A" stop-opacity="0"/></radialGradient>')
    add(f'<radialGradient id="{p}vig" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{max(w,h)*0.78:.0f}"><stop offset="0.38" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.82"/></radialGradient>')
    add(f'<radialGradient id="{p}hostglow" gradientUnits="userSpaceOnUse" cx="{cx}" cy="{cy}" r="{R*0.42:.0f}"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.95"/><stop offset="0.45" stop-color="#FFF1C4" stop-opacity="0.55"/><stop offset="1" stop-color="#FFE29A" stop-opacity="0"/></radialGradient>')
    for gid, col, op in (("ray", "#FFE1A0", 0.6), ("rayr", "#FF6E5C", 0.45), ("rayb", "#7FA9FF", 0.45), ("rayg", "#9BE38C", 0.35)):
        add(f'<linearGradient id="{p}{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{col}" stop-opacity="{op}"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></linearGradient>')
    add(f'<linearGradient id="{p}stone" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.07"/><stop offset="0.55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.28"/></linearGradient>')
    add(f'<linearGradient id="{p}fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F0B08" stop-opacity="0"/><stop offset="1" stop-color="#0F0B08" stop-opacity="1"/></linearGradient>')
    add(f'<linearGradient id="{p}top" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F0B08" stop-opacity="0.85"/><stop offset="1" stop-color="#0F0B08" stop-opacity="0"/></linearGradient>')
    add(f'<filter id="{p}bloom" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="{R*0.09:.1f}"/></filter>')
    add(f'<filter id="{p}bloom2" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="{R*0.26:.1f}"/></filter>')
    add(f'<filter id="{p}soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{R*0.035:.1f}"/></filter>')
    add(f'<filter id="{p}grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="5"/><feColorMatrix type="matrix" values="0 0 0 0 0.05  0 0 0 0 0.04  0 0 0 0 0.03  0 0 0 -1.7 1.2"/></filter>')
    add(f'<filter id="{p}glassgrain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.35" numOctaves="2" seed="9"/><feColorMatrix type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 -1.2 0.75"/></filter>')
    add(f'<clipPath id="{p}win"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>')
    add('</defs>')

    # Muro de sillares
    add(f'<rect width="{w}" height="{h}" fill="#0E0A07"/>')
    stones = ["#2E251E", "#2A221B", "#33291F", "#2C231C", "#30271F", "#372C23", "#28201A"]
    rowh = max(30, int(R * 0.40))
    y = -int(rowh * 0.4)
    row = 0
    while y < h:
        x = -rnd.randint(int(rowh * 0.4), int(rowh * 2.4))
        while x < w:
            bw = rnd.randint(int(rowh * 2.0), int(rowh * 3.8))
            add(f'<rect x="{x+1.5}" y="{y+1.5}" width="{bw-3}" height="{rowh-3}" rx="2.5" fill="{rnd.choice(stones)}"/>')
            add(f'<rect x="{x+1.5}" y="{y+1.5}" width="{bw-3}" height="{rowh-3}" rx="2.5" fill="url(#{p}stone)"/>')
            add(f'<path d="M{x+4} {y+3} H{x+bw-4}" stroke="#6B5846" stroke-opacity="0.45" stroke-width="1.2"/>')
            add(f'<path d="M{x+4} {y+rowh-3} H{x+bw-4}" stroke="#070504" stroke-opacity="0.7" stroke-width="1.5"/>')
            x += bw
        y += rowh
        row += 1
    add(f'<rect width="{w}" height="{h}" filter="url(#{p}grain)"/>')
    add(f'<rect width="{w}" height="{h}" fill="url(#{p}halo)" style="mix-blend-mode:screen"/>')

    # Dovelas del marco
    n = 28
    r1, r2 = R + 11, R + 34
    for i in range(n):
        a0 = 2 * math.pi * i / n + 0.01
        a1 = 2 * math.pi * (i + 1) / n - 0.01
        P = lambda r, a: (cx + r * math.sin(a), cy - r * math.cos(a))
        q0, q1, q2, q3 = P(r1, a0), P(r2, a0), P(r2, a1), P(r1, a1)
        col = rnd.choice(["#3E3228", "#392D24", "#45382C", "#352A21", "#41342A"])
        add(f'<path d="M{q0[0]:.1f} {q0[1]:.1f} L{q1[0]:.1f} {q1[1]:.1f} A{r2} {r2} 0 0 1 {q2[0]:.1f} {q2[1]:.1f} L{q3[0]:.1f} {q3[1]:.1f} A{r1} {r1} 0 0 0 {q0[0]:.1f} {q0[1]:.1f}Z" fill="{col}"/>')
    for i in range(n):
        a = 2 * math.pi * i / n
        add(f'<path d="M{cx+r1*math.sin(a):.1f} {cy-r1*math.cos(a):.1f} L{cx+r2*math.sin(a):.1f} {cy-r2*math.cos(a):.1f}" stroke="#0B0705" stroke-width="2"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{r2}" fill="url(#{p}frame)" style="mix-blend-mode:screen"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{r1+1.5}" fill="none" stroke="#D9AE72" stroke-opacity="0.45" stroke-width="1.5"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{r2+1.5}" fill="none" stroke="#120D0A" stroke-width="3"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{R+11}" fill="url(#{p}splay)"/>')

    # Vidrio emplomado (teselas de Voronoi)
    pts = []
    dmin = R * 0.085
    tries = 0
    while tries < 30000:
        tries += 1
        rr = R * 1.02 * math.sqrt(rnd.random())
        a = rnd.random() * 2 * math.pi
        x, yy = rr * math.sin(a), -rr * math.cos(a)
        if all((x - u) ** 2 + (yy - v) ** 2 > dmin * dmin for u, v in pts[-400:]) and all((x - u) ** 2 + (yy - v) ** 2 > dmin * dmin for u, v in pts):
            pts.append((x, yy))
    far = [(3 * R * math.cos(t), 3 * R * math.sin(t)) for t in np.linspace(0, 2 * math.pi, 24, endpoint=False)]
    vor = Voronoi(np.array(pts + far))
    lobe_cols = ["ruby", "emerald", "gold", "violet", "azure", "amber", "ruby", "emerald", "gold", "violet", "azure", "amber"]
    petal_cols = ["ruby", "gold"] * 4
    def colour(x, yy):
        r = math.hypot(x, yy) / R
        ang = math.atan2(x, -yy) % (2 * math.pi)
        if r < 0.2:
            return "pale"
        if r < 0.47:
            k = int(((ang / (2 * math.pi)) * 8 - 0.5) % 8 + 0.5) % 8
            best = min(range(8), key=lambda i: math.hypot(x - 0.33 * R * math.sin(2 * math.pi * (i + 0.5) / 8), yy + 0.33 * R * math.cos(2 * math.pi * (i + 0.5) / 8)))
            px, py = 0.33 * R * math.sin(2 * math.pi * (best + 0.5) / 8), -0.33 * R * math.cos(2 * math.pi * (best + 0.5) / 8)
            return petal_cols[best] if math.hypot(x - px, yy - py) < 0.15 * R else "blue"
        best = min(range(12), key=lambda i: math.hypot(x - 0.70 * R * math.sin(2 * math.pi * i / 12), yy + 0.70 * R * math.cos(2 * math.pi * i / 12)))
        lx, ly = 0.70 * R * math.sin(2 * math.pi * best / 12), -0.70 * R * math.cos(2 * math.pi * best / 12)
        if math.hypot(x - lx, yy - ly) < 0.25 * R:
            return lobe_cols[best]
        if r > 0.86:
            return "gold" if rnd.random() < 0.35 else "ruby"
        return "blue" if rnd.random() < 0.85 else "azure"
    add(f'<g id="{p}glass" clip-path="url(#{p}win)">')
    add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#150E09"/>')
    for i, (x, yy) in enumerate(pts):
        reg = vor.regions[vor.point_region[i]]
        if not reg or -1 in reg:
            continue
        poly = vor.vertices[reg]
        d = "M" + " L".join(f"{cx+vx:.1f} {cy+vy:.1f}" for vx, vy in poly) + "Z"
        add(f'<path d="{d}" fill="{jitter(PAL[colour(x, yy)], rnd)}" stroke="#140D08" stroke-width="{max(1.1, R*0.014):.1f}" stroke-linejoin="round"/>')
    add(f'<rect x="{cx-R}" y="{cy-R}" width="{2*R}" height="{2*R}" filter="url(#{p}glassgrain)" opacity="0.18" style="mix-blend-mode:overlay"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#{p}sky)" style="mix-blend-mode:screen"/>')
    # Tracería de piedra
    tw = max(2.5, R * 0.035)
    for i in range(12):
        a = 2 * math.pi * i / 12
        add(f'<circle cx="{cx+0.70*R*math.sin(a):.1f}" cy="{cy-0.70*R*math.cos(a):.1f}" r="{0.25*R:.1f}" fill="none" stroke="#100A06" stroke-width="{tw:.1f}"/>')
    for i in range(8):
        a = 2 * math.pi * (i + 0.5) / 8
        add(f'<circle cx="{cx+0.33*R*math.sin(a):.1f}" cy="{cy-0.33*R*math.cos(a):.1f}" r="{0.15*R:.1f}" fill="none" stroke="#100A06" stroke-width="{tw*0.8:.1f}"/>')
    for i in range(12):
        a = 2 * math.pi * (i + 0.5) / 12
        add(f'<path d="M{cx+0.47*R*math.sin(a):.1f} {cy-0.47*R*math.cos(a):.1f} L{cx+R*math.sin(a):.1f} {cy-R*math.cos(a):.1f}" stroke="#100A06" stroke-width="{tw:.1f}"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{0.47*R:.1f}" fill="none" stroke="#100A06" stroke-width="{tw*1.2:.1f}"/>')
    # La Hostia en el centro
    rc = R * 0.19
    add(f'<circle cx="{cx}" cy="{cy}" r="{R*0.42:.0f}" fill="url(#{p}hostglow)"/>')
    for i in range(24):
        a = 2 * math.pi * i / 24
        l = rc * (1.62 if i % 2 == 0 else 1.32)
        add(f'<path d="M{cx+rc*1.05*math.sin(a):.1f} {cy-rc*1.05*math.cos(a):.1f} L{cx+l*math.sin(a):.1f} {cy-l*math.cos(a):.1f}" stroke="#FFE9AE" stroke-width="{max(1.2, R*0.016):.1f}" stroke-linecap="round"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{rc:.1f}" fill="#FFFBF0" stroke="#E2B23C" stroke-width="{max(1.5, R*0.02):.1f}"/>')
    add(f'<path d="M{cx} {cy-rc*0.55:.1f} V{cy+rc*0.55:.1f} M{cx-rc*0.38:.1f} {cy-rc*0.12:.1f} H{cx+rc*0.38:.1f}" stroke="#D6A53A" stroke-width="{max(1.3, R*0.016):.1f}" stroke-linecap="round"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#{p}rim)"/>')
    add('</g>')
    # Resplandor: la luz atraviesa el vidrio
    add(f'<use href="#{p}glass" filter="url(#{p}bloom2)" opacity="0.38" style="mix-blend-mode:screen"/>')
    add(f'<use href="#{p}glass" filter="url(#{p}bloom)" opacity="0.42" style="mix-blend-mode:screen"/>')
    add(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#140D08" stroke-width="{tw*1.2:.1f}"/>')

    if rays:
        add(f'<g filter="url(#{p}soft)" style="mix-blend-mode:screen">')
        dx = -0.36
        shafts = [(-0.72, "rayb"), (-0.45, "ray"), (-0.18, "rayr"), (0.10, "ray"), (0.38, "rayg"), (0.64, "ray")]
        for t, gid in shafts:
            x0 = cx + R * t
            y0 = cy + math.sqrt(max(0.0, R * R - (x0 - cx) ** 2)) * 0.55
            L = h - y0
            w0, w1 = R * 0.13, R * 0.34
            xb = x0 + dx * L
            add(f'<polygon points="{x0-w0/2:.0f},{y0:.0f} {x0+w0/2:.0f},{y0:.0f} {xb+w1/2:.0f},{h} {xb-w1/2:.0f},{h}" fill="url(#{p}{gid})"/>')
        add('</g>')

    add(f'<rect width="{w}" height="{h}" fill="url(#{p}vig)"/>')
    if header_fade:
        add(f'<rect width="{w}" height="80" fill="url(#{p}top)"/>')
    if bottom_fade:
        add(f'<rect y="{h-100}" width="{w}" height="100" fill="url(#{p}fade)"/>')
    add('</svg>')
    return "".join(o)

if __name__ == "__main__":
    print(vitral())
