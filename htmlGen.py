import os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>OneShot Resource Archive</title>
    <style>
        :root {{
            --bg: #0f0a14;
            --panel: rgba(30, 20, 40, 0.7);
            --pink: #ff79c6;
            --purple: #bd93f9;
            --text: #f8f8f2;
            --border: rgba(255, 121, 198, 0.2);
        }}
        body {{
            background-color: var(--bg);
            background-image: radial-gradient(circle at 20% 30%, rgba(189, 147, 249, 0.1) 0%, transparent 40%);
            color: var(--text);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 2rem;
            margin: 0;
        }}
        header {{ border-bottom: 1px solid var(--pink); margin-bottom: 3rem; padding-bottom: 1rem; }}
        h1 {{ color: var(--pink); text-transform: uppercase; letter-spacing: 0.3rem; margin: 0; }}
        
        .character-block {{ margin-bottom: 4rem; }}
        .character-header {{
            color: var(--purple);
            font-size: 1.4rem;
            border-left: 4px solid var(--purple);
            padding-left: 15px;
            margin-bottom: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        .emote-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 1.5rem;
        }}
        .emote-card {{
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 12px;
            text-align: center;
            backdrop-filter: blur(10px);
            transition: transform 0.2s, border-color 0.2s;
        }}
        .emote-card:hover {{ 
            border-color: var(--pink); 
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }}
        .emote-card img {{
            width: 96px; 
            height: 96px;
            image-rendering: pixelated;
            display: block;
            margin: 0 auto;
        }}
        .emote-name {{ 
            font-size: 0.7rem; 
            display: block; 
            margin-top: 8px; 
            opacity: 0.8; 
            word-wrap: break-word;
            font-family: monospace;
        }}
    </style>
</head>
<body>
    <header><h1>OneShot Resource Archive</h1></header>
    <main>
{content}
    </main>
</body>
</html>
"""

def generate():
    content = ""
    for root, dirs, files in sorted(os.walk('.')):
        if root == '.' or root.startswith('./.'): continue
        
        category = os.path.basename(root)
        images = [f for f in files if f.lower().endswith('.png')]
        
        if not images: continue
        
        content += f'        <section class="character-block">\n'
        content += f'            <div class="character-header">{category}</div>\n'
        content += f'            <div class="emote-grid">\n'
        
        for img in sorted(images):
            img_path = f"{category}/{img}"
            name = img.replace('.png', '')
            content += f'                <div class="emote-card">\n'
            content += f'                    <img src="{img_path}">\n'
            content += f'                    <span class="emote-name">{name}</span>\n'
            content += f'                </div>\n'
        
        content += f'            </div>\n'
        content += f'        </section>\n'

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(HTML_TEMPLATE.format(content=content))
    print("✨ index.html fixed and generated!")

if __name__ == "__main__":
    generate()