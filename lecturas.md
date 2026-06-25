---
layout: archive
title: "Mi Biblioteca"
permalink: /lecturas/
author_profile: true
---

Lecturas sincronizadas desde Goodreads. Si quieres ver mi perfil completo, puedes encontrarme [aquí](https://www.goodreads.com/user/show/187136448-jorge-navarro).

{% for libro in site.data.lecturas_goodreads %}
<div class="libro-card">
  <img class="libro-cover" src="{{ libro.image }}" alt="{{ libro.title }}" loading="lazy">
  <div>
    <h2 class="archive__item-title libro-title">{{ libro.title }}</h2>
    <p class="libro-meta">{{ libro.author }}</p>
    {% assign rnum = libro.rating | plus: 0 %}{% assign rrest = 5 | minus: rnum %}<span class="libro-stars">{% for i in (1..rnum) %}★{% endfor %}{% for i in (1..rrest) %}☆{% endfor %} {{ libro.rating }}/5</span>
    <p class="libro-excerpt">{{ libro.review | strip_html | truncate: 220 }}</p>
    <a href="{{ libro.link }}" class="btn btn--primary btn--small" target="_blank" rel="noopener">Leer reseña →</a>
  </div>
</div>
{% endfor %}
