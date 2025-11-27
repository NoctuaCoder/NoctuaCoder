<div align="center">

# 🦉 Noctua Profile Collection

**Interactive HTML Profile Cards & Portfolio Pages with Celestial Theme**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](./LICENSE)

*A collection of stunning, interactive profile pages featuring glassmorphism, particle animations, and celestial aesthetics* ✨

[Live Demos](#-live-demos) • [Features](#-features) • [Pages](#-pages) • [Usage](#-usage)

</div>

---

## ✨ Features

### 🎨 Visual Excellence
- **Glassmorphism UI** - Frosted glass effects with blur and transparency
- **Celestial Theme** - Purple, pink, and cyan cosmic color palette
- **Particle Animations** - Interactive floating particles and stars
- **Smooth Transitions** - Buttery-smooth CSS animations
- **Responsive Design** - Perfect on all devices

### 🎭 Interactive Elements
- **Animated Owl Logo** - Mystical floating owl with glowing aura and blinking eyes
- **Aurora Background** - Dynamic northern lights animation
- **Custom Cursor** - Glowing cursor with particle trail
- **Hover Effects** - Engaging micro-interactions
- **Scroll Animations** - Elements animate as you scroll

### 💫 Multiple Designs
- **Profile Card** - Compact interactive profile with glassmorphism
- **Full Portfolio** - Complete portfolio page with projects and skills
- **Matrix Terminal** - Interactive browser terminal with command system
- **Aurora Page** - Stunning aurora borealis background effect
- **Orbit Animation** - Planetary orbit visualization

---

## 🌐 Live Demos

> **Main Portfolio**: [noctuacoder.github.io/NoctuaCoder/portfolio.html](https://noctuacoder.github.io/NoctuaCoder/portfolio.html)

### Available Pages

| Page | Description | Demo |
|------|-------------|------|
| **Noctua-profile.html** | Interactive profile card with animated owl | [View Demo](https://noctuacoder.github.io/NoctuaCoder/Noctua-profile.html) |
| **portfolio.html** | Full portfolio with projects showcase | [View Demo](https://noctuacoder.github.io/NoctuaCoder/portfolio.html) |
| **profile-card.html** | Glassmorphism profile card | [View Demo](https://noctuacoder.github.io/NoctuaCoder/profile-card.html) |
| **matrix-owl.html** | Interactive terminal experience | [View Demo](https://noctuacoder.github.io/NoctuaCoder/matrix-owl.html) |
| **aurora.html** | Aurora borealis background | [View Demo](https://noctuacoder.github.io/NoctuaCoder/aurora.html) |
| **orbit.html** | Planetary orbit animation | [View Demo](https://noctuacoder.github.io/NoctuaCoder/orbit.html) |

---

## 📸 Screenshots

````carousel
![Noctua Profile Card - Interactive profile with animated owl logo and glassmorphism effects](/home/alana/.gemini/antigravity/scratch/NoctuaCoder/assets/screenshot-placeholder.png)
<!-- slide -->
![Portfolio Page - Full portfolio showcase with celestial theme](/home/alana/.gemini/antigravity/scratch/NoctuaCoder/assets/screenshot-placeholder.png)
<!-- slide -->
![Matrix Terminal - Interactive browser terminal with command system](/home/alana/.gemini/antigravity/scratch/NoctuaCoder/assets/screenshot-placeholder.png)
````

> 📸 *Add actual screenshots to `/assets` directory and update paths above*

---

## 🚀 Usage

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/NoctuaCoder/Noctua-profile.html.git
cd Noctua-profile.html
```

2. **Open in browser**
```bash
# Simply open any HTML file in your browser
open Noctua-profile.html
# or
firefox portfolio.html
```

3. **Customize**
- Edit HTML files to update content
- Modify CSS variables for colors
- Add your own images to `/assets`

### Hosting on GitHub Pages

1. Push to GitHub repository
2. Go to repository Settings → Pages
3. Select branch (usually `main`) and root directory
4. Save and wait for deployment
5. Access at `https://yourusername.github.io/repository-name/`

---

## 📁 Pages Overview

### 🦉 Noctua-profile.html

The signature profile card featuring:
- Animated owl logo with mystical effects
- Glassmorphism card design
- Social media links
- Skills showcase
- Particle background

**Best for**: GitHub profile, portfolio landing page

### 🌟 portfolio.html

Complete portfolio page with:
- Hero section with custom cursor
- Projects gallery with live demos
- Skills and technologies
- Contact section
- Aurora background effect

**Best for**: Personal website, developer portfolio

### 💻 matrix-owl.html

Interactive terminal experience:
- Command-line interface
- Matrix rain animation
- Easter eggs and commands
- State management
- Typing sound effects

**Best for**: Creative portfolio, tech showcase

### 🌌 aurora.html

Pure visual experience:
- Northern lights animation
- Canvas-based rendering
- Smooth color transitions
- Minimal UI

**Best for**: Background template, visual showcase

---

## 🎨 Customization

### Changing Colors

All pages use CSS variables for easy theming. Edit the `:root` section:

```css
:root {
  --primary: #8B5CF6;      /* Purple */
  --secondary: #EC4899;    /* Pink */
  --accent: #06B6D4;       /* Cyan */
  --bg-dark: #0F0F1A;      /* Background */
  --text-light: #E5E7EB;   /* Text */
}
```

### Updating Content

1. **Personal Info**: Edit the HTML content directly
2. **Projects**: Update project cards in `portfolio.html`
3. **Skills**: Modify skill tags and icons
4. **Social Links**: Update href attributes in link sections

### Adding Your Images

```bash
# Add images to assets folder
cp your-photo.jpg assets/
cp project-screenshot.png assets/

# Update HTML
<img src="assets/your-photo.jpg" alt="Your Name">
```

---

## 🛠️ Technology Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with custom properties
- **Vanilla JavaScript** - No frameworks, pure JS
- **Canvas API** - Particle and aurora animations
- **SVG** - Scalable vector graphics for icons

---

## 📦 File Structure

```
Noctua-profile.html/
├── assets/                    # Images and media
│   ├── owl-logo.svg
│   ├── screenshots/
│   └── icons/
├── Noctua-profile.html       # Main profile card
├── portfolio.html            # Full portfolio page
├── profile-card.html         # Glassmorphism card
├── matrix-owl.html           # Interactive terminal
├── aurora.html               # Aurora background
├── orbit.html                # Orbit animation
├── banner.svg                # GitHub banner
├── generate_header.py        # SVG generator script
└── README.md                 # This file
```

---

## 🎯 Use Cases

### GitHub Profile
Use `Noctua-profile.html` as your GitHub profile page:
1. Create repository named `yourusername`
2. Add `Noctua-profile.html` as `index.html`
3. Enable GitHub Pages
4. Your profile is live!

### Personal Portfolio
Use `portfolio.html` for your developer portfolio:
- Showcase projects with live demos
- Display skills and technologies
- Provide contact information
- Link to GitHub and social media

### Creative Showcase
Use `matrix-owl.html` for a unique experience:
- Stand out from traditional portfolios
- Engage visitors with interactivity
- Show technical skills creatively

---

## 🤝 Contributing

Contributions welcome! Ideas for improvements:

- [ ] Add more page templates
- [ ] Create theme variations (dark/light)
- [ ] Add more particle effects
- [ ] Implement smooth page transitions
- [ ] Create mobile-optimized versions
- [ ] Add accessibility improvements

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🦉 About

Part of the **Noctua** design system - a collection of celestial-themed web components and pages.

Created by **[NoctuaCoder](https://github.com/NoctuaCoder)** - *Converting starlight into source code*

### Related Projects

- 🎯 [Noctua Focus](https://github.com/NoctuaCoder/noctua-focus) - Pomodoro timer with sound mixer
- 🚀 [Noctua Command Center](https://github.com/NoctuaCoder/noctua-command-center) - Productivity dashboard
- ✨ [Stellar Task Manager](https://github.com/NoctuaCoder/stellar-task-manager) - Task management app
- 💬 [Noctua Assistant](https://github.com/NoctuaCoder/noctua-assistant) - Portfolio chatbot

---

<div align="center">

### ⭐ If you like these designs, please star this repository!

Made with 💜 and ✨ under the night sky

**[⬆ back to top](#)**

</div>
