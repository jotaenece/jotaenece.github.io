---
layout: archive
title: "Mi Biblioteca"
permalink: /lecturas/
author_profile: true
---

Aquí comparto mis últimas lecturas sincronizadas desde Goodreads. Si quieres ver mi perfil completo, puedes encontrarme [aquí](https://www.goodreads.com/user/show/187136448-jorge-navarro).

<div class="grid__wrapper">
  {% for libro in site.data.lecturas_goodreads %}
    <div class="grid__item" style="border: 1px solid #444; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
      <article class="archive__item">
        <h2 class="archive__item-title">{{ libro.title }}</h2>
        <p><strong>Autor:</strong> {{ libro.author }}</p>
        <p><strong>Puntuación:</strong> {{ libro.rating }} / 5 ⭐</p>
        <div class="archive__item-excerpt">
          {{ libro.review | strip_html | truncate: 200 }}
        </div>
        <a href="{{ libro.link }}" class="btn btn--primary">Leer reseña completa</a>
      </article>
    </div>
  {% endfor %}
</div>
