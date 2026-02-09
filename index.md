---
layout: home
author_profile: true
header:
  overlay_image: /assets/images/header.jpg
  overlay_filter: 0.5
  excerpt: ""
  
  actions:
    - label: "Explorar Relatos"
      url: "/taller/"
    - label: "Ver Biblioteca"
      url: "/lecturas/"

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
