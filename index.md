---
layout: home
author_profile: true
title: # Sin título
funcionalidades_row:
  - image_path: "/assets/images/taller.jpg"
    alt: "Sección Taller"
    title: "El Taller"
    url: "/taller/"
    btn_label: "Entrar"
    btn_class: "btn--primary"
  - image_path: "/assets/images/biblioteca.jpg"
    alt: "Sección Biblioteca"
    title: "La Biblioteca"
    url: "/lecturas/"
    btn_label: "Leer Reviews"
    btn_class: "btn--info"


<p id="typing-text" style="font-family: 'Courier New', Courier, monospace; color: #00ff00; background: transparent; padding: 10px 0; min-height: 25px; font-weight: bold;"></p>

<script>
  window.addEventListener('DOMContentLoaded', (event) => {
    // He añadido un pequeño retraso (300ms) para que el efecto sea más natural al cargar
    setTimeout(() => {
      const text = ">> Ejecutando: Data_Engineer.py ... OK. >> Cargando: Escritura_Creativa.exe ... OK.";
      let i = 0;
      const target = document.getElementById("typing-text");

      function typeWriter() {
        if (i < text.length) {
          target.innerHTML += text.charAt(i);
          i++;
          setTimeout(typeWriter, 40);
        }
      }
      typeWriter();
    }, 300);
  });
</script>

<style>
  #typing-text::after {
    content: "|";
    animation: blink 1s infinite;
  }
  @keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
  }
</style>



{% include feature_row id="funcionalidades_row" %}



### 📖 Progreso de lectura: *El Juicio Final de Carl*
<div style="background-color: #333; border-radius: 13px; padding: 3px;">
  <div style="background-color: #3498db; width: 5%; height: 20px; border-radius: 10px; text-align: center; color: white; font-size: 12px; line-height: 20px;">
    5%
  </div>
</div>
