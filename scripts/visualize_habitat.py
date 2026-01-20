#!/usr/bin/env python3
"""Visualize the habitat STEP file with openings highlighted.

Generates an HTML file with an interactive 3D viewer using three.js.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STEP = REPO_ROOT / "reference" / "Osterath_Habitat_1225 AF.step"
DEFAULT_OUTPUT = REPO_ROOT / "renders" / "habitat_viewer.html"


def load_step_to_stl(step_path: Path) -> bytes:
    """Load STEP file and convert to STL format."""
    import cadquery as cq
    from cadquery import importers
    import tempfile

    shape = importers.importStep(str(step_path))
    if isinstance(shape, cq.Workplane):
        wp = shape
    else:
        wp = cq.Workplane().add(shape)

    # Export to STL
    with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as f:
        temp_path = f.name

    cq.exporters.export(wp, temp_path, exportType="STL")

    with open(temp_path, "rb") as f:
        stl_data = f.read()

    Path(temp_path).unlink()
    return stl_data


def create_html_viewer(stl_data: bytes, openings: list) -> str:
    """Create an HTML file with three.js viewer."""
    import base64

    stl_base64 = base64.b64encode(stl_data).decode("utf-8")

    # Create markers for openings
    markers_js = json.dumps(openings, indent=2)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gimli2 Habitat Viewer</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
        #container {{ width: 100vw; height: 100vh; }}
        #info {{
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 15px;
            border-radius: 8px;
            font-size: 14px;
            max-width: 300px;
            z-index: 100;
        }}
        #info h2 {{ margin-bottom: 10px; font-size: 16px; }}
        #info ul {{ list-style: none; padding: 0; }}
        #info li {{ margin: 5px 0; padding: 5px; border-radius: 4px; cursor: pointer; }}
        #info li:hover {{ background: rgba(255,255,255,0.2); }}
        .window {{ border-left: 3px solid #4CAF50; padding-left: 8px; }}
        .door {{ border-left: 3px solid #2196F3; padding-left: 8px; }}
        .hatch {{ border-left: 3px solid #FF9800; padding-left: 8px; }}
        #controls {{
            position: absolute;
            bottom: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 10px;
            border-radius: 8px;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div id="container"></div>
    <div id="info">
        <h2>Gimli2 Habitat Openings</h2>
        <ul id="openings-list"></ul>
    </div>
    <div id="controls">
        <b>Controls:</b> Left-click drag to rotate | Right-click drag to pan | Scroll to zoom
    </div>

    <script type="importmap">
    {{
        "imports": {{
            "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
            "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/"
        }}
    }}
    </script>

    <script type="module">
        import * as THREE from 'three';
        import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
        import {{ STLLoader }} from 'three/addons/loaders/STLLoader.js';

        const openings = {markers_js};

        // Setup scene
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x1a1a2e);

        // Camera
        const camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 1, 100000);
        camera.position.set(8000, 5000, 8000);

        // Renderer
        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        document.getElementById('container').appendChild(renderer.domElement);

        // Controls
        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.target.set(0, 1200, 3000);

        // Lights
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
        scene.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
        directionalLight.position.set(5000, 10000, 5000);
        scene.add(directionalLight);

        const directionalLight2 = new THREE.DirectionalLight(0xffffff, 0.4);
        directionalLight2.position.set(-5000, 5000, -5000);
        scene.add(directionalLight2);

        // Load STL model
        const stlData = "{stl_base64}";
        const stlBlob = new Blob([Uint8Array.from(atob(stlData), c => c.charCodeAt(0))], {{ type: 'application/octet-stream' }});
        const stlUrl = URL.createObjectURL(stlBlob);

        const loader = new STLLoader();
        loader.load(stlUrl, (geometry) => {{
            const material = new THREE.MeshPhongMaterial({{
                color: 0x8899aa,
                transparent: true,
                opacity: 0.85,
                side: THREE.DoubleSide
            }});
            const mesh = new THREE.Mesh(geometry, material);
            scene.add(mesh);
        }});

        // Add opening markers
        const markerGroup = new THREE.Group();
        scene.add(markerGroup);

        const colors = {{
            window: 0x4CAF50,
            door: 0x2196F3,
            hatch: 0xFF9800
        }};

        openings.forEach((opening, index) => {{
            if (!opening.center_mm) return;

            const [x, y, z] = opening.center_mm;
            const color = colors[opening.kind] || 0xffffff;

            // Create sphere marker
            const geometry = new THREE.SphereGeometry(50, 16, 16);
            const material = new THREE.MeshBasicMaterial({{ color: color }});
            const sphere = new THREE.Mesh(geometry, material);
            sphere.position.set(x, y, z);
            markerGroup.add(sphere);

            // Create ring around marker
            const ringGeometry = new THREE.RingGeometry(60, 80, 32);
            const ringMaterial = new THREE.MeshBasicMaterial({{ color: color, side: THREE.DoubleSide }});
            const ring = new THREE.Mesh(ringGeometry, ringMaterial);
            ring.position.set(x, y, z);
            ring.lookAt(camera.position);
            markerGroup.add(ring);

            // Add label sprite
            const canvas = document.createElement('canvas');
            canvas.width = 256;
            canvas.height = 64;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#' + color.toString(16).padStart(6, '0');
            ctx.fillRect(0, 0, 256, 64);
            ctx.fillStyle = 'white';
            ctx.font = 'bold 24px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(opening.id, 128, 40);

            const texture = new THREE.CanvasTexture(canvas);
            const spriteMaterial = new THREE.SpriteMaterial({{ map: texture }});
            const sprite = new THREE.Sprite(spriteMaterial);
            sprite.position.set(x, y + 150, z);
            sprite.scale.set(300, 75, 1);
            markerGroup.add(sprite);
        }});

        // Populate openings list
        const listEl = document.getElementById('openings-list');
        openings.forEach((opening) => {{
            const li = document.createElement('li');
            li.className = opening.kind;
            li.innerHTML = `<b>${{opening.id}}</b> - ${{opening.model}} (${{opening.kind}})<br>
                           <small>${{opening.location}}</small>`;
            li.onclick = () => {{
                if (opening.center_mm) {{
                    const [x, y, z] = opening.center_mm;
                    controls.target.set(x, y, z);
                    camera.position.set(x + 3000, y + 2000, z + 3000);
                }}
            }};
            listEl.appendChild(li);
        }});

        // Animation loop
        function animate() {{
            requestAnimationFrame(animate);
            controls.update();

            // Make rings face camera
            markerGroup.children.forEach(child => {{
                if (child.geometry && child.geometry.type === 'RingGeometry') {{
                    child.lookAt(camera.position);
                }}
            }});

            renderer.render(scene, camera);
        }}
        animate();

        // Handle resize
        window.addEventListener('resize', () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});
    </script>
</body>
</html>'''
    return html


def load_openings_from_yaml(yaml_path: Path) -> list:
    """Load openings from habitat.yml."""
    import yaml

    with yaml_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    openings = []
    features = data.get("features", {})

    for win in features.get("windows", []):
        openings.append({
            "id": win.get("id"),
            "model": win.get("model"),
            "kind": "window",
            "location": win.get("location"),
            "center_mm": win.get("center_mm"),
        })

    for door in features.get("doors", []):
        openings.append({
            "id": door.get("id"),
            "model": door.get("model"),
            "kind": "door",
            "location": door.get("location"),
            "center_mm": door.get("center_mm"),
        })

    for hatch in features.get("hatches", []):
        openings.append({
            "id": hatch.get("id"),
            "model": hatch.get("model"),
            "kind": "hatch",
            "location": hatch.get("location"),
            "center_mm": hatch.get("center_mm"),
        })

    return openings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate an interactive 3D viewer for the habitat.",
    )
    parser.add_argument(
        "--step",
        type=Path,
        default=DEFAULT_STEP,
        help="Path to the STEP file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Path to output HTML file.",
    )
    parser.add_argument(
        "--habitat",
        type=Path,
        default=REPO_ROOT / "habitat.yml",
        help="Path to habitat.yml.",
    )
    args = parser.parse_args()

    print(f"Loading STEP file: {args.step}")
    stl_data = load_step_to_stl(args.step)
    print(f"  Converted to STL: {len(stl_data)} bytes")

    print(f"Loading openings from: {args.habitat}")
    openings = load_openings_from_yaml(args.habitat)
    print(f"  Found {len(openings)} openings")

    print(f"Generating HTML viewer...")
    html = create_html_viewer(stl_data, openings)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(f"  Saved to: {args.output}")
    print()
    print(f"Open in browser: file://{args.output.resolve()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
