# Cartão de Visita Virtual — Fábio Sichineli

## Sobre o projeto
Cartão de visita digital de Fábio Sichineli (Precisão Analítica / Instituto Precisão).
Página única, estática (HTML + CSS embutido), publicada pelo GitHub Pages.

- Domínio: https://cartao.precisaoanalitica.com.br (definido no arquivo `CNAME` — não apagar)
- Branch publicado: `master`

## Estrutura
- `index.html` — o cartão inteiro (estilos dentro de `<style>`)
- `assets/logo_precisao.png` — logo exibida no cartão
- `assets/qrcode.png` — QR code (dourado sobre preto) que aponta para o cartão
- `generate_qr.py` — script que gera o QR code (biblioteca `qrcode`); o caminho de saída
  no script é de outra máquina e precisa ser ajustado antes de rodar

## Identidade visual
- Fundo preto (#0a0a0a) com detalhes dourados (`--gold: #caa44a`, `--gold-strong: #e5c56f`)
- Fontes: Boska (títulos) e Satoshi (texto), via Fontshare; ícones via Font Awesome
- Layout pensado para celular (largura máxima de 430px)

## Contatos exibidos
WhatsApp, e-mail (contato@precisaoanalitica.com.br), LinkedIn, Instagram (@institutoprecisao)
e o site precisaoanalitica.com.br. Ao alterar algum contato, conferir todos os links.

## Preferências
- Responder e escrever sempre em português do Brasil
- O usuário não é programador: explicar as mudanças em linguagem simples
- Manter o cartão leve (imagens otimizadas; ele é aberto principalmente pelo celular)
