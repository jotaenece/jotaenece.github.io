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
---

<p id="typing-text" style="font-family: monospace; color: #00ff00; background: #1a1a1a; padding: 15px; border-radius: 5px; min-height: 25px;"></p>

<script>
  // Esta función espera a que TODO el HTML esté listo
  window.addEventListener('DOMContentLoaded', (event) => {
    const text = ">> Ejecutando: Data_Engineer.py ... OK. >> Cargando: Escritura_Creativa.exe ... OK.";
    let i = 0;
    const target = document.getElementById("typing-text");

    function typeWriter() {
      if (i < text.length) {
        target.innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, 50);
      }
    }
    typeWriter();
  });
</script>

---

{% include feature_row id="funcionalidades_row" %}

---

### 📖 Progreso de lectura: *El Juicio Final de Carl*
<div style="background-color: #333; border-radius: 13px; padding: 3px;">
  <div style="background-color: #3498db; width: 5%; height: 20px; border-radius: 10px; text-align: center; color: white; font-size: 12px; line-height: 20px;">
    5%
  </div>
</div>
