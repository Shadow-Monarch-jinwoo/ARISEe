import os

base_dir = r"C:\Users\SAKSHAM JAISWAL\.gemini\antigravity\scratch\arise-landing-page"

pages = [
    {
        "filename": "training-grounds.html",
        "title": "[!] TRAINING GROUND",
        "text": "Access to advanced combat simulations<br>and skill development modules is currently<br>restricted. System optimization and<br>safety protocols are being updated.<br>Feature will be available soon."
    },
    {
        "filename": "dungeons.html",
        "title": "[!] DUNGEONS",
        "text": "Gateway access to specific dungeon<br>instances is currently restricted.<br>Feature will be available soon."
    },
    {
        "filename": "guilds.html",
        "title": "**[!] GUILDS**",
        "text": "Access to guild formation, management, and<br>collaborative features is currently restricted. Guild<br>registry protocols and community communication<br>channels are undergoing essential System updates.<br>Feature will be available soon."
    },
    {
        "filename": "skill-tree.html",
        "title": "[!] SKILL TREE",
        "text": "Advanced skill pathway analysis<br>is currently under computation.<br>Feature will be available soon."
    }
]

template = """<!DOCTYPE html><html class="dark" lang="en" style=""><head>
<meta charset="utf-8">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<title>ARISE - {page_title}</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Geist:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<script id="tailwind-config">
tailwind.config = {{
    darkMode: "class",
    theme: {{
        extend: {{
            "colors": {{
                "primary-fixed": "#00E5FF",
                "background": "#020713",
            }},
            "fontFamily": {{
                "body-base": ["Inter"],
                "display-lg": ["Geist"],
                "label-caps": ["JetBrains Mono"],
                "headline-md": ["Geist"],
                "code-sm": ["JetBrains Mono"],
                "display-lg-mobile": ["Geist"]
            }}
        }}
    }}
}}
</script>
<style>
    body {{
        background-color: #020713;
        background-image: radial-gradient(circle at center, #071a33 0%, #020713 100%);
        color: #e5e2e1;
        overflow-x: hidden;
        margin: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .glow-text {{
        text-shadow: 0 0 10px rgba(255,255,255,0.5), 0 0 20px rgba(255,255,255,0.3);
    }}
</style>
</head>
<body class="antialiased relative font-body-base">
    
    <div class="relative w-[1100px] h-[650px] max-w-[95vw] max-h-[90vh] flex items-center justify-center">
        <!-- Complex SVG Frame matching the image -->
        <svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 1100 650" preserveAspectRatio="none">
            <defs>
                <filter id="neon-blue" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="6" result="blur" />
                    <feMerge>
                        <feMergeNode in="blur" />
                        <feMergeNode in="SourceGraphic" />
                    </feMerge>
                </filter>
                <filter id="neon-cyan" x="-20%" y="-20%" width="140%" height="140%">
                    <feGaussianBlur stdDeviation="3" result="blur" />
                    <feMerge>
                        <feMergeNode in="blur" />
                        <feMergeNode in="SourceGraphic" />
                    </feMerge>
                </filter>
                <pattern id="tech-grid" width="40" height="40" patternUnits="userSpaceOnUse">
                    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0,229,255,0.03)" stroke-width="1"/>
                </pattern>
            </defs>
            
            <rect x="0" y="0" width="1100" height="650" fill="url(#tech-grid)" />
            
            <rect x="180" y="140" width="740" height="370" fill="rgba(0,10,25,0.4)" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" />
            
            <path d="M 120,80 L 980,80" stroke="#1b63ff" stroke-width="12" filter="url(#neon-blue)" opacity="0.8" />
            <path d="M 120,80 L 980,80" stroke="#00e5ff" stroke-width="4" filter="url(#neon-cyan)" />
            
            <path d="M 280,80 L 300,50 L 800,50 L 820,80" fill="none" stroke="#1b63ff" stroke-width="4" filter="url(#neon-blue)" opacity="0.6" />
            <path d="M 280,80 L 300,50 L 800,50 L 820,80" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#neon-cyan)" />

            <path d="M 120,570 L 980,570" stroke="#1b63ff" stroke-width="12" filter="url(#neon-blue)" opacity="0.8" />
            <path d="M 120,570 L 980,570" stroke="#00e5ff" stroke-width="4" filter="url(#neon-cyan)" />

            <path d="M 380,570 L 410,610 L 690,610 L 720,570" fill="none" stroke="#1b63ff" stroke-width="4" filter="url(#neon-blue)" opacity="0.6" />
            <path d="M 380,570 L 410,610 L 690,610 L 720,570" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#neon-cyan)" />

            <path d="M 120,80 L 80,120 L 80,250 L 100,270 L 100,380 L 80,400 L 80,530 L 120,570" fill="none" stroke="#1b63ff" stroke-width="6" filter="url(#neon-blue)" opacity="0.7" />
            <path d="M 120,80 L 80,120 L 80,250 L 100,270 L 100,380 L 80,400 L 80,530 L 120,570" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#neon-cyan)" />
            <path d="M 110,130 L 110,240 M 110,410 L 110,520" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#neon-cyan)" opacity="0.5" />

            <path d="M 980,80 L 1020,120 L 1020,250 L 1000,270 L 1000,380 L 1020,400 L 1020,530 L 980,570" fill="none" stroke="#1b63ff" stroke-width="6" filter="url(#neon-blue)" opacity="0.7" />
            <path d="M 980,80 L 1020,120 L 1020,250 L 1000,270 L 1000,380 L 1020,400 L 1020,530 L 980,570" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#neon-cyan)" />
            <path d="M 990,130 L 990,240 M 990,410 L 990,520" fill="none" stroke="#00e5ff" stroke-width="2" filter="url(#neon-cyan)" opacity="0.5" />
            
            <polygon points="120,80 150,80 120,110" fill="#00e5ff" filter="url(#neon-cyan)" opacity="0.8"/>
            <polygon points="980,80 950,80 980,110" fill="#00e5ff" filter="url(#neon-cyan)" opacity="0.8"/>
            <polygon points="120,570 150,570 120,540" fill="#00e5ff" filter="url(#neon-cyan)" opacity="0.8"/>
            <polygon points="980,570 950,570 980,540" fill="#00e5ff" filter="url(#neon-cyan)" opacity="0.8"/>
        </svg>

        <div class="absolute inset-0 flex flex-col items-center justify-center p-[40px]" style="top: 140px; left: 180px; width: 740px; height: 370px;">
            <div class="flex items-center space-x-4 mb-10 border border-white/20 bg-black/40 px-6 py-2 shadow-[0_4px_20px_rgba(0,0,0,0.5)]">
                <div class="w-8 h-8 rounded-full border-[1.5px] border-white/70 flex items-center justify-center bg-transparent">
                    <span class="text-white/90 font-bold text-lg leading-none">!</span>
                </div>
                <h1 class="font-display-lg-mobile text-2xl text-white tracking-[0.1em] glow-text">{page_title}</h1>
            </div>

            <p class="text-center font-body-base text-[20px] text-[#b0d8e0] leading-[1.8] max-w-xl tracking-wide opacity-90 text-shadow-sm">
                {page_text}
            </p>
        </div>

        <div class="absolute bottom-[44px] left-1/2 -translate-x-1/2 z-30">
            <a href="index.html" class="flex items-center space-x-2 border-[1.5px] border-white/30 px-6 py-[6px] bg-[#020b14]/80 hover:bg-[#00e5ff]/20 text-[#a2d8e4] hover:text-white font-label-caps uppercase tracking-widest transition-all shadow-[0_0_10px_rgba(0,229,255,0.2)]">
                <span class="material-symbols-outlined text-base">arrow_back</span>
                <span class="text-[13px]">BACK</span>
            </a>
        </div>
    </div>

</body>
</html>
"""

for page in pages:
    filepath = os.path.join(base_dir, page["filename"])
    content = template.format(page_title=page["title"], page_text=page["text"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {page['filename']}")
