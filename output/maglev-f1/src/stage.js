// MAGLAP interactive levitation stage.
// A procedural 1:24 formula-style car floating over a maglev base, built in three.js.
// Units: 1 unit = 1 cm. Car nose points +Z, up is +Y.
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass.js';
import { OutputPass } from 'three/examples/jsm/postprocessing/OutputPass.js';

export const LIVERIES = {
  navy:   { body: '#14306f', accent: '#e3111f', tyre: '#ff2233', wing: '#141a2c', nose: '#ffcc1a', matte: true },
  carbon: { body: '#0d0e11', accent: '#ff1a2d', tyre: '#ff2233', wing: '#111214', glossy: true },
  arctic: { body: '#e9edf2', accent: '#1f5bff', tyre: '#2a66ff', wing: '#121316', glossy: true },
  rosso:  { body: '#8f0a14', accent: '#16171a', tyre: '#ffd23a', wing: '#121316', glossy: true },
};

const BASE_R = 9.2, BASE_H = 3.0, GAP = 2.2;

// ---------- small geometry helpers ----------
function canvasTex(w, h, draw) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}

// Loft a closed body through superellipse cross sections.
// stations: [{z, cx, hw, y0, y1, n}] ordered from front to back.
function loft(stations, seg = 40) {
  const pos = [], uv = [], idx = [];
  const rings = stations.length;
  for (let i = 0; i < rings; i++) {
    const s = stations[i];
    const cy = (s.y0 + s.y1) / 2, hh = (s.y1 - s.y0) / 2, n = s.n || 3.2;
    for (let j = 0; j <= seg; j++) {
      const a = (j / seg) * Math.PI * 2;
      const ca = Math.cos(a), sa = Math.sin(a);
      const x = Math.sign(ca) * Math.pow(Math.abs(ca), 2 / n) * s.hw;
      const y = Math.sign(sa) * Math.pow(Math.abs(sa), 2 / n) * hh;
      pos.push((s.cx || 0) + x, cy + y, s.z);
      uv.push(j / seg, i / (rings - 1));
    }
  }
  for (let i = 0; i < rings - 1; i++) for (let j = 0; j < seg; j++) {
    const a = i * (seg + 1) + j, b = a + seg + 1;
    idx.push(a, b, a + 1, b, b + 1, a + 1);
  }
  // caps
  const capFor = (ring, flip) => {
    const s = stations[ring];
    const c = pos.length / 3;
    pos.push(s.cx || 0, (s.y0 + s.y1) / 2, s.z); uv.push(0.5, ring / (rings - 1));
    for (let j = 0; j < seg; j++) {
      const a = ring * (seg + 1) + j;
      if (flip) idx.push(c, a + 1, a); else idx.push(c, a, a + 1);
    }
  };
  capFor(0, false); capFor(rings - 1, true);
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx); g.computeVertexNormals();
  return g;
}

// Airfoil extruded along X. chord along -Z from leading edge, thickness t.
function airfoil(width, chord, t, camber = 0.06) {
  const sh = new THREE.Shape();
  const N = 24, up = [], lo = [];
  for (let i = 0; i <= N; i++) {
    const x = i / N; // 0 leading, 1 trailing
    const yt = 5 * t * (0.2969 * Math.sqrt(x) - 0.126 * x - 0.3516 * x * x + 0.2843 * x ** 3 - 0.1036 * x ** 4);
    const yc = camber * chord * 4 * x * (1 - x);
    up.push([x * chord, yc + yt * chord]); lo.push([x * chord, yc - yt * chord]);
  }
  sh.moveTo(up[0][0], up[0][1]);
  up.forEach(p => sh.lineTo(p[0], p[1]));
  lo.reverse().forEach(p => sh.lineTo(p[0], p[1]));
  const g = new THREE.ExtrudeGeometry(sh, { depth: width, bevelEnabled: false, curveSegments: 4 });
  g.translate(0, 0, -width / 2);
  g.rotateY(Math.PI / 2); // chord now along -Z? after rotate: shape x -> -z, depth z -> x
  return g;
}

function plate(shapePts, thick) {
  const sh = new THREE.Shape(shapePts.map(p => new THREE.Vector2(p[0], p[1])));
  const g = new THREE.ExtrudeGeometry(sh, { depth: thick, bevelEnabled: false });
  g.translate(0, 0, -thick / 2);
  return g;
}

function rod(a, b, r, mat) {
  const A = new THREE.Vector3(...a), B = new THREE.Vector3(...b);
  const len = A.distanceTo(B);
  const m = new THREE.Mesh(new THREE.CylinderGeometry(r, r, len, 8), mat);
  m.position.copy(A).add(B).multiplyScalar(0.5);
  m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), B.clone().sub(A).normalize());
  return m;
}

// ---------- materials ----------
function makeMaterials() {
  const carbonTex = canvasTex(256, 256, (g, w, h) => {
    g.fillStyle = '#0c0d0f'; g.fillRect(0, 0, w, h);
    const s = 16;
    for (let y = 0; y < h; y += s) for (let x = 0; x < w; x += s) {
      const odd = ((x + y) / s) % 2;
      const grd = g.createLinearGradient(x, y, odd ? x + s : x, odd ? y : y + s);
      grd.addColorStop(0, '#1b1d21'); grd.addColorStop(0.5, '#0a0b0d'); grd.addColorStop(1, '#17191c');
      g.fillStyle = grd; g.fillRect(x + 1, y + 1, s - 2, s - 2);
    }
  });
  carbonTex.wrapS = carbonTex.wrapT = THREE.RepeatWrapping; carbonTex.repeat.set(6, 6);
  return {
    carbon: new THREE.MeshPhysicalMaterial({ map: carbonTex, roughness: 0.32, metalness: 0.2, clearcoat: 1, clearcoatRoughness: 0.18 }),
    rubber: new THREE.MeshStandardMaterial({ color: '#141416', roughness: 0.82, metalness: 0 }),
    rim: new THREE.MeshStandardMaterial({ color: '#1a1b1e', roughness: 0.35, metalness: 0.85 }),
    hub: new THREE.MeshStandardMaterial({ color: '#c9a64a', roughness: 0.5, metalness: 1 }),
    dark: new THREE.MeshStandardMaterial({ color: '#050506', roughness: 0.6 }),
    visor: new THREE.MeshPhysicalMaterial({ color: '#0a0a0c', roughness: 0.3, metalness: 0.3, clearcoat: 0.5, clearcoatRoughness: 0.3 }),
    rainLight: new THREE.MeshStandardMaterial({ color: '#ff1020', emissive: '#ff1020', emissiveIntensity: 2.5 }),
    body: new THREE.MeshPhysicalMaterial({ roughness: 0.22, metalness: 0.35, clearcoat: 1, clearcoatRoughness: 0.2 }),
    accent: new THREE.MeshPhysicalMaterial({ roughness: 0.35, metalness: 0.2, clearcoat: 1, clearcoatRoughness: 0.25 }),
    tyreBand: new THREE.MeshStandardMaterial({ roughness: 0.6 }),
    wing: new THREE.MeshPhysicalMaterial({ roughness: 0.3, metalness: 0.25, clearcoat: 1, clearcoatRoughness: 0.25 }),
  };
}

function liveryTexture(l) {
  // u wraps around the section (0 = right side middle), v runs nose -> tail
  return canvasTex(1024, 512, (g, w, h) => {
    g.fillStyle = l.body; g.fillRect(0, 0, w, h);
    if (l.nose) { g.fillStyle = l.nose; g.fillRect(0, 0, w, h * 0.09); }
    g.strokeStyle = l.accent; g.lineWidth = 7;
    // pinstripe along both flanks, sweeping up toward the tail
    for (const u0 of [0.06, 0.44]) {
      g.beginPath();
      for (let v = 0.04; v <= 0.98; v += 0.01) {
        const u = u0 + (u0 < 0.25 ? 1 : -1) * 0.06 * Math.sin(v * Math.PI);
        const x = u * w, y = v * h;
        v === 0.04 ? g.moveTo(x, y) : g.lineTo(x, y);
      }
      g.stroke();
    }
    // spine stripe
    g.lineWidth = 5; g.beginPath(); g.moveTo(0.25 * w, 0.02 * h); g.lineTo(0.25 * w, 0.6 * h); g.stroke();
    // soft sheen gradient to avoid flat look
    const grd = g.createLinearGradient(0, 0, 0, h);
    grd.addColorStop(0, 'rgba(255,255,255,0.05)'); grd.addColorStop(1, 'rgba(0,0,0,0.12)');
    g.fillStyle = grd; g.fillRect(0, 0, w, h);
  });
}

// ---------- car ----------
function buildCar(M) {
  const car = new THREE.Group();

  // floor plank
  const half = [[-10.2, 2.6], [-8.5, 3.3], [-3, 3.5], [3.2, 3.5], [4.6, 2.0], [7.6, 1.1]];
  const pts = half.map(([z, x]) => [x, z]).concat(half.slice().reverse().map(([z, x]) => [-x, z]));
  const floor = new THREE.Mesh(plate(pts, 0.22), M.carbon);
  floor.rotation.x = Math.PI / 2; floor.position.y = 0.42; car.add(floor);

  // monocoque + nose + engine cover
  const body = new THREE.Mesh(loft([
    { z: 11.9, hw: 0.28, y0: 0.95, y1: 1.25, n: 2.4 },
    { z: 10.6, hw: 0.55, y0: 0.85, y1: 1.6 },
    { z: 8.6, hw: 0.82, y0: 0.75, y1: 2.0 },
    { z: 6.0, hw: 1.05, y0: 0.62, y1: 2.45 },
    { z: 3.8, hw: 1.25, y0: 0.55, y1: 2.7 },
    { z: 1.2, hw: 1.35, y0: 0.5, y1: 2.85 },
    { z: -0.6, hw: 1.3, y0: 0.5, y1: 3.55, n: 2.8 },
    { z: -2.6, hw: 1.15, y0: 0.5, y1: 3.25, n: 2.8 },
    { z: -5.4, hw: 0.9, y0: 0.55, y1: 2.45 },
    { z: -8.4, hw: 0.55, y0: 0.6, y1: 1.65 },
    { z: -10.4, hw: 0.35, y0: 0.75, y1: 1.25, n: 2.4 },
  ], 48), M.body);
  car.add(body);

  // sidepods (with undercut) — mirrored
  for (const s of [1, -1]) {
    const pod = new THREE.Mesh(loft([
      { z: 3.4, cx: s * 2.25, hw: 0.95, y0: 0.6, y1: 1.95, n: 3.6 },
      { z: 2.2, cx: s * 2.45, hw: 1.15, y0: 0.55, y1: 2.15, n: 3.6 },
      { z: -0.8, cx: s * 2.35, hw: 1.1, y0: 0.55, y1: 2.0, n: 3.4 },
      { z: -3.8, cx: s * 1.85, hw: 0.8, y0: 0.55, y1: 1.55, n: 3 },
      { z: -6.6, cx: s * 1.05, hw: 0.42, y0: 0.6, y1: 1.05, n: 2.6 },
    ], 32), M.body);
    car.add(pod);
    const inlet = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 1.0), M.dark);
    inlet.position.set(s * 2.3, 1.45, 3.42); car.add(inlet);
    // mirror
    car.add(rod([s * 1.2, 2.5, 3.6], [s * 1.95, 2.95, 3.4], 0.05, M.carbon));
    const mir = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.32, 0.22), M.body);
    mir.position.set(s * 2.15, 2.98, 3.35); car.add(mir);
  }

  // engine cover fin
  const fin = new THREE.Mesh(plate([[-0.8, 3.4], [-8.6, 1.9], [-9.4, 1.9], [-9.4, 1.5], [-2, 3.0]], 0.07), M.body);
  fin.rotation.y = -Math.PI / 2; fin.position.x = 0; car.add(fin);

  // cockpit opening + helmet + airbox intake + camera
  const cockpit = new THREE.Mesh(new THREE.SphereGeometry(1, 24, 12), M.dark);
  cockpit.scale.set(0.95, 0.25, 1.6); cockpit.position.set(0, 2.82, 1.7); car.add(cockpit);
  const helmet = new THREE.Mesh(new THREE.SphereGeometry(0.56, 24, 16), M.accent);
  helmet.position.set(0, 3.05, 1.05); car.add(helmet);
  const visor = new THREE.Mesh(new THREE.SphereGeometry(0.575, 24, 8, -0.9, 1.8, 1.25, 0.45), M.visor);
  visor.position.copy(helmet.position); car.add(visor);
  const intake = new THREE.Mesh(new THREE.CircleGeometry(0.42, 20), M.dark);
  intake.scale.set(1, 0.75, 1); intake.position.set(0, 3.28, -0.45); car.add(intake);
  const tcam = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.18, 0.35), M.carbon);
  tcam.position.set(0, 3.85, -0.75); car.add(tcam);
  car.add(rod([0, 3.55, -0.75], [0, 3.82, -0.75], 0.07, M.carbon));

  // halo
  const haloCurve = new THREE.CatmullRomCurve3([
    new THREE.Vector3(-1.25, 2.75, -0.1), new THREE.Vector3(-1.2, 3.45, 0.8), new THREE.Vector3(-0.85, 3.7, 2.1),
    new THREE.Vector3(0, 3.78, 2.75), new THREE.Vector3(0.85, 3.7, 2.1), new THREE.Vector3(1.2, 3.45, 0.8),
    new THREE.Vector3(1.25, 2.75, -0.1),
  ]);
  car.add(new THREE.Mesh(new THREE.TubeGeometry(haloCurve, 64, 0.13, 10), M.carbon));
  car.add(rod([0, 3.74, 2.75], [0, 2.5, 3.9], 0.12, M.carbon));

  // wheels
  const tyreProfile = (R, W) => {
    const p = [], r0 = R * 0.66, rr = W * 0.22;
    p.push(new THREE.Vector2(r0, -W / 2));
    for (let i = 0; i <= 8; i++) { const a = -Math.PI / 2 + (i / 8) * (Math.PI / 2); p.push(new THREE.Vector2(R - rr + Math.cos(a) * rr, -W / 2 + rr + Math.sin(a) * rr)); }
    for (let i = 0; i <= 8; i++) { const a = (i / 8) * (Math.PI / 2); p.push(new THREE.Vector2(R - rr + Math.cos(a) * rr, W / 2 - rr + Math.sin(a) * rr)); }
    p.push(new THREE.Vector2(r0, W / 2));
    return p;
  };
  const wheels = [];
  const mkWheel = (R, W) => {
    const w = new THREE.Group();
    const tyre = new THREE.Mesh(new THREE.LatheGeometry(tyreProfile(R, W), 48), M.rubber);
    tyre.rotation.z = Math.PI / 2; w.add(tyre);
    for (const side of [1, -1]) {
      const band = new THREE.Mesh(new THREE.RingGeometry(R * 0.8, R * 0.845, 48), M.tyreBand);
      band.rotation.y = side * Math.PI / 2; band.position.x = side * (W / 2 + 0.005); w.add(band);
      const cover = new THREE.Mesh(new THREE.CircleGeometry(R * 0.66, 40), M.rim);
      cover.rotation.y = side * Math.PI / 2; cover.position.x = side * (W / 2 - 0.08); w.add(cover);
      const hub = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.22, 0.12, 16), M.hub);
      hub.rotation.z = Math.PI / 2; hub.position.x = side * (W / 2 - 0.02); w.add(hub);
      for (let k = 0; k < 5; k++) {
        const sp = new THREE.Mesh(new THREE.BoxGeometry(0.04, R * 0.5, 0.16), M.dark);
        sp.position.x = side * (W / 2 - 0.06); sp.rotation.x = (k / 5) * Math.PI * 2;
        sp.translateY(R * 0.36); w.add(sp);
      }
    }
    wheels.push(w);
    return w;
  };
  const FR = 1.72, RR = 1.78;
  const wheelPos = [[3.95, FR, 6.7, FR, 1.25], [-3.95, FR, 6.7, FR, 1.25], [3.85, RR, -7.4, RR, 1.62], [-3.85, RR, -7.4, RR, 1.62]];
  for (const [x, y, z, R, W] of wheelPos) {
    const w = mkWheel(R, W); w.position.set(x, y, z); car.add(w);
    const s = Math.sign(x), inner = x - s * W / 2;
    const bodyX = s * (z > 0 ? 0.9 : 1.0);
    car.add(rod([bodyX, 1.0, z + 0.9], [inner, y - 0.35, z], 0.06, M.carbon));
    car.add(rod([bodyX, 1.0, z - 0.9], [inner, y - 0.35, z], 0.06, M.carbon));
    car.add(rod([bodyX, 2.0, z + 0.7], [inner, y + 0.45, z], 0.06, M.carbon));
    car.add(rod([bodyX, 2.0, z - 0.7], [inner, y + 0.45, z], 0.06, M.carbon));
  }

  // front wing: main plane + two flaps per side + endplates
  const fw = new THREE.Group();
  const main = new THREE.Mesh(airfoil(9.6, 1.5, 0.1, 0.05), M.wing); main.position.set(0, 0.55, 11.6); fw.add(main);
  for (const s of [1, -1]) {
    const f1 = new THREE.Mesh(airfoil(3.5, 1.0, 0.09), M.wing); f1.position.set(s * 2.9, 0.82, 10.35); f1.rotation.x = -0.32; fw.add(f1);
    const f2 = new THREE.Mesh(airfoil(3.2, 0.8, 0.09), M.accent); f2.position.set(s * 3.05, 1.12, 9.65); f2.rotation.x = -0.6; fw.add(f2);
    const ep = new THREE.Mesh(plate([[11.8, 0.45], [9.2, 0.45], [9.0, 1.55], [10.2, 1.5], [11.8, 0.9]], 0.07), M.wing);
    ep.rotation.y = -Math.PI / 2; ep.position.x = s * 4.8; fw.add(ep);
  }
  fw.add(rod([0.35, 1.1, 10.4], [0.35, 0.6, 10.9], 0.06, M.carbon));
  fw.add(rod([-0.35, 1.1, 10.4], [-0.35, 0.6, 10.9], 0.06, M.carbon));
  car.add(fw);

  // rear wing
  const rw = new THREE.Group();
  const rMain = new THREE.Mesh(airfoil(7.3, 1.7, 0.11, 0.08), M.wing); rMain.position.set(0, 4.15, -8.1); rMain.rotation.x = 0.12; rw.add(rMain);
  const rFlap = new THREE.Mesh(airfoil(7.3, 1.0, 0.1), M.wing); rFlap.position.set(0, 4.75, -9.55); rFlap.rotation.x = -0.45; rw.add(rFlap);
  const beam = new THREE.Mesh(airfoil(5.4, 0.9, 0.12), M.wing); beam.position.set(0, 2.05, -9.0); rw.add(beam);
  for (const s of [1, -1]) {
    const ep = new THREE.Mesh(plate([[-7.7, 4.1], [-7.9, 5.2], [-10.3, 5.3], [-10.3, 2.4], [-9.0, 1.6], [-8.4, 3.4]], 0.08), M.wing);
    ep.rotation.y = -Math.PI / 2; ep.position.x = s * 3.7; rw.add(ep);
    const stripe = new THREE.Mesh(new THREE.BoxGeometry(0.02, 0.09, 2.4), M.accent);
    stripe.position.set(s * 3.75, 5.05, -9.05); rw.add(stripe);
  }
  rw.add(rod([0, 1.6, -8.3], [0, 4.0, -8.6], 0.1, M.carbon));
  car.add(rw);

  // diffuser strakes + rain light
  for (let k = -3; k <= 3; k++) {
    const st = new THREE.Mesh(plate([[-9.8, 0.4], [-11.2, 1.2], [-11.2, 0.4]], 0.05), M.carbon);
    st.rotation.y = -Math.PI / 2; st.position.x = k * 0.75; car.add(st);
  }
  const rain = new THREE.Mesh(new THREE.BoxGeometry(0.55, 0.42, 0.08), M.rainLight);
  rain.position.set(0, 1.45, -10.55); car.add(rain);

  car.traverse(o => { if (o.isMesh) { o.castShadow = true; } });
  car.userData.wheels = wheels;
  return car;
}

// ---------- base ----------
function buildBase(M) {
  const g = new THREE.Group();
  const r = BASE_R, h = BASE_H, e = 0.45;
  const prof = [new THREE.Vector2(0, 0), new THREE.Vector2(r - 0.25, 0), new THREE.Vector2(r, 0.25), new THREE.Vector2(r, h - e)];
  for (let i = 1; i <= 8; i++) { const a = (i / 8) * Math.PI / 2; prof.push(new THREE.Vector2(r - e + Math.cos(a) * e, h - e + Math.sin(a) * e)); }
  prof.push(new THREE.Vector2(0, h));
  const shell = new THREE.Mesh(new THREE.LatheGeometry(prof, 96),
    new THREE.MeshPhysicalMaterial({ color: '#040405', roughness: 0.78, metalness: 0.6, clearcoat: 0, envMapIntensity: 0.06 }));
  shell.receiveShadow = true; g.add(shell);

  const ledMat = new THREE.MeshStandardMaterial({ color: '#ff1a1f', emissive: '#ff1a1f', emissiveIntensity: 5 });
  const ring = new THREE.Mesh(new THREE.TorusGeometry(r + 0.01, 0.065, 8, 160), ledMat);
  ring.rotation.x = Math.PI / 2; ring.position.y = 0.62; g.add(ring);
  // soft halo around the LED strip (stands in for bloom, cheaper and cleaner)
  const haloMats = [];
  for (const [tube, op] of [[0.22, 0.35], [0.55, 0.14], [1.1, 0.06]]) {
    const m = new THREE.MeshBasicMaterial({ color: '#ff2020', transparent: true, opacity: op, blending: THREE.AdditiveBlending, depthWrite: false });
    const h2 = new THREE.Mesh(new THREE.TorusGeometry(r + 0.02, tube, 12, 160), m);
    h2.rotation.x = Math.PI / 2; h2.position.y = 0.62; g.add(h2); haloMats.push([m, op]);
  }

  const glowTex = canvasTex(512, 512, (c, w) => {
    const grd = c.createRadialGradient(w / 2, w / 2, 0, w / 2, w / 2, w / 2);
    grd.addColorStop(0, 'rgba(255,40,40,1)'); grd.addColorStop(0.35, 'rgba(230,10,20,0.75)');
    grd.addColorStop(0.75, 'rgba(120,0,8,0.18)'); grd.addColorStop(1, 'rgba(0,0,0,0)');
    c.fillStyle = grd; c.fillRect(0, 0, w, w);
  });
  const topGlow = new THREE.Mesh(new THREE.CircleGeometry(r - 0.6, 64),
    new THREE.MeshBasicMaterial({ map: glowTex, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false }));
  topGlow.rotation.x = -Math.PI / 2; topGlow.position.y = h + 0.02; topGlow.scale.set(0.8, 0.8, 1); g.add(topGlow);

  // floor glow + contact shadow
  const floorGlow = new THREE.Mesh(new THREE.CircleGeometry(r * 2.4, 64),
    new THREE.MeshBasicMaterial({ map: glowTex, transparent: true, opacity: 0.55, blending: THREE.AdditiveBlending, depthWrite: false }));
  floorGlow.rotation.x = -Math.PI / 2; floorGlow.position.y = 0.01; g.add(floorGlow);

  const light = new THREE.PointLight('#ff2a2a', 60, 30, 1.6); light.position.set(0, h + 0.6, 0); g.add(light);
  g.userData = { ledMat, topGlow, floorGlow, light, glowTex, haloMats };
  return g;
}

// ---------- stage ----------
export function createStage(el, opts = {}) {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
  } catch (e) { el.classList.add('is-fallback'); return null; }
  const bg = new THREE.Color(opts.background || '#0a0b0d');
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 0.95;
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.domElement.className = 'stage-canvas';
  el.prepend(renderer.domElement);

  const scene = new THREE.Scene(); scene.background = bg;
  scene.fog = new THREE.Fog(bg, 70, 140);
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(renderer), 0.04).texture;

  const camera = new THREE.PerspectiveCamera(30, 1, 0.5, 400);
  const HOME = new THREE.Vector3(31, 12.5, 39);
  camera.position.copy(HOME);

  const M = makeMaterials();
  Object.values(M).forEach(m => { m.envMapIntensity = 0.55; });
  const base = buildBase(M); scene.add(base);
  const car = buildCar(M);
  const pivot = new THREE.Group(); pivot.add(car); scene.add(pivot);
  car.scale.setScalar(0.92);

  // floor
  const floor = new THREE.Mesh(new THREE.CircleGeometry(160, 64),
    new THREE.MeshStandardMaterial({ color: '#0c0d0f', roughness: 0.92, metalness: 0, envMapIntensity: 0.05 }));
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; scene.add(floor);

  // lights
  const key = new THREE.SpotLight('#ffffff', 260, 120, 0.32, 0.8, 1.4);
  key.position.set(10, 38, 14); key.target.position.set(0, 7, 0); scene.add(key.target); key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.bias = -0.0004;
  scene.add(key);
  const rim = new THREE.DirectionalLight('#c9d4ff', 0.7); rim.position.set(-25, 12, -30); scene.add(rim);
  const fill = new THREE.HemisphereLight('#d8dcff', '#120406', 0.35); scene.add(fill);
  const front = new THREE.DirectionalLight('#ffffff', 1.1); front.position.set(20, 14, 26); scene.add(front);

  // air-gap measurement guide
  const gapGroup = new THREE.Group();
  const lineMat = new THREE.LineDashedMaterial({ color: '#ffffff', dashSize: 0.25, gapSize: 0.18, transparent: true, opacity: 0.85 });
  const gapGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 1, 0)]);
  const gapLine = new THREE.Line(gapGeo, lineMat); gapLine.computeLineDistances(); gapGroup.add(gapLine);
  gapGroup.position.set(BASE_R - 0.4, BASE_H, 0); gapGroup.visible = false; scene.add(gapGroup);

  let viewMoved = false;
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(0, 5, 0);
  controls.enableDamping = true; controls.dampingFactor = 0.08; controls.enablePan = false;
  controls.minDistance = 20; controls.maxDistance = 80;
  controls.minPolarAngle = 0.35; controls.maxPolarAngle = 1.5;
  controls.rotateSpeed = 0.7; controls.zoomSpeed = 0.6;
  controls.enableZoom = opts.zoom !== false;
  controls.update();

  // bloom
  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(256, 256), 0.8, 0.45, 1.7);
  if (opts.bloom === true) composer.addPass(bloom);
  composer.addPass(new OutputPass());

  const state = {
    spinning: !reduce, power: true, livery: opts.livery || 'carbon', showGap: false,
    lift: GAP, liftV: 0, spinSpeed: 0.45, spinCur: reduce ? 0 : 0.45,
  };

  function setLivery(name) {
    const l = LIVERIES[name] || LIVERIES.carbon; state.livery = name;
    if (M.body.map) M.body.map.dispose();
    M.body.map = liveryTexture(l); M.body.color.set('#ffffff'); M.body.needsUpdate = true;
    M.body.metalness = name === 'arctic' ? 0.15 : l.matte ? 0.1 : 0.35;
    M.body.roughness = l.matte ? 0.55 : 0.22; M.body.clearcoat = l.matte ? 0.15 : 1;
    M.accent.color.set(l.accent); M.tyreBand.color.set(l.tyre); M.wing.color.set(l.wing);
    el.dispatchEvent(new CustomEvent('stage:livery', { detail: name }));
  }
  setLivery(state.livery);

  function setPower(on) {
    state.power = on;
    const u = base.userData;
    u.ledMat.emissiveIntensity = on ? 5 : 0.0; u.ledMat.color.set(on ? '#ff1a1f' : '#2a0b0c');
    u.topGlow.visible = on; u.floorGlow.visible = on; u.haloMats.forEach(([m, op]) => { m.opacity = on ? op : 0; }); u.light.intensity = on ? 60 : 0;
    el.classList.toggle('is-off', !on);
    el.dispatchEvent(new CustomEvent('stage:power', { detail: on }));
  }
  function setSpin(on) { state.spinning = on; el.dispatchEvent(new CustomEvent('stage:spin', { detail: on })); }
  function setGap(on) { state.showGap = on; gapGroup.visible = on; el.classList.toggle('show-gap', on); }
  function resetView() { camera.position.copy(HOME); viewMoved = false; resize(); controls.update(); }

  // resize
  function resize() {
    const w = el.clientWidth, h = el.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false); composer.setSize(w, h);
    camera.aspect = w / h;
    const narrow = w / h < 0.9;
    camera.fov = narrow ? 44 : 30;
    if (!viewMoved) { controls.target.y = narrow ? 2 : 4.6; controls.update(); }
    camera.updateProjectionMatrix();
  }
  new ResizeObserver(resize).observe(el); resize();

  // visibility-aware loop
  let visible = true, raf = 0;
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; if (visible && !raf) loop(); }, { threshold: 0.01 }).observe(el);
  document.addEventListener('visibilitychange', () => { if (!document.hidden && visible && !raf) loop(); });

  const clock = new THREE.Clock();
  const labelEl = el.querySelector('[data-gap-label]');
  const tmp = new THREE.Vector3();
  let t = 0;
  function loop() {
    raf = 0;
    if (!visible || document.hidden) return;
    const dt = Math.min(clock.getDelta(), 0.05); t += dt;
    // levitation: spring toward target lift
    const restLift = 0.02; // resting on the base when power is off
    const target = state.power ? GAP + Math.sin(t * 1.7) * (reduce ? 0 : 0.14) : restLift;
    const k = state.power ? 22 : 40, c = state.power ? 5.5 : 9;
    state.liftV += ((target - state.lift) * k - state.liftV * c) * dt;
    state.lift += state.liftV * dt;
    if (!state.power && state.lift < restLift) { state.lift = restLift; state.liftV = 0; }
    pivot.position.y = BASE_H + state.lift - 0.42 * 0.92 + 0.03;
    // spin eases in and out; stops when power is off
    const want = state.spinning && state.power ? state.spinSpeed : 0;
    state.spinCur += (want - state.spinCur) * Math.min(1, dt * 2.2);
    pivot.rotation.y += state.spinCur * dt;
    // subtle wobble so it reads as floating, not fixed
    pivot.rotation.z = state.power && !reduce ? Math.sin(t * 1.1) * 0.012 : 0;
    pivot.rotation.x = state.power && !reduce ? Math.cos(t * 0.9) * 0.01 : 0;

    if (state.showGap) {
      const bottom = pivot.position.y + 0.42 * 0.92;
      const gapH = Math.max(0.01, bottom - BASE_H);
      gapLine.scale.y = gapH; gapLine.computeLineDistances();
      if (labelEl) {
        tmp.set(BASE_R - 0.4, BASE_H + gapH / 2, 0).project(camera);
        labelEl.style.transform = `translate(${(tmp.x * 0.5 + 0.5) * el.clientWidth}px, ${(-tmp.y * 0.5 + 0.5) * el.clientHeight}px)`;
      }
    }
    controls.update();
    composer.render();
    raf = requestAnimationFrame(loop);
  }
  loop();

  // a nudge so first-time visitors see it can be dragged
  if (!reduce && opts.hint !== false) {
    let s = 0; const az0 = controls.getAzimuthalAngle();
    const nudge = () => { s += 0.02; if (s > 1) return; const k = Math.sin(s * Math.PI) * 0.35;
      const off = camera.position.clone().sub(controls.target); const sph = new THREE.Spherical().setFromVector3(off);
      sph.theta = az0 + k; camera.position.copy(controls.target).add(new THREE.Vector3().setFromSpherical(sph)); requestAnimationFrame(nudge); };
    setTimeout(nudge, 1200);
    controls.addEventListener('start', () => { s = 2; viewMoved = true; el.classList.add('was-dragged'); });
  }

  el.classList.add('is-ready');
  return { setLivery, setPower, setSpin, setGap, resetView, state };
}

// Auto-wire every [data-maglev-stage] element on the page.
function wire(el) {
  const api = createStage(el, { livery: el.dataset.livery, zoom: el.dataset.zoom !== 'false', bloom: el.dataset.bloom === 'true' });
  if (!api) return;
  el._stage = api;
  el.querySelectorAll('[data-stage-livery]').forEach(b => b.addEventListener('click', () => api.setLivery(b.dataset.stageLivery)));
  const sync = () => {
    el.querySelectorAll('[data-stage-livery]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.stageLivery === api.state.livery)));
    el.querySelectorAll('[data-stage-toggle="spin"]').forEach(b => b.setAttribute('aria-pressed', String(api.state.spinning)));
    el.querySelectorAll('[data-stage-toggle="power"]').forEach(b => b.setAttribute('aria-pressed', String(api.state.power)));
    el.querySelectorAll('[data-stage-toggle="gap"]').forEach(b => b.setAttribute('aria-pressed', String(api.state.showGap)));
  };
  el.querySelectorAll('[data-stage-toggle]').forEach(b => b.addEventListener('click', () => {
    const k = b.dataset.stageToggle;
    if (k === 'spin') api.setSpin(!api.state.spinning);
    if (k === 'power') api.setPower(!api.state.power);
    if (k === 'gap') api.setGap(!api.state.showGap);
    if (k === 'reset') api.resetView();
    sync();
  }));
  ['stage:livery', 'stage:spin', 'stage:power'].forEach(ev => el.addEventListener(ev, sync));
  sync();
}
function init() { document.querySelectorAll('[data-maglev-stage]').forEach(el => { if (!el._stage) wire(el); }); }
window.MaglevStage = { init, createStage, LIVERIES };
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
