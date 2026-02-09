---
layout: home
author_profile: true
title:  # Esto elimina el título "jotaenece" o "Home" del cuerpo de la página
# ELIMINAMOS EL HEADER, COMENTANDOLO
# header:
#  overlay_image: /assets/images/header.jpg
#  overlay_filter: 0.5
#  excerpt: ""

# Única fila con dos elementos
funcionalidades_row:
  - image_path: /assets/images/taller.jpg
    alt: "Sección Taller"
    title: "El Taller"
    excerpt: "Donde el código se convierte en narrativa. Relatos, ejercicios y borradores."
    url: "/taller/"
    btn_label: "Entrar"
    btn_class: "btn--primary"
  - image_path: /assets/images/biblioteca.jpg
    alt: "Sección Biblioteca"
    title: "La Biblioteca"
    excerpt: "Curación de lecturas, reseñas técnicas y mis favoritos de Goodreads."
    url: "/lecturas/"
    btn_label: "Leer Reviews"
    btn_class: "btn--info"
---

{% include feature_row id="funcionalidades_row" %}

---

<script>
  const text = ">> Ejecutando: Data_Engineer.py ... OK. >> Cargando: Escritura_Creativa.exe ... OK.";
  let i = 0;
  function typeWriter() {
    if (i < text.length) {
      document.getElementById("typing-text").innerHTML += text.charAt(i);
      i++;
      setTimeout(typeWriter, 50);
    }
  }
  typeWriter();
</script>

---

<h3>📖 Progreso de lectura actual: <i>El Juicio Final de Carl - Matt Dinniman</i></h3>
<div style="background-color: #333; border-radius: 13px; padding: 3px;">
  <div style="background-color: #3498db; width: 5%; height: 20px; border-radius: 10px; text-align: center; color: white; font-size: 12px; line-height: 20px;">
    5%
  </div>
</div>

---

[<i class="fab fa-goodreads"></i> Sígueme en Goodreads](https://goodreads.com/tu-perfil){: .btn .btn--success}

---

<p id="typing-text" style="font-family: monospace; color: #00ff00;"></p>

