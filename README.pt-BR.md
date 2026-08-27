<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/noctua_editorial_header_twilight_wide.png?v=1" />
  <source media="(prefers-color-scheme: light)" srcset="./assets/noctua_editorial_header_light_wide.png?v=1" />
  <img width="100%" alt="Paisagem editorial tecnológica do Noctua" src="./assets/noctua_editorial_header_light_wide.png?v=1" />
</picture>

# Noctua Lab

### Compiling the night.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com/?lines=Converting+starlight+into+source+code...;Linux+%C2%B7+IA+local+%C2%B7+Autonomia+de+software;Construindo+sistemas+silenciosos+para+mundos+barulhentos&font=Fira%20Code&center=true&vCenter=true&width=800&height=50&duration=3500&pause=900&color=FFEBC9&background=70809000" />
    <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com/?lines=Converting+starlight+into+source+code...;Linux+%C2%B7+IA+local+%C2%B7+Autonomia+de+software;Construindo+sistemas+silenciosos+para+mundos+barulhentos&font=Fira%20Code&center=true&vCenter=true&width=800&height=50&duration=3500&pause=900&color=708090&background=EAE0C800" />
    <img alt="Texto de apresentação animado" src="https://readme-typing-svg.demolab.com/?lines=Converting+starlight+into+source+code...;Linux+%C2%B7+IA+local+%C2%B7+Autonomia+de+software;Construindo+sistemas+silenciosos+para+mundos+barulhentos&font=Fira%20Code&center=true&vCenter=true&width=800&height=50&duration=3500&pause=900&color=708090&background=EAE0C800" />
  </picture>
</p>

[English](./README.md) · [Português do Brasil](./README.pt-BR.md) · [Sistema de cores](./docs/PROFILE_PALETTE.md) · [Automações](./docs/PROFILE_AUTOMATIONS.md)

Experimentos, ferramentas e sistemas construídos em torno de **Linux, IA local e autonomia de software**.

[![GitHub](https://img.shields.io/badge/GitHub-708090?style=for-the-badge&logo=github&logoColor=FFEBC9)](https://github.com/NoctuaCoder)
[![Contato](https://img.shields.io/badge/Contato-C4B9C9?style=for-the-badge&logo=gmail&logoColor=FFEBC9)](mailto:38922657+NoctuaCoder@users.noreply.github.com)

</div>

---

## O que eu construo

O Noctua Lab é um espaço pessoal de código aberto para construir e testar software voltado a desktops Linux, modelos de linguagem locais, ferramentas para desenvolvedores e sistemas de interface. O objetivo é simples: tornar o trabalho visível por meio de repositórios, documentação, demonstrações e código que possa ser examinado e executado.

<div align="center">

![Pilares centrais: autonomia, privacidade, reprodutibilidade e experiência](./assets/core-pillars-topics.svg?v=2)

</div>

## Mapa de projetos

| Área | Projeto | Papel no ecossistema |
|---|---|---|
| **Desktop Linux** | [**noctua-niri**](https://github.com/NoctuaCoder/noctua-niri) | O principal experimento de ambiente desktop: dotfiles para Niri, componentes QML, integração com Quickshell, temas e fluxos de instalação. |
| **Infraestrutura de IA local** | [**ArbiterAI**](https://github.com/NoctuaCoder/ArbiterAI) | Runtime local para agentes de código que planeja tarefas, usa ferramentas, integra-se ao Git e executa trabalhos em sandboxes Docker efêmeros. |
| **Ferramentas para LLMs** | [**voidkitty-llm**](https://github.com/NoctuaCoder/voidkitty-llm) | Ferramenta em Rust para baixar modelos GGUF, gerenciar processos llama-server e servir modelos locais por interface web e API. |
| **Design de desktop** | [**noctua-material**](https://github.com/NoctuaCoder/noctua-material) | Tema SDDM inspirado em Material, com foco em estados de login, apresentação do desktop e estilização em QML. |

## Foco atual

A prioridade é profundidade, não quantidade: tornar os projetos existentes mais fáceis de instalar, entender e avaliar.

No `noctua-niri`, isso significa melhorar screenshots, instruções de instalação, exemplos de configuração e um roadmap prático. No `ArbiterAI`, significa tornar os limites do sandbox, o fluxo de execução e a arquitetura do projeto fáceis de inspecionar. Os outros projetos complementam o mesmo ecossistema nos lados de LLMs e interfaces.

## Evidência antes de adjetivos

| Projeto | O que explorar no código |
|---|---|
| **noctua-niri** | Componentes QML e Quickshell, configuração do Niri, previews visuais e scripts de instalação. |
| **ArbiterAI** | Sandbox Docker, fluxo local com Ollama, execução de ferramentas, integração com Git e estrutura do projeto. |
| **voidkitty-llm** | Download de modelos GGUF, seleção de quantização, serving em modo hot, modo multimodelo e API compatível com OpenAI. |
| **noctua-material** | Estrutura do tema SDDM, estados de login, componentes visuais e instruções de instalação. |

## Arsenal técnico

<div align="center">

![Python](https://img.shields.io/badge/Python-C4B9C9?style=for-the-badge&logo=python&logoColor=FFEBC9&labelColor=708090)
![TypeScript](https://img.shields.io/badge/TypeScript-C4B9C9?style=for-the-badge&logo=typescript&logoColor=FFEBC9&labelColor=708090)
![Rust](https://img.shields.io/badge/Rust-C4B9C9?style=for-the-badge&logo=rust&logoColor=FFEBC9&labelColor=708090)
![QML](https://img.shields.io/badge/QML-C4B9C9?style=for-the-badge&logo=qt&logoColor=FFEBC9&labelColor=708090)
![Docker](https://img.shields.io/badge/Docker-C4B9C9?style=for-the-badge&logo=docker&logoColor=FFEBC9&labelColor=708090)
![Ollama](https://img.shields.io/badge/Ollama-C4B9C9?style=for-the-badge&logo=ollama&logoColor=FFEBC9&labelColor=708090)

</div>

| Área | Tecnologias |
|---|---|
| **Linguagens** | Python · Rust · TypeScript · Bash |
| **Sistemas** | Linux · Wayland · Niri · Docker |
| **IA** | llama.cpp · GGUF · LLMs locais · Agentes de código |
| **Interface** | QML · Quickshell · Electron |
| **Ferramentas** | Git · GitHub Actions · Neovim |

## Painel de sistemas ao vivo

<div align="center">

<img src="https://github-stats-extended.vercel.app/api?username=NoctuaCoder&theme=radical&show_icons=true&hide_border=true&bg_color=708090&title_color=FFEBC9&icon_color=EAE0C8&text_color=F1E8C7&border_color=C4B9C9&ring_color=9CA764" width="49%" alt="Estatísticas do GitHub" />
<img src="https://github-stats-extended.vercel.app/api/top-langs/?username=NoctuaCoder&layout=compact&theme=radical&hide_border=true&bg_color=708090&title_color=FFEBC9&text_color=F1E8C7&border_color=C4B9C9" width="41%" alt="Linguagens de programação mais usadas" />

</div>

## Centrais de atividade

<div align="center">

![Centrais de atividade: perfil, Linux e Niri, agentes de código locais e ferramentas para LLMs](./assets/activity-hub-cards-pt.svg?v=1)

</div>

## Trilha de contribuições

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NoctuaCoder/NoctuaCoder/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NoctuaCoder/NoctuaCoder/output/github-contribution-grid-snake.svg" />
  <img alt="Animação da cobra no gráfico de contribuições do GitHub" src="https://raw.githubusercontent.com/NoctuaCoder/NoctuaCoder/output/github-contribution-grid-snake.svg" />
</picture>

</div>

## Constelação 3D de contribuições

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/NoctuaCoder/NoctuaCoder/output-3d-contrib/night.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/NoctuaCoder/NoctuaCoder/output-3d-contrib/day.svg" />
  <img alt="Calendário 3D de contribuições do GitHub" src="https://raw.githubusercontent.com/NoctuaCoder/NoctuaCoder/output-3d-contrib/day.svg" />
</picture>

</div>

O gráfico nativo de contribuições está disponível no [perfil principal](https://github.com/NoctuaCoder). Commits, releases, issues, instruções de instalação e detalhes de implementação ficam registrados em cada repositório.

## Contato

Se você se interessa por desktops Linux, IA local, ferramentas em Rust, agentes de código ou interfaces em QML, explore os projetos e abra uma discussão no repositório relacionado ao seu interesse.

<div align="center">

[![Explorar projetos](https://img.shields.io/badge/Explorar_projetos-708090?style=for-the-badge&logo=github&logoColor=FFEBC9)](https://github.com/NoctuaCoder)
[![Enviar mensagem](https://img.shields.io/badge/Enviar_mensagem-C4B9C9?style=for-the-badge&logo=gmail&logoColor=FFEBC9)](mailto:38922657+NoctuaCoder@users.noreply.github.com)

`SISTEMAS LOCAIS · OPEN SOURCE · IA PRÁTICA`

</div>
