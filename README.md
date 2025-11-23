<div align="center">

<!-- Animated SVG Header with 4-Pointed Stars -->
<svg width="100%" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="starGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00FFFF;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00BFFF;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="100%" height="200" fill="url(#starGradient)" opacity="0.05"/>
  
  <!-- Animated 4-Pointed Stars -->
  <g filter="url(#glow)">
    <!-- Star 1 -->
    <g transform="translate(100, 50)">
      <animateTransform attributeName="transform" type="rotate" from="0 100 50" to="360 100 50" dur="4s" repeatCount="indefinite"/>
      <rect x="98" y="40" width="4" height="20" fill="#00FFFF" opacity="0.8"/>
      <rect x="90" y="48" width="20" height="4" fill="#00FFFF" opacity="0.8"/>
    </g>
    
    <!-- Star 2 -->
    <g transform="translate(300, 150)">
      <animateTransform attributeName="transform" type="rotate" from="0 300 150" to="360 300 150" dur="6s" repeatCount="indefinite"/>
      <rect x="298" y="143" width="4" height="14" fill="#00BFFF" opacity="0.6"/>
      <rect x="293" y="148" width="14" height="4" fill="#00BFFF" opacity="0.6"/>
    </g>
    
    <!-- Star 3 -->
    <g transform="translate(500, 80)">
      <animateTransform attributeName="transform" type="rotate" from="0 500 80" to="360 500 80" dur="5s" repeatCount="indefinite"/>
      <rect x="498" y="72" width="4" height="16" fill="#4A9EFF" opacity="0.7"/>
      <rect x="492" y="78" width="16" height="4" fill="#4A9EFF" opacity="0.7"/>
    </g>
    
    <!-- Star 4 -->
    <g transform="translate(700, 120)">
      <animateTransform attributeName="transform" type="rotate" from="0 700 120" to="360 700 120" dur="7s" repeatCount="indefinite"/>
      <rect x="698" y="112" width="4" height="16" fill="#00FFFF" opacity="0.8"/>
      <rect x="692" y="118" width="16" height="4" fill="#00FFFF" opacity="0.8"/>
    </g>
    
    <!-- Star 5 -->
    <g transform="translate(900, 60)">
      <animateTransform attributeName="transform" type="rotate" from="0 900 60" to="360 900 60" dur="5.5s" repeatCount="indefinite"/>
      <rect x="898" y="53" width="4" height="14" fill="#00BFFF" opacity="0.6"/>
      <rect x="893" y="58" width="14" height="4" fill="#00BFFF" opacity="0.6"/>
    </g>
  </g>
  
  <!-- Constellation Lines -->
  <line x1="100" y1="50" x2="300" y2="150" stroke="#00BFFF" stroke-width="1" opacity="0.3"/>
  <line x1="300" y1="150" x2="500" y2="80" stroke="#00BFFF" stroke-width="1" opacity="0.3"/>
  <line x1="500" y1="80" x2="700" y2="120" stroke="#00BFFF" stroke-width="1" opacity="0.3"/>
  <line x1="700" y1="120" x2="900" y2="60" stroke="#00BFFF" stroke-width="1" opacity="0.3"/>
</svg>

<!-- ASCII Art Owl Constellation -->
<pre style="color: #00FFFF; font-size: 10px; line-height: 1.2; text-shadow: 0 0 10px #00FFFF;">
        ✦           ✦
    ✦      ___      ✦
          (o,o)
    ✦     {`"'}     ✦
          -"-"-
        ✦       ✦
</pre>

<!-- Title Section -->
<h1 style="font-size: 4em; font-weight: 700; background: linear-gradient(135deg, #00FFFF 0%, #00BFFF 50%, #4A9EFF 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 20px 0; letter-spacing: 3px;">
  NoctuaCoder
</h1>

<p style="font-size: 1.3em; color: #00BFFF; margin-bottom: 30px;">
  ✨ <em>Crafting stellar experiences by night</em> ✨
</p>

<!-- Animated Divider -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,50:00BFFF,100:4A9EFF&height=100&section=header&animation=twinkling" width="100%"/>

</div>

<br/>

<!-- Profile Section with Stellar Theme -->
<div align="center">

<table>
<tr>
<td width="50%" valign="top">

### 🌟 About Me

<img align="right" src="https://github.com/NoctuaCoder.png" width="200" style="border-radius: 50%; border: 3px solid #00FFFF; box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);"/>

```yaml
name: Alana
role: Full Stack Developer
location: Brazil 🇧🇷
timezone: GMT-3
motto: "Code by night, dream by day"

currently:
  - Building Stellar Dots v2.0
  - Exploring glassmorphism design
  - Creating beautiful UIs
  
interests:
  - UI/UX Design
  - System Customization
  - Open Source
  - Astronomy & Stars ✨
```

</td>
<td width="50%" valign="top">

### 💫 Quick Stats

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=NoctuaCoder&show_icons=true&theme=transparent&hide_border=true&title_color=00FFFF&icon_color=00BFFF&text_color=00BFFF&bg_color=0A0E27)

![Streak Stats](https://github-readme-streak-stats.herokuapp.com/?user=NoctuaCoder&theme=transparent&hide_border=true&background=0A0E2700&ring=00FFFF&fire=00BFFF&currStreakLabel=00FFFF&sideLabels=00BFFF&currStreakNum=00FFFF&sideNums=00BFFF&dates=4A9EFF)

</div>

</td>
</tr>
</table>

</div>

<br/>

<!-- Constellation Divider -->
<div align="center">

```
    ✦         ✦         ✦         ✦         ✦
      ·   ·   ·   ·   ·   ·   ·   ·   ·
    ✦         ✦         ✦         ✦         ✦
```

</div>

<br/>

<!-- Skills Constellation -->
<div align="center">

## 🌌 Skills Constellation

<table>
<tr>
<td width="33%" align="center">

### ⭐ Languages

![Shell](https://img.shields.io/badge/Shell_Script-★★★★★-00FFFF?style=for-the-badge&logo=gnu-bash&logoColor=00FFFF&labelColor=0A0E27)
![Python](https://img.shields.io/badge/Python-★★★★☆-00BFFF?style=for-the-badge&logo=python&logoColor=00BFFF&labelColor=0A0E27)
![JavaScript](https://img.shields.io/badge/JavaScript-★★★★☆-4A9EFF?style=for-the-badge&logo=javascript&logoColor=4A9EFF&labelColor=0A0E27)
![Rust](https://img.shields.io/badge/Rust-★★★☆☆-00FFFF?style=for-the-badge&logo=rust&logoColor=00FFFF&labelColor=0A0E27)

</td>
<td width="33%" align="center">

### 💎 Frontend

![HTML5](https://img.shields.io/badge/HTML5-00FFFF?style=for-the-badge&logo=html5&logoColor=00FFFF&labelColor=0A0E27)
![CSS3](https://img.shields.io/badge/CSS3-00BFFF?style=for-the-badge&logo=css3&logoColor=00BFFF&labelColor=0A0E27)
![React](https://img.shields.io/badge/React-4A9EFF?style=for-the-badge&logo=react&logoColor=4A9EFF&labelColor=0A0E27)
![Tailwind](https://img.shields.io/badge/Tailwind-00FFFF?style=for-the-badge&logo=tailwind-css&logoColor=00FFFF&labelColor=0A0E27)

</td>
<td width="33%" align="center">

### 🎨 Design

![Figma](https://img.shields.io/badge/Figma-00FFFF?style=for-the-badge&logo=figma&logoColor=00FFFF&labelColor=0A0E27)
![UI/UX](https://img.shields.io/badge/UI/UX-00BFFF?style=for-the-badge&logo=adobe&logoColor=00BFFF&labelColor=0A0E27)
![Glassmorphism](https://img.shields.io/badge/Glassmorphism-4A9EFF?style=for-the-badge&logoColor=4A9EFF&labelColor=0A0E27)

</td>
</tr>
</table>

<!-- Language Stats as Constellation -->
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=NoctuaCoder&layout=compact&theme=transparent&hide_border=true&title_color=00FFFF&text_color=00BFFF&bg_color=0A0E27&langs_count=8" width="500"/>

</div>

<br/>

<!-- Constellation Divider -->
<div align="center">

```
    ✦         ✦         ✦         ✦         ✦
      ·   ·   ·   ·   ·   ·   ·   ·   ·
    ✦         ✦         ✦         ✦         ✦
```

</div>

<br/>

<!-- Featured Projects Galaxy -->
<div align="center">

## 🌠 Featured Projects Galaxy

</div>

<table width="100%">
<tr>
<td width="50%" valign="top">

### 🌟 [Stellar Dots](https://github.com/NoctuaCoder/stellar-dots)

<img src="https://img.shields.io/badge/Status-Active-00FFFF?style=flat-square"/> <img src="https://img.shields.io/badge/Type-Dotfiles-00BFFF?style=flat-square"/>

Premium glassmorphism collection for Hyprland featuring:
- ✨ 10+ beautiful menus
- 🎨 8 stunning themes  
- ⚡ 30+ utility scripts
- 💎 Modern UI/UX design

**Tech Stack:** `Shell` `CSS` `Hyprland` `Rofi` `Waybar`

<a href="https://github.com/NoctuaCoder/stellar-dots">
  <img src="https://img.shields.io/badge/View_Project-00FFFF?style=for-the-badge&logo=github&logoColor=0A0E27"/>
</a>

</td>
<td width="50%" valign="top">

### 💎 [Matrix Owl Terminal](https://noctuacoder.github.io/NoctuaCoder/matrix-owl.html)

<img src="https://img.shields.io/badge/Status-Live-00FFFF?style=flat-square"/> <img src="https://img.shields.io/badge/Type-Interactive-00BFFF?style=flat-square"/>

Cyberpunk terminal experience with:
- 🌊 Matrix rain effect in blue
- 🦉 ASCII owl art
- ✨ Glitch animations
- 💫 Terminal interface

**Tech Stack:** `HTML` `CSS` `JavaScript` `Canvas`

<a href="https://noctuacoder.github.io/NoctuaCoder/matrix-owl.html">
  <img src="https://img.shields.io/badge/Live_Demo-00BFFF?style=for-the-badge&logo=firefox&logoColor=0A0E27"/>
</a>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎨 [Stellar Profile](https://noctuacoder.github.io/NoctuaCoder/stellar-profile.html)

<img src="https://img.shields.io/badge/Status-Live-00FFFF?style=flat-square"/> <img src="https://img.shields.io/badge/Type-Portfolio-00BFFF?style=flat-square"/>

Interactive celestial portfolio with:
- ⭐ Animated 4-pointed stars
- 🌌 Parallax effects
- 💫 Glassmorphism UI
- ✨ Smooth animations

**Tech Stack:** `HTML` `CSS` `JavaScript` `SVG`

<a href="https://noctuacoder.github.io/NoctuaCoder/stellar-profile.html">
  <img src="https://img.shields.io/badge/Live_Demo-4A9EFF?style=for-the-badge&logo=firefox&logoColor=0A0E27"/>
</a>

</td>
<td width="50%" valign="top">

### 🌈 Design System

<img src="https://img.shields.io/badge/Status-In_Progress-4A9EFF?style=flat-square"/> <img src="https://img.shields.io/badge/Type-Library-00BFFF?style=flat-square"/>

Comprehensive UI component library:
- 🎨 Modern aesthetics
- ♿ Accessible design
- 📱 Responsive components
- 🎭 Dark mode support

**Tech Stack:** `React` `TypeScript` `Tailwind` `Storybook`

<img src="https://img.shields.io/badge/Coming_Soon-00FFFF?style=for-the-badge"/>

</td>
</tr>
</table>

<br/>

<!-- Constellation Divider -->
<div align="center">

```
    ✦         ✦         ✦         ✦         ✦
      ·   ·   ·   ·   ·   ·   ·   ·   ·
    ✦         ✦         ✦         ✦         ✦
```

</div>

<br/>

<!-- GitHub Activity & Trophies -->
<div align="center">

## 🏆 Achievements Constellation

![Trophies](https://github-profile-trophy.vercel.app/?username=NoctuaCoder&theme=darkhub&no-frame=true&no-bg=true&column=4&margin-w=15&margin-h=15&title_color=00FFFF&icon_color=00BFFF&text_color=00BFFF)

### 📊 Contribution Graph

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=NoctuaCoder&theme=react-dark&hide_border=true&bg_color=0A0E27&color=00FFFF&line=00BFFF&point=4A9EFF&area=true&area_color=00BFFF)

</div>

<br/>

<!-- Constellation Divider -->
<div align="center">

```
    ✦         ✦         ✦         ✦         ✦
      ·   ·   ·   ·   ·   ·   ·   ·   ·
    ✦         ✦         ✦         ✦         ✦
```

</div>

<br/>

<!-- Social Constellation -->
<div align="center">

## 🌌 Connect Across the Stars

<table>
<tr>
<td align="center" width="25%">

### ⭐ GitHub
<a href="https://github.com/NoctuaCoder">
  <img src="https://img.shields.io/badge/NoctuaCoder-00FFFF?style=for-the-badge&logo=github&logoColor=0A0E27"/>
</a>

</td>
<td align="center" width="25%">

### 💎 Email
<a href="mailto:your@email.com">
  <img src="https://img.shields.io/badge/Contact_Me-00BFFF?style=for-the-badge&logo=gmail&logoColor=0A0E27"/>
</a>

</td>
<td align="center" width="25%">

### ✨ Instagram
<a href="https://instagram.com/yourusername">
  <img src="https://img.shields.io/badge/@yourusername-4A9EFF?style=for-the-badge&logo=instagram&logoColor=0A0E27"/>
</a>

</td>
<td align="center" width="25%">

### 🌟 Portfolio
<a href="https://noctuacoder.github.io/NoctuaCoder/stellar-profile.html">
  <img src="https://img.shields.io/badge/View_Portfolio-00FFFF?style=for-the-badge&logo=firefox&logoColor=0A0E27"/>
</a>

</td>
</tr>
</table>

</div>

<br/><br/>

<!-- Footer with Constellation -->
<div align="center">

<!-- Animated Wave Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,50:00BFFF,100:4A9EFF&height=120&section=footer" width="100%"/>

<!-- Footer Constellation -->
<pre style="color: #00BFFF; font-size: 8px; line-height: 1.2; opacity: 0.6;">
    ✦       ✦       ✦       ✦       ✦       ✦       ✦
      ·   ·   ·   ·   ·   ·   ·   ·   ·   ·   ·
    ✦       ✦       ✦       ✦       ✦       ✦       ✦
</pre>

<sub style="color: #00BFFF; opacity: 0.8;">
  ✨ Crafted with passion under the stars • © 2025 NoctuaCoder 🦉
</sub>

<br/>

<img src="https://komarev.com/ghpvc/?username=NoctuaCoder&color=00FFFF&style=flat-square&label=Profile+Views"/>

</div>
