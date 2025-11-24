import random

def generate_star(id):
    x = random.randint(0, 1000)
    y = random.randint(0, 200)
    scale = random.uniform(0.5, 1.5)
    opacity_dur = random.uniform(2, 5)
    float_dur = random.uniform(4, 8)
    delay = random.uniform(0, 5)
    
    # Colors: Cyan, Deep Sky Blue, Dodger Blue
    colors = ["#00FFFF", "#00BFFF", "#1E90FF"]
    color = random.choice(colors)
    
    # 4-pointed star path (curved)
    # Center 0,0. Radius 10.
    path = "M0,-10 Q0,0 10,0 Q0,0 0,10 Q0,0 -10,0 Q0,0 0,-10 Z"
    
    return f"""
    <g transform="translate({x}, {y}) scale({scale})">
        <path d="{path}" fill="{color}" opacity="0.8">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="{opacity_dur}s" begin="{delay}s" repeatCount="indefinite" />
            <animateTransform attributeName="transform" type="translate" values="0,0; 0,-15; 0,0" dur="{float_dur}s" begin="{delay}s" repeatCount="indefinite" additive="sum"/>
            <animateTransform attributeName="transform" type="scale" values="1;1.2;1" dur="{opacity_dur}s" begin="{delay}s" repeatCount="indefinite" additive="sum"/>
        </path>
    </g>"""

svg_content = f"""<svg width="1000" height="200" viewBox="0 0 1000 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background (Transparent) -->
  <rect width="100%" height="100%" fill="transparent"/>
  
  <!-- Stars Container with Glow -->
  <g filter="url(#glow)">
"""

# Generate 60 stars
for i in range(60):
    svg_content += generate_star(i)

svg_content += """
  </g>
  
  <!-- Constellation Lines (Subtle background connection) -->
  <path d="M100,50 L300,150 L500,80 L700,120 L900,60" stroke="#00BFFF" stroke-width="1" opacity="0.15" fill="none"/>
</svg>"""

with open("assets/header.svg", "w") as f:
    f.write(svg_content)

print("Header SVG generated successfully!")
