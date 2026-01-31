#!/usr/bin/env python3
"""Visualize the habitat with internal systems (Alde, Tanks, Batteries).

Generates an HTML file with an interactive 3D viewer using three.js.
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
import tempfile
from pathlib import Path

try:
    import cadquery as cq
    from cadquery import importers
except ImportError:
    print("Error: cadquery not installed. Please install it (`pip install cadquery`)")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STEP = REPO_ROOT / "reference" / "Osterath_Habitat_1225 AF.step"
DEFAULT_OUTPUT = REPO_ROOT / "renders" / "systems_viewer.html"

# COLORS (Hex)
COLOR_SHELL = 0x8899aa
COLOR_ALDE = 0xff4444      # Red
COLOR_WATER = 0x4444ff     # Blue
COLOR_BATTERY = 0xffaa00   # Orange/Yellow
COLOR_ELEC = 0xaa44ff      # Purple
COLOR_ZONE = 0x44aa44      # Green (Translucent)


def create_box(width, depth, height, x, y, z):
    """Create a box at specific center coordinates."""
    # CadQuery box is centered. We want to place it at specific global coords.
    # We create it at origin then translate.
    # Note: Habitat coords: Y is "up" (0 is floor), Z is longitudinal, X is lateral.
    # CadQuery default: usually Z is up. We need to be careful with orientation.
    # Let's assume standard vehicle: Z=Fwd, Y=Up, X=Right.
    # CQ Workplane("XY") -> Z is up.
    # We should stick to the Viewer's coordinate system which comes from the STEP.
    # In the Viewer (three.js):
    #   The STEP file dictates the orientation.
    #   visualize_habitat.py sets: camera up?
    #   Let's assume the STEP is Z=Up, Y=Right, X=Back? Or something.
    #   WAIT. visualize_habitat.py: `camera.position.set(8000, 5000, 8000);`
    #   Let's check `habitat.yml`: up_axis: Z. forward_axis: Y.
    #   So in the STEP: Z is UP. Y is Forward. X is Side.
    #   BUT my previous reasoning said Y is Up.
    #   Let's double check `habitat.yml`:
    #   `up_axis: Z`
    #   `forward_axis: Y`
    #   So:
    #     Z = Height (0 to 2160)
    #     Y = Length (-2390 to 2390)
    #     X = Width (-1140 to 1140)
    
    #   RE-MAPPING My placement logic:
    #   Alde (Rear Driver):
    #     Old Logic (Y=Up): X=-840, Y=150, Z=-2090.
    #     New Logic (Z=Up): X=-840, Z=150, Y=-2090.
    
    #   Let's use this mapping:
    #   Global X = Width (-1140 Driver, +1140 Pass)
    #   Global Y = Length (-2390 Rear, +2390 Front)
    #   Global Z = Height (0 Floor, 2160 Ceiling)
    
    box = cq.Workplane("XY").box(width, depth, height)
    return box.translate((x, y, z))

def generate_systems_geometry() -> dict:
    """Generate STL data for all systems."""
    components = {}

    # Helper to export STL
    def export_stl(shape):
        with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as f:
            path = f.name
        cq.exporters.export(shape, path, exportType="STL")
        with open(path, "rb") as f:
            data = f.read()
        Path(path).unlink()
        return data

    # 1. ALDE HEATER
    # Driver Side Rear Garage Arm.
    # Size: 420(W) x 500(L) x 300(H)
    # Pos: Driver (-840), Rear (-2090), Floor (150 center)
    alde = create_box(420, 500, 300, -840, -2090, 150)
    components['alde'] = {
        'data': export_stl(alde),
        'color': COLOR_ALDE,
        'name': 'Alde Heater'
    }

    # 2. ELECTRICAL CORE (Victron)
    # Passenger Side Rear Garage Arm.
    # Size: 200(W) x 400(L) x 500(H)
    # Pos: Pass (+840), Rear (-2090), Floor/Wall (400 center -> 800 top)
    elec = create_box(200, 400, 500, 840, -2090, 400)
    components['electrical'] = {
        'data': export_stl(elec),
        'color': COLOR_ELEC,
        'name': 'Electrical Core'
    }

    # 3. WATER TANK 1 (Standard)
    # Passenger Side Kitchen Base.
    # Size: 500(W) x 1000(L) x 500(H) (250L approx)
    # Pos: Pass (+840), Mid-Rear (-1000?), Floor (250 center)
    tank1 = create_box(500, 1000, 500, 840, -1000, 250)
    components['tank1'] = {
        'data': export_stl(tank1),
        'color': COLOR_WATER,
        'name': 'Water Tank 1 (Standard)'
    }

    # 4. WATER TANK 2 (Low Profile)
    # Driver Side Dinette Base.
    # Size: 500(W) x 1250(L) x 400(H) (250L approx)
    # Pos: Driver (-840), Mid-Rear (-1000?), Floor (200 center)
    tank2 = create_box(500, 1250, 400, -840, -1000, 200)
    components['tank2'] = {
        'data': export_stl(tank2),
        'color': COLOR_WATER,
        'name': 'Water Tank 2 (Low Profile)'
    }

    # 5. BATTERIES (300kg)
    # Passenger Side Kitchen Base (Forward of tank?) or Stacked?
    # Let's put them forward of the tank in the kitchen line.
    # Size: 400(W) x 600(L) x 400(H)
    # Pos: Pass (+840), Mid-Front (-100?), Floor (200 center)
    batteries = create_box(400, 600, 400, 840, 0, 200)
    components['batteries'] = {
        'data': export_stl(batteries),
        'color': COLOR_BATTERY,
        'name': 'Battery Bank (300kg)'
    }

    # 6. EXTERNAL DIESEL (Reference)
    # Driver Side, Mid-Ship.
    # Size: 500(W) x 1500(L) x 600(H)
    # Pos: Driver (-1500 outside?), Mid (-500), Under (-300)
    # Just for balance ref.
    diesel = create_box(500, 1500, 600, -1140, -500, -300)
    components['diesel'] = {
        'data': export_stl(diesel),
        'color': 0x555555,
        'name': 'Diesel Tank (Ref)'
    }

    # 7. ZONES (Transparent Context)
    
    # Garage Zone (Rear 600mm)
    # 2280(W) x 600(D) x 2160(H)
    # Pos: 0, -2090, 1080 (center height)
    garage_zone = create_box(2280, 600, 2160, 0, -2090, 1080)
    components['zone_garage'] = {
        'data': export_stl(garage_zone),
        'color': COLOR_ZONE,
        'name': 'Zone: Garage'
    }

    # Kitchen Zone (Passenger)
    # 600(W) x 2300(L) x 2160(H)
    # Pos: +840 (1140-300), Z=0 (approx midship?), 1080
    # Actually Kitchen is "behind bathroom". Bathroom is ~1200 from front.
    # Front=+2390. Bathroom end=+1190.
    # Kitchen starts +1190, goes back 2300 to -1110.
    # Center Z = (+1190 - 1110) / 2 = +40.
    kitchen_zone = create_box(600, 2300, 2160, 840, 40, 1080)
    components['zone_kitchen'] = {
        'data': export_stl(kitchen_zone),
        'color': COLOR_ZONE,
        'name': 'Zone: Kitchen'
    }

    # Bathroom Zone (Driver Front)
    # 1200(L) x 1000(W)? 
    # Let's say it's Full Height. 
    # Driver Side (-1140 wall). Width ~900mm?
    # Length 1200 from front.
    # Pos: X = -1140 + 450 = -690.
    # Z = 2390 - 600 = 1790.
    bathroom_zone = create_box(900, 1200, 2160, -690, 1790, 1080)
    components['zone_bathroom'] = {
        'data': export_stl(bathroom_zone),
        'color': COLOR_ZONE,
        'name': 'Zone: Bathroom'
    }

    # Dinette Zone (Driver Side, opposite Kitchen)
    # Similar length to kitchen?
    # Starts behind driver seat (front) or behind bathroom?
    # Usually Dinette is behind Driver Seat (if no bathroom on that side?).
    # Wait, Bathroom is Driver Side?
    # ZONE-001-bathroom.yml: "Location: Driver side, front corner".
    # So Dinette is BEHIND Bathroom.
    # Z range: Same as Kitchen? (+40 center).
    # Width: ~1000mm? (Bench + Table + Bench).
    dinette_zone = create_box(1000, 2300, 2160, -640, 40, 1080)
    components['zone_dinette'] = {
        'data': export_stl(dinette_zone),
        'color': COLOR_ZONE,
        'name': 'Zone: Dinette'
    }

    return components

def create_multi_model_html(shell_stl: bytes, components: dict) -> str:
    """Create HTML with multiple STLs."""
    
    # Prepare shell
    shell_b64 = base64.b64encode(shell_stl).decode("utf-8")
    
    # Prepare components JS object
    comps_js = []
    for key, data in components.items():
        is_zone = 'Zone:' in data['name']
        opacity = 0.1 if is_zone else 1.0
        
        comps_js.append({
            'name': data['name'],
            'color': data['color'],
            'opacity': opacity,
            'data': base64.b64encode(data['data']).decode("utf-8")
        })

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gimli2 Habitat Systems</title>
    <style>
        body {{ margin: 0; overflow: hidden; background: #1a1a2e; color: white; font-family: sans-serif; }}
        #info {{ position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.8); padding: 15px; border-radius: 8px; }}
        .legend-item {{ display: flex; align-items: center; margin: 5px 0; }}
        .color-box {{ width: 20px; height: 20px; margin-right: 10px; border-radius: 4px; }}
    </style>
    <script type="importmap">
    {{
        "imports": {{
            "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
            "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
        }}
    }}
    </script>
</head>
<body>
    <div id="info">
        <h3>System Layout</h3>
        <div id="legend"></div>
        <p><small>Left-Click: Rotate | Right-Click: Pan | Scroll: Zoom</small></p>
    </div>
    <script type="module">
        import * as THREE from 'three';
        import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
        import {{ STLLoader }} from 'three/addons/loaders/STLLoader.js';

        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a2e);

        // Camera
        // Z is Up in our data, but THREE usually creates Y-up cameras. 
        // We will rotate the meshes or adjust camera.
        // Let's rely on OrbitControls auto-handling or just set Up axis.
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 100000);
        camera.up.set(0, 0, 1); // Z is UP
        camera.position.set(5000, -5000, 4000); // Isometric-ish view

        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.target.set(0, 0, 1000);

        // Lights
        const ambient = new THREE.AmbientLight(0xffffff, 0.4);
        scene.add(ambient);
        const sun = new THREE.DirectionalLight(0xffffff, 1);
        sun.position.set(2000, -2000, 5000);
        scene.add(sun);
        const fill = new THREE.DirectionalLight(0xffffff, 0.5);
        fill.position.set(-2000, 2000, 1000);
        scene.add(fill);

        // Loader
        const loader = new STLLoader();

        function loadModel(b64, color, name, opacity=1.0) {{
            const bin = atob(b64);
            const buf = new ArrayBuffer(bin.length);
            const view = new Uint8Array(buf);
            for (let i=0; i<bin.length; i++) view[i] = bin.charCodeAt(i);
            const blob = new Blob([buf], {{type: 'application/octet-stream'}});
            const url = URL.createObjectURL(blob);

            loader.load(url, (geo) => {{
                const mat = new THREE.MeshPhongMaterial({{
                    color: color, 
                    transparent: opacity < 1.0, 
                    opacity: opacity,
                    side: THREE.DoubleSide
                }});
                const mesh = new THREE.Mesh(geo, mat);
                scene.add(mesh);
                
                // Add to legend
                const legend = document.getElementById('legend');
                const item = document.createElement('div');
                item.className = 'legend-item';
                item.innerHTML = `<div class="color-box" style="background: #${{color.toString(16).padStart(6,'0')}}"></div> ${{name}}`;
                legend.appendChild(item);
            }});
        }}

        // Load Shell
        loadModel("{shell_b64}", {COLOR_SHELL}, "Habitat Shell", 0.3);

        // Load Components
        const components = {json.dumps(comps_js)};
        components.forEach(c => loadModel(c.data, c.color, c.name, c.opacity));

        function animate() {{
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }}
        animate();

        window.onresize = () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }};
    </script>
</body>
</html>'''
    return html

def main():
    print("Generating Habitat Systems Visualization...")
    import cadquery as cq # Verify import

    # 1. Load Shell
    print(f"Loading shell from {DEFAULT_STEP}...")
    shape = importers.importStep(str(DEFAULT_STEP))
    # Export Shell to STL
    with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as f:
        shell_path = f.name
    cq.exporters.export(shape, shell_path, exportType="STL")
    with open(shell_path, "rb") as f:
        shell_data = f.read()
    Path(shell_path).unlink()

    # 2. Generate Components
    print("Generating system components...")
    comps = generate_systems_geometry()

    # 3. Create HTML
    print("Building viewer...")
    html = create_multi_model_html(shell_data, comps)
    
    DEFAULT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_OUTPUT.write_text(html, encoding="utf-8")
    
    print(f"Success! Viewer saved to:")
    print(f"file://{DEFAULT_OUTPUT}")

if __name__ == "__main__":
    main()
